# -*- coding: utf-8 -*-

# Scrapy settings for chronikScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'chronikScraper'

SPIDER_MODULES = ['chronikScraper.spiders']
NEWSPIDER_MODULE = 'chronikScraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'chronik scraper'

ITEM_PIPELINES = {
    'chronikScraper.pipelines.EntryPipeline': 10,
}

# limits
#   concurrent items (per response) to process in parallel in  pipeline
CONCURRENT_ITEMS = 1 # default: 100
#   maximum number of concurrent (ie. simultaneous) requests (scraper)
CONCURRENT_REQUESTS = 1 # default: 16
#   The amount of time (in secs) that the downloader should wait before
#   downloading consecutive pages from the same website
DOWNLOAD_DELAY = 0.5 # default: 0.0s
#   wait a random amount of time (between 0.5 and 1.5 * DOWNLOAD_DELAY)
RANDOMIZE_DOWNLOAD_DELAY = True # default: True

LOG_LEVEL = 'INFO' # default: DEBUG; order: CRITICAL, ERROR, WARNING, INFO, DEBUG
