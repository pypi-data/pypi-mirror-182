
# 深層分位点回帰 [deep_q_reg]
# 【動作確認 / 使用例】

import sys
import fies
from sout import sout
from ezpip import load_develop
# 深層分位点回帰 [deep_q_reg]
deep_q_reg = load_develop("deep_q_reg", "../", develop_flag = True)

# データ準備
data = fies["boston_4th_feature.json"]
train_x = data["x"]	# [[0.538], [0.469], ... (all_n = 506)]
train_y = data["y"]	# [24.0, 21.6, ... (all_n = 506)]

# データのレビュー
import quantile_scatter
quantile_scatter.plot([e[0] for e in train_x], train_y)

# パラメータ
params = fies["params.yml"]

# 深層分位点回帰 [deep_q_reg]
dqr = deep_q_reg.Deep_Q_Reg(params)

# 学習 [deep_q_reg]
dqr.train(train_x, train_y)

test_x = sorted(train_x, key = lambda e: e[0])
# 推論 [deep_q_reg]
pred_y = dqr.predict(test_x)	# 今回は自己交差

# 結果の確認
sout(pred_y)	# 内側の次元は、paramsで指定されたquant_lsの順序に従う

# 可視化
from matplotlib import pyplot as plt
for i in range(pred_y.shape[1]):
	x_ls = [e[0] for e in test_x]
	y_ls = [e[i] for e in pred_y]
	plt.plot(x_ls, y_ls)
plt.show()
