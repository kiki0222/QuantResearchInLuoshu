# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:04:37 2019

@author: qiqi.chen
"""
import pandas as pd
import sqlite3
import os
import time
from multiprocessing import Pool

ROOT_FOLDER = r'\\win-g12\ResearchWorks\Interns\qiqi.chen\rolltable\\'


def gen_mostactive(instrument,method):
    #instrument = 'WH'
    #method = 'TotalVolume'
    folder1 = 'input'
    database1_path = os.path.join(ROOT_FOLDER, folder1, 'Future_Daily.db')
    con1 = sqlite3.connect(database1_path)
    csvname1 = 'Future_Daily'
    sql = "select * from Future_Daily where Instrument = "+'"'+instrument+'"'
    data = pd.read_sql_query(sql,con1)
    con1.close()
    
    data_each_instrument = data.sort_values(by = ['TradingDay',method,'Contract'],na_position = 'first')
    mostactive = data_each_instrument.groupby('TradingDay').tail(1)
    mostactive = mostactive.drop(columns = ['index','Ticker'])
    mostactive = mostactive.reset_index(drop = True)
    
    # determine contract and its prices
    for line in range(1,len(mostactive)):
        contract = mostactive.loc[line,'Contract']
        contract_lag = mostactive.loc[line-1,'Contract']
        tradingday =  mostactive.loc[line,'TradingDay']
        data_now = data_each_instrument.loc[data_each_instrument['TradingDay'] == tradingday]
      
        if contract != contract_lag :
            if contract < contract_lag :
                mostactive.loc[line, 'Contract'] = mostactive.loc[line-1,'Contract']
                for lag in range(line+1):
                    tradingday_lag = mostactive.loc[line-lag,'TradingDay']
                    data_lag = data_each_instrument.loc[data_each_instrument['TradingDay'] == tradingday_lag]
                    data_active = data_lag.loc[data_lag['Contract'] == contract_lag]
                    if len(data_active != 0) :
                        mostactive.loc[line, 'MaturityMonth'] = data_active['MaturityMonth'].values[0]
                        mostactive.loc[line,'ClosePrice'] = data_active['ClosePrice'].values[0]
                        mostactive.loc[line,'HighestPrice'] = data_active['HighestPrice'].values[0]
                        mostactive.loc[line,'LowestPrice'] = data_active['LowestPrice'].values[0]
                        mostactive.loc[line,'OpenInterest'] = data_active['OpenInterest'].values[0]
                        mostactive.loc[line,'OpenPrice'] = data_active['OpenPrice'].values[0]
                        mostactive.loc[line,'SettlementPrice'] = data_active['SettlementPrice'].values[0]
                        mostactive.loc[line,'TotalVolume'] = data_active['TotalVolume'].values[0]
                        mostactive.loc[line,'Turnover'] = data_active['Turnover'].values[0]
                        break
            else:
                if (contract_lag in data_now['Contract'].values) == False and str(contract_lag) > str(mostactive.loc[line,'TradingDay'])[2:-2]:
                    mostactive.loc[line, 'Contract'] = mostactive.loc[line-1,'Contract']
                    for lag in range(line):
                        tradingday_lag = mostactive.loc[line-lag-1,'TradingDay']
                        data_lag = data_each_instrument.loc[data_each_instrument['TradingDay'] == tradingday_lag]
                        data_active = data_lag.loc[data_lag['Contract'] == contract_lag]
                        if len(data_active != 0) :
                            mostactive.loc[line, 'MaturityMonth'] = data_active['MaturityMonth'].values[0]
                            mostactive.loc[line,'ClosePrice'] = data_active['ClosePrice'].values[0]
                            mostactive.loc[line,'HighestPrice'] = data_active['HighestPrice'].values[0]
                            mostactive.loc[line,'LowestPrice'] = data_active['LowestPrice'].values[0]
                            mostactive.loc[line,'OpenInterest'] = data_active['OpenInterest'].values[0]
                            mostactive.loc[line,'OpenPrice'] = data_active['OpenPrice'].values[0]
                            mostactive.loc[line,'SettlementPrice'] = data_active['SettlementPrice'].values[0]
                            mostactive.loc[line,'TotalVolume'] = data_active['TotalVolume'].values[0]
                            mostactive.loc[line,'Turnover'] = data_active['Turnover'].values[0]
                            break
   
    # calculate history factor                    
    for line in range(1,len(mostactive)):
        contract = mostactive.loc[line,'Contract']
        contract_lag = mostactive.loc[line-1,'Contract']
        if contract > contract_lag :
            for lag in range(line):
                tradingday_lag =  mostactive.loc[line-lag-1,'TradingDay']
                data_lag = data_each_instrument.loc[data_each_instrument['TradingDay'] == tradingday_lag]
                index2_list = data_lag.loc[data_lag['Contract'] == contract].index.tolist()
                if len(index2_list) != 0:
                    index2 = index2_list[0]
                    index1_list = data_lag.loc[data_lag['Contract'] == contract_lag].index.tolist()
                    if len(index1_list) != 0:
                        index1 = index1_list[0]
                        mostactive.loc[line,'history_factor'] = data_lag.loc[index1,'ClosePrice']*1.0/data_lag.loc[index2,'ClosePrice']
                        mostactive.loc[line,'lag'] = lag+1
                        break
                else:
                    mostactive.loc[line,'history_factor'] = 1
                    mostactive.loc[line,'lag'] = 0
                    break
        else:
            mostactive.loc[line,'history_factor'] = 1
            mostactive.loc[line,'lag'] = 0

    mostactive['history_factor'] = mostactive['history_factor'].fillna(1)
    mostactive['lag'] = mostactive['lag'].fillna(0)
    mostactive['factor_multiply'] = mostactive['history_factor'].cumprod()
    mostactive['method'] = method
    
    folder2 = 'output'
    database2_path = os.path.join(ROOT_FOLDER, folder2,'AdjustedDailyData.db') 
    con2 = sqlite3.connect(database2_path)
    csvname2 = 'AdjustedDailyData'
    
    mostactive.to_sql(csvname2, con2, if_exists = 'append', index = False)
    con2.close()



if __name__ == '__main__':
    time_start = time.time()
    
    instruments = [ 
        'IF', 'IC', 'IH', 'TF', 'T', 'TS',
        'ag', 'al', 'au', 'bu', 'cu', 'fu', 'hc', 'ni', 'pb', 'rb', 'ru', 'sn', 'zn', 'wr', 'sc', 'sp',
        'AP','CF', 'CY', 'FG', 'JR', 'LR', 'MA', 'OI', 'PM', 'RI', 'RM', 'RS', 'SM', 'SF', 'SR', 'TA', 'WH', 'TC', 'ZC',
        'a', 'b', 'bb', 'c', 'cs', 'eg', 'fb', 'i', 'j', 'jd', 'jm', 'l', 'm', 'p', 'pp', 'v', 'y'
    ]
    
    method_list = ['OpenInterest', 'Turnover', 'TotalVolume']
    
    print('Parent process  %s.' %os.getpid()) 
    p = Pool(20)
    for x in range(len(method_list)):
        for y in range(len(instruments)):
            p.apply_async(gen_mostactive, args=(instruments[y],method_list[x],))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

    time_end = time.time()
    print('totally cost',time_end-time_start)

        

