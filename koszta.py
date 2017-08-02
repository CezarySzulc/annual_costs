import pandas as pd
import matplotlib.pyplot as plt


FILE_NAME = 'koszta.xlsx'

def read_xls(file_name):
    """read excel file file and join in one dataFrame"""
    cost_xls = pd.ExcelFile(file_name)

    for index, element in enumerate(cost_xls.sheet_names):
        print('\tAdd ' + element)
        if not index:
            df = cost_xls.parse(index)
        else:
            df = df.join(cost_xls.parse(index), how='outer', lsuffix=element)
            
    return df


def clear_data_frame(df):
    """clear dataFrame"""
    df = df[pd.notnull(df.index)]
    df = df.fillna(0)
    df = df.filter(regex='0$', axis=1)
    
    return df
    
def show_month_costs(df):
    df = df.transpose()
    df.index = pd.to_datetime(df.index)
    df = df.resample('M').sum()
    print(df.sum(axis=1).values)
    plt.plot(df.index, df.sum(axis=1).values, marker = '.', linestyle = 'none')
    plt.xlabel('date')
    plt.ylabel('costs sum')
    plt.margins(0.02)
    plt.grid()
    plt.show()

df = read_xls(FILE_NAME)
df = clear_data_frame(df)
show_month_costs(df)
"""
print(df.shape)
print(df.transpose().sum())
df['SUM'] = df.transpose().sum()
df = df.sort_values(by='SUM')
print(df.index)
print((df.SUM).sum())
"""

