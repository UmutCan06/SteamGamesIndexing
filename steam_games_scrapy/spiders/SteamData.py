# -*- coding: utf-8 -*-
import scrapy
from ..items import SteamGamesItem



class SteamdataSpider(scrapy.Spider):
    name = "SteamData"

    start_urls = []
    for c in range(1,200):
        start_urls.append('http://store.steampowered.com/search/?page={}'.format(c))

        def parse(self, response):
            links = response.css("a.search_result_row::attr(href)").extract()
            for l in links[:25]:
                # l = response.urljoin(l)
                yield scrapy.Request(l, callback=self.parse_doc)

        def parse_doc(self, response):
            name = response.css("div.apphub_AppName::text")[0].extract()
            year = response.css("div.release_date span.date::text")[0].extract()
            image = response.css("img.game_header_image_full::attr(src)")[0].extract()
            summary = response.css("div.game_description_snippet::text")[0].extract().strip()
            price =  response.css("div.game_purchase_price::text")[0].extract().strip()
            reviews = response.css("div.summary span.game_review_summary::text")[0].extract()
            tag = []
            for i in range(5):
                tag.append(response.css("div.glance_tags a::text")[i].extract().strip())

            game_data = SteamGamesItem(name=name,year=year,image=image,summary=summary,tag=tag,price=price,reviews=reviews)

            yield game_data