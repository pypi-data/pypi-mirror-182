params = {
    'normalize_x': True,    # xの自動正規化
    'quant_ls': [0.25, 0.5, 0.75],    # 予測対象分位点一覧
    # 層構成
    'layers': [
        {
            'activation': 'ReLU',    # 活性化関数名 (torch.nn配下の名前を指定する。Tanh, ReLU, Sigmoid など)
            'out_n': 8    # 層の出力次元数 (入力次元数は学習データや前層設定から自動的に判断される)
        },
        {'activation': 'ReLU', 'out_n': 8}
    ],
    # 学習パラメータ
    'mini_batch_n': 10000,    # 繰り返し学習回数 (ミニバッチ学習)
    'mini_batch_size': 256    # ミニバッチのサイズ
}