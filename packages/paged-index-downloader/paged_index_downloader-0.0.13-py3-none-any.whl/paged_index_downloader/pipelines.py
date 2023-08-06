import datetime
import csv

from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings


class CSVPipeline(object):

    def __init__(self):
        self.time_format = "%Y-%m-%d_%H%M%S"
        self.seen = set()
        self.file = None
        self.writer = None
        self.filename = "default"

    def open_spider(self, spider):
        now = datetime.datetime.now()
        now_str = now.strftime(self.time_format)
        data_directory = get_project_settings()["DATA_DIRECTORY"]
        target_dir = data_directory + "/" + spider.name + "/"
        if spider.colnames is not None:
            self.filename = target_dir + spider.name + "_" + now_str + ".csv"
            self.file = open(self.filename, 'w')
            self.writer = csv.DictWriter(
                self.file,
                fieldnames=spider.colnames,
                lineterminator='\n'
            )
            self.writer.writeheader()

    def process_item(self, item, spider):
        item = dict(item)
        paragraphs = item.pop("paragraphs")
        row = {col: item[col] for col in spider.colnames}
        dupe_check = row['section'] + '_' + row['url_hash']
        if dupe_check in self.seen:
            raise DropItem("Dupe found: " + dupe_check)
        else:
            self.writer.writerow(row)
            self.seen.add(dupe_check)
            with open(f"articles/{spider.name}/{spider.name}-{item['url_hash']}.txt", "w") as f:
                f.write(item["url"] + "\n\n")
                for p in paragraphs:
                    f.write(p + "\n\n")

    def close_spider(self, spider):
        print("Finished processing file: " + self.filename)
        self.file.close()
