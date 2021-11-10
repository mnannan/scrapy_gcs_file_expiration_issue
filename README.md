This repo aims to reproduce an issue in scrapy about file expiration with GCS.

# How to reproduce

* Install requirements.txt `pip install -r requirements.txt`
* set `GOOGLE_APPLICATION_CREDENTIALS` env var as described [here](https://cloud.google.com/docs/authentication/production#passing_variable)
* set `FILE_STORE` with the path where you want to export images on GCS. **Make sure that you path include 
a prefix like `gs://my_bucket/my_prefix`, paths without the prefix like `gs://my_bucket` are the only ones working with caching**.
You can also set `GCS_PROJECT_ID`.

* run ```scrapy crawl my_spider```
  * At that step scrapy will upload the file in `FILE_STORE/full/27200bf84dab638cb6b102bf709d8b17201a31d5.png`
* check that there has been a file uploaded in `FILE_STORE`.
* rerun ```scrapy crawl my_spider```
  * We would expect that scrapy does not redownload the file again but by looking at 
scraper stats we can see `'file_status_count/downloaded': 1` instead of `'file_status_count/uptodate': 1`.
  * The number of `downloader/request_count` is not the right one too as we would have expected `1` instead of `2`.
