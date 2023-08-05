# 機械学習用の正規化ツール [eznorm]
# 【動作確認 / 使用例】

import sys
from sout import sout
from ezpip import load_develop
# 機械学習用の正規化ツール [eznorm]
eznorm = load_develop("eznorm", "../", develop_flag = True)

# ダミーデータ
train_x = [
	[1, -10, 0.3],
	[2, -5, 0.1],
	[1, -10, 0.5],
]
test_x = [[2, -5, 0.2], [1, -7, 0.3]]

# 学習データの正規化
norm_params = eznorm.fit(train_x)	# 学習データへの適合 (正規化パラメータを返す) [eznorm]
norm_train_x = eznorm.normalize(train_x, norm_params)	# データの正規化 [eznorm]

# 結果確認
print(norm_train_x)

# 推論データの正規化
norm_test_x = eznorm.normalize(test_x, norm_params)	# データの正規化 [eznorm]

# 結果確認
print(norm_test_x)
