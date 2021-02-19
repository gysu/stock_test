import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "http://isin.twse.com.tw/isin/C_public.jsp?strMode=2"

#strMode=2就是上市，而strMode=4就是上櫃

res = requests.get(url)

soup = BeautifulSoup(res.text,'lxml')

tables = soup.find("table",{"class":"h4"})
tds = tables.find_all("td")

for td in tds:
    td  = td.getText()
    if td.strip() == "上市認購(售)權證" :
       break
    
