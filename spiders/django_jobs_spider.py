import scrapy


class DjangojobsSpider(scrapy.Spider):
    name = 'djangojobs'
    custom_settings = {
        "FEEDS": {
            "djangojobs.csv": {
                "format": "csv",
                "encoding": "utf8",
                "overwrite": "True"
            }
        },
        "CONCURRENT_REQUESTS": 1,
    }
    start_urls = [
        'https://djangojobs.net/jobs/?page=1',
        'https://djangojobs.net/jobs/?page=2',
        'https://djangojobs.net/jobs/?page=3',
        'https://djangojobs.net/jobs/?page=4',
        'https://djangojobs.net/jobs/?page=5',
        'https://djangojobs.net/jobs/?page=6',
        'https://djangojobs.net/jobs/?page=7',
        'https://djangojobs.net/jobs/?page=8',
        'https://djangojobs.net/jobs/?page=9',
        'https://djangojobs.net/jobs/?page=10',
        'https://djangojobs.net/jobs/?page=11',
        'https://djangojobs.net/jobs/?page=12',
        'https://djangojobs.net/jobs/?page=13',
        'https://djangojobs.net/jobs/?page=14',
        'https://djangojobs.net/jobs/?page=15',
        'https://djangojobs.net/jobs/?page=16',
        'https://djangojobs.net/jobs/?page=17'
    ]

    job_counter = 0

    def parse(self, response):
        title = response.css('h4 a::text').getall()
        link = response.css('h4 a::attr(href)').getall()
        location_pub_date = response.css("div.clearfix div.float-right::text").getall()
        remote_relocation = response.css('div.clearfix::text').getall()
        if self.job_counter <= 95:
            jobs_in_page = 6
        else:
            jobs_in_page = 4

        for i in range(0, jobs_in_page):
            location = location_pub_date[i][:-15].split(',')
            if len(location) == 2:
                location = [location[0], '', [location[1]]]
            else:
                location = [location[0], '', '']
            yield {
                'title': title[i*2].replace(',', ''),
                'company': title[i*2+1].replace(',', ''),
                'link': f"https://djangojobs.net{link[i]}",
                'city': location[0],
                'state': location[1],
                'country': location[2],
                'pub_date': location_pub_date[i][-12:],
                'post_type': '',
                'category': '',
                'remote': remote_relocation[i*2][13:16].strip(),
                'relocation': remote_relocation[i*2][-16:-13].strip()
            }
            self.job_counter += 1

        print(f'Total Django_jobs yielded : {self.job_counter}')
