import pandas as pd
import matplotlib.pyplot as plt


FILE_NAME = 'koszta.xlsx'

def read_xls(file_name):
    cost_xls = pd.ExcelFile(file_name)

    for index, element in enumerate(cost_xls.sheet_names):
        print('\tAdd ' + element)
        if not index:
            df = cost_xls.parse(index)
        else:
            df = df.join(cost_xls.parse(index), how='outer', lsuffix=element)
#==============================================================================
#     while True:
#         try:
#             month = int(input('Select month, eg. 0 \n'))
#             if month >= 0 and month <= index:
#                 break
#         except ValueError:
#             print('Select correct number')
#==============================================================================
            
    return df

def clear_data_frame(df): 
    df = df[pd.notnull(df.index)]
    df = df.fillna(0)
    df = df.filter(regex='0$', axis=1)
    
    return df

df = read_xls(FILE_NAME)
df = clear_data_frame(df)
print(df.shape)
print(df.transpose().sum())

df['SUM'] = df.transpose().sum()
df = df.sort_values(by='SUM')
print(df.index)
print((df.SUM).sum())