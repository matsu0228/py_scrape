# setup

- install python3
- setup dev
```
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

# my env

```
pip freeze | grep -e request -e lxml -e beautiful -e python

beautifulsoup4==4.6.0
lxml==4.0.0
requests==2.18.4

```
