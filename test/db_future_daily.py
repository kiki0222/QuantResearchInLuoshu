# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:57:57 2019

@author: qiqi.chen
"""

import pandas as pd
import os
import re
import sqlite3

ROOT_FOLDER = r'\\win-g12\ResearchWorks\Interns\qiqi.chen\Future_Daily\\'

if __name__ == '__main__':
    
    folder = 'RawData'
    date_str = '20181206'
    year = date_str[:4]
    year_month = date_str[:6]
    rawdata_path = os.path.join(ROOT_FOLDER,folder,year,year_month,date_str)
    database_path = os.path.join(ROOT_FOLDER,'Future_Daily.db')
    con = sqlite3.connect(database_path)
    csvname = 'Future_Daily'
    
    future_daily = pd.DataFrame()
    for(dirpath,dirnames,filenames)in os.walk(rawdata_path):
        for fn in range(len(filenames)):
            filepath = os.path.join(dirpath,filenames[fn])
            data = pd.read_csv(filepath)
            instrument = re.findall(r'[a-z,A-Z]+',filenames[fn])[0]
            ticker = filenames[fn].split('.')[0]
            contract = int(re.findall(r'\d+',filenames[fn])[0])
            maturitymonth = contract//100*12+contract%100
            exchange = filenames[fn].split('.')[1]
            data.loc[0,'Instrument'] = instrument
            data.loc[0,'Ticker'] = ticker
            data.loc[0,'Contract'] = contract
            data.loc[0,'MaturityMonth'] = maturitymonth
            data.loc[0,'Exchange'] = exchange
            order = ['Instrument','Ticker','Contract','MaturityMonth','Exchange','TradingDay','ClosePrice','HighestPrice','LowestPrice','OpenInterest','OpenPrice','SettlementPrice','TotalVolume','Turnover']
            data = data[order]
            future_daily = future_daily.append(data)
    future_daily['Contract'] = future_daily['Contract'].apply(int)
    future_daily['MaturityMonth'] = future_daily['MaturityMonth'].apply(int)
    future_daily = future_daily.reset_index(drop = True)
    future_daily.to_sql(csvname,con,if_exists = 'replace',index = True)
    con.close()
            
    