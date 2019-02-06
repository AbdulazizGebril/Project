
# coding: utf-8

# In[1]:


import requests
import alpha_vantage
import pandas as pd
import csv
from config import api_key
from functools import reduce
from iex import Stock


# In[2]:


API_URL = "https://www.alphavantage.co/query"


# In[3]:


stocks=["aapl"]


# In[4]:


series_type=["open","close","high","low"]


# # DAILY_STOCK_DATA

# In[5]:


daily_open_price=[]
daily_close_price=[]
daily_high_price=[]
daily_low_price=[]
daily_volume=[]
stock_name=[]
daily_date=[]


for stock in stocks:
    data_daily = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "outputsize": "full",
        "datatype": "json",
        "apikey":api_key }

    response_daily = requests.get(API_URL, data_daily)
    stock_data_daily=response_daily.json()
    

    values_daily = stock_data_daily["Time Series (Daily)"]

    
    keys_daily = (values_daily.keys())
    for key in keys_daily:
        stock_name.append(stock)
        daily_date.append(key)
        daily_open_price.append(values_daily[key]['1. open'])
        daily_close_price.append(values_daily[key]['4. close'])
        daily_high_price.append(values_daily[key]['2. high'])
        daily_low_price.append(values_daily[key]['3. low'])
        daily_volume.append(values_daily[key]['5. volume'])
        


# In[6]:


daily_stock_df=pd.DataFrame(stock_name, columns=["Stock"])
daily_stock_df["Date"]=daily_date
daily_stock_df["Open"]=daily_open_price
daily_stock_df["Close"]=daily_close_price
daily_stock_df["High"]=daily_high_price
daily_stock_df["Low"]=daily_low_price
daily_stock_df["Volume"]=daily_volume


# # SMA_VALUES

# In[7]:


sma_open_list=[]
sma_close_list=[]
high_list=[]
low_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        sma_data = {
            "function": "SMA",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey": api_key }
        if series =="open":
            response = requests.get(API_URL, sma_data)
            open_sma=response.json()
            sma_open_values= open_sma["Technical Analysis: SMA"]
            sma_open_keys= (sma_open_values.keys())
            for key in sma_open_keys:
                stock_name.append(stock)
                date.append(key)
                sma_open_list.append(sma_open_values[key]["SMA"])
        if series=="high":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, sma_data)
            high_sma=response.json()
            sma_high_values= high_sma["Technical Analysis: SMA"]
            sma_high_keys= (sma_high_values.keys())
            for key in sma_high_keys:
                stock_name.append(stock)
                date.append(key)
                high_list.append(sma_high_values[key]["SMA"])
        
        if series=="low":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, sma_data)
            low_sma=response.json()
            sma_low_values= low_sma["Technical Analysis: SMA"]
            sma_low_keys= (sma_low_values.keys())
            for key in sma_low_keys:
                stock_name.append(stock)
                date.append(key)
                low_list.append(sma_low_values[key]["SMA"])
                
        
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, sma_data)
            close_sma=response.json()
            sma_close_values= close_sma["Technical Analysis: SMA"]
            sma_close_keys= (sma_close_values.keys())
            for key in sma_close_keys:
                stock_name.append(stock)
                date.append(key)
                sma_close_list.append(sma_close_values[key]["SMA"])

    


# In[8]:


sma_df=pd.DataFrame(stock_name, columns=["Stock"])
sma_df["Date"]=date
sma_df["SMA_OPEN"]=sma_open_list
sma_df["SMA_HIGH"]=high_list
sma_df["SMA_LOW"]=low_list
sma_df["SMA_CLOSE"]=sma_close_list


# # MACD_VALUES

# In[10]:


macd_open_list=[]
macd_hist_open_list=[]
macd_signal_open_list=[]
macd_close_list=[]
macd_hist_close_list=[]
macd_signal_close_list=[]
high_list=[]
high_signal_list=[]
high_hist_list=[]
low_list=[]
low_signal_list=[]
low_hist_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        macd_data = {
            "function": "MACD",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, macd_data)
            open_macd=response.json()
            macd_open_values= open_macd["Technical Analysis: MACD"]
            macd_open_keys= (macd_open_values.keys())
            for key in macd_open_keys:
                stock_name.append(stock)
                date.append(key)
                macd_open_list.append(macd_open_values[key]["MACD"])
                macd_signal_open_list.append(macd_open_values[key]["MACD_Signal"])
                macd_hist_open_list.append(macd_open_values[key]["MACD_Hist"])
        
        if series =="high":
            stock_name=[]                
            date=[]
            response = requests.get(API_URL, macd_data)
            high_macd=response.json()
            macd_high_values= high_macd["Technical Analysis: MACD"]
            macd_high_keys= (macd_high_values.keys())
            for key in macd_high_keys:
                stock_name.append(stock)
                date.append(key)
                high_list.append(macd_high_values[key]["MACD"])
                high_signal_list.append(macd_high_values[key]["MACD_Signal"])
                high_hist_list.append(macd_high_values[key]["MACD_Hist"])
        
        if series =="low":
            stock_name=[]                
            date=[]
            response = requests.get(API_URL, macd_data)
            low_macd=response.json()
            macd_low_values= low_macd["Technical Analysis: MACD"]
            macd_low_keys= (macd_low_values.keys())
            for key in macd_low_keys:
                stock_name.append(stock)
                date.append(key)
                low_list.append(macd_close_values[key]["MACD"])
                low_signal_list.append(macd_close_values[key]["MACD_Signal"])
                low_hist_list.append(macd_close_values[key]["MACD_Hist"])
        
        if series =="close":
            stock_name=[]                
            date=[]
            response = requests.get(API_URL, macd_data)
            close_macd=response.json()
            macd_close_values= close_macd["Technical Analysis: MACD"]
            macd_close_keys= (macd_close_values.keys())
            for key in macd_close_keys:
                stock_name.append(stock)
                date.append(key)
                macd_close_list.append(macd_close_values[key]["MACD"])
                macd_signal_close_list.append(macd_close_values[key]["MACD_Signal"])
                macd_hist_close_list.append(macd_close_values[key]["MACD_Hist"])
        
        


# In[11]:


macd_df=pd.DataFrame(stock_name, columns=["Stock"])
macd_df["Date"]=date
macd_df["MACD_OPEN"]=macd_open_list
macd_df["MACD_SIGNAL_OPEN"]=macd_signal_open_list
macd_df["MACD_HIST_OPEN"]=macd_hist_open_list
macd_df["MACD_HIGH"]=high_list
macd_df["MACD_SIGNAL_HIGH"]=high_signal_list
macd_df["MACD_HIST_HIGH"]=high_hist_list
macd_df["MACD_LOW"]=low_list
macd_df["MACD_SIGNAL_LOW"]=low_signal_list
macd_df["MACD_HIST_LOW"]=low_hist_list
macd_df["MACD_CLOSE"]=macd_close_list
macd_df["MACD_SIGNAL_CLOSE"]=macd_signal_close_list
macd_df["MACD_HIST_CLOSE"]=macd_hist_close_list



