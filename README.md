# nachgeradelt.de - Coding da Vinci Ost 2018

velo Open Access: Wir machen regionales #Radfahrerwissen wieder sichtbar.

Behauptung: die alten Tourenbücher funktionieren noch weitgehend, denn Orte, Wege und Straßen sind meist noch da, wo sie um 1900 waren.

Idee: Eine Webanwendung, um diese Behauptung exemplarisch für eine historische Radtourenbeschreibungen um Leipzig zu überprüfen und, um ggf. anschließend als Event zu veranstalten und Nachahmer zu aktivieren. Über Filterfunktionen soll digitalisiertes Wissen auch von (anderen) Kulturgütern entlang der Strecke darstellbar sein. Die Webanwendung soll im Idealfall Nachnutzung ermöglichen. In der Pilotphase ensteht eine Tour bei oder um Leipzig.

Entstehen soll ein Dossier der digitalisierten Geschichte entlang der Tour.
Entlang der Strecken könnten auch die digitalisierten Kulturgüter (z. B. Fotos vom Flachsanbau in der Lausitz, andere Sammlungen, ...) anderer Datengeber/CdVost-Instititionen verknüpft werden - aber auch bspw. die ortsbezogenen Werbeanzeigen anlang der Strecken: Gastwirtschaften/Bundeshotels, Werkstätten, Fabriken, Handel.

* Demo: http://leipzig-data.de/Nachgeradelt/#/
* Kollektion 'Das Fahrrad': http://digital.slub-dresden.de/kollektionen/185/
* Datensatz: https://codingdavinci.de/daten/#slub-dresden

Weitere Quellen in Wikisource:

* Tourenbücher, https://de.wikisource.org/wiki/Tourenb%C3%BCcher_f%C3%BCr_Radfahrer
* Jahrbuch der dt. Radfahrer-vereine 1897, https://de.wikisource.org/wiki/Jahrbuch_der_deutschen_Radfahrer-Vereine
* Liederbuch des Gau 19 Rostock des Deutschen Radfahrer-Bundes, https://de.wikisource.org/wiki/Liederbuch_des_Gau_19_Rostock_des_Deutschen_Radfahrer-Bundes

## Projektkommunikation

* [CdV Ost Hackdash](https://hackdash.org/projects/5ad21c1e35377d7f73a9a145)
* [Etherpad](https://etherpad.gwdg.de/p/Radfahrerwissen)
* [Trello](https://trello.com/b/KkCvwa9g/das-fahrrad)

## Anmerkungen

Die Demo nutzte zur Berechnung der Routen den Service von [OpenRoute](https://openrouteservice.org/). Der Service nutzt einen eindeutigen Key zur Authentisierung. Dieser Key ist für kostenlose Lizensen allerdings auf 25.000 Anfragen
begrenzt und wird danach invalide. Damit die Demo unabhängig von diesen Service funktioniert,
wurden die GeoJson für beide Routen als Konstanten hinterlegt. 
