import re 
import urllib.parse
from bs4 import BeautifulSoup

class HtmlParser():
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'lxml')
        new_urls = self.get_new_urls(page_url,soup)
        new_data = self.get_new_data(page_url,soup)
        return new_urls,new_data
    
    #获取新URL
    def get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.select('div .para a[href]')
        for link in links:
            # print(link)
            if 'item' in link['href']:
                new_url = link['href']
                new_full_url = urllib.parse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)
        #print(new_urls)


        # links = soup.find_all('a',href=re.compile(r'/item/'))
        # for link in links:
            # new_url =link['href']
            # new_full_url = urllib.parse.urljoin(page_url,new_url)
            # new_urls.add(new_full_url)
        return new_urls
    #获取标题与摘要
    def get_new_data(self,page_url,soup):
        data = {}
        data['url'] = str(page_url)
        title = soup.select('.lemmaWgt-lemmaTitle-title h1')
        data['title'] = title[0].text.strip()
        content = soup.find('div',class_='para')
        data['content'] = content.get_text()
        return data
#url ='https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'