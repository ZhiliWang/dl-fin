import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime

'''
# was planning to do a loop but dynamically doing so is bad in python
tickers = ["^SSMI", "^NDX", "^BSESN", "^BVSP", "^DJI", "^GDAXI", "^GSPC", 
			"^HSI", "^MXX", "^N225", "000001.ss"]
'''
tickers = ["SSMI", "NDX", "BSESN", "BVSP", "DJI", "GDAXI", "GSPC", 
			"HSI", "MXX", "N225", "SSE"]
output_path = ["~/Documents/fin/SSMI",
				"~/Documents/fin/NDX",
				"~/Documents/fin/BSESN",
				"~/Documents/fin/BVSP",
				"~/Documents/fin/DJI",
				"~/Documents/fin/GDAXI",
				"~/Documents/fin/GSPC",
				"~/Documents/fin/HSI",
				"~/Documents/fin/MXX",
				"~/Documents/fin/N225",
				"~/Documents/fin/SSE",]
'''pd.read_csv test'''
# input of DataReader: stock/index ticker, web source, start date, end date
# sse: Shanghai
# deprecated data source: yahoo, google
# available data source: iex, quandl (need free accounts sign-ups)
ssmi = web.DataReader("000001.ss", "yahoo", datetime.datetime(1950,1,1),
					datetime.date.today())
ndx  = web.DataReader("^dji", "yahoo", datetime.datetime(1950,1,1), 
					datetime.date.today())
bxesn = web.DataReader("000001.ss", "yahoo", datetime.datetime(1950,1,1),
					datetime.date.today())
dji  = web.DataReader("^dji", "yahoo", datetime.datetime(1950,1,1), 
					datetime.date.today())
sse = web.DataReader("000001.ss", "yahoo", datetime.datetime(1950,1,1),
					datetime.date.today())
dji  = web.DataReader("^dji", "yahoo", datetime.datetime(1950,1,1), 
					datetime.date.today())
sse = web.DataReader("000001.ss", "yahoo", datetime.datetime(1950,1,1),
					datetime.date.today())
dji  = web.DataReader("^dji", "yahoo", datetime.datetime(1950,1,1), 
					datetime.date.today())
sse = web.DataReader("000001.ss", "yahoo", datetime.datetime(1950,1,1),
					datetime.date.today())
dji  = web.DataReader("^dji", "yahoo", datetime.datetime(1950,1,1), 
					datetime.date.today())
sse = web.DataReader("000001.ss", "yahoo", datetime.datetime(1950,1,1),
					datetime.date.today())
dji  = web.DataReader("^dji", "yahoo", datetime.datetime(1950,1,1), 
					datetime.date.today())



# default columns looks like this: [Date,High,Low,Open,Close,Volume,Adj Close]
# find undeprecated source to change columns

# Check out the data:
###print(sse)
###print(sse.index)
###print(sse.columns)

