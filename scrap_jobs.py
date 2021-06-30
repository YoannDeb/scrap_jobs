import pathlib
import os
import csv

import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.django_jobs_spider import DjangojobsSpider
from spiders.python_jobs_spider import PythonjobsSpider


def create_csv(folder, csv_name, headers, information_lists):
    """create csv file with a list of lists

    :param folder: name of the folder the file will be created into
    :param csv_name: name of the csv file
    :param headers: headers of the csv file (first row)
    :param information_lists: a list of lists of information
    """
    os.makedirs(pathlib.Path.cwd() / 'data' / folder, exist_ok=True)
    with open(
            pathlib.Path.cwd() / 'data' / folder / csv_name, 'w', newline='', encoding='utf-8-sig'
    ) as f:
        csv.writer(f).writerow(headers)
        for i in range(0, len(information_lists)):
            csv.writer(f).writerow(information_lists[i])


def main():

    # Crawling DjangojobsSpider
    process = CrawlerProcess()
    process.crawl(DjangojobsSpider)
    process.crawl(PythonjobsSpider)
    process.start()

    # File organizing
    os.makedirs(pathlib.Path.cwd() / 'data', exist_ok=True)
    os.replace(pathlib.Path.cwd() / 'djangojobs.csv', pathlib.Path.cwd() / 'data' / 'djangojobs.csv')
    os.replace(pathlib.Path.cwd() / 'pythonjobs.csv', pathlib.Path.cwd() / 'data' / 'pythonjobs.csv')

    # extract info from csv
    lists_of_all_information = []
    with open(pathlib.Path.cwd() / 'data' / 'pythonjobs.csv', 'r', encoding='utf-8') as f:
        content = csv.reader(f)
        for row in content:
            lists_of_all_information.append(row)
    csv_headers = lists_of_all_information.pop(0)

    # filter by category
    list_of_categories = ["Data_Analyst", "Developer_Engineer", "Manager_Executive", "Other", "Researcher_Scientist"]
    for i in range(0, 5):
        category = list_of_categories[i]
        lists_of_jobs_in_category = []
        for job in lists_of_all_information:
            if category[:4] in job[8]:
                lists_of_jobs_in_category.append(job)
        if lists_of_jobs_in_category:
            create_csv("sorted_by_category", f"Category_{category}.csv", csv_headers, lists_of_jobs_in_category)

    # filter by type
    list_of_types = ['Back end', 'Big Data', 'Cloud', 'Database', 'Evangelism', 'Finance', 'Front end', 'Fundraising', 'Image Processing', 'Integration', 'Lead', 'Machine Learning', 'Management', 'Numeric processing', 'Operations', 'Systems', 'Testing', 'Text Processing', 'Web']
    for job_type in list_of_types:
        lists_of_jobs_in_types = []
        for job in lists_of_all_information:
            if job_type in job[7]:
                lists_of_jobs_in_types.append(job)
        if lists_of_jobs_in_types:
            filename_job_type = job_type.replace(" ", "_")
            create_csv("sorted_by_type", f"Type_{filename_job_type}.csv", csv_headers, lists_of_jobs_in_types)


if __name__ == '__main__':
    main()
