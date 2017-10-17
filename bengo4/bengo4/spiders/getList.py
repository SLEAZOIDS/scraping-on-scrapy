# -*- coding: utf-8 -*-
import scrapy
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from bengo4.items import Bengo4Item

class GetlistSpider(scrapy.Spider):
    name = 'getList'
    allowed_domains = ['www.bengo4.com']
    start_urls = ['https://www.bengo4.com/search/result/']

    def parse(self, response):
        for sel in response.css("div[class*='profile']"):
            article = Bengo4Item()
            article['name'] = sel.css("a.uaLbl_111::text").extract_first()
            article['office'] = sel.css("p.office::text").extract_first()
            #TODO アドレス取れない・・・
            article['address'] = sel.css("span.address__txt::text").extract_first()
            article['tel'] = sel.css("span.tel__txt::text").extract_first()
            yield article

        next_page = response.css('a.btn_next::attr(href)').extract_first()
        
        #TODO 全ページ舐めるのは時間がかかるので２ページまで
        page_url_split = next_page.split("=")
        page_no = int(page_url_split[-1])
        if next_page is not None and page_no <= 2:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
