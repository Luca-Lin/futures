import pandas as pd
from datetime import date
# Get Current Date
today = date.today()

# https://www.learncodewithmike.com/2020/11/python-pandas-dataframe-tutorial.html
print("抓取資料1....")
margin_table = pd.read_html("https://www.taifex.com.tw/cht/5/stockMargining")
margin_df = margin_table[0]

print("OK")
print("===============")
print("抓取資料2....")
prices_table = pd.read_html("https://histock.tw/stock/future.aspx")

prices_df = prices_table[-1]
prices_df.to_csv('./csv/prices.csv',index=False)

print(prices_df)
print("OK")
print("開始合併資料表...")
tmp = prices_df.loc[prices_df["到期月份"] == 202110]
filter_price = tmp.filter(items=["契約","成交價"]).rename(columns={"契約": "股票期貨英文代碼", "成交價":"成交價"})

result = pd.merge(margin_df, filter_price, on="股票期貨英文代碼")
print("合併成功....")
print(result)

result.to_csv('./csv/'+str(today)+'.csv',index=False)

# excel open csv encoding = utf-8
# https://officeguide.cc/excel-import-csv-file-with-utf8-big5-encoding-tutorial-examples/