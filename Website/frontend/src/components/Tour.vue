<template>
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <h2>Abfahrt</h2>
        <select>
          <option value="">Start</option>
        </select>

        <h2>Distanz</h2>

        <h2>Ziel</h2>
        <select>
          <option value="">Ziel</option>
        </select>

        <h2>{{ tours }}</h2>
        <ul>
          <li>
            <a href="https://vuejs.org" target="_blank">Tour 1</a>
          </li>
          <li>
            <a href="https://forum.vuejs.org" target="_blank">Tour 2</a>
          </li>
          <li>
            <a href="https://chat.vuejs.org" target="_blank">Tour 3</a>
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

  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet'

export default {
  name: 'Tour',
  components: { LMap, LTileLayer, LMarker },
  data () {
    return {
      tours: 'Touren',
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

</style>
