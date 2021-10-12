import pandas as pd

# https://www.learncodewithmike.com/2020/11/python-pandas-dataframe-tutorial.html
margin_table = pd.read_html("https://www.taifex.com.tw/cht/5/stockMargining")
margin_df = margin_table[0]
print(margin_df)
margin_df.to_csv('margin.csv',index=False)

print("===============")
prices_table = pd.read_html("https://histock.tw/stock/future.aspx")
prices_df = prices_table[0]
print(prices_df)
prices_df.to_csv('prices.csv',index=False)
