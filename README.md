# setup

- install python3

- setup dev
```
rm -r myvenv
python3 -m venv myvenv

ls
-> myenv
```

- install following
```
pip install requests
pip install lxml
pip install beautifulsoup4
```

## trouble shooting

- "No module named":https://qiita.com/tukiyo3/items/d51a3a60bd158bbcc579 

# usage

- init
```
soup = BeautifulSoup(html, "html.parser")
```
- get element
```
soup.find_all("a")
soup.find("a")
soup.find_all("a", attrs={"class": "link", "href": "/link"})

import re
soup.find_all(re.compile("^b"))
soup.find_all("a", text=re.compile("hello"))

soup.select('a[href^="http://"]')
```
- edit
```
a = soup.find("a")
a["target"] = "_blank"

```
- output
```
soup.div.prettify()
```

- documentation
 - https://qiita.com/itkr/items/513318a9b5b92bd56185
 - https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text 



# my env

```
pip freeze | grep -e request -e lxml -e beautiful -e python

beautifulsoup4==4.6.0 
lxml==4.0.0
requests==2.18.4

```

# connect db

- @ marriadb_con/connect_lib
- connect db
```
import MySQLdb

def connect_lib():
    connection = MySQLdb.connect(
        host="localhost",
        db="news",
        user="***", 
        passwd="***"
    )
    return connection
```
- insert
```
def insert_data(cur, con, data):
    cur.executemany("insert into sample (id, title, link) values (%s, %s, %s)", data)
    con.commit()
```