# # EMA_VALUES

# In[12]:


ema_open_list=[]
ema_close_list=[]
high_list=[]
low_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        ema_data = {
            "function": "EMA",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, ema_data)
            open_ema=response.json()
            ema_open_values= open_ema["Technical Analysis: EMA"]
            ema_open_keys= (ema_open_values.keys())
            for key in ema_open_keys:
                stock_name.append(stock)
                date.append(key)
                ema_open_list.append(ema_open_values[key]["EMA"])
                
        
        if series=="high":
            stock_name=[]
           
            response = requests.get(API_URL, ema_data)
            high_ema=response.json()
            ema_high_values= high_ema["Technical Analysis: EMA"]
            ema_high_keys= (ema_high_values.keys())
            for key in ema_high_keys:
                if key in date:
                    stock_name.append(stock)
                    high_list.append(ema_high_values[key]["EMA"])
        
        if series=="low":
            stock_name=[]
            
            response = requests.get(API_URL, ema_data)
            low_ema=response.json()
            ema_low_values= low_ema["Technical Analysis: EMA"]
            ema_low_keys= (ema_low_values.keys())
            for key in ema_low_keys:
                if key in date:
                    stock_name.append(stock)
                    low_list.append(ema_low_values[key]["EMA"])
        
        
        
        if series=="close":
            stock_name=[]
            
            response = requests.get(API_URL, ema_data)
            close_ema=response.json()
            ema_close_values= close_ema["Technical Analysis: EMA"]
            ema_close_keys= (ema_close_values.keys())
            for key in ema_close_keys:
                if key in date:
                    stock_name.append(stock)
                    ema_close_list.append(ema_close_values[key]["EMA"])
        


# In[13]:


ema_df=pd.DataFrame(stock_name, columns=["Stock"])
ema_df["Date"]=date
ema_df["EMA_OPEN"]=ema_open_list
ema_df["EMA_HIGH"]=high_list
ema_df["EMA_LOW"]=low_list
ema_df["EMA_CLOSE"]=ema_close_list



# In[14]:





# # RSI_VALUES

# In[15]:


rsi_open_list=[]
rsi_close_list=[]
high_list=[]
low_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        rsi_data = {
            "function": "RSI",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, rsi_data)
            open_rsi=response.json()
            rsi_open_values= open_rsi["Technical Analysis: RSI"]
            rsi_open_keys= (rsi_open_values.keys())
            for key in rsi_open_keys:
                stock_name.append(stock)
                date.append(key)
                rsi_open_list.append(rsi_open_values[key]["RSI"])
                
     
        
        if series=="high":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, rsi_data)
            high_rsi=response.json()
            rsi_high_values= high_rsi["Technical Analysis: RSI"]
            rsi_high_keys= (rsi_high_values.keys())
            for key in rsi_high_keys:
                stock_name.append(stock)
                date.append(key)
                high_list.append(rsi_high_values[key]["RSI"])
        
        
        
        if series=="low":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, rsi_data)
            low_rsi=response.json()
            rsi_low_values= low_rsi["Technical Analysis: RSI"]
            rsi_low_keys= (rsi_low_values.keys())
            for key in rsi_low_keys:
                stock_name.append(stock)
                date.append(key)
                low_list.append(rsi_low_values[key]["RSI"])
        
        
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, rsi_data)
            close_rsi=response.json()
            rsi_close_values= close_rsi["Technical Analysis: RSI"]
            rsi_close_keys= (rsi_close_values.keys())
            for key in rsi_close_keys:
                stock_name.append(stock)
                date.append(key)
                rsi_close_list.append(rsi_close_values[key]["RSI"])


# In[16]:


rsi_df=pd.DataFrame(stock_name, columns=["Stock"])
rsi_df["Date"]=date
rsi_df["RSI_OPEN"]=rsi_open_list
rsi_df["RSI_HIGH"]=high_list
rsi_df["RSI_LOW"]=low_list
rsi_df["RSI_CLOSE"]=rsi_close_list



# # ADX_VALUES

# In[17]:


adx_list=[]
stock_name=[]
date=[]
for stock in stocks:
    adx_data = {
        "function": "ADX",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, adx_data)
    adx_json=response.json()
    adx_values= adx_json["Technical Analysis: ADX"]
    adx_keys= (adx_values.keys())
    for key in adx_keys:
        stock_name.append(stock)
        date.append(key)
        adx_list.append(adx_values[key]["ADX"])
        
    
    


# In[18]:


adx_df=pd.DataFrame(stock_name, columns=["Stock"])
adx_df["Date"]=date
adx_df["ADX_VALUE"]=adx_list


# # STOCH_VALUES

# In[20]:


slowd_list=[]
slowk_list=[]
stock_name=[]
date=[]
for stock in stocks:
    stoch_data = {
        "function": "STOCH",
        "symbol": stock,
        "interval": "daily",
        "fastkperiod":"5",
        "slowkperiod": "3",
        "slowdperiod":"3",
        "datatype":"json",
        "apikey":api_key }
        
    response = requests.get(API_URL, stoch_data)
    stoch_json=response.json()

    

    stoch_values = stoch_json["Technical Analysis: STOCH"]
    
    stoch_keys = (stoch_values.keys())

    for key in stoch_keys:
        stock_name.append(stock)
        date.append(key)
        slowk_list.append(stoch_values[key]['SlowK'])
        slowd_list.append(stoch_values[key]['SlowD'])
       


# In[21]:


stoch_df=pd.DataFrame(stock_name, columns=["Stock"])
stoch_df["Date"]=date
stoch_df["SlowD_VALUES"]=slowd_list
stoch_df["SlowK_VALUES"]=slowk_list

        


# In[22]:


fastk_list=[]
fastd_list=[]
stock_name=[]
date=[]
for stock in stocks:
    stochf_data = {
        "function": "STOCHF",
        "symbol": stock,
        "interval": "daily",
        "fastkperiod":"5",
        "fastdperiod":"3",
        "datatype":"json",
        "apikey":api_key }
        
    response = requests.get(API_URL, stochf_data)
    stochf_json=response.json()
    stochf_values = stochf_json["Technical Analysis: STOCHF"]
    
    stochf_keys = (stochf_values.keys())

    for key in stoch_keys:
        stock_name.append(stock)
        date.append(key)
        fastk_list.append(stochf_values[key]['FastK'])
        fastd_list.append(stochf_values[key]['FastD'])
       


# In[23]:


stochf_df=pd.DataFrame(stock_name, columns=["Stock"])
stochf_df["Date"]=date
stochf_df["FastK_VALUES"]=slowd_list
stochf_df["FastD_VALUES"]=slowk_list


