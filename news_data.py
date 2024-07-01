import requests
from bs4 import BeautifulSoup
def get_news(company):
    url = f"https://www.google.com/search?q={company}+company&tbm=nws&source=lmns&tbs=qdr:h"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
    response = requests.get(url,headers=header)   
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        frame = soup.find("div",class_="dURPMd")
        if frame is None:
            print("No News")
            return None
        items = frame.find_all("div",class_="SoaBEf")
        
        for item in items:
            print(item.find('div',class_="n0jPhd ynAwRc MBeuO nDgy9d").get_text())
            print(item.find('a')['href'])
