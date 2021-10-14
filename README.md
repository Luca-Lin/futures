## 需求
只需要10月份的股票期貨
需要將 股票期貨價格 * 2000 * 保證金倍率
但價格 與 保證金倍率 在不同網站

[保證金比例網站](https://www.taifex.com.tw/cht/5/stockMargining)
<br>
[股票期貨價格網站](https://histock.tw/stock/future.aspx)
<br>
[StockList.csv 來源](https://goodinfo.tw/StockInfo/StockList.asp?MARKET_CAT=%E6%99%BA%E6%85%A7%E9%81%B8%E8%82%A1&INDUSTRY_CAT=%E8%82%A1%E7%A5%A8%E6%9C%9F%E8%B2%A8%E6%A8%99%E7%9A%84)

## Beautiful Soup

原本使用 Beautiful Soup 做爬蟲工具，但發現 Pandas 在處理表格上更為方便，也有可能是我不會用 Beautiful Soup XD

## Pandas.py

**1.pd.read_html()**<br>
填寫你要爬取的網站

**2.Series and DataFrame**<br>
Series 為單串列資料
DataFrame 為二維資料
這邊抓出來的資料格式為 DataFrame

**3.資料處理**<br>
用 DataFrame.loc 將符合條件的資料篩選出來，條件是 到期月份 == 202110 ，這邊的 到期月份 用dtype看資料格式是 int64
之後使用 DataFrame.filter() 將 欄位是契約及成交價 抓成另一個變數並且重新命名

**4.pd.merge()**<br>
最後再透過 Pandas 提供的 API merge() ，將兩個 dataframe 透過相同的 Key 合併

## Pandas_ReadCSV.py

Pandas.py 的優化版本，爬蟲抓取完[保證金比例網站](https://www.taifex.com.tw/cht/5/stockMargining)之後，自己手動從[這網站下載 StockList.csv](https://goodinfo.tw/StockInfo/StockList.asp?MARKET_CAT=%E6%99%BA%E6%85%A7%E9%81%B8%E8%82%A1&INDUSTRY_CAT=%E8%82%A1%E7%A5%A8%E6%9C%9F%E8%B2%A8%E6%A8%99%E7%9A%84)到 ./csv 目錄，讀取 csv 檔案再透過股票代碼合併。

<br>

合併之後再進行保證金計算