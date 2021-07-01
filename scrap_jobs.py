import pathlib
import os

from scrapy.crawler import CrawlerProcess
from spiders.django_jobs_spider import DjangojobsSpider
from spiders.python_jobs_spider import PythonjobsSpider

from csv_management.csv_management import extract_csv_info
from filter.filter import filter_by_category, filter_by_type


def main():
    """Main function :
    - Crawl spiders simultaneously.
    - Move the created csv files in a data folder.
    - Filter the jobs by category and type,
     creating a file by type and category, in a dedicated folder.
    """

    # Crawling Spiders
    process = CrawlerProcess()
    process.crawl(DjangojobsSpider)
    process.crawl(PythonjobsSpider)
    process.start()

    # Organize Files
    os.makedirs(pathlib.Path.cwd() / 'data', exist_ok=True)
    os.replace(pathlib.Path.cwd() / 'djangojobs.csv', pathlib.Path.cwd() / 'data' / 'djangojobs.csv')
    os.replace(pathlib.Path.cwd() / 'pythonjobs.csv', pathlib.Path.cwd() / 'data' / 'pythonjobs.csv')

    # Filter
    lists_of_all_information, csv_headers = extract_csv_info()
    filter_by_category(csv_headers, lists_of_all_information)
    filter_by_type(csv_headers, lists_of_all_information)


if __name__ == '__main__':
    main()
