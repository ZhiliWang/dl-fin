import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime

'''pd.read_csv test'''
sse = web.DataReader("000001.ss","yahoo",datetime.datetime(1995,1,1),datetime.date.today())
print (sse)
#print (df_csvsave.index)
#print (df_csvsave.colums)
sse.to_csv(r'~/Documents/fin/sse.csv',columns=df_csvsave.columns,index=True)

