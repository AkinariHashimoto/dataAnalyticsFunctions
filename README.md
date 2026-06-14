# dataAnalyticsFunctions

データ分析でよく使う前処理・可視化関数をまとめたPythonパッケージです。  
A Python package of utility functions for common data analysis tasks.

## インストール / Installation

```bash
pip install git+https://github.com/AkinariHashimoto/dataAnalyticsFunctions.git
```

## 使い方 / Usage

```python
from dataAnalyticsFunctions import function as daf
```

## 関数一覧 / Functions

### nullCheck(df)
欠損値を含むカラムと件数を表示し、pd.Series で返す。  
Prints and returns columns with missing values.

```python
daf.nullCheck(df)
```

### columnsType(df)
各カラムのデータ型を表示し、pd.Series で返す。  
Prints and returns the data type of each column.

```python
daf.columnsType(df)
```

### corr(df, x, y)
数値カラムの相関行列をヒートマップで表示する。  
Displays a heatmap of the correlation matrix for numeric columns.

```python
daf.corr(df, x=10, y=8)
```

### std(df)
数値カラムを StandardScaler で標準化する。  
Standardizes numeric columns using StandardScaler.

```python
df_std = daf.std(df)
```

### dummy(df_train, df_test, columns, target)
指定カラムをダミー変数化し、train/test のカラムを揃える。  
Applies one-hot encoding and aligns columns between train and test.

```python
df_train_dummy, df_test_dummy = daf.dummy(df_train, df_test, columns=['col1', 'col2'], target='price')
```

### targetEncoding(df_train, df_test, columns, target)
指定カラムをターゲットエンコーディングする。  
Applies target encoding to specified columns.

```python
df_train_enc, df_test_enc, te_values = daf.targetEncoding(df_train, df_test, columns=['col1'], target='price')
```

## ライセンス / License

[MIT](LICENSE)
