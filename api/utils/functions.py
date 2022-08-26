import pandas as pd
import numpy as np
import os


def combineColumns(df):
    if df['description'].isnull().sum() > 0:
        for i in range(len(df['description'])):
            if df['description'][i] is None or df['description'][i] is np.NaN:
                df['description'][i] = ""

    df2 = pd.DataFrame()
    df2['title'] = df['title'].astype(str) + " " + df['description'].astype(str)
    return df2


def downloadFileIfNotAvailable():
    if not os.path.exists("TF-IDF.pkl"):
        print('Downloading missing file TF-IDF.pkl')
        os.system("wget https://store3.gofile.io/download/c9324af4-fb56-4a94-979f-250a8d64371f/TF-IDF.pkl")
    if not os.path.exists("ANN-N.h5"):
        print('Downloading missing file TF-IDF.pkl')
        os.system("wget https://store3.gofile.io/download/264d9274-48b1-4a16-8720-fc94f2c3af50/ANN-N.h")