# In[24]:


stoch_table=pd.merge(stoch_df,stochf_df , on=["Date","Stock"])


# # CCI_VALUES

# In[25]:


cci_list=[]
stock_name=[]
date=[]
for stock in stocks:
    cci_data = {
        "function": "CCI",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, cci_data)
    cci_json=response.json()
    cci_values= cci_json["Technical Analysis: CCI"]
    cci_keys= (cci_values.keys())
    for key in cci_keys:
        stock_name.append(stock)
        date.append(key)
        cci_list.append(cci_values[key]["CCI"])
        


# In[26]:


cci_df=pd.DataFrame(stock_name, columns=["Stock"])
cci_df["Date"]=date
cci_df["CCI_VALUE"]=cci_list


# # AROON_VALUES

# In[27]:


aroonUp_list=[]
aroonDown_list=[]
stock_name=[]
date=[]
for stock in stocks:
    aroon_data = {
        "function": "AROON",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, aroon_data)
    aroon_json=response.json()
    aroon_values= aroon_json["Technical Analysis: AROON"]
    

    aroon_keys= (aroon_values.keys())
    for key in aroon_keys:
        stock_name.append(stock)
        date.append(key)
        aroonUp_list.append(aroon_values[key]["Aroon Up"])
        aroonDown_list.append(aroon_values[key]["Aroon Down"])
        


# In[28]:


aroon_df=pd.DataFrame(stock_name, columns=["Stock"])
aroon_df["Date"]=date
aroon_df["AroonUP_VALUE"]=aroonUp_list
aroon_df["AroonDown_VALUE"]=aroonDown_list


# # BBANDS_VALUES

# In[29]:


Ubands_open_list=[]
Mbands_open_list=[]
Lbands_open_list=[]
Ubands_high_list=[]
Mbands_high_list=[]
Lbands_high_list=[]
Ubands_low_list=[]
Mbands_low_list=[]
Lbands_low_list=[]
Ubands_close_list=[]
Mbands_close_list=[]
Lbands_close_list=[]


stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        bbands_data = {
            "function": "BBANDS",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, bbands_data)
            open_bbands=response.json()
            bbands_open_values= open_bbands["Technical Analysis: BBANDS"]
            bbands_open_keys= (bbands_open_values.keys())
            

            for key in bbands_open_keys:
                stock_name.append(stock)
                date.append(key)
                Ubands_open_list.append(bbands_open_values[key]["Real Upper Band"])
                Mbands_open_list.append(bbands_open_values[key]["Real Middle Band"])
                Lbands_open_list.append(bbands_open_values[key]["Real Lower Band"])
                
                
        if series =="high":
            stock_name=[]                
            date=[]
            response = requests.get(API_URL, bbands_data)
            high_bbands=response.json()
            bbands_high_values= high_bbands["Technical Analysis: BBANDS"]
            bbands_high_keys= (bbands_high_values.keys())
            for key in bbands_high_keys:
                stock_name.append(stock)
                date.append(key)
                Ubands_high_list.append(bbands_high_values[key]["Real Upper Band"])
                Mbands_high_list.append(bbands_high_values[key]["Real Middle Band"])
                Lbands_high_list.append(bbands_high_values[key]["Real Lower Band"])
                
        if series =="low":
            stock_name=[]                
            date=[]
            response = requests.get(API_URL, bbands_data)
            low_bbands=response.json()
            bbands_low_values= low_bbands["Technical Analysis: BBANDS"]
            bbands_low_keys= (bbands_low_values.keys())
            for key in bbands_low_keys:
                stock_name.append(stock)
                date.append(key)
                Ubands_low_list.append(bbands_low_values[key]["Real Upper Band"])
                Mbands_low_list.append(bbands_low_values[key]["Real Middle Band"])
                Lbands_low_list.append(bbands_low_values[key]["Real Lower Band"])
        
       
    
        if series =="close":
            stock_name=[]                
            date=[]
            response = requests.get(API_URL, bbands_data)
            close_bbands=response.json()
            bbands_close_values= close_bbands["Technical Analysis: BBANDS"]
            bbands_close_keys= (bbands_close_values.keys())
            for key in bbands_close_keys:
                stock_name.append(stock)
                date.append(key)
                Ubands_close_list.append(bbands_close_values[key]["Real Upper Band"])
                Mbands_close_list.append(bbands_close_values[key]["Real Middle Band"])
                Lbands_close_list.append(bbands_close_values[key]["Real Lower Band"])
        


# In[30]:


bbands_df=pd.DataFrame(stock_name, columns=["Stock"])
bbands_df["Date"]=date
bbands_df["UPPER_BBANDS_OPEN"]=Ubands_open_list
bbands_df["MIDDLE_BBAND_OPEN"]=Mbands_open_list
bbands_df["LOWER_BBAND_OPEN"]=Lbands_open_list
bbands_df["UPPER_BBANDS_HIGH"]=Ubands_high_list
bbands_df["MIDDLE_BBAND_HIGH"]=Mbands_high_list
bbands_df["LOWER_BBAND_HIGH"]=Lbands_high_list
bbands_df["UPPER_BBANDS_LOW"]=Ubands_low_list
bbands_df["MIDDLE_BBAND_LOW"]=Mbands_low_list
bbands_df["LOWER_BBAND_LOW"]=Lbands_low_list
bbands_df["UPPER_BBAND_CLOSE"]=Ubands_close_list
bbands_df["MIDDLE_BBAND_CLOSE"]=Mbands_close_list
bbands_df["LOWER_BBAND_CLOSE"]=Lbands_close_list




# # Chaikin A/D_VALUES

# In[31]:


ad_list=[]
stock_name=[]
date=[]
for stock in stocks:
    ad_data = {
        "function": "AD",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, ad_data)
    ad_json=response.json()
    ad_values= ad_json["Technical Analysis: Chaikin A/D"]
    ad_keys= (ad_values.keys())
    for key in ad_keys:
        stock_name.append(stock)
        date.append(key)
        ad_list.append(ad_values[key]["Chaikin A/D"])
        


# In[32]:


ad_df=pd.DataFrame(stock_name, columns=["Stock"])
ad_df["Date"]=date
ad_df["Chaikin A/D_VALUE"]=ad_list


# # OBV_VALUES

# In[33]:


obv_list=[]
stock_name=[]
date=[]
for stock in stocks:
    obv_data = {
        "function": "OBV",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, obv_data)
    obv_json=response.json()
    obv_values= obv_json["Technical Analysis: OBV"]
    obv_keys= (obv_values.keys())
    for key in obv_keys:
        stock_name.append(stock)
        date.append(key)
        obv_list.append(obv_values[key]["OBV"])


# In[34]:


obv_df=pd.DataFrame(stock_name, columns=["Stock"])
obv_df["Date"]=date
obv_df["OBV_VALUES"]=obv_list


