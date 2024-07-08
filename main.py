import news_data
import stock
import database

import pandas as pd

if __name__=='__main__':
    conn,cursor = database.connect_DB('stock.db')
    # old version (S & P 500 리스트 database에 저장)
    '''
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500 = pd.read_html(url)[0]

    
    sql = 'CREATE TABLE IF NOT EXISTS CompanyInfo (name TEXT, symbol TEXT)'
    database.sql_exe(cursor,sql,conn)
    sql = 'DELETE FROM CompanyInfo'
    database.sql_exe(cursor,sql,conn)
    for i,row in sp500.iterrows():
        sql = "INSERT INTO CompanyInfo VALUES(?, ?)"
        database.sql_exe(cursor,sql,conn,para=(row['Security'],row['Symbol']))
    '''

    sql = "SELECT name FROM CompanyInfo"
    #리스트를 다 돌면서 해당 기업 이름이 포함된 뉴스 존재 체크
    rows = database.get_data(sql,cursor)
    sql = 'CREATE TABLE IF NOT EXISTS CompanyNews (name TEXT, title TEXT, url TEXT)'
    database.sql_exe(cursor,sql,conn)
    for row in rows:
        print(f"---------------------current company {row[0]}--------------------")
        ans=news_data.get_news(row[0])
        if ans is None:
            continue
        titles = ans[0]
        urls = ans[1]
        for title,url in zip(titles, urls):
            sql = "INSERT INTO CompanyNews VALUES(?, ?, ?)"
            database.sql_exe(cursor,sql,conn,para=(row[0],title,url))
    
    
    '''
    url = "https://api.nasdaq.com/api/screener/stocks?exchange=nasdaq&download=true"
    reponse = requests.get(url)
    print(reponse)
    data = reponse.json()
    nasdaq = pd.DataFrame(data['data']['rows'])
    print(nasdaq)
    '''

    '''
    conn,cursor = connect_DB('stock.db')
    sql = 'CREATE TABLE IF NOT EXISTS CompanyInfo (name TEXT, symbol TEXT)'
    sql_exe(cursor,sql,conn)
    sql = 'DELETE FROM CompanyInfo'
    sql_exe(cursor,sql,conn)
    for i,row in sp500.iterrows():
        sql = "INSERT INTO CompanyInfo VALUES(?, ?)"
        sql_exe(cursor,sql,conn,para=(row['Security'],row['Symbol']))

    sql='CREATE TABLE IF NOT EXISTS CurrentInfo (time TEXT, symbol TEXT, price REAL)'
    sql_exe(cursor,sql,conn)

    sql = "SELECT symbol FROM CurrentInfo"
    rows = get_data(sql,cursor)

    sql = 'DELETE FROM CurrentInfo'
    sql_exe(cursor,sql,conn)
    #끝나는 조건이 필요한 경우 추가 
    while True:
        tz_NY = pytz.timezone("America/New_York")
        #현재 뉴욕을 시간을 DATE에 저장 
        date = datetime.datetime.now(tz_NY)
        print(f'current price update : {date}')
        for row in rows:
            currentPrice=get_current_price(row[0])
            sql ="INSERT INTO CurrentInfo VALUES(?,?,?)"
            sql_exe(cursor,sql,conn,para=(currentPrice[0],row[0],currentPrice[1]))
        time.sleep(60)
    cursor.close()
    conn.close()
    '''
