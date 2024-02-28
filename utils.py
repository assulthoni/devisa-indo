import pandas as pd

FILE_PATH = 'Data Cadangan Devisa Indonesia.xlsx'


def read_data(sheet_name='summary long'):
    df = pd.read_excel(FILE_PATH, sheet_name=sheet_name)
    return df


def read_data_detail():
    df = pd.read_excel(FILE_PATH, sheet_name='detail cadangan lain long')
    return df


def get_year():
    df = read_data()
    return list(df['Tahun'].values)


print(read_data().head())
