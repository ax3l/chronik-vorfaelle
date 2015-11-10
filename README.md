Visualisierung Flüchtlingsfeindlicher Vorfälle in Deutschland 2015
------------------------------------------------------------------

Dies ist ein Projekt zur Visualisierung, Archivierung, Aufbereitung
und journalistischen Weiternutzung der gesammelten Daten von
  https://www.mut-gegen-rechte-gewalt.de/service/chronik-vorfaelle

mit freundlicher Genehmigung der Amadeu Antonio Stiftung.


## Inhalt dieses Repositories

Dieses Repository ("Archiv") ist in folgende unabhängige Branches
("Zweige") gegliedert:

- `readme`: enthält diese Information
- `data`: exportierte und um Koordinaten angereicherte Rohdaten,
          werden unregelmäßig aktualisiert
- `scraper`: Skripte zum Erstellen der Daten
- `gh-pages`: statische HTML Seiten mit interaktiven Karten welche
              unter https://ax3l.github.io/chronik-vorfaelle/
              besucht werden können


## In Arbeit

- Quellen-Links in GeoJSON und Pop-Up Beschreibungen übernehmen
- Filtern nach Kategorie
- "uncluster" Knopf
- Legende
- Animation Zeitverlauf


## Danksagungen

Vielen Dank an die großartigen Menschen von mut-gegen-rechte-gewalt.de
für das akribische Sammeln und Dokumentieren der Vorfälle.

Kudos an die Entwickler und Communities folgender Open-Source Projekte:
- [python](http://python.org)
- [scrapy](http://scrapy.org)
- [geographic JSON](http://geojson.org) WG (IETF)
- [geopy](https://github.com/geopy/geopy)
- [leaflet.js](http://leafletjs.com) ([PruneCluster](https://github.com/SINTEF-9012/PruneCluster) plugin)
- [OpenStreetMap](http://openstreetmap.org)

Für Hosting und Vorschau Visualisierungen danke an GitHub &
[MapBox](http://mapbox.com).
