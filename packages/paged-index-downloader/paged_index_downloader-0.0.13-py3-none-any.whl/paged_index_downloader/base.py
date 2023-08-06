import hashlib
import locale
import textwrap

import bs4
import scrapy
from datetime import datetime

from . import pipelines


def item_postprocess(func):
    def wrapper(self, response, **kwargs):
        gen = func(self, response, **kwargs)
        for item in gen:
            if "publish_datetime" in item.keys():
                if item["publish_datetime"] is not None:
                    item["publish_date"] = item["publish_datetime"].strftime("%Y-%m-%d")
                    item["publish_time"] = item["publish_datetime"].strftime("%H:%M")
            item["paragraphs"] = ["\n".join(textwrap.wrap(p)) for p in item["paragraphs"]]
            yield item
    return wrapper


class CoreSpider(scrapy.Spider):

    pipeline = {pipelines.CSVPipeline}
    colnames = [
        "url_hash",
        "url",
        "site",
        "scraped_from",
        "section",
        "headline",
        "author",
        "publish_datetime",
        "publish_time",
        "publish_date",
        "scraped_datetime"
    ]

    def __init__(self):
        super().__init__()
        self.urls = []
        self.class_name = type(self).__name__

    def url_hash(self, url):
        hasher = hashlib.sha3_224(url.encode("utf-8"))
        return hasher.hexdigest()

    def start_requests(self):
        locale.setlocale(locale.LC_TIME, self.settings.attributes["LOCALE"].value)
        self.page_range = list(range(1, int(self.settings.attributes["N_PAGES"].value)))
        self.sections = self.settings.attributes["SECTIONS"].value
        self.create_urls(self.url_gen, self.sections, self.page_range)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.urls:
            item = {"section": url[1]}
            yield scrapy.Request(
                url=url[0],
                callback=self.parse,
                headers=headers,
                cb_kwargs=item
            )

    def create_urls(self, func, sections, pages):
        self.urls = []
        for section in sections:
            for page in pages:
                new_url = func(section, page), section
                self.urls.append(new_url)

    def parse(self, response, **kwargs):
        soup = bs4.BeautifulSoup(response.text)
        item = {
            "scraped_datetime": str(datetime.now()),
            "scraped_from": response.url,
            "site": self.name,
            "publish_datetime": None,
            "publish_time": None,
            "publish_date": None,
            "section": kwargs["section"]
        }
        return soup, item

    def parse_articles(self, response, **kwargs):
        item = {
            "url": response.url,
            "url_hash": None,
            "headline": None,
            "paragraphs": None,
            "author": None
        }
        item["url"] = response.url
        item["url_hash"] = self.url_hash(response.url)
        item = {**item, **kwargs}
        soup = bs4.BeautifulSoup(response.text)
        return soup, item
