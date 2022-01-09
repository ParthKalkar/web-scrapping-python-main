import scrapy
from ..items import CompanyscrapingItem


class BuscomSpider(scrapy.Spider):
    name = 'buscom'
    page_number = 2
    count = 0
    start_urls = ['https://datacvr.virk.dk/data/visninger?soeg=&oprettet=null&ophoert=null&branche=&language=en-gb&type=undefined']

    def parse(self, response):
        items = CompanyscrapingItem()

        address = response.css('.address::text').extract()
        CVR = response.css('.cvr p+ p::text').extract()
        Status = response.css('.status p+ p::text').extract()
        Business_type = response.css('.type p+ p::text').extract()
        
        items['address'] = address
        items['CVR'] = CVR
        items['Status'] = Status
        items['Business_type'] = Business_type

        yield items

        next_page = 'https://datacvr.virk.dk/data/visninger?branche=&language=en-gb&ophoert=null&oprettet=null&page=' + str(BuscomSpider.page_number)+ '&soeg=&type=undefined'

        if BuscomSpider.count < 30:
            BuscomSpider.page_number += 1
            BuscomSpider.count += 1
            yield response.follow(next_page, callback=self.parse)