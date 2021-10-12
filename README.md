## 需求
只需要10月份的股票期貨
需要將 股票期貨價格 * 2000 * 保證金倍率
但價格 與 保證金倍率 在不同網站

[保證金倍率網站](https://www.taifex.com.tw/cht/5/stockMargining)
[股票期貨價格網站](https://histock.tw/stock/future.aspx)

## Beautiful Soup

原本使用 Beautiful Soup 做爬蟲工具，但發現 Pandas 在處理表格上更為方便，也有可能是我不會用 Beautiful Soup XD

## Pandas

**1.pd.read_html()**
填寫你要爬取的網站

**2.Series and DataFrame**
Series 為單串列資料
DataFrame 為二維資料
這邊抓出來的資料格式為 DataFrame

**3.資料處理**
用 DataFrame.loc 將符合條件的資料篩選出來，條件是 到期月份 == 202110 ，這邊的 到期月份 用dtype看資料格式是 int64
之後使用 DataFrame.filter() 將 欄位是契約及成交價 抓成另一個變數並且重新命名

**4.pd.merge()**
最後再透過 Pandas 提供的 API merge() ，將兩個 dataframe 透過相同的 Key 合併
