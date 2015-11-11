#!/usr/bin/env bash
#

cd chronikScraper

scrapy crawl chronikScraper
mv vorfaelle.geojson ../

cd ..

