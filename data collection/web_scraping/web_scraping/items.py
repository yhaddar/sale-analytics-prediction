# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    main_category = scrapy.Field()
    sub_category = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    rating = scrapy.Field()
    no_of_ratings = scrapy.Field()
    discount_price = scrapy.Field()
    actual_price = scrapy.Field()
