import yfinance as yf
import datetime
import pytz
import pandas as pd
import sqlite3
import time
import requests
'''
get_current_price: 회사 심볼을 파라미터로 전달 받아 뉴욕 시간 기준으로 현재 가격을 리턴하는 함수
'''
def get_current_price(symbol):
    #전달받은 심볼의 주식데이터를 yfinance에서 받아옴
    data = yf.Ticker(symbol)
    #현재가격, 주소, 등등 현재 해당하는 심볼의 회사에 대한 정보를 RESULT에 저장 
    result = data.info
    '''
    for key in result:
        print(f'{key} = {result[key]}')
    data = ['regular']
    '''
    #뉴욕 시간대를 TZ_NY에 저장 
    tz_NY = pytz.timezone("America/New_York")
    #현재 뉴욕을 시간을 DATE에 저장 
    date = datetime.datetime.now(tz_NY)
    #야후 파이낸스에서 받아온 현재 심볼에 해당하는 회사가 현재 가격을 가지고 있으면 저장하여 리턴 
    if 'currentPrice' in result:
        return [date.strftime("%Y-%m-%d %H:%M:%S"),result['currentPrice']]
    #현재 가격을 가지고 있지 않으면 비워서 리턴 
    return [date.strftime("%Y-%m-%d %H:%M:%S"),None]

def connect_DB(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    print(f"{db_name} connect!")
    return conn, cursor

def sql_exe(cursor,sql,conn,para=None):
    #print(sql,para)
    if para:
        cursor.execute(sql,para)
    else:
        print(sql)
        cursor.execute(sql)
    conn.commit()

def get_data(sql,cursor):
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
'test'

