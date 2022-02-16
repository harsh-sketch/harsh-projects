#top 250 movies from imdb

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.imdb.com/chart/top/',
    ]

    def parse(self, response):
        for quote in response.css('div.pagecontent div.article span.ab_widget div.seen-collection div.article div.lister table tr'):
            no  = quote.css('td.titleColumn::text')
            print(no)
            yield {
                'name' : quote.css('td.titleColumn a::text').get(),
                'year' : quote.css('td.titleColumn span.secondaryInfo::text').get(),  
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
