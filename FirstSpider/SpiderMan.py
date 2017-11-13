import DataOutput
import HtmlDownloader
import HtmlParser
import UrlManager

class SpiderMan():
    def __init__(self):
        self.manager = UrlManager.UrlManager()
        self.output = DataOutput.DataOutput()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
    def craw(self,root_url,data_num):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size() < int(data_num)):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls,data = self.parser.parser(new_url,html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print("已经抓取%s个链接"%self.manager.old_url_size())
            except Exception as e:
                print('抓取失败')
        self.output.output_html()
		
if __name__=="__main__":
    url='https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
    data_num = 20
    spider_man = SpiderMan()
    spider_man.craw(url,data_num)