# # MINUS_DI , MINUS_DM, PLUS_DI, PLUS_DM --------VALUES

# In[35]:


functions_pm=["MINUS_DI","MINUS_DM","PLUS_DI","PLUS_DM"]
minusDi_list=[]
minusDm_list=[]
plusDi_list=[]
plusDm_list=[]
stock_name=[]
date=[]
date_1=[]
for function in functions_pm:
    for stock in stocks:
        pm_data = {
            "function": function,
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "datatype": "json",
            "apikey":api_key }
        if function == "MINUS_DI":
            response = requests.get(API_URL, pm_data)
            minusDi_json=response.json()
            minusDi_values= minusDi_json["Technical Analysis: MINUS_DI"]
            minusDi_keys= (minusDi_values.keys())
            for key in minusDi_keys:
                stock_name.append(stock)
                date.append(key)
                minusDi_list.append(minusDi_values[key]["MINUS_DI"])
                
        elif function == "MINUS_DM":
            stock_name=[]
            response = requests.get(API_URL, pm_data)
            minusDM_json=response.json()
            minusDM_values= minusDM_json["Technical Analysis: MINUS_DM"]
            minusDM_keys= (minusDM_values.keys())
            for key in minusDM_keys:
                stock_name.append(stock)
                if key in date:
                    minusDm_list.append(minusDM_values[key]["MINUS_DM"])
        
        elif function == "PLUS_DI":
            stock_name=[]
            response = requests.get(API_URL, pm_data)
            plusDi_json=response.json()
            plusDi_values= plusDi_json["Technical Analysis: PLUS_DI"]
            plusDi_keys= (plusDi_values.keys())
            for key in plusDi_keys:
                stock_name.append(stock)
                if key in date:
                    plusDi_list.append(plusDi_values[key]["PLUS_DI"])
                
        
        elif function == "PLUS_DM":
            #stock_name=[]
            response = requests.get(API_URL, pm_data)
            plusDm_json=response.json()
            plusDm_values= plusDm_json["Technical Analysis: PLUS_DM"]
            plusDm_keys= (plusDm_values.keys())
            for key in plusDm_keys:
                if key in date:
                    plusDm_list.append(plusDm_values[key]["PLUS_DM"])
                
            
       
                


# In[36]:


plus_df=pd.DataFrame(stock_name, columns=["Stock"])
plus_df["Date"]=date
plus_df["MINUS_DI"]=minusDi_list
plus_df["MINUS_DM"]=minusDm_list
plus_df["PLUS_DI"]=plusDi_list
plus_df["PLUS_DM"]=plusDm_list






# # WMA-DEMA-TRIMA-TEMA---------VALUES

# In[38]:


tema_open_list=[]
tema_close_list=[]
dema_open_list=[]
dema_close_list=[]
stock_name=[]
date=[]
functions=["TEMA","DEMA"]
for stock in stocks:
    for function in functions:
        for series in series_type:
            data = {
                "function": function,
                "symbol": stock,
                "interval": "daily",
                "time_period":"60",
                "series_type": series,
                "datatype": "json",
                "apikey":api_key }
            if series =="open" and function == "TEMA":
                response = requests.get(API_URL, data)
                open_tema=response.json()
        
                tema_open_values= open_tema["Technical Analysis: TEMA"]
                tema_open_keys= (tema_open_values.keys())
                for key in tema_open_keys:
                    stock_name.append(stock)
                    date.append(key)
                    tema_open_list.append(tema_open_values[key]["TEMA"])
                
            if series =="open" and function =="DEMA":
                response = requests.get(API_URL, data)
                open_dema=response.json()
                dema_open_values= open_dema["Technical Analysis: DEMA"]
                dema_open_keys= (dema_open_values.keys())
                for key in dema_open_keys:
                    if key in date:
                        dema_open_list.append(dema_open_values[key]["DEMA"])
                
            if series=="close" and function =="TEMA":
                response = requests.get(API_URL, data)
                close_tema=response.json()
                tema_close_values= close_tema["Technical Analysis: TEMA"]
                tema_close_keys= (tema_close_values.keys())
                for key in tema_close_keys:
                    if key in date:
                        tema_close_list.append(tema_close_values[key]["TEMA"])
        
            if series=="close" and function =="DEMA":
                response = requests.get(API_URL, data)
                close_dema=response.json()
                dema_close_values= close_dema["Technical Analysis: DEMA"]
                dema_close_keys= (dema_close_values.keys())
                for key in dema_close_keys:
                    if key in date:
                        dema_close_list.append(dema_close_values[key]["DEMA"])
        


# In[39]:


dt_df=pd.DataFrame(stock_name, columns=["Stock"])
dt_df["Date"]=date
dt_df["TEMA_OPEN"]=tema_open_list
dt_df["TEMA_CLOSE"]=tema_close_list
dt_df["DEMA_OPEN"]=dema_open_list
dt_df["DEMA_CLOSE"]=dema_close_list


# # CMO_VALUES

# In[41]:


cmo_open_list=[]
cmo_close_list=[]
high_list=[]
low_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        cmo_data = {
            "function": "CMO",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, cmo_data)
            open_cmo=response.json()
            cmo_open_values= open_cmo["Technical Analysis: CMO"]
            cmo_open_keys= (cmo_open_values.keys())
            for key in cmo_open_keys:
                stock_name.append(stock)
                date.append(key)
                cmo_open_list.append(cmo_open_values[key]["CMO"])
                
        if series=="high":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, cmo_data)
            high_cmo=response.json()
            cmo_high_values= high_cmo["Technical Analysis: CMO"]
            cmo_high_keys= (cmo_high_values.keys())
            for key in cmo_high_keys:
                stock_name.append(stock)
                date.append(key)
                high_list.append(cmo_high_values[key]["CMO"])
                 
        if series=="low":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, cmo_data)
            low_cmo=response.json()
            cmo_low_values= low_cmo["Technical Analysis: CMO"]
            cmo_low_keys= (cmo_low_values.keys())
            for key in cmo_low_keys:
                stock_name.append(stock)
                date.append(key)
                low_list.append(cmo_low_values[key]["CMO"])
        
        
        
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, cmo_data)
            close_cmo=response.json()
            cmo_close_values= close_cmo["Technical Analysis: CMO"]
            cmo_close_keys= (cmo_close_values.keys())
            for key in cmo_close_keys:
                stock_name.append(stock)
                date.append(key)
                cmo_close_list.append(cmo_close_values[key]["CMO"])
        


# In[42]:


cmo_df=pd.DataFrame(stock_name, columns=["Stock"])
cmo_df["Date"]=date
cmo_df["CMO_OPEN"]=cmo_open_list
cmo_df["CMO_HIGH"]=high_list
cmo_df["CMO_LOW"]=low_list
cmo_df["CMO_CLOSE"]=cmo_close_list


