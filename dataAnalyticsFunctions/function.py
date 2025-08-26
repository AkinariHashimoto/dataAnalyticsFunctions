def hello():
    return "Hello from analytics!"


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
#from scipy import stats
#from sklearn.model_selection import train_test_split
#from sklearn.model_selection import KFold


#nullチェック
def nullCheck(df):
    print("欠損値を含むカラム")
    for c in df.columns:
        if df[c].isnull().sum() != 0:
            print(c + "　：　" + str(df[c].isnull().sum()))

#カラムの型
def columnsType(df):
    print("カラムの型")
    for c in df.columns:
        print(c + "　：　" + str(df[c].dtypes))

#数値のみカラムの相関
def corr(df, x, y):
  #数値のみカラム
  numeric_columns = df.select_dtypes(include=['number']).columns

  #相関行列を求める
  corr_matrix = df[numeric_columns].corr()

  #相関行列を図示
  plt.figure(figsize=(x, y))
  sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
  plt.title('Correlation Matrix')
  plt.show()

#標準化
def std(df):
  std_scaler = StandardScaler()
  std_scaler.fit(df)
  df_std = pd.DataFrame(std_scaler.transform(df), columns=df.columns)

  return df_std

#ダミー変数
def dummy(df_train, df_test, list, target):
  df_train_dummy = pd.get_dummies(df_train, columns=list)
  df_test_dummy = pd.get_dummies(df_test, columns=list)

  for c in df_train_dummy.columns:
    if c==target:
      continue
    if c not in df_test_dummy:
      df_train_dummy.drop(c, axis=1, inplace=True)

  for c in df_test_dummy.columns:
    if c not in df_train_dummy:
      df_test_dummy.drop(c, axis=1, inplace=True)

  return (df_train_dummy, df_test_dummy)

#target encoding関数
def targetEncoding(df_train, df_test, list):
  #変数定義
  values=[]
  keys1=[]
  keys2=[]
  key_name=[]
  df_train_cat_mean=df_train
  df_test_cat_mean=df_test
  #目的変数の全体平均
  mean=df_train['SalePrice'].mean()

  for c in list:
    array = df_train[c].unique()
    for d in array:
      keys1.append(c)
      keys2.append(d)
      key_name.append(str(c)+"_"+str(d))
      dft = df_train[df_train[c].isin([d])]
      df_train_cat_mean = df_train_cat_mean.replace({c:{d:dft['SalePrice'].mean()}})
      values.append(dft['SalePrice'].mean())
      te_values = pd.DataFrame([keys1, keys2, values], columns=[key_name])

      df_test_cat_mean[str(c)+"_mean"]=mean
      df_test_cat_mean[str(c)+"_mean"]=df_test_cat_mean[str(c)+"_mean"].mask(df_test_cat_mean[c]==d, dft['SalePrice'].mean())
      df_test_cat_mean[c] = df_test_cat_mean[str(c)+"_mean"]
      df_test_cat_mean=df_test_cat_mean.drop(str(c)+"_mean", axis=1)

  return (df_train_cat_mean, df_test_cat_mean, te_values)

