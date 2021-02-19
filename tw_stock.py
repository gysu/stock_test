import twstock
import numpy as np
import matplotlib.pyplot as plt
import json
import time
import pandas as pd
import plotly.graph_objects as go

print(twstock.codes)
#類別
class Stock:
    #建構式
    def __init__(self, stock_no):
        self.stock_no = stock_no   #股票代號屬性
        print(self.stock_no)

    #方法    
    def bigday3(self):
       # stock_no = '2330'
       
        """即時資料"""
        tw2330=twstock.realtime.get(self.stock_no) 
        print(tw2330)
        
        
        status = tw2330['success']
        print(status)
        try :
            #json轉dataframe
            df = pd.DataFrame(tw2330)
            print(df.head(5))
            name = tw2330['info']['name']
            now_price=tw2330['realtime']['latest_trade_price']
            print('name:{} now_price:{}'.format(name,now_price))
    
            """歷史資料"""
            tw2330=twstock.Stock(self.stock_no) 
            high_price = tw2330.high[-3:] 
       #繪製初始圖框，記得要plot(繪製)及show(顯示)
       # plt.figure(figsize=(24,8) ,dpi=72,facecolor="white",edgecolor="green")
       # plt.plot()
       # plt.show()
       # 獲取 2000 年 10 月至今日之股票資料
            df1 = pd.DataFrame(tw2330.fetch_from(2020, 10))
            print(df1.head())
        

        #print(tw2330.price[-3:])
        #print(tw2330.high[-3:])
        #print(tw2330.low[-3:])
            print( float(now_price) , float(max(high_price)))
            if float(now_price) > float(max(high_price)):
                result='ok'
                return result 
            else:
                result='no'
                return result 
        #jsontext = json.dumps(tw2330)
        #jsontext = json.loads(tw2330)
      
        except :
            result ='false'
            return result
          
        
      
         
stock_no = '2237'
chk = Stock(stock_no)
print(chk.bigday3())    
time.sleep(3)
#  Stock 物件的屬性	 說明
#  price	 傳回近 31 天的收盤價 (單位=元) 串列
#  capacity	 傳回近 31 天的成交量 (單位=股) 串列
#  turnover	 傳回近 31 天的成交金額 (單位=元) 串列
#  transaction	 傳回近 31 天的成交筆數 (單位=筆) 串列
#  close	 傳回近 31 天的收盤價 (單位=元) 串列 (同 price)
#  change	 傳回近 31 天收盤價的漲跌幅 (單位=元) 串列 
#  open 	 傳回近 31 天的開盤價 (單位=元) 串列
#  low	 傳回近 31 天的最低價 (單位=元) 串列
#  high	 傳回近 31 天的最高價 (單位=元) 串列
#  date	 傳回近 31 天的交易日期 datetime 物件串列
#  sid	 傳回股票代號字串
#  data	 傳回近 31 天的 Stock 物件全部資料內容 (Data 物件) 串列
#  raw_data	 傳回近 31 天所擷取之原始資料串列
#stock.fetch_from(2000, 10) # 獲取 2000 年 10 月至今日之股票資料