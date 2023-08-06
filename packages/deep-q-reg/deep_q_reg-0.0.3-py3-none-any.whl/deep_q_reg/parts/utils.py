
# 共通ツール [utils.py]

import sys
import fies
from sout import sout
# デフォルトパラメータ [default_params.py]
from . import default_params

# 省略されているparamsをdefault値に設定 [utils.py]
def params_completion(params):
	# 設定されていないパラメータを設定していく (元のparamsの値も汚染する)
	for key in default_params.params:
		if key in params: continue
		params[key] = default_params.params[key]
	return params
