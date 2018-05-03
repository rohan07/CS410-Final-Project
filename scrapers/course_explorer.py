'''
to get department codes:
https://courses.illinois.edu/schedule/2018/fall

for each department code, to get course codes:
https://courses.illinois.edu/schedule/2018/fall/AAS

for each course, to get instructor (and other course information)
https://courses.illinois.edu/schedule/2018/fall/AAS/100

https://stackoverflow.com/questions/40479789/how-to-scrape-all-the-content-of-each-link-with-scrapy
https://stackoverflow.com/questions/23662069/scrapy-parse-javascript
'''
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
import js2xml, js2xml.jsonlike
import re
from bs4 import BeautifulSoup


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
        sel = Selector(response)
        soup = BeautifulSoup(response.text, 'lxml')

        scripts = response.selector.xpath('//script/text()').extract()
        js = js2xml.parse(scripts[1])
        jsp = js2xml.jsonlike.getall(js)[0]

        dept = None
        num = None
        title = None
        description = None
        instructors = []

        # get dept and num
        general_info = soup.find("div", {"class" : "lead app-table-lead"})
        general_info_2 = general_info.find("h1")
        dept = general_info_2.text.split()[0]
        num = general_info_2.text.split()[1]

        # get title and description
        detail_info_big = soup.find("div", {"id" : "app-course-info"})
        detail_info = detail_info_big.findAll("div", {"class":"col-sm-12"})

        if (len(detail_info) == 2):
            title = detail_info[0].find("span", {"class":"app-label app-text-engage"}).text
            description = detail_info[1].findAll("p")[1].text.strip()
        else:
            title = detail_info[0].text
            description = detail_info[2].findAll("p")[1].text.strip()

        # if we want to map crn to instuctor, we need to remove the set off instuctors, record crn in
        # the loop below, zip the two together, and insert len(crn) times
        # crn = []

        for j in jsp:
            soup_inst = BeautifulSoup(j['instructor'])
            found_instructor = soup_inst.text
            instructors.append(found_instructor)

            # soup_crn = BeautifulSoup(j['crn'])
            # found_crn = soup_crn.text
            # crn.append(found_crn)

        instructors = set(instructors)

        return {
            "dept" : dept,
            "title" : title,
            "num" : num,
            "description": description,
            "instructors" : instructors
        }


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'LOG_LEVEL': 'WARNING',
    'FEED_FORMAT' : 'json',
    'FEED_URI' : 'result.json'
})

process.crawl(CourseSpider)
process.start() # the script will block here until the crawling is finished
