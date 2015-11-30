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
            #print("FOUND ENTRY!")
            item = ChronikscraperItem()

            item['title'] = sel.css('div.field-name-field-art ::text').extract()[0]
            item['date'] = sel.css('div.field-name-field-date ::text').extract()[0]
            #print("FOUND: " + item['date'] + " " + item['title'])
            item['city'] = sel.css('div.field-name-field-city ::text').extract()[0]
            item['state'] = sel.css('div.field-name-field-bundesland ::text').extract()[0]
            # remove empty newlines and spaces
            source_list = filter( None, map( unicode.strip, sel.css('div.field-name-field-source > .field-items ::text').extract() ) )
            item['source'] = ", ".join( source_list )
            # just strip (trailing) spaces in some list elements
            item['source_href'] = map( unicode.strip, sel.css('div.field-name-field-source > .field-items a::attr(href)').extract() )
            # export of type "own investigations" from mut-gegen-rechte-gewalt.de
            #   should link to their page
            if (item['source'].lower() == u"eigene recherche" or item['source'].lower() == u"eigene angabe") and \
               len(item['source_href']) == 0:
                item['source_href'] = [u"https://www.mut-gegen-rechte-gewalt.de/service/chronik-vorfaelle"]

            #print(item['source'])
            #print(item['source_href'])

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
