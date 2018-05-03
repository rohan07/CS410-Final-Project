'''
to get department codes:
https://courses.illinois.edu/schedule/2018/fall

for each department code, to get course codes:
https://courses.illinois.edu/schedule/2018/fall/AAS

for each course, to get instructor (and other course information)
https://courses.illinois.edu/schedule/2018/fall/AAS/100

https://stackoverflow.com/questions/40479789/how-to-scrape-all-the-content-of-each-link-with-scrapy
'''
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor


class CourseSpider(CrawlSpider):
    name = "course_explorer"
    start_urls = ['https://courses.illinois.edu/schedule/2018/fall']
    rules = (
        Rule(LinkExtractor(
            allow = ("https://courses.illinois.edu/schedule/2018/fall/[A-Z]*$")),
        ),
        Rule(LinkExtractor(
            allow = ("https://courses.illinois.edu/schedule/2018/fall/[A-Z]*/[0-9]+$")),
            callback = 'parse_page'
        ),
      )

    def parse_page(self, response):
        # print('Got a response from %s.' % response.url)
        sel = Selector(response)


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(CourseSpider)
process.start() # the script will block here until the crawling is finished
