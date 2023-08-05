
# 共通ツール [utils.py]

import sys
import fies
from sout import sout
from relpath import rel2abs

# 省略されているparamsをdefault値に設定 [utils.py]
def params_completion(params):
	# デフォルト引数一覧を読み込む
	default_params = fies[rel2abs("./default_params.yml"), "yaml"]
	# 設定されていないパラメータを設定していく (元のparamsの値も汚染する)
	for key in default_params:
		if key in params: continue
		params[key] = default_params[key]
	return params
