# 深層分位点回帰 [deep_q_reg]

import sys
import torch
import eznorm
import random
import numpy as np
from tqdm import tqdm
from sout import sout
# 共通ツール [utils.py]
from .parts import utils

# 層一覧の作成
def gen_layers(input_dim, params):
	# pytorchのlayerたちを格納する専用のリスト型コンテナ (層をtorchシステムに明示的に検知させるために必要)
	layers = torch.nn.ModuleList()
	# 最初の入力次元数の設定
	pre_n = input_dim	# 入力次元数 (初回学習データの形状から自動的に判定される)
	# 中間層の積層
	for l_info in params["layers"]:
		# 線形層
		ll = torch.nn.Linear(pre_n, l_info["out_n"])
		layers.append(ll)
		# 活性化関数を名前で引き当て (getattrはpython標準機能で、obj.nameのnameに相当する文字列を変数として指定できるもの)
		act_fn = getattr(torch.nn, l_info["activation"])()	# 少しわかりにくいが、ここで関数コールしてはじめて層の形になる
		layers.append(act_fn)
		# 今回の出力次元数を次層の入力次元数に設定
		pre_n = l_info["out_n"]
	# 最終層はquant_ls長の次元を持つ線形層
	final_out_n = len(params["quant_ls"])
	final_l = torch.nn.Linear(pre_n, final_out_n)
	layers.append(final_l)
	return layers

# 深層学習モデルを表すオブジェクト (pytorchで定められた形式; 外部からforwardを渡せるようにしてある)
class NNet(
	torch.nn.Module	# pytorchで定められた深層学習用クラスを継承
):
	# 初期化処理
	def __init__(self,
		input_dim,	# 入力次元数 (初回学習データの形状から自動的に判定される)
		params = {}	# 設定値
	):
		# 親クラスの初期化
		super().__init__()
		# 設定値
		self.params = params
		# layers変数に積層 (層をtorchシステムに明示的に検知させるために必要。pytorchでは、このクラスに明示的にlayerを束縛しておかないと検知されない仕掛けになっている。)
		self.layers = gen_layers(input_dim, self.params)	# 層一覧の作成
	# pytorchで定められた「forward」関数 (順伝播処理を記述することで層構成を表現する関数)
	def forward(self, x):
		# self.layers の定めにまっすぐ従って積層
		for layer in self.layers:
			x = layer(x)
		return x

# x, y データを numpy.array に変換 (テンソルの階数チェックも実施)
def to_np_array(raw_x, raw_y):
	# 型変換
	np_x, np_y = np.array(raw_x), np.array(raw_y)
	# テンソルの階数をチェック
	if len(np_x.shape) != 2: raise Exception("[deep-q-reg error] The rank of the x tensor must be 2. (Must be a double nested list.)")
	if len(np_y.shape) != 1: raise Exception("[deep-q-reg error] The rank of the y tensor must be 1. (Must be a non-nested flat list.)")
	return np_x, np_y[:,None]

# ミニバッチを取り出して繰り返す
def mini_batch_iter(train_x, train_y, params):
	all_idx_ls = [i for i, _ in enumerate(train_x)]
	mini_batch_size = params["mini_batch_size"]
	if len(all_idx_ls) < mini_batch_size: mini_batch_size = len(all_idx_ls)	# 学習データが少なすぎるときはmini_batchのsizeを補正
	for i in tqdm(range(params["mini_batch_n"])):
		batch_idx_ls = random.sample(all_idx_ls, mini_batch_size)
		batch_x = torch.Tensor(train_x[batch_idx_ls, :])
		batch_y = torch.Tensor(train_y[batch_idx_ls, :])
		yield batch_x, batch_y

# 分位点lossの計算に使われるhuber関数
def huber(x, k = 0.1):
	return torch.where(x.abs() < k, 0.5 * x.pow(2), k * (x.abs() - 0.5 * k))	# whereは三項演算子

# 分位点loss
def quantile_huber_loss(
	true_y,	# 実際のy値
	pred_y,	# その時の推論値
	tau,	# 分位点のリスト
):
	u = true_y - pred_y
	s = tau - (u < torch.Tensor([0])).float()
	return torch.mean(s.abs() * huber(u))

# 深層分位点回帰 [deep_q_reg]
class Deep_Q_Reg:
	# 初期化処理
	def __init__(self,
		params	# 設定値
	):
		# 初回学習時に層構成等を決める (define-by-runのため)
		self.nnet = None
		# 省略されているparamsをdefault値に設定 [utils.py]
		self.params = utils.params_completion(params)
	# 学習 [deep_q_reg]
	def train(self,
		train_x,
		train_y
	):
		# x, y データを numpy.array に変換 (テンソルの階数チェックも実施)
		train_x, train_y = to_np_array(train_x, train_y)
		# 学習データの正規化
		if self.params["normalize_x"] is True:
			self.norm_params = eznorm.fit(train_x)	# 学習データへの適合 (正規化パラメータを返す) [eznorm]
			train_x = eznorm.normalize(train_x, self.norm_params)	# データの正規化 [eznorm]
		# 深層学習モデルを表すオブジェクト (pytorchで定められた形式; 外部からforwardを渡せるようにしてある)
		self.nnet = NNet(
			input_dim = train_x.shape[1],	# 入力次元数 (初回学習データの形状から自動的に判定される)
			params = self.params)
		# 層構成のデバッグ表示
		print(self.nnet.layers)
		# 学習
		print("training...")
		tau = torch.Tensor(np.array(self.params["quant_ls"]))
		opt = torch.optim.Adam(self.nnet.parameters(), lr = 1e-2, amsgrad = True)
		for batch_x, batch_y in mini_batch_iter(train_x, train_y, self.params):	# ミニバッチを取り出して繰り返す
			loss = quantile_huber_loss(	# 分位点loss
				batch_y, self.nnet(batch_x), tau)
			opt.zero_grad()	# 勾配の初期化
			loss.backward()	# 誤差逆伝播
			opt.step()	# 最適化プロセスを一ステップすすめる
	# 推論 [deep_q_reg]
	def predict(self, test_x):
		# 正規化
		np_test_x = np.array(test_x)
		if self.params["normalize_x"] is True: np_test_x = eznorm.normalize(np_test_x, self.norm_params)	# データの正規化 [eznorm]
		# 形式変換
		torch_test_x = torch.Tensor(np_test_x)
		# 推論
		raw_pred_y = self.nnet(torch_test_x)
		# 形式を変換
		pred_y = raw_pred_y.detach().numpy()
		return pred_y
