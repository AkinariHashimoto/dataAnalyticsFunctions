import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
#from scipy import stats
#from sklearn.model_selection import train_test_split
#from sklearn.model_selection import KFold


def hello():
    return "Hello from analytics!"


#nullチェック
def nullCheck(df):
    result = {c: df[c].isnull().sum() for c in df.columns if df[c].isnull().sum() != 0}
    print("欠損値を含むカラム")
    for c, count in result.items():
        print(c + "　：　" + str(count))
    return pd.Series(result, name="null_count")


#カラムの型
def columnsType(df):
    result = {c: str(df[c].dtypes) for c in df.columns}
    print("カラムの型")
    for c, dtype in result.items():
        print(c + "　：　" + dtype)
    return pd.Series(result, name="dtype")


#数値のみカラムの相関
def corr(df, x, y):
    numeric_columns = df.select_dtypes(include=['number']).columns
    corr_matrix = df[numeric_columns].corr()

    plt.figure(figsize=(x, y))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()


#標準化
def std(df):
    numeric_df = df.select_dtypes(include=['number'])
    std_scaler = StandardScaler()
    df_std = pd.DataFrame(std_scaler.fit_transform(numeric_df), columns=numeric_df.columns)
    return df_std


#ダミー変数
def dummy(df_train, df_test, columns, target):
    df_train_dummy = pd.get_dummies(df_train.copy(), columns=columns)
    df_test_dummy = pd.get_dummies(df_test.copy(), columns=columns)

    feature_cols = [c for c in df_train_dummy.columns if c != target]
    df_test_dummy = df_test_dummy.reindex(columns=feature_cols, fill_value=0)

    return (df_train_dummy, df_test_dummy)


#target encoding関数
def targetEncoding(df_train, df_test, columns, target):
    values = []
    keys1 = []
    keys2 = []
    key_name = []
    df_train_cat_mean = df_train.copy()
    df_test_cat_mean = df_test.copy()
    mean = df_train[target].mean()

    for c in columns:
        array = df_train[c].unique()
        for d in array:
            keys1.append(c)
            keys2.append(d)
            key_name.append(str(c) + "_" + str(d))
            dft = df_train[df_train[c].isin([d])]
            df_train_cat_mean = df_train_cat_mean.replace({c: {d: dft[target].mean()}})
            values.append(dft[target].mean())

            df_test_cat_mean[str(c) + "_mean"] = mean
            df_test_cat_mean[str(c) + "_mean"] = df_test_cat_mean[str(c) + "_mean"].mask(
                df_test_cat_mean[c] == d, dft[target].mean()
            )
            df_test_cat_mean[c] = df_test_cat_mean[str(c) + "_mean"]
            df_test_cat_mean = df_test_cat_mean.drop(str(c) + "_mean", axis=1)

    te_values = pd.DataFrame([keys1, keys2, values], columns=key_name)

    return (df_train_cat_mean, df_test_cat_mean, te_values)
