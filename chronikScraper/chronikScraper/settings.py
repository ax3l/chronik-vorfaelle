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

LOG_LEVEL = 'INFO' # default: DEBUG; order: CRITICAL, ERROR, WARNING, INFO, DEBUG
