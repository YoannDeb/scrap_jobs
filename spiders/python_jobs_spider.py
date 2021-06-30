import scrapy


class PythonjobsSpider(scrapy.Spider):
    name = 'pythonjobs'
    custom_settings = {
        "FEEDS": {
            "pythonjobs.csv": {
                "format": "csv",
                "encoding": "utf8",
                "overwrite": "True"
            }
        },
        "CONCURRENT_REQUESTS": 1,
    }
    start_urls = [
        'https://www.python.org/jobs/?page=1',
        'https://www.python.org/jobs/?page=2',
        'https://www.python.org/jobs/?page=3',
        'https://www.python.org/jobs/?page=4'
    ]

    def parse(self, response):
        for job in response.css('ol.list-recent-jobs li'):
            raw_type_known = job.css('.listing-job-type a ::text').getall()
            raw_type_unknown = job.css('.listing-job-type::text').getall()
            post_type = ", ".join(raw_type_known) + "".join(raw_type_unknown[-1].strip())
            location = job.css('.listing-location a::text').get().split(",")
            if len(location) == 2:
                location = [location[0], '', location[1]]
            #location = ["Boston", "NYC", "United States"]
            yield {
                'title': job.css('.listing-company-name a::text').get(),
                'company': job.css('.listing-company-name::text').getall()[-1].strip(),
                'link': f"https://www.python.org/jobs{job.css('.listing-company-name a::attr(href)').get()}",
                'city': location[0],
                'state': location[1],
                'country': location[-1],
                'pub_date': job.css('time::text').get(),
                'post_type': post_type,
                'category': job.css('.listing-company-category a::text').get(),
                'remote': '',
                'relocation': ''
            }