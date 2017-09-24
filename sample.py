import requests
from bs4 import BeautifulSoup

target_url = 'https://www.google.co.jp/'
r = requests.get(target_url)         #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

for a in soup.find_all('a'):
      print(a.get('href'))         #リンクを表示