# # ROC_VALUES

# In[43]:


roc_open_list=[]
roc_close_list=[]
high_list=[]
low_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        roc_data = {
            "function": "ROC",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, roc_data)
            open_roc=response.json()
            roc_open_values= open_roc["Technical Analysis: ROC"]
            roc_open_keys= (roc_open_values.keys())
            for key in roc_open_keys:
                stock_name.append(stock)
                date.append(key)
                roc_open_list.append(roc_open_values[key]["ROC"])
                
        if series=="high":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, roc_data)
            high_roc=response.json()
            roc_high_values= high_roc["Technical Analysis: ROC"]
            roc_high_keys= (roc_high_values.keys())
            for key in roc_high_keys:
                stock_name.append(stock)
                date.append(key)
                high_list.append(roc_high_values[key]["ROC"])
                
        if series=="low":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, roc_data)
            low_roc=response.json()
            roc_low_values= low_roc["Technical Analysis: ROC"]
            roc_low_keys= (roc_low_values.keys())
            for key in roc_low_keys:
                stock_name.append(stock)
                date.append(key)
                low_list.append(roc_low_values[key]["ROC"])
        
        
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, roc_data)
            close_roc=response.json()
            roc_close_values= close_roc["Technical Analysis: ROC"]
            roc_close_keys= (roc_close_values.keys())
            for key in roc_close_keys:
                stock_name.append(stock)
                date.append(key)
                roc_close_list.append(roc_close_values[key]["ROC"])
        


# In[44]:


roc_df=pd.DataFrame(stock_name, columns=["Stock"])
roc_df["Date"]=date
roc_df["ROC_OPEN"]=roc_open_list
roc_df["ROC_HIGH"]=high_list
roc_df["ROC_LOW"]=low_list
roc_df["ROC_CLOSE"]=roc_close_list


# # ROCR_VALUES

# In[46]:


rocr_open_list=[]
rocr_close_list=[]
high_list=[]
low_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        rocr_data = {
            "function": "ROCR",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, rocr_data)
            open_rocr=response.json()
            rocr_open_values= open_rocr["Technical Analysis: ROCR"]
            rocr_open_keys= (rocr_open_values.keys())
            for key in rocr_open_keys:
                stock_name.append(stock)
                date.append(key)
                rocr_open_list.append(rocr_open_values[key]["ROCR"])
                
        
        if series=="high":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, rocr_data)
            high_rocr=response.json()
            rocr_high_values= high_rocr["Technical Analysis: ROCR"]
            rocr_high_keys= (rocr_high_values.keys())
            for key in rocr_high_keys:
                stock_name.append(stock)
                date.append(key)
                high_list.append(rocr_high_values[key]["ROCR"])
                
        if series=="low":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, rocr_data)
            low_rocr=response.json()
            rocr_low_values= low_rocr["Technical Analysis: ROCR"]
            rocr_low_keys= (rocr_low_values.keys())
            for key in roc_low_keys:
                stock_name.append(stock)
                date.append(key)
                low_list.append(rocr_low_values[key]["ROCR"])
        
        
        
        
        
        
        
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, rocr_data)
            close_rocr=response.json()
            rocr_close_values= close_rocr["Technical Analysis: ROCR"]
            rocr_close_keys= (rocr_close_values.keys())
            for key in rocr_close_keys:
                stock_name.append(stock)
                date.append(key)
                rocr_close_list.append(rocr_close_values[key]["ROCR"])
        


# In[47]:


rocr_df=pd.DataFrame(stock_name, columns=["Stock"])
rocr_df["Date"]=date
rocr_df["ROCR_OPEN"]=rocr_open_list
rocr_df["ROCR_HIGH"]=high_list
rocr_df["ROCR_LOW"]=low_list
rocr_df["ROCR_CLOSE"]=rocr_close_list



# # ADXR_VALUES

# In[48]:


adxr_list=[]
stock_name=[]
date=[]
for stock in stocks:
    adxr_data = {
        "function": "ADXR",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, adxr_data)
    adxr_json=response.json()
    adxr_values= adxr_json["Technical Analysis: ADXR"]
    adxr_keys= (adxr_values.keys())
    for key in adxr_keys:
        stock_name.append(stock)
        date.append(key)
        adxr_list.append(adxr_values[key]["ADXR"])
        


# In[49]:


adxr_df=pd.DataFrame(stock_name, columns=["Stock"])
adxr_df["Date"]=date
adxr_df["ADXR_VALUE"]=adxr_list


# # APO_VALUES

# In[50]:


apo_open_list=[]
apo_close_list=[]
high_list=[]
low_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        apo_data = {
            "function": "APO",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, apo_data)
            open_apo=response.json()
            apo_open_values= open_apo["Technical Analysis: APO"]
            apo_open_keys= (apo_open_values.keys())
            for key in apo_open_keys:
                stock_name.append(stock)
                date.append(key)
                apo_open_list.append(apo_open_values[key]["APO"])
        
        if series=="high":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, apo_data)
            high_apo=response.json()
            apo_high_values= high_apo["Technical Analysis: APO"]
            apo_high_keys= (apo_high_values.keys())
            for key in apo_high_keys:
                stock_name.append(stock)
                date.append(key)
                high_list.append(apo_high_values[key]["APO"])
        
        
        if series=="low":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, apo_data)
            low_apo=response.json()
            apo_low_values= low_apo["Technical Analysis: APO"]
            apo_low_keys= (apo_low_values.keys())
            for key in apo_low_keys:
                stock_name.append(stock)
                date.append(key)
                low_list.append(apo_low_values[key]["APO"])
        
        
        
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, apo_data)
            close_apo=response.json()
            apo_close_values= close_apo["Technical Analysis: APO"]
            apo_close_keys= (apo_close_values.keys())
            for key in apo_close_keys:
                stock_name.append(stock)
                date.append(key)
                apo_close_list.append(apo_close_values[key]["APO"])


# In[51]:


apo_df=pd.DataFrame(stock_name, columns=["Stock"])
apo_df["Date"]=date
apo_df["APO_OPEN"]=apo_open_list
apo_df["APO_HIGH"]=high_list
apo_df["APO_LOW"]=low_list
apo_df["APO_CLOSE"]=apo_close_list


# # PPO_VALUES

# In[53]:


