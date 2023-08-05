# eznorm

下の方に日本語の説明があります

## Overview
- Easy to use normalization tool for machine learning.
- Normalization is performed on test data as well as on training parameters to prevent leakage.
- Automatically prevents division by zero for features with a standard deviation of zero

## Usage
```python
import eznorm

train_x = [
	[1, -10, 0.3],
	[2, -5, 0.1],
	[1, -10, 0.5],
]
test_x = [[2, -5, 0.2], [1, -7, 0.3]]

# Normalize training data
norm_params = eznorm.fit(train_x)	# Fit the data to the normalization parameters (returns normalization parameters) [eznorm]
norm_train_x = eznorm.normalize(train_x, norm_params)	# Normalize the data [eznorm]
"""
norm_train_x:
[[-0.70710678 -0.70710678  0.        ]
 [ 1.41421356  1.41421356 -1.22474487]
 [-0.70710678 -0.70710678  1.22474487]]
"""

# Normalize test data
norm_test_x = eznorm.normalize(test_x, norm_params)	# Normalize the data [eznorm]
"""
norm_test_x:
[[ 1.41421356  1.41421356 -0.61237244]
 [-0.70710678  0.56568542  0.        ]]
"""
```


## 概要
- 機械学習の正規化処理を簡単に実施するツール
- テストデータに対してもにも学習時のパラメータで正規化を実施することでリーケージを防止
- 標準偏差が0の特徴量に対してのゼロ割りを自動的に防止

## 使用例
```python
import eznorm

train_x = [
	[1, -10, 0.3],
	[2, -5, 0.1],
	[1, -10, 0.5],
]
test_x = [[2, -5, 0.2], [1, -7, 0.3]]

# 学習データの正規化
norm_params = eznorm.fit(train_x)	# 学習データへの適合 (正規化パラメータを返す) [eznorm]
norm_train_x = eznorm.normalize(train_x, norm_params)	# データの正規化 [eznorm]
"""
norm_train_x:
[[-0.70710678 -0.70710678  0.        ]
 [ 1.41421356  1.41421356 -1.22474487]
 [-0.70710678 -0.70710678  1.22474487]]
"""

# テストデータの正規化
norm_test_x = eznorm.normalize(test_x, norm_params)	# データの正規化 [eznorm]
"""
norm_test_x:
[[ 1.41421356  1.41421356 -0.61237244]
 [-0.70710678  0.56568542  0.        ]]
"""
```
