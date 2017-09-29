import requests
from bs4 import BeautifulSoup

target_url = 'http://capsule-official.com/news/?category_cd=event'
r = requests.get(target_url)         #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

for title in soup.find_all('h2'):
     a = title.find('a')
     s_tname = a.string #link_text
     s_link  = a.get('href')
     print( s_tname, s_link )