ppo_open_list=[]
ppo_close_list=[]
high_list=[]
low_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        ppo_data = {
            "function": "PPO",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, ppo_data)
            open_ppo=response.json()
            ppo_open_values= open_ppo["Technical Analysis: PPO"]
            ppo_open_keys= (ppo_open_values.keys())
            for key in ppo_open_keys:
                stock_name.append(stock)
                date.append(key)
                ppo_open_list.append(ppo_open_values[key]["PPO"])
                
                
        if series=="high":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, ppo_data)
            high_ppo=response.json()
            ppo_high_values= high_ppo["Technical Analysis: PPO"]
            ppo_high_keys= (ppo_high_values.keys())
            for key in ppo_high_keys:
                stock_name.append(stock)
                date.append(key)
                high_list.append(ppo_high_values[key]["PPO"])
        
        
        if series=="low":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, ppo_data)
            low_ppo=response.json()
            ppo_low_values= low_ppo["Technical Analysis: PPO"]
            ppo_low_keys= (ppo_low_values.keys())
            for key in ppo_low_keys:
                stock_name.append(stock)
                date.append(key)
                low_list.append(ppo_low_values[key]["PPO"])
        
        
        
        
        
        
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, ppo_data)
            close_ppo=response.json()
            ppo_close_values= close_ppo["Technical Analysis: PPO"]
            ppo_close_keys= (ppo_close_values.keys())
            for key in ppo_close_keys:
                stock_name.append(stock)
                date.append(key)
                ppo_close_list.append(ppo_close_values[key]["PPO"])


# In[54]:


ppo_df=pd.DataFrame(stock_name, columns=["Stock"])
ppo_df["Date"]=date
ppo_df["PPO_OPEN"]=ppo_open_list
ppo_df["PPO_HIGH"]=high_list
ppo_df["PPO_LOW"]=low_list
ppo_df["PPO_CLOSE"]=ppo_close_list


# # MOM_VALUES

# In[56]:


mom_open_list=[]
mom_close_list=[]
high_list=[]
low_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        mom_data = {
            "function": "MOM",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, mom_data)
            open_mom=response.json()
            mom_open_values= open_mom["Technical Analysis: MOM"]
            mom_open_keys= (mom_open_values.keys())
            for key in mom_open_keys:
                stock_name.append(stock)
                date.append(key)
                mom_open_list.append(mom_open_values[key]["MOM"])
                
        
        if series=="high":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, mom_data)
            high_mom=response.json()
            mom_high_values= high_mom["Technical Analysis: MOM"]
            mom_high_keys= (mom_high_values.keys())
            for key in mom_high_keys:
                stock_name.append(stock)
                date.append(key)
                high_list.append(mom_high_values[key]["MOM"])
        
        if series=="low":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, mom_data)
            low_mom=response.json()
            mom_low_values= low_mom["Technical Analysis: MOM"]
            mom_low_keys= (mom_low_values.keys())
            for key in mom_low_keys:
                stock_name.append(stock)
                date.append(key)
                low_list.append(mom_low_values[key]["MOM"])
        
        
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, mom_data)
            close_mom=response.json()
            mom_close_values= close_mom["Technical Analysis: MOM"]
            mom_close_keys= (mom_close_values.keys())
            for key in mom_close_keys:
                stock_name.append(stock)
                date.append(key)
                mom_close_list.append(mom_close_values[key]["MOM"])


# In[57]:


mom_df=pd.DataFrame(stock_name, columns=["Stock"])
mom_df["Date"]=date
mom_df["MOM_OPEN"]=mom_open_list
mom_df["MOM_HIGH"]=high_list
mom_df["MOM_LOW"]=low_list
mom_df["MOM_CLOSE"]=mom_close_list


# # BOP_VALUES

# In[58]:


bop_list=[]
stock_name=[]
date=[]
for stock in stocks:
    bop_data = {
        "function": "BOP",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, bop_data)
    bop_json=response.json()
    bop_values= bop_json["Technical Analysis: BOP"]
    bop_keys= (bop_values.keys())
    for key in bop_keys:
        stock_name.append(stock)
        date.append(key)
        bop_list.append(bop_values[key]["BOP"])
        


# In[59]:


bop_df=pd.DataFrame(stock_name, columns=["Stock"])
bop_df["Date"]=date
bop_df["BOP_VALUE"]=bop_list


# # MFI_VALUES

# In[60]:


mfi_list=[]
stock_name=[]
date=[]
for stock in stocks:
    mfi_data = {
        "function": "MFI",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, mfi_data)
    mfi_json=response.json()
    mfi_values= mfi_json["Technical Analysis: MFI"]
    mfi_keys= (mfi_values.keys())
    for key in mfi_keys:
        stock_name.append(stock)
        date.append(key)
        mfi_list.append(mfi_values[key]["MFI"])
        


# In[61]:


mfi_df=pd.DataFrame(stock_name, columns=["Stock"])
mfi_df["Date"]=date
mfi_df["MFI_VALUE"]=mfi_list


# # DX_VALUES

# In[62]:


dx_list=[]
stock_name=[]
date=[]
for stock in stocks:
    dx_data = {
        "function": "DX",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, dx_data)
    dx_json=response.json()
    dx_values= dx_json["Technical Analysis: DX"]
    dx_keys= (dx_values.keys())
    for key in dx_keys:
        stock_name.append(stock)
        date.append(key)
        dx_list.append(dx_values[key]["DX"])
        


# In[63]:


dx_df=pd.DataFrame(stock_name, columns=["Stock"])
dx_df["Date"]=date
dx_df["DX_VALUE"]=dx_list


# # SAR_VALUES

# In[64]:


sar_list=[]
stock_name=[]
date=[]
for stock in stocks:
    sar_data = {
        "function": "SAR",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, sar_data)
    sar_json=response.json()
    sar_values= sar_json["Technical Analysis: SAR"]
    sar_keys= (sar_values.keys())
    for key in sar_keys:
        stock_name.append(stock)
        date.append(key)
        sar_list.append(sar_values[key]["SAR"])


# In[65]:


sar_df=pd.DataFrame(stock_name, columns=["Stock"])
sar_df["Date"]=date
sar_df["SAR_VALUE"]=sar_list


# # TRANGE_VALUES

# In[66]:


trange_list=[]
stock_name=[]
date=[]
for stock in stocks:
    trange_data = {
        "function": "TRANGE",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, trange_data)
    trange_json=response.json()
    trange_values= trange_json["Technical Analysis: TRANGE"]
    trange_keys= (trange_values.keys())
    for key in trange_keys:
        stock_name.append(stock)
        date.append(key)
        trange_list.append(trange_values[key]["TRANGE"])


# In[67]:


trange_df=pd.DataFrame(stock_name, columns=["Stock"])
trange_df["Date"]=date
trange_df["TRANGE_VALUE"]=trange_list


# # ATR_VALUES

# In[68]:


atr_list=[]
stock_name=[]
date=[]
for stock in stocks:
    atr_data = {
        "function": "ATR",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, atr_data)
    atr_json=response.json()
    atr_values= atr_json["Technical Analysis: ATR"]
    atr_keys= (atr_values.keys())
    for key in atr_keys:
        stock_name.append(stock)
        date.append(key)
        atr_list.append(atr_values[key]["ATR"])


# In[69]:


atr_df=pd.DataFrame(stock_name, columns=["Stock"])
atr_df["Date"]=date
atr_df["ATR_VALUE"]=atr_list


