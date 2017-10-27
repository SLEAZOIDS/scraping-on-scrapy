# -*- coding: utf-8 -*-
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import scrapy
from yahoo.items import YahooItem

class SearchSpider(scrapy.Spider):
    name = 'search'

    allowed_domains = ['search.yahoo.co.jp']
    
    urls = 'https://search.yahoo.co.jp/search?p=車'
    start_urls = [urls]

    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "USER_AGENT":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0"
    }

    #現在のページ番号
    page = 0

    def parse(self, response):
        # for sel in response.xpath('//div[@class="w"]'):
        for sel in response.css('div.w'):
            article = YahooItem()
            article['title'] = sel.css("a::text").extract_first()
            yield article
        
        # 次のページへの処理。”次へ　ボタンだとうまくいかなかった”
        if self.page < 5:
            self.page += 1
            next_urls = self.urls+"&b="+str(self.page)+"1"
            yield scrapy.Request(next_urls, callback=self.parse)
        
