# -*- coding: utf-8 -*-
import scrapy


class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['www.google.co.jp']
    start_urls = ['https://www.google.co.jp/search?q=%E6%9D%B1%E4%BA%AC+%E9%9B%A2%E5%A9%9A+%E5%BC%81%E8%AD%B7%E5%A3%AB&oq=%E6%9D%B1%E4%BA%AC+%E9%9B%A2%E5%A9%9A&aqs=chrome.1.69i57j0l5.7959j0j1&sourceid=chrome&ie=UTF-8']

    def parse(self, response):
        print('AAAAAAAAAAAAAAAA')
        for sel in response.css("div[class*='_pdd']"):
            print('CCCCCCCCCC')
            article = GoogleItem()
            # article['title'] = sel.css("a::text").extract_first()
            yield article
        # next_page = response.css('a.btn_next::attr(href)').extract_first()

        print('BBBBBBBBBBBB')
        
        #TODO 全ページ舐めるのは時間がかかるので２ページまで
        # page_url_split = next_page.split("=")
        # page_no = int(page_url_split[-1])
        # if next_page is not None and page_no <= 2:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
