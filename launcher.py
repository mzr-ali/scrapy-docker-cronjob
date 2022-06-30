import os
import sys
from datetime import datetime

from scrapy.crawler import CrawlerProcess
from scrapy.spiderloader import SpiderLoader
from scrapy.utils import project
from scrapy.utils.log import configure_logging


def crawler_function():
    settings = {}
    project_settings = project.get_project_settings()  # Fetch Scrapy Project Setting
    spider_loader = SpiderLoader(project_settings)  # Load Spiders from Settings
    spider = spider_loader.load('quotes')  # get Spider by name from Loaded Spider list

    feed_url = '/app/output/data-{}.csv'.format(os.getenv('OUTPUT'))

    settings['FEEDS'] = {feed_url: {'format': 'csv'}}

    configure_logging(settings)

    process = CrawlerProcess({**project_settings, **settings})
    process.crawl(spider)
    process.start()


if __name__ == '__main__':
    try:
        crawler_function()
    except IndexError:
        event = None
        crawler_function()