# # NATR_VALUES

# In[70]:


natr_list=[]
stock_name=[]
date=[]
for stock in stocks:
    natr_data = {
        "function": "NATR",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, natr_data)
    natr_json=response.json()
    natr_values= natr_json["Technical Analysis: NATR"]
    natr_keys= (natr_values.keys())
    for key in natr_keys:
        stock_name.append(stock)
        date.append(key)
        natr_list.append(natr_values[key]["NATR"])


# In[71]:


natr_df=pd.DataFrame(stock_name, columns=["Stock"])
natr_df["Date"]=date
natr_df["NATR_VALUE"]=natr_list


# # WILLR_VALUES

# In[72]:


willr_list=[]
stock_name=[]
date=[]
for stock in stocks:
    willr_data = {
        "function": "WILLR",
        "symbol": stock,
        "interval": "daily",
        "time_period":"60",
        "datatype": "json",
        "apikey":api_key }
        
    response = requests.get(API_URL, willr_data)
    willr_json=response.json()
    willr_values= willr_json["Technical Analysis: WILLR"]
    willr_keys= (willr_values.keys())
    for key in willr_keys:
        stock_name.append(stock)
        date.append(key)
        willr_list.append(willr_values[key]["WILLR"])
        
    


# In[73]:


willr_df=pd.DataFrame(stock_name, columns=["Stock"])
willr_df["Date"]=date
willr_df["WILLR_VALUE"]=willr_list


# # HT_TRENDLINE, SINE, TRENDMODE, DCPERIOD, DCPHASE, PHASOR_VALUES

# In[74]:


open_list=[]
close_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        data = {
            "function": "HT_TRENDLINE",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, data)
            open_data=response.json()
            open_values= open_data["Technical Analysis: HT_TRENDLINE"]
            open_keys= (open_values.keys())
            for key in open_keys:
                stock_name.append(stock)
                date.append(key)
                open_list.append(open_values[key]["HT_TRENDLINE"])
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, data)
            close_data=response.json()
            close_values= close_data["Technical Analysis: HT_TRENDLINE"]
            close_keys= (close_values.keys())
            for key in close_keys:
                stock_name.append(stock)
                date.append(key)
                close_list.append(close_values[key]["HT_TRENDLINE"])
        


# In[75]:


trendline_df=pd.DataFrame(stock_name, columns=["Stock"])
trendline_df["Date"]=date
trendline_df["HT_TRENDLINE_OPEN"]=open_list
trendline_df["HT_TRENDLINE_CLOSE"]=close_list


# In[76]:


open_list=[]
open_list_2=[]
close_list=[]
close_list_2=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        data = {
            "function": "HT_SINE",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, data)
            open_data=response.json()
            open_values= open_data["Technical Analysis: HT_SINE"]
            open_keys= (open_values.keys())
            for key in open_keys:
                stock_name.append(stock)
                date.append(key)
                open_list.append(open_values[key]["LEAD SINE"])
                open_list_2.append(open_values[key]["SINE"])
                
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, data)
            close_data=response.json()
            close_values= close_data["Technical Analysis: HT_SINE"]
            close_keys= (close_values.keys())
            for key in close_keys:
                stock_name.append(stock)
                date.append(key)
                close_list.append(close_values[key]["LEAD SINE"])
                close_list_2.append(close_values[key]["SINE"])
        
        


# In[77]:


sine_df=pd.DataFrame(stock_name, columns=["Stock"])
sine_df["Date"]=date
sine_df["LEAD_SINE_OPEN"]=open_list
sine_df["SINE_OPEN"]=open_list_2
sine_df["LEAD_SINE_CLOSE"]=close_list
sine_df["SINE_CLOSE"]=close_list_2


# In[78]:


open_list=[]
close_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        data = {
            "function": "HT_TRENDMODE",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, data)
            open_data=response.json()
           

            open_values= open_data["Technical Analysis: HT_TRENDMODE"]
            open_keys= (open_values.keys())
            for key in open_keys:
                stock_name.append(stock)
                date.append(key)
                open_list.append(open_values[key]["TRENDMODE"])
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, data)
            close_data=response.json()
            close_values= close_data["Technical Analysis: HT_TRENDMODE"]
            close_keys= (close_values.keys())
            for key in close_keys:
                stock_name.append(stock)
                date.append(key)
                close_list.append(close_values[key]["TRENDMODE"])
        


# In[79]:


trendmode_df=pd.DataFrame(stock_name, columns=["Stock"])
trendmode_df["Date"]=date
trendmode_df["HT_TRENDMODE_OPEN"]=open_list
trendmode_df["HT_TRENDMODE_CLOSE"]=close_list


# In[80]:


open_list=[]
close_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        data = {
            "function": "HT_DCPERIOD",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, data)
            open_data=response.json()


            open_values= open_data["Technical Analysis: HT_DCPERIOD"]
            open_keys= (open_values.keys())
            for key in open_keys:
                stock_name.append(stock)
                date.append(key)
                open_list.append(open_values[key]["DCPERIOD"])
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, data)
            close_data=response.json()
            close_values= close_data["Technical Analysis: HT_DCPERIOD"]
            close_keys= (close_values.keys())
            for key in close_keys:
                stock_name.append(stock)
                date.append(key)
                close_list.append(close_values[key]["DCPERIOD"])
        


# In[81]:


dcperiod_df=pd.DataFrame(stock_name, columns=["Stock"])
dcperiod_df["Date"]=date
dcperiod_df["HT_DCPERIOD_OPEN"]=open_list
dcperiod_df["HT_DCPERIOD_CLOSE"]=close_list


# In[82]:


open_list=[]
close_list=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        data = {
            "function": "HT_DCPHASE",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, data)
            open_data=response.json()


            open_values= open_data["Technical Analysis: HT_DCPHASE"]
            open_keys= (open_values.keys())
            for key in open_keys:
                stock_name.append(stock)
                date.append(key)
                open_list.append(open_values[key]["HT_DCPHASE"])
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, data)
            close_data=response.json()
            close_values= close_data["Technical Analysis: HT_DCPHASE"]
            close_keys= (close_values.keys())
            for key in close_keys:
                stock_name.append(stock)
                date.append(key)
                close_list.append(close_values[key]["HT_DCPHASE"])
        


# In[83]:


dcphase_df=pd.DataFrame(stock_name, columns=["Stock"])
dcphase_df["Date"]=date
dcphase_df["HT_DCPHASE_OPEN"]=open_list
dcphase_df["HT_DCPHASE_CLOSE"]=close_list


# In[85]:


