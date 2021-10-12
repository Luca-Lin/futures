import pandas as pd

# https://www.learncodewithmike.com/2020/11/python-pandas-dataframe-tutorial.html

margin_table = pd.read_html("https://www.taifex.com.tw/cht/5/stockMargining")
margin_df = margin_table[0]
# test = margin_df.loc[margin_df["結算保證金適用比例"] == "10.00%"]
# a = test[test["股票期貨英文代碼"] == "CAF"].filter(items=["結算保證金適用比例"])

# a = margin_df["股票期貨英文代碼"]

print("===============")
prices_table = pd.read_html("https://histock.tw/stock/future.aspx")
prices_df = prices_table[0]
# prices_df.to_csv('prices.csv',index=False)

tmp = prices_df.loc[prices_df["到期月份"] == 202110]
filter_price = tmp.filter(items=["契約","成交價"]).rename(columns={"契約": "股票期貨英文代碼", "成交價":"成交價"})

result = pd.merge(margin_df, filter_price, on="股票期貨英文代碼")
print(result)

result.to_csv('result.csv',index=False)

# excel open csv encoding = utf-8
# https://officeguide.cc/excel-import-csv-file-with-utf8-big5-encoding-tutorial-examples/