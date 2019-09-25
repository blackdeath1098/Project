import datetime as datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

user_stock_symbol = ""

print("Welcome to the stock tracker")
print("This script is in CLI and gives you the data from yahoo finance for the past week")
print("Please enter the stock symbol you want to know about")
user_stock_symbol = input("")
user_stock_symbol = user_stock_symbol.upper()

#Start and end dates for the timeframe of the stock prices
start = (datetime.datetime.now() - datetime.timedelta(days=7)).date()
end = datetime.datetime.now()


#Reads the price of SPY from yahoo finance from the start date to the end date 
df = web.DataReader(user_stock_symbol, 'yahoo', start, end)

#Prints the data
print(df.head(7))

#df.to_csv('SPY.csv')




