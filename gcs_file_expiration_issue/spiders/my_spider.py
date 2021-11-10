import scrapy


class MySpiderSpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['example.org']
    start_urls = ['http://example.org/']

    custom_settings = {
        'ITEM_PIPELINES':  {
            'scrapy.pipelines.files.FilesPipeline': 1
        },
        'FILES_URLS_FIELD': 'files',
        'FILES_RESULT_FIELD':  'files_processed',
        'FILES_STORE': './data/',
        'GCS_PROJECT_ID': 'project_id',
    }

    def parse(self, response):
        return {
            'files': ['https://scrapy.org/img/scrapylogo.png'],
        }
