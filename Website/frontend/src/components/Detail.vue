<template>
  <div class="detail">
    <h2>Deine historische Radtour:
      <br/> {{$route.params.id === '46' ? 'Leipzig - Dessau - Wörlitz' : 'Leipzig - Altenburg - Werdau'}}</h2>
    <div v-show="$route.params.id === '100'">
      <p>
        Über Lobstädt — Altenburg — Crimmitschau
      </p>
      <p>
        79,6 km guter, erst ebener, dann welliger und hügeliger Strasse.
      </p>
      <div class="teaser">
        <div class="galleryItem">
          <a title="By Appaloosa [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Altes_Rathaus_Leipzig_2013.jpg">
            <img width="512" alt="Altes Rathaus Leipzig 2013" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Altes_Rathaus_Leipzig_2013.jpg/512px-Altes_Rathaus_Leipzig_2013.jpg">
          </a>
        </div>
        <div class="galleryItem">
          <a title="By NcMhlr at de.wikipedia [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], from Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Altenburg-Schloss.jpg">
            <img width="512" alt="Altenburg-Schloss" src="https://upload.wikimedia.org/wikipedia/commons/3/33/Altenburg-Schloss.jpg">
          </a>
        </div>
        <div class="galleryItem">
          <a title="By André Karwath aka Aka [CC BY-SA 2.5 (https://creativecommons.org/licenses/by-sa/2.5)], from Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Werdau_-_townhall_(aka).jpg">
            <img width="512" alt="Werdau - townhall (aka)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Werdau_-_townhall_%28aka%29.jpg/512px-Werdau_-_townhall_%28aka%29.jpg">
          </a>
        </div>
      </div>
      <button class="accordion">
        <h3>Leipzig nach Zwenkau</h3>
      </button>
      <div class="panel">
        <h4>Wegbeschreibung</h4>
        <p>
          0,0. 0,0 Leipzig. 111. P. T. B. S. No. l. Ausfahrt Königsplatz, Peterssteinw., Zeitzerstr., Südpl., Südstr., Leipzigerstr.
          i. Connewitz, dann r. üb. d. Brücke, hier d. Coburger Str. üb. 7,0 Gautzsch; 1.8 Zöbigker; 1,1 Prödel; n. 4,6
        </p>
        <h4>Wegpunkte</h4>
        <h5>Leipzig</h5>
        <h6>Karl-Liebknecht-Straße (ehem. Zeitzer Straße und Südstraße)</h6>
        <p>
          Zeitzer Straße und Südstraße wurden 1933 zusammengelegt und in Adolf-Hitler-Straße umbenannt. Nach Ende des Zweiten Weltkriegs
          erhielt sie unter US-amerikanischer Besatzung zunächst ihren alten Namen zurück, bevor sie im selben Jahr unter
          sowjetischer Besatzung in Karl-Liebknecht-Straße umbenannt wurde.
        </p>
        <h6>Restaurant Forsthaus Raschwitz</h6>
        <p>
          Das Restaurant „Forsthaus Raschwitz“ lädt schon 1900 alle Radfahrenden zu einer Pause ein:
        </p>
        <p>
          „Hier geben sich die Radlerinnen und Radler ihr Rendezvous, und wenn man an Sonn- und Festtagen die Straße beobachtet, sollte
          man fast glauben, es seien die Stahlrosse zur alleinherrschenden Macht auf dem Gebiete des Verkehrswesens geworden."
        </p>
        <p>
          aus SLUB Dresden: "Adreßbuch für die südlichen Vororte Leipzigs", 1904,
          <a href="http://digital.slub-dresden.de/id403758513-19040000">http://digital.slub-dresden.de/id403758513-19040000</a>, IV. Abt., S. 4.
        </p>
        <p>
          Restaurant Forsthaus Raschwitz
          <br> Koburger Straße 33
          <br> 04416 Markkleeberg
        </p>
        <h5>Zwenkau</h5>
        <p>
          14,5. 14,5 Zwenkau. 133. P. T. B. Hier r. n. Markranstädt 12,6; Zw. früher bed. Ort, jetzt Landstädtchen, wurde i. J. 974
          v. Kaiser Otto II. dem Stifte Merseburg geschenkt. Auf einem Hügel an der Elsterniederung Reste einer im Mittelalter
          berühmten Burg; 1315 wurde bei ein. Belagerung ders. Friedr. d. Lahme, Markgr. Friedr. d. Gebissenen Sohn, m. ein.
          Pfeile erschossen.
        </p>
        <h6>Gaststätte Schützenhaus</h6>
        <p>
          Wer einkehren möchte, wo sich schon 1904 der Radfahrer-Verein Zwenkau traf, kann das in der Gaststätte „Schützenhaus“ tun.
        </p>

        <div>
          <img src="http://digital.slub-dresden.de/fileadmin/data/403758513-19040000/403758513-19040000_tif/jpegs/00000431.tif.large.jpg"
            alt="Anzeige Restaurant 'Zum Schützenhaus' Zwenkau">
          <p>SLUB Dresden: "Adreßbuch für die südlichen Vororte Leipzigs", 1904,
            <a href="http://digital.slub-dresden.de/id403758513-19040000">http://digital.slub-dresden.de/id403758513-19040000</a>, IV. Abt., S. 4.</p>
        </div>
        <p>
          Gaststätte Schützenhaus
          <br> Geschwister-Scholl-Platz 1
          <br> 04442 Zwenkau
        </p>
      </div>
      <button class="accordion">
        <h3>Zwenkau nach Altenburg</h3>
      </button>
      <div class="panel">
        <h4>Wegbeschreibung</h4>
        <p>
          Weiter üb. Kotzschbar u. Imnitz (m. alt. Kapelle) zur 1,2 Strassengabelung; h. 1. üb. 2,9 Pulgar; 2.0 Medewitzsch: 4,1 Bahnh.
          Kieritzsch P. T. B.; 3,4 n.
        </p>
        <h4>Wegpunkte</h4>
        <h5>Neukieritzsch (ehem. Medewitzsch, Pulgar)</h5>
        <p>
          Das Dorf Medewitzsch wurde 1934 nach Lippendorf eingemeindet, dabei verdrängte der Ortsname Lippendorf den Ortsnamen Medewitzsch.
          Heute gehört Lippendorf zur Gemeinde Neukieritzsch.
        </p>
        <p>
          Die Gemeinde Pulgar wurde ab 1971 schrittweise abgebrochen und mit den Chemischen Werken Böhlen überbaut. Heute gehören die
          Flächen zur Gemeinde Neukieritzsch.
        </p>
        <div>
          <img src="http://fotothek.slub-dresden.de/fotos/df/dk/0010000/df_dk_0010001_4840_1894.jpg" alt="Äquidistantenkarte 42: Section Lobstädt, 1894">
          <p>
            SLUB/Deutsche Fotothek: "Äquidistantenkarte 42: Section Lobstädt", 1894,
            <a href="http://www.deutschefotothek.de/documents/obj/71055352">http://www.deutschefotothek.de/documents/obj/71055352</a> (CC-BY-SA 4.0).
          </p>
        </div>
        <h5>Lobstädt</h5>
        <p>
          13,6. 28,1 **Lobstädt**. 140. P. T. B. Hier Strassengabelung (1. l. n. 4,6 Borna), r. weiter sanft steigend üb. 4,5 r. Blumroda
          (h. 1. n. 5,0 Borna); 4,0 Serbitz; 0,8 Treben, P. T, B.; 3,1 Zschaschelwitz; üb. d. Str. Lucka-Geithain (l. n.
          19,1 Geithain, r. n. 15,9 Lucka); mit stark. Fall 4,5 n.
        </p>
        <h5>Altenburg</h5>
        <p>
          16,9. 45,0 **Altenburg**. 178. P. T. B. Hier r. n. 10,9 Schmölln; 24,8 Ronneburg; 11,7 Meuselwitz; l. n. 22,1 Penig und 18.0
          Waldenburg. Residenz d. Herzöge v. Sachs-Altenburg aus d. Hause Wettin ernestinischer L. Alte, ber. 980 urk. erw.
          St., i. 12. Jahrh. Reichsst., anf. d. 14. Jahrh. an d. Haus Wettin. Auf mächt., steil. Porphyrfelsen d. herzogl.
          Schloss a. d. 11. Jahrh. Nach verschied. Bränden 1706—44 neu geb. (die 1865 und 1868 abgebr. Flügel sind ern.),
          m. prächt. Saale, Rüstkammer, Kunstkammer, schönem Park. 8. Juli 1455 Prinzenraub (Kurf. Friedr. d. Sanftmüt. v.
          Sachs. Söhne Ernst u. Albert. Kunz v. Kaufungen). Am Fusse d. Schlossberges Siegesdenkm. u. Denkmal Kais. Wilh.
          I. Am Markte d. 1562-64 im deutsch. Renaissancestil erb. Rath. Von Kirchen sind zu erw. die 1087 geb. u. 1878 ern.
          Bartholomäik., die 1411 erb. spätgot. Schlosskirche. Sehensw. noch die Roten Spitzen, ehem. Augustinerkl., 1172
          v. Kaiser Friedr. I. gegr., 1533 aufgeh., 1872 ern., enth. das Staatsarchiv. —A. hat schöne Promenaden an 3 grossen
          Teichen.
        </p>
      </div>
      <button class="accordion">
        <h3>Altenburg nach Crimmitschau</h3>
      </button>
      <div class="panel">
        <h4>Wegbeschreibung</h4>
        <p>
          Von A. hügelig w. üb. 1. 3,4 Mockern; 1,0 Gardschütz; r. 1,0 Lehndorf, P. T. B.; 2,0 Zehma; 1,5 Löhmigen; 3,0 Gössnitz (hier
          r. üb. Nörditz, Nietzschka n. 6,6 Schmölln, —hinter Gössn. r. üb. Schönhain, Frankenhausen gute Str. n. 8,0 Crimmitschau);
          4.0 Guteborn (hinter Guteb. 1. n. 1,9 Meerane); 4,3 Gasth. Silberner Pelikan (hier l. n. 6,5 Glauchau, geradeaus
          üb. Mosel n. 12,5 Zwickau); weiter r. n. 4,3 (Fall!)
        </p>
        <h4>Wegpunkte</h4>
        <h5>Crimmitschau</h5>
        <p>
          24,5. 69,5 Crimmitschau. 230. P. T. B. Cr. wird 1210 als Stadt erwähnt; 1430 v. d. hussit. Tschechen verbrannt, im dreissigjähr.
          Kriege fünfmal geplündert; besass 1794 noch seine Ringmauern mit 3 Thoren und 2 Türmen. 1748 Einführung der Streichgarnspinnerei
          durch David Oehler.
        </p>
        <h6>Textilstadt Crimmitschau</h6>
        <p>
          Anknüpfend an die Initiative von David Friedrich Oehler hat sich Crimmitschau zu einem Zentrum der Textilindustrie entwickelt.
          Wer 1899 nach Crimmitschau radelt, sieht schon von weitem die vielen Fabrikgebäude, die Crimmitschau den Spitznamen
          „Stadt der 100 Schornsteine“ eingebracht haben:
        </p>
        <p>
          „Der Reisende staunt bei dem Herannahen [...] über den wahren Wald von Dampfessen, welcher sich oft dicht zusammengedrängt
          auf allen Stellen erhebt[...], so dass der ganze Platz den Anblick gewährt, als sei er eine einzige große Fabrik.“
        </p>
        <p>
          aus SLUB Dresden: "Album der Sächsischen Industrie", 1856,
          <a href="http://digital.slub-dresden.de/id252070399">http://digital.slub-dresden.de/id252070399</a>, Bd. 1, S. 119, (CC-BY-SA 4.0).
        </p>
        <div>
          <img src="http://fotothek.slub-dresden.de/fotos/df/dk/0005000/df_dk_0005155.jpg" alt="Ansicht von Crimmitschau, Lithografie, 1860">
          <p>
            SLUB/Deutsche Fotothek: G. Frank, "Ansicht von Crimmitschau", Lithografie, 1860,
            <a href="http://www.deutschefotothek.de/documents/obj/70401522">http://www.deutschefotothek.de/documents/obj/70401522</a> (CC-BY-SA 4.0).
          </p>
        </div>
        <h6>Industriearchitektur</h6>
        <p>
          Manche der Tuchfabriken, Spinnereien und Färbereien, welche das Stadtbild lange Zeit geprägt haben, existieren auch heute
          noch und sind in der Datenbank des Projekts
          <a href="https://www.industrie-kultur-ost.de/datenbank/textilindustrie/gebiet-zwickau/">Industrie.Kultur.Ost</a> erfasst.
        </p>
        <div>
          <img src="http://digital.slub-dresden.de/fileadmin/data/252070399/252070399_tif/jpegs/00000383.tif.large.jpg" alt="Vigogne-Spinnerei von H. F. Kürzel in Crimmitschau">
          <p>
            SLUB Dresden: "Album der Sächsischen Industrie", 1856,
            <a href="http://digital.slub-dresden.de/id252070399">http://digital.slub-dresden.de/id252070399</a>, Bd. 1, (CC-BY-SA 4.0).
          </p>
        </div>
        <h6>Sächsisches Industriemuseum</h6>
        <p>
          In der historischen Tuchfabrik Gebr. Pfau ist inzwischen das Sächsische Industriemuseum untergebracht und macht die damaligen
          Produktionsbedingungen erlebbar.
        </p>
        <p>
          Sächsisches Industriemuseum
          <br> Tuchfabrik Gebr. Pfau
          <br> Leipziger Straße 125
          <br> 08451 Crimmitschau
        </p>
      </div>
      <button class="accordion">
        <h3>Crimmitschau nach Werdau</h3>
      </button>
      <div class="panel">
        <h4>Wegbeschreibung</h4>
        <h5>Werdau</h5>
        <p>
          10,1. 79,6 Werdau. 281. P. T. B. Hier l. n. 10,0 Zwickau. —1298 als Stadt angeführt; 1430 Zerstörung durch d. Hussiten, 1633
          Pest. W. hatte früher starke Stadtmauer mit zwei Thoren. — Bedeutende Textilindustrie.
        </p>
        <h6>Fahrradfieber um 1900</h6>
        <p>
          Auch Werdau hat 1899 eine aktive Radler-Szene: Laut den historischen Adressbüchern gibt es in der Stadt im Jahr 1903 fünf
          verschiedene Radfahrer-Klubs, von denen drei seit 1897 neu gegründet wurden.
        </p>
        <p>
          aus SLUB Dresden: "Adreßbuch der Fabrikstadt Werdau mit den Vororten Leubnitz, Steinpleis und Langenhessen", 1903,
          <a href="http://digital.slub-dresden.de/id380404613-19030000">http://digital.slub-dresden.de/id380404613-19030000</a> (CC-BY-SA 4.0).
        </p>
        <h6>Arbeiter-Radfahrer</h6>
        <p>
          Wer fährt überhaupt Rad um 1900? Wegen der hohen Anschaffungskosten war Radfahren zunächst vor allem ein Sport des Bürgertums.
          Um 1900 ändert sich das: Als die Preise für Fahrräder sinken, können sich auch besser verdienende Fabrikarbeiter*innen
          ein gebrauchtes Rad leisten.
        </p>
        <p>
          In den 1890er Jahren gründen sich spezielle Arbeiter-Radfahrer-Klubs wie der „Arbeiter-Radfahrerbund Solidarität“, der sich
          ausdrücklich als Teil der Arbeiterbewegung versteht. Auch die Industriestadt Werdau verzeichnet für 1903 einen
          Ableger der „Solidarität“.
        </p>
        <p>
          Ihre Kritik an den bürgerlichen Vereinen bringt die „Solidarität“ so auf den Punkt: „[…] in diesen bürgerlichen radsportlichen
          Organisationen hat[] man es sich zur Aufgabe gemacht, in der Hauptsache dem Radrennsport zu huldigen und sich an
          allem möglichen patriotischen Klimbim zu beteiligen.“
        </p>
        <p>
          aus FES Bibliothek: A. Frahnert, "Werden und Wachsen des Arbeiter-Radfahrer-Bundes Solidarität: die Bundesgeschichte bis
          zum Jahre 1926", 1927,
          <a href="https://library.fes.de/opac/id/181481">https://library.fes.de/opac/id/181481</a>, S. 9.
        </p>
      </div>
      <div class="source">
        <p>
          aus SLUB Dresden: B. Böhm, "Touren-Buch des Sächsischen Radfahrer-Bundes", 1899,
          <a href="http://digital.slub-dresden.de/id407531238">http://digital.slub-dresden.de/id407531238</a> (CC-BY-SA 4.0).
        </p>
      </div>
    </div>
    <div v-show="$route.params.id === '46'">
      <p>Über Eutritzsch — Wiederitzsch — Delitzsch — Wolfen</p>
      <div class="teaser">
        <div class="galleryItem">
          <a title="By Appaloosa [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Altes_Rathaus_Leipzig_2013.jpg">
            <img width="512" alt="Altes Rathaus Leipzig 2013" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Altes_Rathaus_Leipzig_2013.jpg/512px-Altes_Rathaus_Leipzig_2013.jpg">
          </a>
        </div>
        <div class="galleryItem">
          <a title="Mewes [Public domain], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Bauhaus.JPG">
            <img width="512" alt="Bauhaus" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Bauhaus.JPG/512px-Bauhaus.JPG">
          </a>
        </div>
        <div class="galleryItem">
          <a title="I, Nikater [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:W%C3%B6rlitzer_See_mit_St._Petri.jpg">
            <img width="512" alt="Wörlitzer See mit St. Petri" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/W%C3%B6rlitzer_See_mit_St._Petri.jpg/512px-W%C3%B6rlitzer_See_mit_St._Petri.jpg">
          </a>
        </div>
      </div>
      <button class="accordion">
        <h3>Leipzig nach Eutritzsch</h3>
      </button>
      <div class="panel">
        <h4>Wegbeschreibung</h4>
        <p>Vom <a href="https://de.wikipedia.org/wiki/Leipzig">Marktplatz</a>, Katharinenstraße, Brühl, Am Hallischen Tor, Blücherplatz, Blücherstraße, Eutritzscher Straße, rechts
          Delitzscher Straße, Vorstadt Eutritzsch (3,5 km). Alte historische Gosenschänke. Außerhalb des Ortes Straßengabelung.</p>
        <h4>Wegpunkte</h4>
        <h5><a href="https://www.wikidata.org/wiki/Q49233392">Kraftwerk Eutritzscher Straße 14b</a></h5>
        <p><a href="http://www.leipziger-industriekultur.de/eutritzscher-strase-14a-kraftwerk/">Kraftwerk</a> mit Verwaltungsgebäude und Schalthaus, Verwaltungs- und Wohngebäude, Personalhaus, Maschinenhaus, Speise-
          und Kultursaal, mit Werkstattgebäude, Kühlturm, Kohleförderungsanlage, Schornstein, mit Gasometer und Einfriedung
          <a title="von Dguendel [GFDL (http://www.gnu.org/copyleft/fdl.html) oder CC BY 3.0 (https://creativecommons.org/licenses/by/3.0)], vom Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Leipzig,_W%C3%A4rmekraftwerk_Nord_-2.jpg">
            <img width="512" alt="Leipzig, Wärmekraftwerk Nord -2" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Leipzig%2C_W%C3%A4rmekraftwerk_Nord_-2.jpg/512px-Leipzig%2C_W%C3%A4rmekraftwerk_Nord_-2.jpg">
          </a>
        </p>
        <h5><a href="https://de.wikipedia.org/wiki/Eutritzsch">Eutritzsch</a></h5>
        <p>Im Jahr 1890 wurde die bis dahin selbständige Gemeinde Eutritzsch mit ihren damals 9.623 Einwohnern in die Stadt
          Leipzig eingemeindet.</p>
        <h5>Ehemaliges Rathaus</h5>
        <p><a href="https://denkmalliste.denkmalpflege.sachsen.de/CardoMap/Denkmalliste_Report.aspx?HIDA_Nr=09294423">Ehemaliges Rathaus</a> in Formen der Neorenaissance mit Schaugiebel, Uhrtürmchen und Einfriedung. Nach den Entwürfen
          des Leipziger Architekten Ottomar Jummel, der auch das Bismarckhaus am Leipziger Marktplatz entworfen hatte, im
          Jahre 1888 errichtet worden
          <a title="By Tino Strauss [GFDL (http://www.gnu.org/copyleft/fdl.html), CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/) or CC BY-SA 2.5 (https://creativecommons.org/licenses/by-sa/2.5)], from Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Rathaus_Eutritzsch_01.jpg">
            <img width="512" alt="Rathaus Eutritzsch 01" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Rathaus_Eutritzsch_01.jpg/512px-Rathaus_Eutritzsch_01.jpg">
          </a>
        </p>
      </div>
      <button class="accordion">
        <h3>Eutritzsch nach Wiederitzsch</h3>
      </button>
      <div class="panel">
        <h4>Wegbeschreibung</h4>
        <p>Geradeaus, dann am Krankenhaus St. Georg vorbei nach Wiederitzsch (3,3 km).
        </p>
        <h4>Wegpunkte</h4>
        <h5>Handschwengelpumpe Gräfestraße</h5>
        <p><a href="https://www.wikidata.org/wiki/Q49275003">Handschwengelpumpe</a> mit Brunnenschacht und Abdeckplatte (Typ Kleiner Löwe)
        </p>
        <h5>Krankenhaus Sankt Georg - heute Klinikum St. Georg Leipzig</h5>
        <p>Das <a href="https://de.wikipedia.org/wiki/Klinikum_St._Georg_Leipzig">Klinikum St. Georg</a> ist das älteste und nach dem Universitätsklinikum das zweitgrößte Krankenhaus in Leipzig.</p>
        <h5><a href="https://www.wikidata.org/wiki/Q49279411">Apelstein Delitzscher Landstraße</a></h5>
        <p><a href="https://de.wikipedia.org/wiki/Apelsteine">Apelstein</a> Nr. 21 (N); in Ecklage Seehausener Straße, Gedenkstein zur Erinnerung an die Kämpfe der Völkerschlacht
          bei Leipzig 1813 in und um Wiederitzsch, 12.000 Polen und Franzosen unter den Generälen Dombrowski, Souham und
          Delmas gegen Langerons
          <a title="Martin Geisler [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], from Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Apelstein-21.jpg">
            <img width="512" alt="Apelstein-21" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Apelstein-21.jpg/512px-Apelstein-21.jpg">
          </a>
        </p>
      </div>
      <button class="accordion">
        <h3>Wiederitzsch nach Delitzsch</h3>
      </button>
      <div class="panel">
        <h4>Wegbeschreibung</h4>
        <p>Ueber die sächsisch-preußische Grenze, durch Schladitz (4,6 km), mäßig abwärts über die alte Salzstraße nach Lemsel
          (3,6 km), Brodenaundorf (1,0 km) und Delitzsch (6,0 km).</p>
        <h4>Wegpunkte</h4>
        <h5><a href="https://www.wikidata.org/wiki/Q49259638">Gustav-Adolf-Denkmal</a></h5>
        <p>Gedenkstein, Schlacht bei Breitenfeld (1631) bei Breitenfeld am 17. September 1631; bedeutsames militärhistorisches
          und kirchengeschichtliches Denkmal, Erinnerungswert und Bedeutung für die Volksbildung
          <a title="By Nino Schramm [Copyrighted free use], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Gustav-Adolf-Denkmal_Breitenfeld.jpg">
            <img width="512" alt="Gustav-Adolf-Denkmal Breitenfeld" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Gustav-Adolf-Denkmal_Breitenfeld.jpg/512px-Gustav-Adolf-Denkmal_Breitenfeld.jpg">
          </a>
        </p>
        <h5>Schladitz</h5>
        <p><a href="https://de.wikipedia.org/wiki/Schladitz_%28Rackwitz%29">Schladitz</a> ist eine moderne Wüstung, die sich südlich von Delitzsch befand und mit seinem Ortsteil Kömmlitz zwischen
          1986 und 1990 dem Braunkohleabbau durch den Tagebau Breitenfeld zum Opfer fiel.</p>
        <h5>Wohnhaus, Torhaus, Seitengebäude, Einfriedungsmauer und Toranlage eines Bauernhofes, Am Anger 4</h5>
        <p>Bemerkenswertes, qualitatives Beispiel eines großen Bauernhofes, aufgrund seiner singulären und ortsbildprägenden
          Wirkung erhaltenswert, baugeschichtlich von Bedeutung. Bauernhaus: 2 Geschosse, Satteldach (Kronendeckung), Klinker
          <a title="By Jwaller [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:BrodenaundorfHofruinen.JPG">
            <img width="512" alt="BrodenaundorfHofruinen" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/BrodenaundorfHofruinen.JPG/512px-BrodenaundorfHofruinen.JPG">
          </a>
        </p>
        <h5><a href="https://www.wikidata.org/wiki/Q49471792">Häuslerhaus, Am Anger 5</a></h5>
        <p>eingeschossiges Gebäude mit gründerzeitlichem Klinkergiebel zum Dorfanger, sozialgeschichtlich von Bedeutung Landarbeiterhaus:
          1 Geschoss, hohes Satteldach (Biberschwanzdeckung), Klinker rot, gelbe Klinkergliederung, Segmentbogenfenster,
          Gebäude h</p>
        <h5>Walzenmühle Delitzsch</h5>
        <p>Fabrikantenvilla (Nr. 26) und Fabrikgebäude der Walzenmühle (Nr. 24b), einschließlich des Kopfbaues eines Nebengebäudes
          (Nr. 24d) zwischen der Bahnlinie und Walzenmühle; stattliches gründerzeitliches Fabrikensemble mit reich gegliederter
          Fabrik
        </p>
        <h5><a href="https://de.wikipedia.org/wiki/Delitzsch">Delitzsch</a></h5>
        <p>Altes Schloß, im 30jährigen Krieg zerstört.
          <a title="By Stadtverwaltung Delitzsch [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], from Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Barockpark_und_Barockschloss_Delitzsch.JPG">
            <img width="512" alt="Barockpark und Barockschloss Delitzsch" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Barockpark_und_Barockschloss_Delitzsch.JPG/512px-Barockpark_und_Barockschloss_Delitzsch.JPG">
          </a>
        </p>
        <h5><a href="https://de.wikipedia.org/wiki/St._Peter_und_Paul_(Delitzsch)">St. Peter und Paul</a></h5>
        <p>Die evangelische Stadtkirche Delitzsch ist eine gotische, dreischiffige, vierjochige Hallenkirche aus dem 15. Jahrhundert.
          Sie wurde ab 1404 unter Einbeziehung der unteren Geschosse des Westturms eines möglicherweise vom Ende des 12.
          oder dem Anfang des 13. Jahrhunderts stammenden Vorgängerbaus errichtet, von dem sich ein romanischer Bogenfries
          an der Westwand und im Innern des nördlichen Turmanbaus erhalten hat.</p>
      </div>
      <button class="accordion">
        <h3>Delitzsch nach Wolfen</h3>
      </button>
      <div class="panel">
        <h4>Wegbeschreibung</h4>
        <p>In nördlicher Richtung durch die Stadt über Benndorf (3,2 km) nach Holzweißig (6,1 km). Nordwärts die Bahn kreuzend
          und am Gasth. „Preuß. Krone“ geradeaus. Dieser Gasthof ist eine alte Ausspannung, wo die vom Norden kommenden Messebesucher
          ihre letzte größere Rast vor Leipzig hielten. Dann an den Kohlengruben vorbei zur Kreuzung Zörbig—Bitterfeld. Geradeaus
          auf landschaftlich weniger interessantem Wege nach Wolfen (8,1 km). Dagegen ist dieser Weg nicht ohne Reiz durch
          die zahlreichen Industrieanlagen, von denen er eingesäumt wird. Da treffen wir wieder auf Braunkohlengruben und
          vor allem auf die langgedehnten chemischen Werke der I. G. Farbenindustrie. Von der etwas hoch liegenden Straße
          bietet sich ein schöner Blick nach dem Muldensteiner Berg (rechts) mit den drei riesigen Schornsteinen des großen
          Eisenbahn-Kraftwerkes, während wir im Hintergrund die neun, je 110 m hohen Schornsteine von Golpa-Zschornewitz
          sehen, die eine lebhafte Unterbrechung der den ganzen Horizont bedeckenden dunklen Waldlinie der Dübener Heide
          bilden. Linker Hand sieht man bei günstigem Wetter den Petersberg bei Löbejün. Beim Kilometerstein 18,6 Gabelung.</p>
        <h4>Wegpunkte</h4>
        <h5><a href="https://de.wikipedia.org/wiki/Ausbesserungswerk_Delitzsch">Ausbesserungswerk Delitzsch</a></h5>
        <p>ehemaliges Ausbesserungswerk der Deutschen Reichsbahn im sächsischen Delitzsch, heute Werk der EuroMaint Rail</p>
        <h5>Freigut Benndorf</h5>
        <p>Bereits 1350 war ein Herrensitz vorhanden, der ab 1400 als Rittersitz bezeichnet wurde. Zu dieser Zeit diente das
          Anwesen als Ratsgut der Stadt Delitzsch. 1880 war die Familie Schnapperelle, 1899 die Familie Albert und 1906 die
          Familie Böttcher Besitzer des Freigutes Benndorf. Ab 1913 befand es sich in Besitz der Familie Seyferth und wurde
          1938 an Familie Schäfer verkauft, bevor diese 1945 enteignet wurde. Das Herrenhaus des Freigutes wurde saniert
          und dient heute als Wohnhaus und Ortsbegegnungszentrum.</p>
        <h5><a href="https://www.wikidata.org/wiki/Q49561399">Kirche Benndorf</a></h5>
        <p>bemerkenswerter romanischer Sakralbau, Saalkirche mit eingezogenem Chor und Apsis, kleiner Fachwerk-Kirchturm, baugeschichtlich,
          kunstgeschichtlich und ortsgeschichtlich von Bedeutung. romanische Saalkirche komplett aus Feldsteinen, mit Dachreiter
          <a title="By Jwaller [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:BenndorfDZ-Kirche3.JPG">
            <img width="512" alt="BenndorfDZ-Kirche3" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/BenndorfDZ-Kirche3.JPG/512px-BenndorfDZ-Kirche3.JPG">
          </a>
        </p>
        <h5><a href="https://de.wikipedia.org/wiki/Paupitzsch">Das eiserne Kreuz am Paupitzscher See</a></h5>
        <p>Nach der Stilllegung des Tagebaus Goitzsche im Jahr 1990 begann im gleichen Jahr die Festlegung des Naturschutzgebiets
          Paupitzscher See. Durch die Flutung des Tagebaurestlochs Paupitzsch von 1993 bis 2005 entstand der Paupitzscher
          See. An den ehemaligen Ort erinnern heute ein eisernes Kreuz und ein Findling am Standort der ehemaligen Kirche.
        </p>
        <h5>Arboretum</h5>
        <p>Das Arboretum (Sammlung von Gehölzen) bietet einen schönen Rastplatz mit Spielplatz.</p>
        <h5>Die Wächter der Goitzsche</h5>
        <p>Kunstwerk/Installation von Anatol Herzfeld
          <a title="By Jwaller [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], from Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Goitzschew%C3%A4chter.JPG">
            <img width="512" alt="Goitzschewächter" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Goitzschew%C3%A4chter.JPG/512px-Goitzschew%C3%A4chter.JPG">
          </a>
        </p>
        <h5>Gasthaus "Preußische Krone"</h5>
        <p>Die <a href="https://www.ansichtskarten-bitterfeld.de/wisl_s-cms/_redaktionell/1/Ansichtskarten/70/Mehrbildkarte.html">'Preußische Krone'</a>, ein Gasthof an der Kreuzung der Landstraße Berlin-Halle-Magdeburg-Leipzig war im Jahre 1905
          die Raststation der Reisenden die regelmäßig bei ihren Messebesuchen hier zusammentrafen, als Bitterfeld noch keinen
          Eisenbahnanschluß hatte. Hier soll der Spruch entstanden sein, der weit über die Stadtgrenzen hinaus berühmt wurde
          und bei jeder Gelegenheit mit Bitterfeld in Verbindung gebracht wird: 'Sehn' wir uns nicht in dieser Welt, so sehn'
          wir uns in Bitterfeld!'</p>
        <h5>Dükertürme</h5>
        <p>Ein <a href="https://de.wikipedia.org/wiki/D%C3%BCker">Düker</a> (niederdeutsch, entspricht niederländisch duiker, „Taucher“) ist eine Druckleitung zur Unterquerung einer
          Straße, eines Tunnels, eines Flusses oder von Bahngleisen etc.
          <a title="By Tnemtsoni [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:D%C3%BCkert%C3%BCrme.jpg">
            <img width="256" alt="Dükertürme" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/D%C3%BCkert%C3%BCrme.jpg/256px-D%C3%BCkert%C3%BCrme.jpg">
          </a>
        </p>
        <h5>Silbersee</h5>
        <p><a href="https://de.wikipedia.org/wiki/Silbersee_%28Bitterfeld%29">Silbersee</a> ist die im Volksmund entstandene Bezeichnung für das Restloch des Tagebaues Grube Johannes südlich von
          Wolfen auf Greppiner Flur, in das später Abwässer, Schlämme und Abfälle aus der Filmfabrik Wolfen eingeleitet bzw.
          eingebracht wurden.</p>
        <h5><a href="https://de.wikipedia.org/wiki/I.G._Farben">I.G. Farbenindustrie A.G.</a></h5>
        <p>Gegründet 1925, Zusammenschluss von acht großen Chemiekonzernen zwecks Weltmarkt-Konkurrenzfähigkeit. Damals das
          größte Chemieunternehmen der Welt! Die Interessengemeinschaft hat zahlreiche Patente hervorgebracht, war gleichzeitig
          aber auch aktiver Unterstützer und Akteur der Verbrechen des 3.Reichs.
          <a title="By Chemiepark Bitterfeld-Wolfen GmbH (Chemiepark Bitterfeld-Wolfen GmbH) [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:W21_Fifa_1929_Chemiepark.jpg">
            <img width="512" alt="W21 Fifa 1929 Chemiepark" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/W21_Fifa_1929_Chemiepark.jpg/512px-W21_Fifa_1929_Chemiepark.jpg">
          </a>
        </p>
      </div>
      <button class="accordion">
        <h3>Wolfen nach Dessau</h3>
      </button>
      <div class="panel">
        <h4>Wegbeschreibung</h4>
        <p>Geradeaus und über Boppau (2,2 km) zum Heidekrug (5,7 km). Die sehr gute Straße führt nun durch die Mosigkauer Heide,
          einen schönen Wald, bis zum Forsthaus Heideburg (6,9 km). Dann weiter und durch die Heidestr.., Franzstr., Kavalierstr.
          in Dessau (5,1 km). An der Mulde. Rathaus 1901 erbaut im Stile der deutschen Renaissance mit 75 m hohem Turm. Schloß
          mit Park und Tiergarten. Prächtige Umgebung. Lohnender Abstecher nördlich zur Elbe, vorbei am Gasth. „Elbhaus“
          und Gasth. „Elbzollhaus“. Hier schöner Blick auf die Elbe.</p>
        <h4>Wegpunkte</h4>
        <h5>Wasserturm Bobbau</h5>
        <p>erbaut von 1926 bis Juli 1927, Kapazität 320 Kubikmeter
          <a title="von M_H.DE [GFDL (http://www.gnu.org/copyleft/fdl.html) oder CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], vom Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Bobbau,Wasserturm,Stadt_Bitterfeld-Wolfen.jpg">
            <img width="512" alt="Bobbau,Wasserturm,Stadt Bitterfeld-Wolfen" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Bobbau%2CWasserturm%2CStadt_Bitterfeld-Wolfen.jpg/512px-Bobbau%2CWasserturm%2CStadt_Bitterfeld-Wolfen.jpg">
          </a>
        </p>
        <h5><a href="https://de.wikipedia.org/wiki/Rennstrecke_Dessau">Rennstrecke Dessau</a></h5>
        <p>
          <a title="By M_H.DE [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY 3.0 (https://creativecommons.org/licenses/by/3.0)], from Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Rennstrecke_Dessau,_Kurve_der_Jugend,Jugendkurve.jpg">
            <img width="512" alt="Rennstrecke Dessau, Kurve der Jugend,Jugendkurve" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Rennstrecke_Dessau%2C_Kurve_der_Jugend%2CJugendkurve.jpg/512px-Rennstrecke_Dessau%2C_Kurve_der_Jugend%2CJugendkurve.jpg">
          </a>
        </p>
        <h5><a href="https://de.wikipedia.org/wiki/Jagdschloss_Haideburg">Jagdschloss Haideburg</a></h5>
        <p>1782 bis 1783 errichtet. Fürst Leopold III. Friedrich Franz von Anhalt-Dessau beauftragte den Baumeister Friedrich
          Wilhelm von Erdmannsdorff mit dem Bau als Jagdschloss und Oberförsterei. Es soll dem preußischen Krönungsschloss
          in Königsberg in kleinerer Form nachgestellt worden sein.</p>
        <h5>Bauhaus</h5>
        <p>Das <a href="https://de.wikipedia.org/wiki/Jagdschloss_Haideburg">Bauhausgebäude</a> entstand 1925 bis 1926 nach Plänen von Walter Gropius als Schulgebäude für die Kunst-, Design-
          und Architekturschule Bauhaus.
          <a title="By Lelikron [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], from Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Dessau_Bauhaus_neu.JPG">
            <img width="512" alt="Dessau Bauhaus neu" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Dessau_Bauhaus_neu.JPG/512px-Dessau_Bauhaus_neu.JPG">
          </a>
        </p>
        <h5>Kornhaus</h5>
        <p>Carl Fieger entwarf das <a href="https://de.wikipedia.org/wiki/Kornhaus_%28Dessau%29">Kornhaus</a> in den Jahren 1929/30 im Auftrag der Stadt Dessau und der Schultheiss-Patzenhofer
          Brauerei AG.
          <a title="By M_H.DE [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], from Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Kornhaus_Dessau_an_der_Elbe.jpg">
            <img width="512" alt="Kornhaus Dessau an der Elbe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Kornhaus_Dessau_an_der_Elbe.jpg/512px-Kornhaus_Dessau_an_der_Elbe.jpg">
          </a>
        </p>
        <h5>Elbzollhaus</h5>
        <p>Das <a href="http://www.ansichtskarten-center.de/webshop/shop/ProdukteBilder/52713/AK_51329288_gr_1.jpg">Elbzollhaus</a> ist ein historischer Gebäudekomplex an der Elbbrücke zwischen Dessau und Roßlau. Fürst Franz (1740–1817)
          ließ das Zollhaus 1789 nach einem Entwurf des deutschen Architekten Friedrich Wilhelm von Erdmannsdorff (1736–1800)
          bauen.
        </p>
      </div>
      <button class="accordion">
        <h3>Dessau nach Wörlitz</h3>
      </button>
      <div class="panel">
        <h4>Wegbeschreibung</h4>
        <p>Ausfahrt über die Muldenbrücke und links die Bahn Dessau—Oranienbaum kreuzend, dann auf schönen Radfahrwegen über
          Jonitz (2,1 km), Naundorf (2 km) und Vockerode (4 km) nach Wörlitz (5 km).</p>
        <h4>Wegpunkte</h4>
        <h5>Luisium</h5>
        <p>Schloss und Garten <a href="https://de.wikipedia.org/wiki/Luisium">Luisium</a> entstanden zwischen 1774 und 1778 als Geschenk für die Fürstin Luise von Brandenburg-Schwedt,
          der Gemahlin des Fürsten Leopold III. Friedrich Franz von Anhalt-Dessau, und sollte der Fürstin als Witwensitz
          dienen.
          <a title="von M_H.DE [GFDL (http://www.gnu.org/copyleft/fdl.html) oder CC BY 3.0 (https://creativecommons.org/licenses/by/3.0)], vom Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Dessau,Orangerie_im_Luisium.jpg">
            <img width="512" alt="Dessau,Orangerie im Luisium" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Dessau%2COrangerie_im_Luisium.jpg/512px-Dessau%2COrangerie_im_Luisium.jpg">
          </a>
        </p>
        <h5>Gustavusburg - Schwedenhaus</h5>
        <p>Als <a href="https://de.wikipedia.org/wiki/Gustavusburg">Gustavusburg</a> oder Gustav Adolf wird ein zum Dessau-Wörlitzer Gartenreich gehörendes Gebäude bezeichnet. Die gebräuchliche
          Bezeichnung Schwedenhaus ist auf ein vergoldeten Relief an der Hauptfassade zurückzuführen, welches den Schwedenkönig
          Gustav Adolph darstellt.
          <a title="von Belebast [CC BY-SA 3.0 de (https://creativecommons.org/licenses/by-sa/3.0/de/deed.en)], vom Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:Goldig-5a.JPG">
            <img width="512" alt="Goldig-5a" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Goldig-5a.JPG/512px-Goldig-5a.JPG">
          </a>
        </p>
        <h5><a href="https://de.wikipedia.org/wiki/W%C3%B6rlitz">Wörlitz</a></h5>
        <p>Kirche mit weithin sichtbarem Turm, 1809 im gotischen Stile erneuert. <a href="https://de.wikipedia.org/wiki/Schloss_W%C3%B6rlitz">Schloß</a> und berühmter sehenswerter Park. Dieser,
          im letzten Drittel des 18. Jahrhunderts angelegt, schließt den Wörlitzer See — Gondelgelegenheit — ein und bietet
          eine Anzahl Sehenswürdigkeiten, z. B. das Gotische Haus mit Sammlungen, den Floratempel, die Kettenbrücke, die
          Luisenklippe, den Venustempel, das Monument, das Pantheon, den „Stein“, den Tempel der Nacht und die Grotte der
          Egeria.
        </p>
        <h5>Gondelfahrt auf dem <a href="https://de.wikipedia.org/wiki/Schloss_W%C3%B6rlitz">Wörlitzer See</a></h5>
        <p>Gondelfahrten sind auch heute noch möglich und können von April bis November gebucht werden!
          <a title="I, Nikater [GFDL (http://www.gnu.org/copyleft/fdl.html) oder CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons"
            href="https://commons.wikimedia.org/wiki/File:W%C3%B6rlitzer_See_mit_St._Petri.jpg">
            <img width="512" alt="Wörlitzer See mit St. Petri" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/W%C3%B6rlitzer_See_mit_St._Petri.jpg/512px-W%C3%B6rlitzer_See_mit_St._Petri.jpg">
          </a>
        </p>
      </div>
      <div class="source">
        <p>
          aus SLUB Dresden: O. Lehmann, "Großes Tourenbuch für Radfahrer", 1930,
          <a href="http://digital.slub-dresden.de/werkansicht/dlf/103042/102/">http://digital.slub-dresden.de/werkansicht/dlf/103042/102/</a> (CC-BY-SA 4.0).
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Detail',
  mounted () {
    const acc = document.getElementsByClassName('accordion')

    for (let i = 0; i < acc.length; i++) {
      acc[i].addEventListener('click', function () {
        /* Deactivate other panels */
        for (let j = 0; j < acc.length; j++) {
          if (i !== j) {
            acc[j].classList.toggle('active')
            let panel = acc[j].nextElementSibling
            panel.style.display = 'none'
          }
        }

        /* Toggle between adding and removing the "active" class,
            to highlight the button that controls the panel */
        this.classList.toggle('active')

        /* Toggle between hiding and showing the active panel */
        var activePanel = this.nextElementSibling
        if (activePanel.style.display === 'block') {
          activePanel.style.display = 'none'
        } else {
          activePanel.style.display = 'block'
        }

        this.scrollIntoView()
      })
    }
  }
}
</script>

<style scoped>
  .detail {
    text-align: left;
    color: #2c3e50;
    margin: 60px auto;
    width: 80%
  }

  .teaser {
    column-count: 3;
    column-width: 33%;
  }

  .accordion {
    background-color: #eee;
    color: #444;
    cursor: pointer;
    padding: 10px;
    width: 100%;
    text-align: left;
    border-style: none none dotted none;
    border-color: #444;
    outline: none;
    transition: 0.4s;
  }

  .active,
  .accordion:hover {
    background-color: #ccc;
  }

  .panel {
    padding: 18px 18px;
    background-color: white;
    display: none;
    overflow: hidden;

  }

  .source {
    padding: 30px 0 0 0;
  }

  img {
    width: 100%;
  }

</style>
