import scrapy
from top_movies.items import TopMoviesItem
from scrapy.loader import ItemLoader

class ScrapingImdbSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top"]

    def parse(self, response):
        for i in range(1, 251):
            href = response.xpath(f"(//ul[@role='presentation'][1]/li//div[@role='group']/a/@href)[{i}]").get()
            link = f'https://www.imdb.com{href}'
            yield scrapy.Request(url=link, callback=self.parse_movies)

    def parse_movies(self, response):
        item = ItemLoader(item=TopMoviesItem(), selector=response)

        item.add_value('rank', response.url)
        item.add_xpath('title','//h1/span')
        item.add_xpath('genres', '//div[@data-testid="genres"]//span')
        item.add_xpath('release_date','((//ul[@role="presentation"])[2]/li/a)[1]')
        if response.xpath('((//ul[@role="presentation"])[2]/li/a)[2]'):
            item.add_xpath('age_rating', '((//ul[@role="presentation"])[2]/li/a)[2]')
            item.add_xpath('duration', '(//ul[@role="presentation"])[2]/li[3]')
        else:
            item.add_value('age_rating', '_')
            item.add_xpath('duration', '(//ul[@role="presentation"])[2]/li[2]')
        item.add_xpath('rating', '(//div[contains(@data-testid,"score")]/span)[1]')
        item.add_xpath('reviews_count', '//div[contains(@data-testid,"score")]/following-sibling::div[2]')

        yield item.load_item()