open_list=[]
open_list_2=[]
close_list=[]
close_list_2=[]
stock_name=[]
date=[]
for stock in stocks:
    for series in series_type:
        data = {
            "function": "HT_PHASOR",
            "symbol": stock,
            "interval": "daily",
            "time_period":"60",
            "series_type": series,
            "datatype": "json",
            "apikey":api_key }
        if series =="open":
            response = requests.get(API_URL, data)
            open_data=response.json()


            open_values= open_data["Technical Analysis: HT_PHASOR"]
            open_keys= (open_values.keys())
            for key in open_keys:
                stock_name.append(stock)
                date.append(key)
                open_list.append(open_values[key]["PHASE"])
                open_list_2.append(open_values[key]["QUADRATURE"])
        if series=="close":
            stock_name=[]
            date=[]
            response = requests.get(API_URL, data)
            close_data=response.json()
            close_values= close_data["Technical Analysis: HT_PHASOR"]
            close_keys= (close_values.keys())
            for key in close_keys:
                stock_name.append(stock)
                date.append(key)
                close_list.append(close_values[key]["PHASE"])
                close_list_2.append(close_values[key]["QUADRATURE"])
        
        


# In[86]:


phasor_df=pd.DataFrame(stock_name, columns=["Stock"])
phasor_df["Date"]=date
phasor_df["HT_PHASE_OPEN"]=open_list
phasor_df["HT_QUADRATURE_OPEN"]=open_list_2
phasor_df["HT_PHASE_CLOSE"]=close_list
phasor_df["HT_QUADRATURE_CLOSE"]=close_list_2


# # MERGED_DATAFRAMES

# In[87]:


dfs=[daily_stock_df, sma_df, macd_df, ema_df, rsi_df, adx_df, stoch_table, cci_df, aroon_df, bbands_df, ad_df, obv_df, plus_df, dt_df, cmo_df, roc_df, rocr_df, adx_df, apo_df, ppo_df, mom_df, bop_df, mfi_df, dx_df, sar_df, trange_df, atr_df, natr_df, willr_df, trendline_df, sine_df, trendmode_df, dcperiod_df, dcphase_df, phasor_df]


# In[88]:


df_final = reduce(lambda left,right: pd.merge(left,right,how="left", on=['Date','Stock']), dfs)


# In[89]:


stock_summary=df_final.fillna(0)


# In[90]:


stock_summary.to_csv("apple_stock_summary.csv", index=False)


# # IEX_DATA

# In[118]:


API_URL= "https://api.iextrading.com/1.0"


# In[119]:


for stock in stocks:
    stockTicker=Stock(stock)
    chart_df= stockTicker.chart_table(range="5y")
    spread_df= stockTicker.effective_spread_table()
    splits=stockTicker.splits(range="5y")
    financials_df=stockTicker.financials()
    stats=stockTicker.stats()


# In[120]:


for stock in stocks:
    response = requests.get(API_URL + "/stock" + "/" + stock + "/dividends" + "/5y")
    dividends_data= response.json()


# In[121]:


for stock in stocks:
    response = requests.get(API_URL + "/stock" + "/" + stock + "/earnings")
    earnings_data= response.json()


# In[122]:


with open('earnings.csv', mode='w') as csv_file:
    fieldnames = ['Stock', 'ACTUAL_EPS',"CONCENSUS_EPS","ESTIMATED_EPS",
                  "ESTIMATES","EPS_DOLLAR","FISCAL_PERIOD","Date",
                  "YEAR_AGO","YEAR_%CHANGE","ESTIMATE_%CHANGE"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    
    
    writer.writeheader()
    for stock in stocks:
        y=earnings_data["earnings"]
        for data in y:
            writer.writerow({"Stock": stock,
                             'ACTUAL_EPS':data["actualEPS"],
                             "CONCENSUS_EPS":data['consensusEPS'],
                             "ESTIMATED_EPS":data['estimatedEPS'],
                             "ESTIMATES":data['numberOfEstimates'],
                             "EPS_DOLLAR":data['EPSSurpriseDollar'],
                             "FISCAL_PERIOD":data['fiscalPeriod'],
                             "Date":data['fiscalEndDate'],
                             "YEAR_AGO":data['yearAgo'],
                             "YEAR_%CHANGE":data['yearAgoChangePercent'],
                             "ESTIMATE_%CHANGE":data['estimatedChangePercent'] })
        


# In[124]:


with open('financials.csv', mode='w') as csv_file:
    fieldnames = ['Stock', 'Date',"GROSS_PROFIT",
                  "REVENUE_COST","OPERATING_REVENUE","TOTAL_REVENUE",
                  "OPERATING_INCOME","NET_INCOME","RND","OPERATING_EXPENSE",
                  "CURRENT_ASSETS","TOTAL_ASSETS","TOTAL_LIABILTY",
                  "CURRENT_CASH","CURRENT_DEBT","TOTAL_CASH",
                  "TOTAL_DEBT","SHAREHOLDER_EQUITY","CASH_CHANGE","CASH_FLOW","GAINS/LOSSES"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    
    
    writer.writeheader()
    for stock in stocks:
        for data in financials_df:
            writer.writerow({"Stock": stock,
                             'Date':data["reportDate"],
                             "GROSS_PROFIT":data['grossProfit'],
                             "REVENUE_COST":data['costOfRevenue'],
                             "OPERATING_REVENUE":data['operatingRevenue'],
                             "TOTAL_REVENUE":data['totalRevenue'],
                             "OPERATING_INCOME":data['operatingIncome'],
                             "NET_INCOME":data['netIncome'],
                             "RND":data['researchAndDevelopment'],
                             "OPERATING_EXPENSE":data['operatingExpense'],
                             "CURRENT_ASSETS":data['currentAssets'],
                             "TOTAL_ASSETS":data['totalAssets'],
                            "TOTAL_LIABILTY":data['totalLiabilities'],
                            "CURRENT_CASH":data['currentCash'],
                            "CURRENT_DEBT":data['currentDebt'],
                            "TOTAL_CASH":data['totalCash'],
                            "TOTAL_DEBT":data['totalDebt'],
                            "SHAREHOLDER_EQUITY":data['shareholderEquity'],
                            "CASH_CHANGE":data['cashChange'],
                            "CASH_FLOW":data['cashFlow'],
                            "GAINS/LOSSES":data['operatingGainsLosses']})
        


# In[125]:


earnings_data= pd.read_csv('earnings.csv')
financial_data=pd.read_csv('financials.csv')


# In[127]:


stock_data=pd.merge(financial_data, earnings_data, on=["Date","Stock"])


# In[136]:



merge_1=pd.merge(stock_summary, stock_data, how="left", on=["Date","Stock"])
Merge_1=merge_1.fillna(0)


# In[143]:


stats_df=pd.DataFrame(stats, index=['i',])


# In[144]:


joined_data=Merge_1.join(stats_df, how="outer")
stock_data_summary=joined_data.fillna(0)


# In[147]:


stock_data_summary


# In[148]:


stock_data_summary.to_csv("stock_data_summary.csv", index=False)

