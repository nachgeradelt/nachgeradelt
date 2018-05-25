<template>
  <!--div class="container-full tour">
    <div class="row">
      <div class="col-md-2">
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
      <div class="col-md-10 map"-->
        <l-map style="height: calc(100% - 50px)" :zoom="zoom" :center="center">
          <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
          <l-marker :lat-lng="marker"></l-marker>
        </l-map>
      <!--/div>
    </div>
  </div-->
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
          100
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
