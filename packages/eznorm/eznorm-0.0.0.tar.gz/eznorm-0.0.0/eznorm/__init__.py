# 機械学習用の正規化ツール [eznorm]

import sys
import numpy as np
from sout import sout

# numpy 型への変換とテンソル階数の確認
def to_np(arg_x):
	np_x = np.array(arg_x)
	if len(np_x.shape) != 2: raise Exception("[eznorm error] The number of dimension (tensor rank) of the data to be normalized must be 2.")
	return np_x

# 学習データへの適合 (正規化パラメータを返す) [eznorm]
def fit(
	train_x	# 正規化パラメータを求めるための
):
	# numpy 型への変換とテンソル階数の確認
	np_x = to_np(train_x)
	# パラメータの算出
	norm_params = {
		"mean": np.mean(np_x, axis = 0),	# 平均
		"std": np.std(np_x, axis = 0),	# 標準偏差
	}
	return norm_params

# データの正規化 [eznorm]
def normalize(
	data_x,	# 正規化対象データ
	norm_params	# 正規化パラメータ
):
	# numpy 型への変換とテンソル階数の確認
	np_x = to_np(data_x)
	# norm_paramsの整形
	mean_tensor = norm_params["mean"][None, :]	# 階数の整形
	std_tensor = norm_params["std"][None, :]	# 階数の整形
	# stdがゼロのデータに対するゼロ割りの防止
	std_tensor[std_tensor == 0] = 1
	# 正規化
	norm_data_x = (np_x - mean_tensor) / std_tensor
	return norm_data_x
