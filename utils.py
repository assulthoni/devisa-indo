import pandas as pd

FILE_PATH = 'data.csv'


def read_data():
    df = pd.read_csv(FILE_PATH)
    return df


def get_year():
    df = read_data()
    return list(df['Tahun'].values)


def get_data_line_chart():
    df = read_data()
    data = df.to_dict('list')
    return data


def get_data_summary_line():
    df = read_data()
    col = [col for col in df.columns if col != 'Tahun']
    df['Total'] = df[col].sum(axis=1)
    return df[['Tahun', 'Total']].to_dict('list')


# print(get_data_summary_line())
