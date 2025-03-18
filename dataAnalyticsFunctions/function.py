def hello():
    return "Hello from analytics!"


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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


