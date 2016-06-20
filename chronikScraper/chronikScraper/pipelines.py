# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem
from geopy.geocoders import Nominatim
import random

class EntryPipeline(object):

    def open_spider(self, spider):
        # print("OPEN PIPELINE")

        ## Categories
        # Brandanschlag
        # Sonstige Angriffe auf Unterkuenfte (Stein-/Boellerwuerfe, Schuesse, rechte Schmierereien etc.)
        # Taetlicher Uebergriff/Koerperverletzung
        # Kundgebung/Demo
        # other (should be empty)
        self.json_object = { "type": "FeatureCollection",
                             "features" : [] }

    def close_spider(self, spider):
        # print("CLOSE PIPELINE")
        file = open('vorfaelle.geojson', 'wb')
        json_txt = json.dumps( dict(self.json_object),
                               sort_keys=True, indent=4 )
        file.write( json_txt )
        file.close()

    def _format_item(self, item):
        return u"{}: {}, {}".format(
                   item["date"],
                   item["city"],
                   item["state"]
               )

    def _same_city_des_date(self, item1, item2):
        if item1["description"] == item2["description"] and \
           item1["city"] == item2["city"] and \
           item1["date"] == item2["date"] :
            return True
        return False

    def process_item(self, item, spider):
        # print("PROCESS ITEM")
        # print(item)

        is_doublicate = False
        same_cdd = filter(lambda e: self._same_city_des_date(e["properties"], item), self.json_object['features'])

        if len(same_cdd) :
            is_doublicate = True
        if is_doublicate:
            print(u"[DUPLICATE] Duplicate chronik entry for " + self._format_item(item) +
                  u" (duplicate of: " + self._format_item(same_cdd[0]["properties"]) + u")"
                 )
            return
            raise DropItem("Duplicate chronik entry for {}: {}".format(
                              item["date"].encode("ascii","ignore"),
                              item["city"].encode("ascii","ignore")
                            )
                          )

        # add geo location
        geolocator = Nominatim()
        place = u"{city}, {state}, Deutschland".format(**item)
        # print(place)
        location = geolocator.geocode(place, timeout=5) # 5sec timeout

        if not location:
            print(u"[GEOMISS] No nominatim chronik entry for " + self._format_item(item))
            return
            raise DropItem("Unknown coordinates for {}: {}".format(
                              item["date"].encode("ascii","ignore"),
                              item["city"].encode("ascii","ignore"),
                              item["state"].encode("ascii","ignore")
                            )
                          )


        lat = location.latitude
        long = location.longitude

        # visualization: adding a few meters noise
        # avoids hiding multiple points for the same city
        noise = 2.e-3 * random.random() - 1.0e-3 # +- 1.e-3
        lat  += noise
        noise = 2.e-3 * random.random() - 1.0e-3 # +- 1.e-3
        long += noise

        # convert to plain json
        #line = json.dumps(dict(item)) + "\n"
        #self.file.write(line)

        # add to GeoJSON object
        #print(self.json_object)
        self.json_object['features'].append(
          {
            "type": "Feature",
            "geometry": { "type": "Point",
                          "coordinates": [long, lat] },
            "properties": dict(item)
          } )

        return item
