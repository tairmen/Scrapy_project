# -*- coding: utf-8 -*-
import scrapy
import json

def make_start_urls():
	urls_list = [];
	for i in range(1,84):
		urls_list.append("https://gcup.ru/forum/30-36976-" + str(i))
	return urls_list;

class PostSpider1(scrapy.Spider):
    name = "HabrSpider"
    start_urls = make_start_urls()
	
    def parse(self, response):
        for i in response.css('table.postTable'): 
            yield {
                'text' : i.css('span.ucoz-forum-post ::text').extract(),
                'postDate' : i.css('td.postIdTop ::text').extract(),
                'author' :  i.css('div.postRankName ::text').extract(),
            }