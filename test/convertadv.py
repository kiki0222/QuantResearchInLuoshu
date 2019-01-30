# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:37:53 2018

@author: qiqi.chen
"""

import pandas as pd
import numpy as np
import os
import datetime

if __name__ == '__main__':
    fpath = 'C:/Users/qiqi.chen/Desktop/football-pro-sample'
    
    data_str=open(fpath,'r').readlines()
    data_str1 = data_str[0]
    data_str1 = data_str1.replace('false','False')
    data_str1 = data_str1.replace('true','True')
    exec('data_dic1='+data_str1)
    
    market = data_dic1['mc']
    df1 = pd.DataFrame()
    clk = data_dic1['clk']
    op = data_dic1['op']
    pt = data_dic1['pt']
    mc = data_dic1['mc']
    mcitem = mc[0]
    market_id = mcitem['id']
    total_volume = mcitem['tv']
    market_con = mcitem['con']
    md = mcitem['marketDefinition']
    betdelay = md['betDelay']
    bettingtype = md['bettingType']
    bspmarket = md['bspMarket']
    bspreconciled = md['bspReconciled']
    complete = md['complete']
    countrycode = md['countryCode']
    crossmatching = md['crossMatching']
    discount = md['discountAllowed']
    event_id = md['eventId']
    event_name = md['eventName']
    eventtypeid = md['eventTypeId']
    inplay = md['inPlay']
    marketbaserate = md['marketBaseRate']
    market_time = md['marketTime']
    try:
        market_type = md['marketType']
    except KeyError:
        market_type = '.'
    market_name = md['name']
    numberofactive = md['numberOfActiveRunners']
    numberofwinner = md['numberOfWinners']
    opendate = md['openDate']
    persistence = md['persistenceEnabled']
    regulators = md['regulators']
    runnersvoidable = md['runnersVoidable']
    market_status = md['status']
    suspend_time = md['suspendTime']
    timezone = md['timezone']
    turninplayenabled = md['turnInPlayEnabled']
    version = md['version']
    runners = md['runners']
    for o in range(len(runners)):
        run = runners[o]
        runners_id = run['id']
        runners_name = run['name']
        sort_priority = run['sortPriority']
        status = run['status']
        try:
            hc = run['hc']
        except KeyError:
            hc = 0
        if mcitem.has_key('rc'):
            rc = mcitem['rc']
            tf = []
            for p in range(len(rc)):
                rcitem = rc[p]
                rc_id = rcitem['id']
                try:
                    rc_hc = rcitem['hc']
                except KeyError:
                    rc_hc = 0
                if (rc_id==runners_id) & (rc_hc==hc):
                    tf.append(1)
                    df1_part = pd.DataFrame()
                    ltp = rcitem['ltp']
                    runner_volume = rcitem['tv']
                    trd = rcitem['trd']
                    for t in range(len(trd)):
                        trditem = trd[t]
                        df1_part.loc[t,'clk'] = clk
                        df1_part.loc[t,'op'] = op
                        df1_part.loc[t,'pt'] = pt
                        df1_part.loc[t,'con'] = market_con
                        df1_part.loc[t,'market_id'] = market_id
                        df1_part.loc[t,'total_volume'] = total_volume
                        df1_part.loc[t,'betdelay'] = betdelay
                        df1_part.loc[t,'bettingtype'] = bettingtype
                        df1_part.loc[t,'bspmarket'] = bspmarket
                        df1_part.loc[t,'bspreconciled'] = bspreconciled
                        df1_part.loc[t,'complete'] = complete
                        df1_part.loc[t,'countrycode'] = countrycode
                        df1_part.loc[t,'crossmatching'] = crossmatching
                        df1_part.loc[t,'discount'] = discount
                        df1_part.loc[t,'event_id '] = event_id
                        df1_part.loc[t,'event_name'] = event_name
                        df1_part.loc[t,'eventtypeid'] = eventtypeid
                        df1_part.loc[t,'inplay'] = inplay
                        df1_part.loc[t,'marketbaserate'] = marketbaserate
                        df1_part.loc[t,'market_time'] = market_time                    
                        df1_part.loc[t,'market_type'] = market_type
                        df1_part.loc[t,'market_name'] = market_name
                        df1_part.loc[t,'numberofactive'] = numberofactive
                        df1_part.loc[t,'numberofwinner'] = numberofwinner
                        df1_part.loc[t,'opendate'] = opendate
                        df1_part.loc[t,'persistence'] = persistence
                        df1_part.loc[t,'regulators'] = regulators
                        df1_part.loc[t,'runnersvoidable'] = runnersvoidable
                        df1_part.loc[t,'market_status'] = market_status
                        df1_part.loc[t,'suspend_time'] = suspend_time
                        df1_part.loc[t,'timezone'] = timezone
                        df1_part.loc[t,'turninplayenabled'] = turninplayenabled
                        df1_part.loc[t,'version'] = version                                          
                        df1_part.loc[t,'runners_id'] = rc_id
                        df1_part.loc[t,'runners_name'] = runners_name
                        df1_part.loc[t,'hc'] = rc_hc
                        df1_part.loc[t,'sort_priority'] = sort_priority
                        df1_part.loc[t,'status'] = status
                        df1_part.loc[t,'ltp'] = ltp
                        df1_part.loc[t,'runner_volume'] = runner_volume
                        df1_part.loc[t,'traded_volume'] = trditem[1]
                        df1_part.loc[t,'traded_price'] = trditem[0]
                    df1 = df1.append(df1_part)
                elif ((rc_id==runners_id) & (rc_hc==hc))==False:
                    tf.append(0)
            if (1 in tf)==False:
                df1_part = pd.DataFrame()
                ltp = np.nan
                runner_volume = np.nan
                traded_volume = np.nan
                traded_price = np.nan
                df1_part.loc[0,'clk'] = clk
                df1_part.loc[0,'op'] = op
                df1_part.loc[0,'pt'] = pt
                df1_part.loc[0,'con'] = market_con
                df1_part.loc[0,'market_id'] = market_id
                df1_part.loc[0,'total_volume'] = total_volume
                df1_part.loc[0,'betdelay'] = betdelay
                df1_part.loc[0,'bettingtype'] = bettingtype
                df1_part.loc[0,'bspmarket'] = bspmarket
                df1_part.loc[0,'bspreconciled'] = bspreconciled
                df1_part.loc[0,'complete'] = complete
                df1_part.loc[0,'countrycode'] = countrycode
                df1_part.loc[0,'crossmatching'] = crossmatching
                df1_part.loc[0,'discount'] = discount
                df1_part.loc[0,'event_id '] = event_id
                df1_part.loc[0,'event_name'] = event_name
                df1_part.loc[0,'eventtypeid'] = eventtypeid
                df1_part.loc[0,'inplay'] = inplay
                df1_part.loc[0,'marketbaserate'] = marketbaserate
                df1_part.loc[0,'market_time'] = market_time                    
                df1_part.loc[0,'market_type'] = market_type
                df1_part.loc[0,'market_name'] = market_name
                df1_part.loc[0,'numberofactive'] = numberofactive
                df1_part.loc[0,'numberofwinner'] = numberofwinner
                df1_part.loc[0,'opendate'] = opendate
                df1_part.loc[0,'persistence'] = persistence
                df1_part.loc[0,'regulators'] = regulators
                df1_part.loc[0,'runnersvoidable'] = runnersvoidable
                df1_part.loc[0,'market_status'] = market_status
                df1_part.loc[0,'suspend_time'] = suspend_time
                df1_part.loc[0,'timezone'] = timezone
                df1_part.loc[0,'turninplayenabled'] = turninplayenabled
                df1_part.loc[0,'version'] = version                                          
                df1_part.loc[0,'runners_id'] = runners_id
                df1_part.loc[0,'runners_name'] = runners_name
                df1_part.loc[0,'hc'] = hc
                df1_part.loc[0,'sort_priority'] = sort_priority
                df1_part.loc[0,'status'] = status
                df1_part.loc[0,'ltp'] = ltp
                df1_part.loc[0,'runner_volume'] = runner_volume
                df1_part.loc[0,'traded_volume'] = traded_volume
                df1_part.loc[0,'traded_price'] = traded_price
                df1 = df1.append(df1_part)                   
        else:
            df1_part = pd.DataFrame()
            ltp = np.nan
            runner_volume = np.nan
            traded_volume = np.nan
            traded_price = np.nan
            df1_part.loc[0,'clk'] = clk
            df1_part.loc[0,'op'] = op
            df1_part.loc[0,'pt'] = pt
            df1_part.loc[0,'con'] = market_con
            df1_part.loc[0,'market_id'] = market_id
            df1_part.loc[0,'total_volume'] = total_volume
            df1_part.loc[0,'betdelay'] = betdelay
            df1_part.loc[0,'bettingtype'] = bettingtype
            df1_part.loc[0,'bspmarket'] = bspmarket
            df1_part.loc[0,'bspreconciled'] = bspreconciled
            df1_part.loc[0,'complete'] = complete
            df1_part.loc[0,'countrycode'] = countrycode
            df1_part.loc[0,'crossmatching'] = crossmatching
            df1_part.loc[0,'discount'] = discount
            df1_part.loc[0,'event_id '] = event_id
            df1_part.loc[0,'event_name'] = event_name
            df1_part.loc[0,'eventtypeid'] = eventtypeid
            df1_part.loc[0,'inplay'] = inplay
            df1_part.loc[0,'marketbaserate'] = marketbaserate
            df1_part.loc[0,'market_time'] = market_time                    
            df1_part.loc[0,'market_type'] = market_type
            df1_part.loc[0,'market_name'] = market_name
            df1_part.loc[0,'numberofactive'] = numberofactive
            df1_part.loc[0,'numberofwinner'] = numberofwinner
            df1_part.loc[0,'opendate'] = opendate
            df1_part.loc[0,'persistence'] = persistence
            df1_part.loc[0,'regulators'] = regulators
            df1_part.loc[0,'runnersvoidable'] = runnersvoidable
            df1_part.loc[0,'market_status'] = market_status
            df1_part.loc[0,'suspend_time'] = suspend_time
            df1_part.loc[0,'timezone'] = timezone
            df1_part.loc[0,'turninplayenabled'] = turninplayenabled
            df1_part.loc[0,'version'] = version                                          
            df1_part.loc[0,'runners_id'] = runners_id
            df1_part.loc[0,'runners_name'] = runners_name
            df1_part.loc[0,'hc'] = hc
            df1_part.loc[0,'sort_priority'] = sort_priority
            df1_part.loc[0,'status'] = status
            df1_part.loc[0,'ltp'] = ltp
            df1_part.loc[0,'runner_volume'] = runner_volume
            df1_part.loc[0,'traded_volume'] = traded_volume
            df1_part.loc[0,'traded_price'] = traded_price
            df1 = df1.append(df1_part)                   
#################add new rows to the  dataframe
    df1 = df1.reset_index(drop = True)
    df1['spf'] = pd.Series(np.nan)
    df1['spn'] = pd.Series(np.nan)
    df1['atb1'] = pd.Series(np.nan)
    df1['atb2'] = pd.Series(np.nan)
    df1['atb3'] = pd.Series(np.nan)
    df1['atb4'] = pd.Series(np.nan)
    df1['atb5'] = pd.Series(np.nan)
    df1['atb6'] = pd.Series(np.nan)
    df1['atb7'] = pd.Series(np.nan)
    df1['atb8'] = pd.Series(np.nan)
    df1['atb9'] = pd.Series(np.nan)
    df1['atb10'] = pd.Series(np.nan)
    df1['atb1v'] = pd.Series(np.nan)
    df1['atb2v'] = pd.Series(np.nan)
    df1['atb3v'] = pd.Series(np.nan)
    df1['atb4v'] = pd.Series(np.nan)
    df1['atb5v'] = pd.Series(np.nan)
    df1['atb6v'] = pd.Series(np.nan)
    df1['atb7v'] = pd.Series(np.nan)
    df1['atb8v'] = pd.Series(np.nan)
    df1['atb9v'] = pd.Series(np.nan)
    df1['atb10v'] = pd.Series(np.nan)
    df1['atl1'] = pd.Series(np.nan)
    df1['atl2'] = pd.Series(np.nan)
    df1['atl3'] = pd.Series(np.nan)
    df1['atl4'] = pd.Series(np.nan)
    df1['atl5'] = pd.Series(np.nan)
    df1['atl6'] = pd.Series(np.nan)
    df1['atl7'] = pd.Series(np.nan)
    df1['atl8'] = pd.Series(np.nan)
    df1['atl9'] = pd.Series(np.nan)
    df1['atl10'] = pd.Series(np.nan)
    df1['atl1v'] = pd.Series(np.nan)
    df1['atl2v'] = pd.Series(np.nan)
    df1['atl3v'] = pd.Series(np.nan)
    df1['atl4v'] = pd.Series(np.nan)
    df1['atl5v'] = pd.Series(np.nan)
    df1['atl6v'] = pd.Series(np.nan)
    df1['atl7v'] = pd.Series(np.nan)
    df1['atl8v'] = pd.Series(np.nan)
    df1['atl9v'] = pd.Series(np.nan)
    df1['atl10v'] = pd.Series(np.nan)  
    df1['spb1'] = pd.Series(np.nan)
    df1['spb2'] = pd.Series(np.nan)
    df1['spb3'] = pd.Series(np.nan)
    df1['spb4'] = pd.Series(np.nan)
    df1['spb5'] = pd.Series(np.nan)
    df1['spb6'] = pd.Series(np.nan)
    df1['spb7'] = pd.Series(np.nan)
    df1['spb8'] = pd.Series(np.nan)
    df1['spb9'] = pd.Series(np.nan)
    df1['spb10'] = pd.Series(np.nan)
    df1['spb1v'] = pd.Series(np.nan)
    df1['spb2v'] = pd.Series(np.nan)
    df1['spb3v'] = pd.Series(np.nan)
    df1['spb4v'] = pd.Series(np.nan)
    df1['spb5v'] = pd.Series(np.nan)
    df1['spb6v'] = pd.Series(np.nan)
    df1['spb7v'] = pd.Series(np.nan)
    df1['spb8v'] = pd.Series(np.nan)
    df1['spb9v'] = pd.Series(np.nan)
    df1['spb10v'] = pd.Series(np.nan)
    df1['spl1'] = pd.Series(np.nan)
    df1['spl2'] = pd.Series(np.nan)
    df1['spl3'] = pd.Series(np.nan)
    df1['spl4'] = pd.Series(np.nan)
    df1['spl5'] = pd.Series(np.nan)
    df1['spl6'] = pd.Series(np.nan)
    df1['spl7'] = pd.Series(np.nan)
    df1['spl8'] = pd.Series(np.nan)
    df1['spl9'] = pd.Series(np.nan)
    df1['spl10'] = pd.Series(np.nan)
    df1['spl1v'] = pd.Series(np.nan)
    df1['spl2v'] = pd.Series(np.nan)
    df1['spl3v'] = pd.Series(np.nan)
    df1['spl4v'] = pd.Series(np.nan)
    df1['spl5v'] = pd.Series(np.nan)
    df1['spl6v'] = pd.Series(np.nan)
    df1['spl7v'] = pd.Series(np.nan)
    df1['spl8v'] = pd.Series(np.nan)
    df1['spl9v'] = pd.Series(np.nan)
    df1['spl10v'] = pd.Series(np.nan)
    for m in range(1,1000):
        data_str2 = data_str[m] 
        data_str2 = data_str2.replace('false','False')
        data_str2 = data_str2.replace('true','True')
        exec('data_dic2='+data_str2)
        clk = data_dic2['clk']
        mc = data_dic2['mc']
        op = data_dic2['op']
        pt = data_dic2['pt']
        mcitem = mc[0]
        market_id = mcitem['id']
        if mcitem.has_key('tv'):
            total_volume = mcitem['tv']
        else:
            total_volume = np.nan
        market_con = mcitem['con']
        rc = mcitem['rc']
        if 1>0:
            if mcitem.has_key('marketDefinition'):
                md = mcitem['marketDefinition']
                betdelay = md['betDelay']
                bettingtype = md['bettingType']
                bspmarket = md['bspMarket']
                bspreconciled = md['bspReconciled']
                complete = md['complete']
                countrycode = md['countryCode']
                crossmatching = md['crossMatching']
                discount = md['discountAllowed']
                event_id = md['eventId']
                event_name = md['eventName']
                eventtypeid = md['eventTypeId']
                inplay = md['inPlay']
                marketbaserate = md['marketBaseRate']
                market_time = md['marketTime']
                try:
                    market_type = md['marketType']
                except KeyError:
                    market_type = '.'
                market_name = md['name']
                numberofactive = md['numberOfActiveRunners']
                numberofwinner = md['numberOfWinners']
                opendate = md['openDate']
                persistence = md['persistenceEnabled']
                regulators = md['regulators']
                runnersvoidable = md['runnersVoidable']
                market_status = md['status']
                suspend_time = md['suspendTime']
                timezone = md['timezone']
                turninplayenabled = md['turnInPlayEnabled']
                version = md['version']
                runners = md['runners']
                for i in range(len(runners)):
                    runners_id = runners[i]['id']
                    runners_name = runners[i]['name']
                    sort_priority = runners[i]['sortPriority']
                    status = runners[i]['status']
                    try:
                        hc = runners[i]['hc']
                    except KeyError:
                        hc = 0
                    tf = []
                    for j in range(len(rc)):
                        rcitem = rc[j]
                        rc_id = rcitem['id']
                        try:
                            rc_hc = rcitem['hc']
                        except KeyError:
                            rc_hc = 0
                        if (rc_id==runners_id) & (rc_hc==hc):
                            tf.append(1)
                            if rcitem.has_key('trd'):
                                trd = rcitem['trd']
                                for t in range(len(trd)):
                                    df1_part = df1[(df1['market_id']==market_id) & (df1['runners_id']==runners_id) & (df1['hc']==hc)][-1:].copy()
                                    df1_part['clk'] = clk
                                    df1_part['op'] = op
                                    df1_part['pt'] = pt
                                    df1_part['con'] = market_con
                                    df1_part['market_id'] = market_id
                                    df1_part['total_volume'] = total_volume
                                    df1_part['betdelay'] = betdelay
                                    df1_part['bettingtype'] = bettingtype
                                    df1_part['bspmarket'] = bspmarket
                                    df1_part['bspreconciled'] = bspreconciled
                                    df1_part['complete'] = complete
                                    df1_part['countrycode'] = countrycode
                                    df1_part['crossmatching'] = crossmatching
                                    df1_part['discount'] = discount
                                    df1_part['event_id '] = event_id
                                    df1_part['event_name'] = event_name
                                    df1_part['eventtypeid'] = eventtypeid
                                    df1_part['inplay'] = inplay
                                    df1_part['marketbaserate'] = marketbaserate
                                    df1_part['market_time'] = market_time                    
                                    df1_part['market_type'] = market_type
                                    df1_part['market_name'] = market_name
                                    df1_part['numberofactive'] = numberofactive
                                    df1_part['numberofwinner'] = numberofwinner
                                    df1_part['opendate'] = opendate
                                    df1_part['persistence'] = persistence
                                    df1_part['regulators'] = regulators
                                    df1_part['runnersvoidable'] = runnersvoidable
                                    df1_part['market_status'] = market_status
                                    df1_part['suspend_time'] = suspend_time
                                    df1_part['timezone'] = timezone
                                    df1_part['turninplayenabled'] = turninplayenabled
                                    df1_part['version'] = version                                          
                                    df1_part['runners_id'] = runners_id
                                    df1_part['runners_name'] = runners_name
                                    df1_part['hc'] = hc
                                    df1_part['sort_priority'] = sort_priority
                                    df1_part['status'] = status
                                    df1_part['tv'] = rcitem['tv']
                                    df1_part['traded_volume'] = trd[t][1]
                                    df1_part['traded_price'] = trd[t][0]
                                    if rcitem.has_key('ltp'):
                                        ltp = rcitem['ltp']
                                        df1_part['ltp'] = ltp
                                    if rcitem.has_key('spf'):
                                        spf = rcitem['spf']
                                        df1_part['spf'] = spf
                                    if rcitem.has_key('spn'):
                                        spn = rcitem['spn']
                                        df1_part['spn'] = spn
                                    if rcitem.has_key('atb'):
                                        df1_part['atb1'] = np.nan
                                        df1_part['atb2'] = np.nan
                                        df1_part['atb3'] = np.nan
                                        df1_part['atb4'] = np.nan
                                        df1_part['atb5'] = np.nan
                                        df1_part['atb6'] = np.nan
                                        df1_part['atb7'] = np.nan
                                        df1_part['atb8'] = np.nan
                                        df1_part['atb9'] = np.nan
                                        df1_part['atb10'] = np.nan
                                        df1_part['atb1v'] = np.nan
                                        df1_part['atb2v'] = np.nan
                                        df1_part['atb3v'] = np.nan
                                        df1_part['atb4v'] = np.nan
                                        df1_part['atb5v'] = np.nan
                                        df1_part['atb6v'] = np.nan
                                        df1_part['atb7v'] = np.nan
                                        df1_part['atb8v'] = np.nan
                                        df1_part['atb9v'] = np.nan
                                        df1_part['atb10v'] = np.nan
                                        pricelist = []
                                        volumelist = []
                                        atblist = rcitem['atb']
                                        for a in range(len(atblist)):
                                            pricelist.append(atblist[a][0])
                                        pricelist.sort(reverse = True)
                                        for p in range(len(pricelist)):
                                            price = pricelist[p]
                                            for a in range(len(atblist)):
                                                if atblist[a][0]==price:
                                                    volumelist.append(atblist[a][1])
                                        for p in range(10):
                                            try:
                                                df1_part['atb'+str(p+1)] = pricelist[p]
                                                df1_part['atb'+str(p+1)+'v'] = volumelist[p]
                                            except IndexError:
                                                pass
                                    if rcitem.has_key('atl'):
                                        df1_part['atl1'] = np.nan
                                        df1_part['atl2'] = np.nan
                                        df1_part['atl3'] = np.nan
                                        df1_part['atl4'] = np.nan
                                        df1_part['atl5'] = np.nan
                                        df1_part['atl6'] = np.nan
                                        df1_part['atl7'] = np.nan
                                        df1_part['atl8'] = np.nan
                                        df1_part['atl9'] = np.nan
                                        df1_part['atl10'] = np.nan
                                        df1_part['atl1v'] = np.nan
                                        df1_part['atl2v'] = np.nan
                                        df1_part['atl3v'] = np.nan
                                        df1_part['atl4v'] = np.nan
                                        df1_part['atl5v'] = np.nan
                                        df1_part['atl6v'] = np.nan
                                        df1_part['atl7v'] = np.nan
                                        df1_part['atl8v'] = np.nan
                                        df1_part['atl9v'] = np.nan
                                        df1_part['atl10v'] = np.nan
                                        pricelist = []
                                        volumelist = []
                                        atblist = rcitem['atl']
                                        for a in range(len(atblist)):
                                            pricelist.append(atblist[a][0])
                                        pricelist.sort()
                                        for p in range(len(pricelist)):
                                            price = pricelist[p]
                                            for a in range(len(atblist)):
                                                if atblist[a][0]==price:
                                                    volumelist.append(atblist[a][1])
                                        for p in range(10):
                                            try:
                                                df1_part['atl'+str(p+1)] = pricelist[p]
                                                df1_part['atl'+str(p+1)+'v'] = volumelist[p]       
                                            except IndexError:
                                                pass
                                    if rcitem.has_key('spb'):
                                        df1_part['spb1'] = np.nan
                                        df1_part['spb2'] = np.nan
                                        df1_part['spb3'] = np.nan
                                        df1_part['spb4'] = np.nan
                                        df1_part['spb5'] = np.nan
                                        df1_part['spb6'] = np.nan
                                        df1_part['spb7'] = np.nan
                                        df1_part['spb8'] = np.nan
                                        df1_part['spb9'] = np.nan
                                        df1_part['spb10'] = np.nan
                                        df1_part['spb1v'] = np.nan
                                        df1_part['spb2v'] = np.nan
                                        df1_part['spb3v'] = np.nan
                                        df1_part['spb4v'] = np.nan
                                        df1_part['spb5v'] = np.nan
                                        df1_part['spb6v'] = np.nan
                                        df1_part['spb7v'] = np.nan
                                        df1_part['spb8v'] = np.nan
                                        df1_part['spb9v'] = np.nan
                                        df1_part['spb10v'] = np.nan
                                        pricelist = []
                                        volumelist = []
                                        atblist = rcitem['spb']
                                        for a in range(len(atblist)):
                                            pricelist.append(atblist[a][0])
                                        pricelist.sort(reverse = True)
                                        for p in range(len(pricelist)):
                                            price = pricelist[p]
                                            for a in range(len(atblist)):
                                                if atblist[a][0]==price:
                                                    volumelist.append(atblist[a][1])
                                        for p in range(10):
                                            try:
                                                df1_part['spb'+str(p+1)] = pricelist[p]
                                                df1_part['spb'+str(p+1)+'v'] = volumelist[p]
                                            except IndexError:
                                                pass
                                    if rcitem.has_key('spl'):
                                        df1_part['spl1'] = np.nan
                                        df1_part['spl2'] = np.nan
                                        df1_part['spl3'] = np.nan
                                        df1_part['spl4'] = np.nan
                                        df1_part['spl5'] = np.nan
                                        df1_part['spl6'] = np.nan
                                        df1_part['spl7'] = np.nan
                                        df1_part['spl8'] = np.nan
                                        df1_part['spl9'] = np.nan
                                        df1_part['spl10'] = np.nan
                                        df1_part['spl1v'] = np.nan
                                        df1_part['spl2v'] = np.nan
                                        df1_part['spl3v'] = np.nan
                                        df1_part['spl4v'] = np.nan
                                        df1_part['spl5v'] = np.nan
                                        df1_part['spl6v'] = np.nan
                                        df1_part['spl7v'] = np.nan
                                        df1_part['spl8v'] = np.nan
                                        df1_part['spl9v'] = np.nan
                                        df1_part['spl10v'] = np.nan
                                        pricelist = []
                                        volumelist = []
                                        atblist = rcitem['spl']
                                        for a in range(len(atblist)):
                                            pricelist.append(atblist[a][0])
                                        pricelist.sort()
                                        for p in range(len(pricelist)):
                                            price = pricelist[p]
                                            for a in range(len(atblist)):
                                                if atblist[a][0]==price:
                                                    volumelist.append(atblist[a][1])
                                        for p in range(10):
                                            try:
                                                df1_part['spl'+str(p+1)] = pricelist[p]
                                                df1_part['spl'+str(p+1)+'v'] = volumelist[p]
                                            except IndexError:
                                                pass                                
                                    df1 = df1.append(df1_part)
                                    df1 = df1.reset_index(drop = True)
                            else:
                                df1_part = df1[(df1['market_id']==market_id) & (df1['runners_id']==runners_id) & (df1['hc']==hc)][-1:].copy()
                                df1_part['clk'] = clk
                                df1_part['op'] = op
                                df1_part['pt'] = pt
                                df1_part['con'] = market_con
                                df1_part['market_id'] = market_id
                                df1_part['total_volume'] = total_volume
                                df1_part['betdelay'] = betdelay
                                df1_part['bettingtype'] = bettingtype
                                df1_part['bspmarket'] = bspmarket
                                df1_part['bspreconciled'] = bspreconciled
                                df1_part['complete'] = complete
                                df1_part['countrycode'] = countrycode
                                df1_part['crossmatching'] = crossmatching
                                df1_part['discount'] = discount
                                df1_part['event_id '] = event_id
                                df1_part['event_name'] = event_name
                                df1_part['eventtypeid'] = eventtypeid
                                df1_part['inplay'] = inplay
                                df1_part['marketbaserate'] = marketbaserate
                                df1_part['market_time'] = market_time                    
                                df1_part['market_type'] = market_type
                                df1_part['market_name'] = market_name
                                df1_part['numberofactive'] = numberofactive
                                df1_part['numberofwinner'] = numberofwinner
                                df1_part['opendate'] = opendate
                                df1_part['persistence'] = persistence
                                df1_part['regulators'] = regulators
                                df1_part['runnersvoidable'] = runnersvoidable
                                df1_part['market_status'] = market_status
                                df1_part['suspend_time'] = suspend_time
                                df1_part['timezone'] = timezone
                                df1_part['turninplayenabled'] = turninplayenabled
                                df1_part['version'] = version                                          
                                df1_part['runners_id'] = runners_id
                                df1_part['runners_name'] = runners_name
                                df1_part['hc'] = hc
                                df1_part['sort_priority'] = sort_priority
                                df1_part['status'] = status
                                df1_part['tv'] = np.nan
                                df1_part['traded_volume'] = np.nan
                                df1_part['traded_price'] = np.nan
                                if rcitem.has_key('ltp'):
                                    ltp = rcitem['ltp']
                                    df1_part['ltp'] = ltp
                                if rcitem.has_key('spf'):
                                    spf = rcitem['spf']
                                    df1_part['spf'] = spf
                                if rcitem.has_key('spn'):
                                    spn = rcitem['spn']
                                    df1_part['spn'] = spn
                                if rcitem.has_key('atb'):
                                    df1_part['atb1'] = np.nan
                                    df1_part['atb2'] = np.nan
                                    df1_part['atb3'] = np.nan
                                    df1_part['atb4'] = np.nan
                                    df1_part['atb5'] = np.nan
                                    df1_part['atb6'] = np.nan
                                    df1_part['atb7'] = np.nan
                                    df1_part['atb8'] = np.nan
                                    df1_part['atb9'] = np.nan
                                    df1_part['atb10'] = np.nan
                                    df1_part['atb1v'] = np.nan
                                    df1_part['atb2v'] = np.nan
                                    df1_part['atb3v'] = np.nan
                                    df1_part['atb4v'] = np.nan
                                    df1_part['atb5v'] = np.nan
                                    df1_part['atb6v'] = np.nan
                                    df1_part['atb7v'] = np.nan
                                    df1_part['atb8v'] = np.nan
                                    df1_part['atb9v'] = np.nan
                                    df1_part['atb10v'] = np.nan
                                    pricelist = []
                                    volumelist = []
                                    atblist = rcitem['atb']
                                    for a in range(len(atblist)):
                                        pricelist.append(atblist[a][0])
                                    pricelist.sort(reverse = True)
                                    for p in range(len(pricelist)):
                                        price = pricelist[p]
                                        for a in range(len(atblist)):
                                            if atblist[a][0]==price:
                                                volumelist.append(atblist[a][1])
                                    for p in range(10):
                                        try:
                                            df1_part['atb'+str(p+1)] = pricelist[p]
                                            df1_part['atb'+str(p+1)+'v'] = volumelist[p]
                                        except IndexError:
                                            pass
                                if rcitem.has_key('atl'):
                                    df1_part['atl1'] = np.nan
                                    df1_part['atl2'] = np.nan
                                    df1_part['atl3'] = np.nan
                                    df1_part['atl4'] = np.nan
                                    df1_part['atl5'] = np.nan
                                    df1_part['atl6'] = np.nan
                                    df1_part['atl7'] = np.nan
                                    df1_part['atl8'] = np.nan
                                    df1_part['atl9'] = np.nan
                                    df1_part['atl10'] = np.nan
                                    df1_part['atl1v'] = np.nan
                                    df1_part['atl2v'] = np.nan
                                    df1_part['atl3v'] = np.nan
                                    df1_part['atl4v'] = np.nan
                                    df1_part['atl5v'] = np.nan
                                    df1_part['atl6v'] = np.nan
                                    df1_part['atl7v'] = np.nan
                                    df1_part['atl8v'] = np.nan
                                    df1_part['atl9v'] = np.nan
                                    df1_part['atl10v'] = np.nan
                                    pricelist = []
                                    volumelist = []
                                    atblist = rcitem['atl']
                                    for a in range(len(atblist)):
                                        pricelist.append(atblist[a][0])
                                    pricelist.sort()
                                    for p in range(len(pricelist)):
                                        price = pricelist[p]
                                        for a in range(len(atblist)):
                                            if atblist[a][0]==price:
                                                volumelist.append(atblist[a][1])
                                    for p in range(10):
                                        try:
                                            df1_part['atl'+str(p+1)] = pricelist[p]
                                            df1_part['atl'+str(p+1)+'v'] = volumelist[p]       
                                        except IndexError:
                                            pass
                                if rcitem.has_key('spb'):
                                    df1_part['spb1'] = np.nan
                                    df1_part['spb2'] = np.nan
                                    df1_part['spb3'] = np.nan
                                    df1_part['spb4'] = np.nan
                                    df1_part['spb5'] = np.nan
                                    df1_part['spb6'] = np.nan
                                    df1_part['spb7'] = np.nan
                                    df1_part['spb8'] = np.nan
                                    df1_part['spb9'] = np.nan
                                    df1_part['spb10'] = np.nan
                                    df1_part['spb1v'] = np.nan
                                    df1_part['spb2v'] = np.nan
                                    df1_part['spb3v'] = np.nan
                                    df1_part['spb4v'] = np.nan
                                    df1_part['spb5v'] = np.nan
                                    df1_part['spb6v'] = np.nan
                                    df1_part['spb7v'] = np.nan
                                    df1_part['spb8v'] = np.nan
                                    df1_part['spb9v'] = np.nan
                                    df1_part['spb10v'] = np.nan
                                    pricelist = []
                                    volumelist = []
                                    atblist = rcitem['spb']
                                    for a in range(len(atblist)):
                                        pricelist.append(atblist[a][0])
                                    pricelist.sort(reverse = True)
                                    for p in range(len(pricelist)):
                                        price = pricelist[p]
                                        for a in range(len(atblist)):
                                            if atblist[a][0]==price:
                                                volumelist.append(atblist[a][1])
                                    for p in range(10):
                                        try:
                                            df1_part['spb'+str(p+1)] = pricelist[p]
                                            df1_part['spb'+str(p+1)+'v'] = volumelist[p]
                                        except IndexError:
                                            pass
                                if rcitem.has_key('spl'):
                                    df1_part['spl1'] = np.nan
                                    df1_part['spl2'] = np.nan
                                    df1_part['spl3'] = np.nan
                                    df1_part['spl4'] = np.nan
                                    df1_part['spl5'] = np.nan
                                    df1_part['spl6'] = np.nan
                                    df1_part['spl7'] = np.nan
                                    df1_part['spl8'] = np.nan
                                    df1_part['spl9'] = np.nan
                                    df1_part['spl10'] = np.nan
                                    df1_part['spl1v'] = np.nan
                                    df1_part['spl2v'] = np.nan
                                    df1_part['spl3v'] = np.nan
                                    df1_part['spl4v'] = np.nan
                                    df1_part['spl5v'] = np.nan
                                    df1_part['spl6v'] = np.nan
                                    df1_part['spl7v'] = np.nan
                                    df1_part['spl8v'] = np.nan
                                    df1_part['spl9v'] = np.nan
                                    df1_part['spl10v'] = np.nan
                                    pricelist = []
                                    volumelist = []
                                    atblist = rcitem['spl']
                                    for a in range(len(atblist)):
                                        pricelist.append(atblist[a][0])
                                    pricelist.sort()
                                    for p in range(len(pricelist)):
                                        price = pricelist[p]
                                        for a in range(len(atblist)):
                                            if atblist[a][0]==price:
                                                volumelist.append(atblist[a][1])
                                    for p in range(10):
                                        try:
                                            df1_part['spl'+str(p+1)] = pricelist[p]
                                            df1_part['spl'+str(p+1)+'v'] = volumelist[p]
                                        except IndexError:
                                            pass                                
                                df1 = df1.append(df1_part)
                                df1 = df1.reset_index(drop = True)
                        elif ((rc_id==runners_id) & (rc_hc==hc))==False:
                            tf.append(0)
            else:    
                for k in range(len(rc)):
                    runners_id = rc[k]['id']
                    try:
                        hc = rc[k]['hc']
                    except KeyError:
                        hc = 0
                    rcitem = rc[k]
                    if rcitem.has_key('trd'):
                        trd = rcitem['trd']
                        for t in range(len(trd)):
                            df1_part = df1[(df1['market_id']==market_id) & (df1['runners_id']==runners_id) & (df1['hc']==hc)][-1:].copy()
                            df1_part['clk'] = clk
                            df1_part['op'] = op
                            df1_part['pt'] = pt
                            df1_part['con'] = market_con
                            df1_part['market_id'] = market_id
                            df1_part['total_volume'] = total_volume                                 
                            df1_part['tv'] = rcitem['tv']
                            df1_part['traded_volume'] = trd[t][1]
                            df1_part['traded_price'] = trd[t][0]
                            if rcitem.has_key('ltp'):
                                ltp = rcitem['ltp']
                                df1_part['ltp'] = ltp
                            if rcitem.has_key('spf'):
                                spf = rcitem['spf']
                                df1_part['spf'] = spf
                            if rcitem.has_key('spn'):
                                spn = rcitem['spn']
                                df1_part['spn'] = spn
                            if rcitem.has_key('atb'):
                                df1_part['atb1'] = np.nan
                                df1_part['atb2'] = np.nan
                                df1_part['atb3'] = np.nan
                                df1_part['atb4'] = np.nan
                                df1_part['atb5'] = np.nan
                                df1_part['atb6'] = np.nan
                                df1_part['atb7'] = np.nan
                                df1_part['atb8'] = np.nan
                                df1_part['atb9'] = np.nan
                                df1_part['atb10'] = np.nan
                                df1_part['atb1v'] = np.nan
                                df1_part['atb2v'] = np.nan
                                df1_part['atb3v'] = np.nan
                                df1_part['atb4v'] = np.nan
                                df1_part['atb5v'] = np.nan
                                df1_part['atb6v'] = np.nan
                                df1_part['atb7v'] = np.nan
                                df1_part['atb8v'] = np.nan
                                df1_part['atb9v'] = np.nan
                                df1_part['atb10v'] = np.nan
                                pricelist = []
                                volumelist = []
                                atblist = rcitem['atb']
                                for a in range(len(atblist)):
                                    pricelist.append(atblist[a][0])
                                pricelist.sort(reverse = True)
                                for p in range(len(pricelist)):
                                    price = pricelist[p]
                                    for a in range(len(atblist)):
                                        if atblist[a][0]==price:
                                            volumelist.append(atblist[a][1])
                                for p in range(10):
                                    try:
                                        df1_part['atb'+str(p+1)] = pricelist[p]
                                        df1_part['atb'+str(p+1)+'v'] = volumelist[p]
                                    except IndexError:
                                        pass
                            if rcitem.has_key('atl'):
                                df1_part['atl1'] = np.nan
                                df1_part['atl2'] = np.nan
                                df1_part['atl3'] = np.nan
                                df1_part['atl4'] = np.nan
                                df1_part['atl5'] = np.nan
                                df1_part['atl6'] = np.nan
                                df1_part['atl7'] = np.nan
                                df1_part['atl8'] = np.nan
                                df1_part['atl9'] = np.nan
                                df1_part['atl10'] = np.nan
                                df1_part['atl1v'] = np.nan
                                df1_part['atl2v'] = np.nan
                                df1_part['atl3v'] = np.nan
                                df1_part['atl4v'] = np.nan
                                df1_part['atl5v'] = np.nan
                                df1_part['atl6v'] = np.nan
                                df1_part['atl7v'] = np.nan
                                df1_part['atl8v'] = np.nan
                                df1_part['atl9v'] = np.nan
                                df1_part['atl10v'] = np.nan
                                pricelist = []
                                volumelist = []
                                atblist = rcitem['atl']
                                for a in range(len(atblist)):
                                    pricelist.append(atblist[a][0])
                                pricelist.sort()
                                for p in range(len(pricelist)):
                                    price = pricelist[p]
                                    for a in range(len(atblist)):
                                        if atblist[a][0]==price:
                                            volumelist.append(atblist[a][1])
                                for p in range(10):
                                    try:
                                        df1_part['atl'+str(p+1)] = pricelist[p]
                                        df1_part['atl'+str(p+1)+'v'] = volumelist[p]       
                                    except IndexError:
                                        pass
                            if rcitem.has_key('spb'):
                                df1_part['spb1'] = np.nan
                                df1_part['spb2'] = np.nan
                                df1_part['spb3'] = np.nan
                                df1_part['spb4'] = np.nan
                                df1_part['spb5'] = np.nan
                                df1_part['spb6'] = np.nan
                                df1_part['spb7'] = np.nan
                                df1_part['spb8'] = np.nan
                                df1_part['spb9'] = np.nan
                                df1_part['spb10'] = np.nan
                                df1_part['spb1v'] = np.nan
                                df1_part['spb2v'] = np.nan
                                df1_part['spb3v'] = np.nan
                                df1_part['spb4v'] = np.nan
                                df1_part['spb5v'] = np.nan
                                df1_part['spb6v'] = np.nan
                                df1_part['spb7v'] = np.nan
                                df1_part['spb8v'] = np.nan
                                df1_part['spb9v'] = np.nan
                                df1_part['spb10v'] = np.nan
                                pricelist = []
                                volumelist = []
                                atblist = rcitem['spb']
                                for a in range(len(atblist)):
                                    pricelist.append(atblist[a][0])
                                pricelist.sort(reverse = True)
                                for p in range(len(pricelist)):
                                    price = pricelist[p]
                                    for a in range(len(atblist)):
                                        if atblist[a][0]==price:
                                            volumelist.append(atblist[a][1])
                                for p in range(10):
                                    try:
                                        df1_part['spb'+str(p+1)] = pricelist[p]
                                        df1_part['spb'+str(p+1)+'v'] = volumelist[p]
                                    except IndexError:
                                        pass
                            if rcitem.has_key('spl'):
                                df1_part['spl1'] = np.nan
                                df1_part['spl2'] = np.nan
                                df1_part['spl3'] = np.nan
                                df1_part['spl4'] = np.nan
                                df1_part['spl5'] = np.nan
                                df1_part['spl6'] = np.nan
                                df1_part['spl7'] = np.nan
                                df1_part['spl8'] = np.nan
                                df1_part['spl9'] = np.nan
                                df1_part['spl10'] = np.nan
                                df1_part['spl1v'] = np.nan
                                df1_part['spl2v'] = np.nan
                                df1_part['spl3v'] = np.nan
                                df1_part['spl4v'] = np.nan
                                df1_part['spl5v'] = np.nan
                                df1_part['spl6v'] = np.nan
                                df1_part['spl7v'] = np.nan
                                df1_part['spl8v'] = np.nan
                                df1_part['spl9v'] = np.nan
                                df1_part['spl10v'] = np.nan
                                pricelist = []
                                volumelist = []
                                atblist = rcitem['spl']
                                for a in range(len(atblist)):
                                    pricelist.append(atblist[a][0])
                                pricelist.sort()
                                for p in range(len(pricelist)):
                                    price = pricelist[p]
                                    for a in range(len(atblist)):
                                        if atblist[a][0]==price:
                                            volumelist.append(atblist[a][1])
                                for p in range(10):
                                    try:
                                        df1_part['spl'+str(p+1)] = pricelist[p]
                                        df1_part['spl'+str(p+1)+'v'] = volumelist[p]
                                    except IndexError:
                                        pass                                
                            df1 = df1.append(df1_part)
                            df1 = df1.reset_index(drop = True)
                    else:
                        df1_part = df1[(df1['market_id']==market_id) & (df1['runners_id']==runners_id) & (df1['hc']==hc)][-1:].copy()
                        df1_part['clk'] = clk
                        df1_part['op'] = op
                        df1_part['pt'] = pt
                        df1_part['con'] = market_con
                        df1_part['market_id'] = market_id
                        df1_part['total_volume'] = total_volume
                        df1_part['betdelay'] = betdelay
                        df1_part['bettingtype'] = bettingtype
                        df1_part['bspmarket'] = bspmarket
                        df1_part['bspreconciled'] = bspreconciled
                        df1_part['complete'] = complete
                        df1_part['countrycode'] = countrycode
                        df1_part['crossmatching'] = crossmatching
                        df1_part['discount'] = discount
                        df1_part['event_id '] = event_id
                        df1_part['event_name'] = event_name
                        df1_part['eventtypeid'] = eventtypeid
                        df1_part['inplay'] = inplay
                        df1_part['marketbaserate'] = marketbaserate
                        df1_part['market_time'] = market_time                    
                        df1_part['market_type'] = market_type
                        df1_part['market_name'] = market_name
                        df1_part['numberofactive'] = numberofactive
                        df1_part['numberofwinner'] = numberofwinner
                        df1_part['opendate'] = opendate
                        df1_part['persistence'] = persistence
                        df1_part['regulators'] = regulators
                        df1_part['runnersvoidable'] = runnersvoidable
                        df1_part['market_status'] = market_status
                        df1_part['suspend_time'] = suspend_time
                        df1_part['timezone'] = timezone
                        df1_part['turninplayenabled'] = turninplayenabled
                        df1_part['version'] = version                                          
                        df1_part['runners_id'] = runners_id
                        df1_part['runners_name'] = runners_name
                        df1_part['hc'] = hc
                        df1_part['sort_priority'] = sort_priority
                        df1_part['status'] = status
                        df1_part['tv'] = np.nan
                        df1_part['traded_volume'] = np.nan
                        df1_part['traded_price'] = np.nan
                        if rcitem.has_key('ltp'):
                            ltp = rcitem['ltp']
                            df1_part['ltp'] = ltp
                        if rcitem.has_key('spf'):
                            spf = rcitem['spf']
                            df1_part['spf'] = spf
                        if rcitem.has_key('spn'):
                            spn = rcitem['spn']
                            df1_part['spn'] = spn
                        if rcitem.has_key('atb'):
                            df1_part['atb1'] = np.nan
                            df1_part['atb2'] = np.nan
                            df1_part['atb3'] = np.nan
                            df1_part['atb4'] = np.nan
                            df1_part['atb5'] = np.nan
                            df1_part['atb6'] = np.nan
                            df1_part['atb7'] = np.nan
                            df1_part['atb8'] = np.nan
                            df1_part['atb9'] = np.nan
                            df1_part['atb10'] = np.nan
                            df1_part['atb1v'] = np.nan
                            df1_part['atb2v'] = np.nan
                            df1_part['atb3v'] = np.nan
                            df1_part['atb4v'] = np.nan
                            df1_part['atb5v'] = np.nan
                            df1_part['atb6v'] = np.nan
                            df1_part['atb7v'] = np.nan
                            df1_part['atb8v'] = np.nan
                            df1_part['atb9v'] = np.nan
                            df1_part['atb10v'] = np.nan
                            pricelist = []
                            volumelist = []
                            atblist = rcitem['atb']
                            for a in range(len(atblist)):
                                pricelist.append(atblist[a][0])
                            pricelist.sort(reverse = True)
                            for p in range(len(pricelist)):
                                price = pricelist[p]
                                for a in range(len(atblist)):
                                    if atblist[a][0]==price:
                                        volumelist.append(atblist[a][1])
                            for p in range(10):
                                try:
                                    df1_part['atb'+str(p+1)] = pricelist[p]
                                    df1_part['atb'+str(p+1)+'v'] = volumelist[p]
                                except IndexError:
                                    pass
                        if rcitem.has_key('atl'):
                            df1_part['atl1'] = np.nan
                            df1_part['atl2'] = np.nan
                            df1_part['atl3'] = np.nan
                            df1_part['atl4'] = np.nan
                            df1_part['atl5'] = np.nan
                            df1_part['atl6'] = np.nan
                            df1_part['atl7'] = np.nan
                            df1_part['atl8'] = np.nan
                            df1_part['atl9'] = np.nan
                            df1_part['atl10'] = np.nan
                            df1_part['atl1v'] = np.nan
                            df1_part['atl2v'] = np.nan
                            df1_part['atl3v'] = np.nan
                            df1_part['atl4v'] = np.nan
                            df1_part['atl5v'] = np.nan
                            df1_part['atl6v'] = np.nan
                            df1_part['atl7v'] = np.nan
                            df1_part['atl8v'] = np.nan
                            df1_part['atl9v'] = np.nan
                            df1_part['atl10v'] = np.nan
                            pricelist = []
                            volumelist = []
                            atblist = rcitem['atl']
                            for a in range(len(atblist)):
                                pricelist.append(atblist[a][0])
                            pricelist.sort()
                            for p in range(len(pricelist)):
                                price = pricelist[p]
                                for a in range(len(atblist)):
                                    if atblist[a][0]==price:
                                        volumelist.append(atblist[a][1])
                            for p in range(10):
                                try:
                                    df1_part['atl'+str(p+1)] = pricelist[p]
                                    df1_part['atl'+str(p+1)+'v'] = volumelist[p]       
                                except IndexError:
                                    pass
                        if rcitem.has_key('spb'):
                            df1_part['spb1'] = np.nan
                            df1_part['spb2'] = np.nan
                            df1_part['spb3'] = np.nan
                            df1_part['spb4'] = np.nan
                            df1_part['spb5'] = np.nan
                            df1_part['spb6'] = np.nan
                            df1_part['spb7'] = np.nan
                            df1_part['spb8'] = np.nan
                            df1_part['spb9'] = np.nan
                            df1_part['spb10'] = np.nan
                            df1_part['spb1v'] = np.nan
                            df1_part['spb2v'] = np.nan
                            df1_part['spb3v'] = np.nan
                            df1_part['spb4v'] = np.nan
                            df1_part['spb5v'] = np.nan
                            df1_part['spb6v'] = np.nan
                            df1_part['spb7v'] = np.nan
                            df1_part['spb8v'] = np.nan
                            df1_part['spb9v'] = np.nan
                            df1_part['spb10v'] = np.nan
                            pricelist = []
                            volumelist = []
                            atblist = rcitem['spb']
                            for a in range(len(atblist)):
                                pricelist.append(atblist[a][0])
                            pricelist.sort(reverse = True)
                            for p in range(len(pricelist)):
                                price = pricelist[p]
                                for a in range(len(atblist)):
                                    if atblist[a][0]==price:
                                        volumelist.append(atblist[a][1])
                            for p in range(10):
                                try:
                                    df1_part['spb'+str(p+1)] = pricelist[p]
                                    df1_part['spb'+str(p+1)+'v'] = volumelist[p]
                                except IndexError:
                                    pass
                        if rcitem.has_key('spl'):
                            df1_part['spl1'] = np.nan
                            df1_part['spl2'] = np.nan
                            df1_part['spl3'] = np.nan
                            df1_part['spl4'] = np.nan
                            df1_part['spl5'] = np.nan
                            df1_part['spl6'] = np.nan
                            df1_part['spl7'] = np.nan
                            df1_part['spl8'] = np.nan
                            df1_part['spl9'] = np.nan
                            df1_part['spl10'] = np.nan
                            df1_part['spl1v'] = np.nan
                            df1_part['spl2v'] = np.nan
                            df1_part['spl3v'] = np.nan
                            df1_part['spl4v'] = np.nan
                            df1_part['spl5v'] = np.nan
                            df1_part['spl6v'] = np.nan
                            df1_part['spl7v'] = np.nan
                            df1_part['spl8v'] = np.nan
                            df1_part['spl9v'] = np.nan
                            df1_part['spl10v'] = np.nan
                            pricelist = []
                            volumelist = []
                            atblist = rcitem['spl']
                            for a in range(len(atblist)):
                                pricelist.append(atblist[a][0])
                            pricelist.sort()
                            for p in range(len(pricelist)):
                                price = pricelist[p]
                                for a in range(len(atblist)):
                                    if atblist[a][0]==price:
                                        volumelist.append(atblist[a][1])
                            for p in range(10):
                                try:
                                    df1_part['spl'+str(p+1)] = pricelist[p]
                                    df1_part['spl'+str(p+1)+'v'] = volumelist[p]
                                except IndexError:
                                    pass                                
                        df1 = df1.append(df1_part)
                        df1 = df1.reset_index(drop = True)
                      
                                

