<template>

  <div class="container about">
    <div class="row">
      <div class="col-md-12">
        <p>Das Projekt Nachgeradelt.de entstand im Frühjahr 2018 im Rahmen des
          <a href="https://codingdavinci.de/events/ost/">Coding da Vinci Ost</a>. Wir sind RadfahrerInnen, HackerInnen, DesignerInnen und geschichtsinteressierte Menschen,
          die gemeinsam von den Fragen angetrieben werden: Wie ging es RadfahrerInnen um die vorletzte Jahrtausendwende?
          Unter welchen Bedingungen und auf welchen Straßen radelten sie? Wie unterschied sich das Radfahren von den heutigen
          Verhältnissen?
        </p>
        <p>Das Projektteam sammelte alle digitalisierten Touren im Umfeld von Leipzig aus dem Datensatz der
          <a href="https://codingdavinci.de/daten/#slub-dresden">Sächsischen Landesbibliothek - Staats- und Universitätsbibliothek Dresden (SLUB).</a> Anschließend wurde eine Strecke
          ausgewählt, testweise befahren und Stationen entlang des Weges digital mit Zusatzinformationen angereichert. Die
          <a href="https://github.com/nachgeradelt/nachgeradelt/blob/master/tourenverzeichnis.csv">komplette Liste aller Touren</a> sowie der Quellcode können auf
          <a href="https://github.com/nachgeradelt/nachgeradelt">Github</a> eingesehen werden.
        </p>
        <div class="teaser">
        <figure>
          <img src="../assets/about.jpeg" alt="Über uns">
          <figcaption>
            Jens N, Johannes, Birte
          </figcaption>
        </figure>
        <figure>
          <img src="../assets/about2.jpeg" alt="Über uns 2">
          <figcaption>
            Jens B, Johannes, Jens N, Gerd & Tobias <br/> (nicht im Bild: Katharina, Justus & Alejandro)
          </figcaption>
        </figure>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'About'
}
</script>
<!-- styling for the component -->
<style scoped>
  .about {
    text-align: center;
    font-size: 18px;
    margin-top: 10px;
  }

  .teaser {
    column-count: 2;
    column-width: 50%;
  }

  .about p {
   margin-bottom: 10px;
  }
  .about img {
    max-width: 100%;
    height: 400px;
  }
</style>
