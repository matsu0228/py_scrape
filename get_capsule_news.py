import sys; sys.path.append('./mariadb_con')
import requests
from bs4 import BeautifulSoup
from mariadb_con import connect_lib
from mariadb_con import insert_data


# sat scrape
target_url = 'http://capsule-official.com/news/?category_cd=event'
r = requests.get(target_url)         #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出
ary_data = []
i = 1

# save db
def save_db(data):
    con = connect_lib()
    cur = con.cursor()
    #
    #insert_data(cur, con, data)
    #
    cur.execute("select * from sample")
    result = cur.fetchall()
    print( result )
    #
    cur.close()
    con.close()

for title in soup.find_all('h2'):
     a = title.find('a')
     s_tname = a.string #link_text
     s_link  = a.get('href')
     # print( s_tname, s_link )
     ary_data.append( [i, 's_tname', s_link] )
     i = i + 1

# print( ary_data )
save_db( ary_data )


