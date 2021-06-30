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
        'https://djangojobs.net/jobs/?page=6'
    ]
    job_counter = 0

    def parse(self, response):
        title = response.css('h4 a::text').getall()
        link = response.css('h4 a::attr(href)').getall()
        location_pub_date = response.css("div.clearfix div.float-right::text").getall()
        remote_relocation = response.css('div.clearfix::text').getall()
        if self.job_counter <= 81:
            jobs_in_page = 19
        else:
            jobs_in_page = 4

        for i in range(0, jobs_in_page+1):
            location = location_pub_date[i][:-15].split(',')
            if len(location) == 2:
                location = [location[0], '', [location[1]]]
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
        # yield scrapy.Request("https://djangojobs.net/jobs/?page=2")
        # yield scrapy.Request("https://djangojobs.net/jobs/?page=3")
        # yield scrapy.Request("https://djangojobs.net/jobs/?page=4")
        # yield scrapy.Request("https://djangojobs.net/jobs/?page=5")

        # for j in range(2, 6):
        #     yield scrapy.Request(f"https://djangojobs.net/jobs/?page={j}", callback=self.parse)
#        for next_page in response.css('a.next'):
#            yield response.follow(next_page, self.parse)

# title = response.css('h4 a::text').get()
# link = f"https://djangojobs.net/{response.css('h4 a::attr(href)').get()}"
# location_pub_date = response.css("div.clearfix div.float-right::text").get()
# city =
# state =
# country =
# pub_date =
# post_type = []
# category = []
# remote_relocation = response.css('div.clearfix::text').get()
# remote =
# relocation =
