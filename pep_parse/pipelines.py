import collections
import csv
import datetime as dt

from pep_parse.settings import BASE_DIR, RESULTS_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.pep_sum = collections.defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.pep_sum[status] += 1
        return item

    def close_spider(self, spider):
        dir_path = BASE_DIR / RESULTS_DIR
        dir_path.mkdir(exist_ok=True)
        now = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f'status_summary_{now}.csv'
        file_path = dir_path / file_name
        results = ['Статус,Количество']
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv_writer = csv.writer(f, dialect='unix')
            total = sum(self.pep_sum.values())
            csv_writer.writerows([
                results,
                *self.pep_sum.items(),
                ['Total', total]
            ])
