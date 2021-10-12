import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://www.taifex.com.tw/cht/5/stockMargining")
soup = BeautifulSoup(response.text, "html.parser")

f = open('output.txt',mode="w",encoding="utf-8")
for item in soup.find_all('table','table_c'):
    print(item.text)
    f.write(item.text)
f.close()