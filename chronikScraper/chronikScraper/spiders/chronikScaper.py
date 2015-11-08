import scrapy
import urlparse

from chronikScraper.items import ChronikscraperItem

class ChronikSpider(scrapy.Spider):
    name = "chronikScraper"
    allowed_domains = ["mut-gegen-rechte-gewalt.de"]
    start_urls = [
        "https://www.mut-gegen-rechte-gewalt.de/service/chronik-vorfaelle"
    ]

    def parse(self, response):
        # parse this page
        for sel in response.css("div.view-content > div.views-row"):
            # print("FOUND ENTRY!")
            item = ChronikscraperItem()

            item['title'] = sel.css('div.field-name-field-art ::text').extract()[0]
            # print("FOUND TITLE: " + sel.css('div.field-name-field-art::text').extract())
            item['date'] = sel.css('div.field-name-field-date ::text').extract()[0]
            item['city'] = sel.css('div.field-name-field-city ::text').extract()[0]
            item['state'] = sel.css('div.field-name-field-bundesland ::text').extract()[0]
            item['source'] = sel.css('div.field-name-field-source > .field-items ::text').extract()
            injured = sel.css('div.field field-name-field-anzahl-verletze ::text').extract()
            if injured:
                 item['injured'] = injured
            item['description'] = sel.css('div.field-name-body ::text').extract()[0]

            yield item

        # crawl next page
        for href in response.css("li.pager-next > a::attr('href')"):
            #url = response.urljoin(href.extract())
            url = urlparse.urljoin(response.url, href.extract())
            # print("FOUND NEXT PAGE: " + url)

            # crawl next page
            if url:
                yield scrapy.Request(url, callback=self.parse)
