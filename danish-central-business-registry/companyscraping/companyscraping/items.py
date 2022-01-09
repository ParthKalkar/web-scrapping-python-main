# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    address = scrapy.Field()
    CVR = scrapy.Field()
    Status = scrapy.Field()
    Business_type = scrapy.Field()
    
