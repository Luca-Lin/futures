import pandas as pd
from datetime import date
import os


def main():

    # Get Current Date
    today = date.today()

    # https://www.learncodewithmike.com/2020/11/python-pandas-dataframe-tutorial.html
    print("抓取資料1....")

    filepath = "./csv/margin.csv"
    if os.path.isfile(filepath):
        print("快取成功")
        margin_table = pd.read_csv(filepath)
        margin_df = margin_table
    else:
        print("檔案不存在，重新抓取....")
        margin_table = pd.read_html("https://www.taifex.com.tw/cht/5/stockMargining")
        margin_df = margin_table[0]
        margin_df.to_csv('./csv/margin.csv',index=False)

    print("OK")

    print("=========================================")

    print("讀取CSV檔案....")
    filepath2 = "./csv/StockList.csv"
    if os.path.isfile(filepath2):
        read_csv = pd.read_csv(filepath2)
        print("讀取成功...")
    else:
        print("請確認 csv 資料夾內有沒有名為 StockList.csv 檔案")
        return
    
    read_csv["股票期貨標的證券代號"] = read_csv["代號"].apply(lambda x:x[2:-1]).astype('int64')

    filter_price = read_csv.filter(["股票期貨標的證券代號","成交"])

    result = pd.merge(margin_df, filter_price, on="股票期貨標的證券代號")
    print(result)

    print("合併成功....")
    result.to_csv('./csv/'+str(today)+'.csv',index=False)

    # print("按任意鍵結束")
    # input()

# excel open csv encoding = utf-8
# https://officeguide.cc/excel-import-csv-file-with-utf8-big5-encoding-tutorial-examples/

main()