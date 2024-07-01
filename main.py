import news_data
import stock
if __name__=='__main__':
    conn,cursor = stock.connect_DB('stock.db')
    sql = "SELECT name FROM CompanyInfo"
    rows = stock.get_data(sql,cursor)
    for row in rows:
        print(f"---------------------current company {row[0]}--------------------")
        print(news_data.get_news(row[0]))
    

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