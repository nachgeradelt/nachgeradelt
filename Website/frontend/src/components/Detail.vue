<template>
<div class="detail">
  <h2>Deine historische Radtour: {{$route.params.id === '46' ?  'Leipzig - Dessau - Wörlitz' : 'Leipzig - Altenburg - Werdau'}}</h2>
  <div v-show="$route.params.id === '100'">
    <p>
      Über Lobstädt — Altenburg — Crimmitschau
    </p>
    <p>
      79,6 km guter, erst ebener, dann welliger und hügeliger Strasse.
    </p>
    <button class="accordion"><h3>Leipzig nach Zwenkau</h3></button>
    <div class="panel">
      <h4>Wegbeschreibung</h4>
      <p>
        0,0. 0,0 Leipzig. 111. P. T. B. S. No. l. Ausfahrt Königsplatz, Peterssteinw., Zeitzerstr., Südpl., Südstr., Leipzigerstr. i. Connewitz, dann r. üb. d. Brücke, hier d. Coburger Str. üb. 7,0 Gautzsch; 1.8 Zöbigker; 1,1 Prödel; n. 4,6
      </p>
      <h4>Wegpunkte</h4>
        <h5>Leipzig</h5>
          <h6>Karl-Liebknecht-Straße (ehem. Zeitzer Straße und Südstraße)</h6>
            <p>
              Zeitzer Straße und Südstraße wurden 1933 zusammengelegt und in Adolf-Hitler-Straße umbenannt. Nach Ende des Zweiten Weltkriegs erhielt sie unter US-amerikanischer Besatzung zunächst ihren alten Namen zurück, bevor sie im selben Jahr unter sowjetischer Besatzung in Karl-Liebknecht-Straße umbenannt wurde.
            </p>
          <h6>Restaurant Forsthaus Raschwitz</h6>
            <p>
              Das Restaurant „Forsthaus Raschwitz“ lädt schon 1900 alle Radfahrenden zu einer Pause ein:
            </p>
            <p>
              „Hier geben sich die Radlerinnen und Radler ihr Rendezvous, und wenn man an Sonn- und Festtagen die Straße beobachtet, sollte man fast glauben, es seien die Stahlrosse zur alleinherrschenden Macht auf dem Gebiete des Verkehrswesens geworden."
            </p>
            <p>
              aus SLUB Dresden: "Adreßbuch für die südlichen Vororte Leipzigs", 1904, <a href="http://digital.slub-dresden.de/id403758513-19040000">http://digital.slub-dresden.de/id403758513-19040000</a>, IV. Abt., S. 4.
            </p>
            <p>
              Restaurant Forsthaus Raschwitz
              <br>
              Koburger Straße 33
              <br>
              04416 Markkleeberg
            </p>
        <h5>Zwenkau</h5>
          <p>
            14,5. 14,5 Zwenkau. 133. P. T. B. Hier r. n. Markranstädt 12,6; Zw. früher bed. Ort, jetzt Landstädtchen, wurde i. J. 974 v. Kaiser Otto II. dem Stifte Merseburg geschenkt. Auf einem Hügel an der Elsterniederung Reste einer im Mittelalter berühmten Burg; 1315 wurde bei ein. Belagerung ders. Friedr. d. Lahme, Markgr. Friedr. d. Gebissenen Sohn, m. ein. Pfeile erschossen.
          </p>
          <h6>Gaststätte Schützenhaus</h6>
            <p>
              Wer einkehren möchte, wo sich schon 1904 der Radfahrer-Verein Zwenkau traf, kann das in der Gaststätte „Schützenhaus“ tun.
            </p>

            <div>
              <img src="http://digital.slub-dresden.de/fileadmin/data/403758513-19040000/403758513-19040000_tif/jpegs/00000431.tif.large.jpg" alt="Anzeige Restaurant 'Zum Schützenhaus' Zwenkau">
              <p>SLUB Dresden: "Adreßbuch für die südlichen Vororte Leipzigs", 1904, <a href="http://digital.slub-dresden.de/id403758513-19040000">http://digital.slub-dresden.de/id403758513-19040000</a>, IV. Abt., S. 4.</p>
            </div>
            <p>
              Gaststätte Schützenhaus
              <br>
              Geschwister-Scholl-Platz 1
              <br>
              04442 Zwenkau
            </p>
    </div>
    <button class="accordion"><h3>Zwenkau nach Altenburg</h3></button>
    <div class="panel">
      <h4>Wegbeschreibung</h4>
      <p>
        Weiter üb. Kotzschbar u. Imnitz (m. alt. Kapelle) zur 1,2 Strassengabelung; h. 1. üb. 2,9 Pulgar; 2.0 Medewitzsch: 4,1 Bahnh. Kieritzsch P. T. B.; 3,4 n.
      </p>
      <h4>Wegpunkte</h4>
        <h5>Neukieritzsch (ehem. Medewitzsch, Pulgar)</h5>
          <p>
            Das Dorf Medewitzsch wurde 1934 nach Lippendorf eingemeindet, dabei verdrängte der Ortsname Lippendorf den Ortsnamen Medewitzsch. Heute gehört Lippendorf zur Gemeinde Neukieritzsch.
          </p>
          <p>
            Die Gemeinde Pulgar wurde ab 1971 schrittweise abgebrochen und mit den Chemischen Werken Böhlen überbaut. Heute gehören die Flächen zur Gemeinde Neukieritzsch.
          </p>
          <div>
            <img src="http://fotothek.slub-dresden.de/fotos/df/dk/0010000/df_dk_0010001_4840_1894.jpg" alt="Äquidistantenkarte 42: Section Lobstädt, 1894">
            <p>
              SLUB/Deutsche Fotothek: "Äquidistantenkarte 42: Section Lobstädt", 1894, <a href="http://www.deutschefotothek.de/documents/obj/71055352">http://www.deutschefotothek.de/documents/obj/71055352</a> (CC-BY-SA 4.0).
            </p>
          </div>
      <h5>Lobstädt</h5>
      <p>
        13,6. 28,1 **Lobstädt**. 140. P. T. B. Hier Strassengabelung (1. l. n. 4,6 Borna), r. weiter sanft steigend üb. 4,5 r. Blumroda (h. 1. n. 5,0 Borna); 4,0 Serbitz; 0,8 Treben, P. T, B.; 3,1 Zschaschelwitz; üb. d. Str. Lucka-Geithain (l. n. 19,1 Geithain,
        r. n. 15,9 Lucka); mit stark. Fall 4,5 n.
      </p>
      <h5>Altenburg</h5>
      <p>
        16,9. 45,0 **Altenburg**. 178. P. T. B. Hier r. n. 10,9 Schmölln; 24,8 Ronneburg; 11,7 Meuselwitz; l. n. 22,1 Penig und 18.0 Waldenburg. Residenz d. Herzöge v. Sachs-Altenburg aus d. Hause Wettin ernestinischer L. Alte, ber. 980 urk. erw. St., i. 12.
        Jahrh. Reichsst., anf. d. 14. Jahrh. an d. Haus Wettin. Auf mächt., steil. Porphyrfelsen d. herzogl. Schloss a. d. 11. Jahrh. Nach verschied. Bränden 1706—44 neu geb. (die 1865 und 1868 abgebr. Flügel sind ern.), m. prächt. Saale, Rüstkammer,
        Kunstkammer, schönem Park. 8. Juli 1455 Prinzenraub (Kurf. Friedr. d. Sanftmüt. v. Sachs. Söhne Ernst u. Albert. Kunz v. Kaufungen). Am Fusse d. Schlossberges Siegesdenkm. u. Denkmal Kais. Wilh. I. Am Markte d. 1562-64 im deutsch. Renaissancestil
        erb. Rath. Von Kirchen sind zu erw. die 1087 geb. u. 1878 ern. Bartholomäik., die 1411 erb. spätgot. Schlosskirche. Sehensw. noch die Roten Spitzen, ehem. Augustinerkl., 1172 v. Kaiser Friedr. I. gegr., 1533 aufgeh., 1872 ern., enth. das Staatsarchiv.
        —A. hat schöne Promenaden an 3 grossen Teichen.
      </p>
    </div>
    <button class="accordion"><h3>Altenburg nach Crimmitschau</h3></button>
    <div class="panel">
      <h4>Wegbeschreibung</h4>
      <p>
        Von A. hügelig w. üb. 1. 3,4 Mockern; 1,0 Gardschütz; r. 1,0 Lehndorf, P. T. B.; 2,0 Zehma; 1,5 Löhmigen; 3,0 Gössnitz (hier r. üb. Nörditz, Nietzschka n. 6,6 Schmölln, —hinter Gössn. r. üb. Schönhain, Frankenhausen gute Str. n. 8,0 Crimmitschau); 4.0
        Guteborn (hinter Guteb. 1. n. 1,9 Meerane); 4,3 Gasth. Silberner Pelikan (hier l. n. 6,5 Glauchau, geradeaus üb. Mosel n. 12,5 Zwickau); weiter r. n. 4,3 (Fall!)
      </p>
      <h4>Wegpunkte</h4>
        <h5>Crimmitschau</h5>
          <p>
            24,5. 69,5 Crimmitschau. 230. P. T. B. Cr. wird 1210 als Stadt erwähnt; 1430 v. d. hussit. Tschechen verbrannt, im dreissigjähr. Kriege fünfmal geplündert; besass 1794 noch seine Ringmauern mit 3 Thoren und 2 Türmen. 1748 Einführung der Streichgarnspinnerei durch David Oehler.
          </p>
          <h6>Textilstadt Crimmitschau</h6>
            <p>
              Anknüpfend an die Initiative von David Friedrich Oehler hat sich Crimmitschau zu einem Zentrum der Textilindustrie entwickelt. Wer 1899 nach Crimmitschau radelt, sieht schon von weitem die vielen Fabrikgebäude, die Crimmitschau den Spitznamen „Stadt der 100 Schornsteine“ eingebracht haben:
            </p>
            <p>
              „Der Reisende staunt bei dem Herannahen [...] über den wahren Wald von Dampfessen, welcher sich oft dicht zusammengedrängt auf allen Stellen erhebt[...], so dass der ganze Platz den Anblick gewährt, als sei er eine einzige große Fabrik.“
            </p>
            <p>
              aus SLUB Dresden: "Album der Sächsischen Industrie", 1856, <a href="http://digital.slub-dresden.de/id252070399">http://digital.slub-dresden.de/id252070399</a>, Bd. 1, S. 119, (CC-BY-SA 4.0).
            </p>
            <div>
              <img src="http://fotothek.slub-dresden.de/fotos/df/dk/0005000/df_dk_0005155.jpg" alt="Ansicht von Crimmitschau, Lithografie, 1860">
              <p>
                SLUB/Deutsche Fotothek: G. Frank, "Ansicht von Crimmitschau", Lithografie, 1860, <a href="http://www.deutschefotothek.de/documents/obj/70401522">http://www.deutschefotothek.de/documents/obj/70401522</a> (CC-BY-SA 4.0).
              </p>
            </div>
          <h6>Industriearchitektur</h6>
            <p>
              Manche der Tuchfabriken, Spinnereien und Färbereien, welche das Stadtbild lange Zeit geprägt haben, existieren auch heute noch und sind in der Datenbank des Projekts <a href="https://www.industrie-kultur-ost.de/datenbank/textilindustrie/gebiet-zwickau/">Industrie.Kultur.Ost</a> erfasst.
            </p>
            <div>
              <img src="http://digital.slub-dresden.de/fileadmin/data/252070399/252070399_tif/jpegs/00000383.tif.large.jpg" alt="Vigogne-Spinnerei von H. F. Kürzel in Crimmitschau">
              <p>
                SLUB Dresden: "Album der Sächsischen Industrie", 1856, <a href="http://digital.slub-dresden.de/id252070399">http://digital.slub-dresden.de/id252070399</a>, Bd. 1, (CC-BY-SA 4.0).
              </p>
            </div>
          <h6>Sächsisches Industriemuseum</h6>
            <p>
              In der historischen Tuchfabrik Gebr. Pfau ist inzwischen das Sächsische Industriemuseum untergebracht und macht die damaligen Produktionsbedingungen erlebbar.
            </p>
            <p>
              Sächsisches Industriemuseum
              <br>
              Tuchfabrik Gebr. Pfau
              <br>
              Leipziger Straße 125
              <br>
              08451 Crimmitschau
            </p>
    </div>
  <button class="accordion"><h3>Crimmitschau nach Werdau</h3></button>
   <div class="panel">
      <h4>Wegbeschreibung</h4>
        <h5>Werdau</h5>
          <p>
            10,1. 79,6 Werdau. 281. P. T. B. Hier l. n. 10,0 Zwickau. —1298 als Stadt angeführt; 1430 Zerstörung durch d. Hussiten, 1633 Pest. W. hatte früher starke Stadtmauer mit zwei Thoren. — Bedeutende Textilindustrie.
          </p>
          <h6>Fahrradfieber um 1900</h6>
            <p>
              Auch Werdau hat 1899 eine aktive Radler-Szene: Laut den historischen Adressbüchern gibt es in der Stadt im Jahr 1903 fünf verschiedene Radfahrer-Klubs, von denen drei seit 1897 neu gegründet wurden.
            </p>
            <p>
              aus SLUB Dresden: "Adreßbuch der Fabrikstadt Werdau mit den Vororten Leubnitz, Steinpleis und Langenhessen", 1903, <a href="http://digital.slub-dresden.de/id380404613-19030000">http://digital.slub-dresden.de/id380404613-19030000</a> (CC-BY-SA 4.0).
            </p>
          <h6>Arbeiter-Radfahrer</h6>
            <p>
              Wer fährt überhaupt Rad um 1900? Wegen der hohen Anschaffungskosten war Radfahren zunächst vor allem ein Sport des Bürgertums. Um 1900 ändert sich das: Als die Preise für Fahrräder sinken, können sich auch besser verdienende Fabrikarbeiter*innen ein gebrauchtes Rad leisten.
            </p>
            <p>
              In den 1890er Jahren gründen sich spezielle Arbeiter-Radfahrer-Klubs wie der „Arbeiter-Radfahrerbund Solidarität“, der sich ausdrücklich als Teil der Arbeiterbewegung versteht. Auch die Industriestadt Werdau verzeichnet für 1903 einen Ableger der „Solidarität“.
            </p>
            <p>
              Ihre Kritik an den bürgerlichen Vereinen bringt die „Solidarität“ so auf den Punkt: „[…] in diesen bürgerlichen radsportlichen Organisationen hat[] man es sich zur Aufgabe gemacht, in der Hauptsache dem Radrennsport zu huldigen und sich an allem möglichen patriotischen Klimbim zu beteiligen.“
            </p>
            <p>
              aus FES Bibliothek: A. Frahnert, "Werden und Wachsen des Arbeiter-Radfahrer-Bundes Solidarität: die Bundesgeschichte bis zum Jahre 1926", 1927, <a href="https://library.fes.de/opac/id/181481">https://library.fes.de/opac/id/181481</a>, S. 9.
            </p>
    </div>
    <div class="source">
      <p>
        aus SLUB Dresden: B. Böhm, "Touren-Buch des Sächsischen Radfahrer-Bundes", 1899, <a href="http://digital.slub-dresden.de/id407531238">http://digital.slub-dresden.de/id407531238</a> (CC-BY-SA 4.0).
      </p>
    </div>
  </div>
  <div v-show="$route.params.id === '46'">
    <p>Über Eutritzsch — Wiederitzsch — Delitzsch — Wolfen</p>
    <button class="accordion"><h3>Leipzig nach Eutritzsch</h3></button>
    <div class="panel">
      <h4>Wegbeschreibung</h4>
      <p>Vom Marktplatz, Katharinenstraße, Brühl, Am Hallischen Tor, Blücherplatz, Blücherstraße, Eutritzscher Straße, rechts Delitzscher Straße, Vorstadt Eutritzsch (3,5 km). Alte historische Gosenschänke. Außerhalb des Ortes Straßengabelung.</p>
      <h4>Wegpunkte</h4>
    </div>
    <button class="accordion"><h3>Eutritzsch nach Wiederitzsch</h3></button>
    <div class="panel">
      <h4>Wegbeschreibung</h4>
      <p>Geradeaus, dann am Krankenhaus St. Georg vorbei nach Wiederitzsch (3,3 km).
      </p>
      <h4>Wegpunkte</h4>
    </div>
    <button class="accordion"><h3>Wiederitzsch nach Delitzsch</h3></button>
    <div class="panel">
      <h4>Wegbeschreibung</h4>
      <p>Ueber die sächsisch-preußische Grenze, durch Schladitz (4,6 km), mäßig abwärts über die alte Salzstraße nach Lemsel (3,6 km), Brodenaundorf (1,0 km) und Delitzsch (6,0 km).</p>
      <h4>Wegpunkte</h4>
    </div>
    <button class="accordion"><h3>Delitzsch nach Wolfen</h3></button>
    <div class="panel">
      <h4>Wegbeschreibung</h4>
      <p>In nördlicher Richtung durch die Stadt über Benndorf (3,2 km) nach Holzweißig (6,1 km). Nordwärts die Bahn kreuzend und am Gasth. „Preuß. Krone“ geradeaus. Dieser Gasthof ist eine alte Ausspannung, wo die vom Norden kommenden Messebesucher ihre letzte größere Rast vor Leipzig hielten. Dann an den Kohlengruben vorbei zur Kreuzung Zörbig—Bitterfeld. Geradeaus auf landschaftlich weniger interessantem Wege nach Wolfen (8,1 km). Dagegen ist dieser Weg nicht ohne Reiz durch die zahlreichen Industrieanlagen, von denen er eingesäumt wird. Da treffen wir wieder auf Braunkohlengruben und vor allem auf die langgedehnten chemischen Werke der I. G. Farbenindustrie. Von der etwas hoch liegenden Straße bietet sich ein schöner Blick nach dem Muldensteiner Berg (rechts) mit den drei riesigen Schornsteinen des großen Eisenbahn-Kraftwerkes, während wir im Hintergrund die neun, je 110 m hohen Schornsteine von Golpa-Zschornewitz sehen, die eine lebhafte Unterbrechung der den ganzen Horizont bedeckenden dunklen Waldlinie der Dübener Heide bilden. Linker Hand sieht man bei günstigem Wetter den Petersberg bei Löbejün. Beim Kilometerstein 18,6 Gabelung.</p>
      <h4>Wegpunkte</h4>
    </div>
    <button class="accordion"><h3>Wolfen nach Dessau</h3></button>
    <div class="panel">
      <h4>Wegbeschreibung</h4>
      <p>Geradeaus und über Boppau (2,2 km) zum Heidekrug (5,7 km). Die sehr gute Straße führt nun durch die Mosigkauer Heide, einen schönen Wald, bis zum Forsthaus Heideburg (6,9 km). Dann weiter und durch die Heidestr.., Franzstr., Kavalierstr. in Dessau (5,1 km). An der Mulde. Rathaus 1901 erbaut im Stile der deutschen Renaissance mit 75 m hohem Turm. Schloß mit Park und Tiergarten. Prächtige Umgebung. Lohnender Abstecher nördlich zur Elbe, vorbei am Gasth. „Elbhaus“ und Gasth. „Elbzollhaus“. Hier schöner Blick auf die Elbe.</p>
      <h4>Wegpunkte</h4>
    </div>
    <button class="accordion"><h3>Dessau nach Wörlitz</h3></button>
    <div class="panel">
      <h4>Wegbeschreibung</h4>
      <p>Ausfahrt über die Muldenbrücke und links die Bahn Dessau—Oranienbaum kreuzend, dann auf schönen Radfahrwegen über Jonitz (2,1 km), Naundorf (2 km) und Vockerode (4 km) nach Wörlitz (5 km).</p>
      <h4>Wegpunkte</h4>
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

<style>
.detail {
  text-align: left;
  color: #2c3e50;
  margin: 60px auto;
  width: 60%
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
  max-height: 5%
}
</style>
