Visualisierung Flüchtlingsfeindlicher Vorfälle in Deutschland 2015-2016
-----------------------------------------------------------------------

Dies ist ein Projekt zur Visualisierung, Archivierung, Aufbereitung
und journalistischen Weiternutzung der gesammelten Daten von
  https://www.mut-gegen-rechte-gewalt.de/service/chronik-vorfaelle

mit freundlicher Genehmigung der Amadeu Antonio Stiftung.


## Inhalt dieses Repositories

Dieses Repository ("Archiv") ist in folgende unabhängige Branches
("Zweige") gegliedert:

- `readme`: enthält diese Information
- `data`: exportierte und um Koordinaten angereicherte Rohdaten,
          werden regelmäßig aktualisiert
          ([letztes Update](https://github.com/ax3l/chronik-vorfaelle/commits/data))
- `scraper`: Skripte zum Erstellen der Daten
- `gh-pages`: statische HTML Seiten mit interaktiven Karten welche
              unter https://ax3l.github.io/chronik-vorfaelle/
              besucht werden können


## Daten zum Download

Die exportierte und um geographische Koordinaten ergänzte
[Chronik](https://www.mut-gegen-rechte-gewalt.de/service/chronik-vorfaelle)
kann wie folgt heruntergeladen werden:

- [GeoJSON](https://raw.githubusercontent.com/ax3l/chronik-vorfaelle/data/vorfaelle.geojson)
  (bevorzugt) [Datenformat](http://geojson.org/)
- [CSV](https://raw.githubusercontent.com/ax3l/chronik-vorfaelle/data/vorfaelle.csv)
  (experimentell) [Datenformat](https://de.wikipedia.org/wiki/CSV_%28Dateiformat%29)


## In Arbeit

- Exportiere und füge letzte Aktualisierung hinzu (JSON)
- "uncluster" Knopf
- cluster: feinkörniger bzw. pro bundesland?
- Animation/Filter Zeitverlauf
- Histogramm: Ereignisse je Woche über Zeit
- Suchfunktion (extra Seite? Filter-Suche nach Stadt/Bundesland/Datum?)
- Screenshot (desktop, mobile, pdf-print) jeder Quelle
  inkl. Datum des Abrufs für das Archiv
  ([khtml2png](http://khtml2png.sourceforge.net/),
   [pdfkit](https://pypi.python.org/pypi/pdfkit/0.4.1),
   [QtWebKit](https://webscraping.com/blog/Webpage-screenshots-with-webkit/))


## Danksagungen

Vielen Dank an die großartigen Menschen von mut-gegen-rechte-gewalt.de
für das akribische Sammeln und Dokumentieren der Vorfälle.

Kudos an die Entwickler und Communities folgender Open-Source Projekte:
- [python](http://python.org)
- [scrapy](http://scrapy.org)
- [geographic JSON](http://geojson.org) WG (IETF)
- [geopy](https://github.com/geopy/geopy)
- [json_to_csv.py](https://github.com/vinay20045/json-to-csv)
- [leaflet.js](http://leafletjs.com) ([PruneCluster](https://github.com/SINTEF-9012/PruneCluster) plugin)
- [OpenStreetMap](http://openstreetmap.org)
- [Humanitarian OpenStreetMap Team](http://hot.openstreetmap.org/)

Für Hosting und Vorschau Visualisierungen danke an GitHub &
[MapBox](http://mapbox.com).
