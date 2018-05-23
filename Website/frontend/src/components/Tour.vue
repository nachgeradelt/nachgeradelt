<template>
  <div class="container tour">
    <div class="row">
      <div class="col-md-3">
        <h2>Abfahrt</h2>
        <select>
          <option value="">Start</option>
          <option value="">Leipzig</option>
        </select>

        <h2>Distanz</h2>
        <div class="slider">
           <vue-slider v-bind="distanceSlider" v-model="distanceSlider.value"></vue-slider>
         </div>

        <h2>Ziel</h2>
        <select>
          <option value="">Ziel</option>
          <option value="">Dessau</option>
          <option value="">Werdau</option>
        </select>

        <h2>{{ tours }}</h2>
        <ul>
          <li>
            <a href="#detail">Tour 1</a>
          </li>
          <li>
            <a href="#detail">Tour 2</a>
          </li>
          <li>
            <a href="#detail">Tour 3</a>
          </li>
        </ul>
      </div>
      <div class="col-md-9">
        <l-map :zoom="zoom" :center="center">
          <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
          <l-marker :lat-lng="marker"></l-marker>
        </l-map>
      </div>

    </div>
    <div class="row">
      <div class="col-md-12">
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <div id="detail">
          <h2>Deine historische Fahrradtour</h2>
          Start: Leipzig  Ziel: Werdau  Streckenlänge: 55 km  Über: Musterstadt
          <br>
          <h3>Streckenbeschreibung</h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut lacus ante. Fusce sed varius justo. Duis non metus molestie, pharetra mauris a, scelerisque lectus. Maecenas accumsan eu nisi nec ullamcorper. Aenean consequat nibh vitae sagittis cursus. Nunc feugiat purus nec dui pretium, eu sagittis eros rutrum. Integer ut luctus ipsum. Donec eu nibh tortor. Nullam eu lacus augue. Phasellus et tristique mauris.
          </p>
          <p>
            In sit amet turpis ultricies, suscipit augue eget, congue sapien. Sed vitae tempor lorem. Donec semper ultricies nulla, sed sodales ipsum finibus at. Curabitur egestas dignissim viverra. Mauris suscipit porta diam, a tincidunt velit condimentum auctor. Phasellus ultricies ligula quis maximus molestie. Aliquam dignissim, justo a lobortis ultrices, velit dolor mollis erat, sed viverra metus turpis eget arcu. Donec vitae imperdiet velit, molestie hendrerit diam. Cras blandit rhoncus dolor, sit amet dictum sapien lacinia sed. Donec urna tellus, imperdiet quis erat ut, vestibulum lacinia ex. Nulla cursus, urna rutrum aliquet pellentesque, justo libero dapibus leo, vel consectetur mauris justo in sem. Etiam tristique vel nulla at porttitor. Etiam convallis vitae mauris id rutrum. In quis nisl vel magna volutpat commodo.
          </p>
          <p>
            Maecenas vel purus sit amet risus elementum posuere eget quis enim. Morbi eu lacinia nunc. Praesent sollicitudin hendrerit venenatis. Phasellus commodo auctor purus, non convallis libero congue vitae. Quisque nibh justo, mollis sed sagittis ut, pulvinar mattis nulla. Praesent eget tempor metus, eget laoreet urna. Nunc elementum rutrum erat quis laoreet.
          </p>
          <p>
            Aliquam at rhoncus augue. Ut eleifend quam felis, in sodales metus auctor a. Vestibulum non velit sit amet felis luctus elementum quis pellentesque ipsum. Donec fermentum euismod diam ut semper. Pellentesque in dapibus ex. Vestibulum porttitor suscipit pellentesque. Nunc sagittis justo quis tristique ultricies.
          </p>
          <p>
            Maecenas pulvinar mi sed ligula ornare euismod. Phasellus posuere tellus ullamcorper libero dictum convallis a euismod ipsum. Nullam libero magna, interdum eget magna ut, posuere congue ligula. Praesent magna enim, viverra et aliquet a, malesuada sed risus. Aliquam nulla nunc, interdum ut arcu sit amet, sollicitudin tristique purus. Suspendisse vitae consectetur massa, at posuere diam. Praesent ipsum velit, posuere vel lorem nec, ultricies mattis tellus. Fusce erat est, fermentum nec elit sed, dignissim sagittis massa. Pellentesque eu placerat metus. Pellentesque semper neque non leo sagittis pharetra. Integer quis tellus leo. Donec lacinia non lacus maximus aliquet. Etiam lacinia augue diam, nec fringilla enim scelerisque sollicitudin.
          </p>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet'
import vueSlider from 'vue-slider-component'

export default {
  name: 'Tour',
  components: { LMap, LTileLayer, LMarker, vueSlider },
  data () {
    return {
      tours: 'Touren',
      distanceSlider: {
        value: [
          0,
          50
        ],
        formatter: '{value} km',
        max: 250
      },
      zoom: 7,
      // eslint-disable-next-line no-undef
      center: L.latLng(51.339673, 12.371364),
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      // TODO: Add dynamic marker
      // eslint-disable-next-line no-undef
      marker: L.latLng(51.339673, 12.371364)
    }
  }
}
// eslint-disable-next-line no-undef
$('a[href^="#"]').on('click', function (event) {
  // eslint-disable-next-line no-undef
  var target = $(this.getAttribute('href'))
  if (target.length) {
    event.preventDefault()
    // eslint-disable-next-line no-undef
    $('html, body').stop().animate({
      scrollTop: target.offset().top
    }, 1000)
  }
})
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tour h2 {
  margin-top: 1em;
}
.tour ul {
   list-style-type: none;
}
.tour a {
  color: #000;
}
.slider {
  margin-top: 2.5em;
}
</style>
