import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

class HtmlDownloader():
    def download(self,url):
        if url is None:
            return
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        res = requests.get(url,headers=header)
        if res.status_code == 200:
            res.encoding = 'utf-8'
            return res.text
        return None