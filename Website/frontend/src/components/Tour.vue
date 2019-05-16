<template>
<div class="tour">
  <div class="map">
    <l-map style="height: calc(100% - 100px)" :zoom="zoom" :center="center" :bounds="bounds">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-geo-json v-if="to !== 'werdau' & distanceSlider.value[0] < length46 & distanceSlider.value[1] > length46" :geojson="geojson46" :options="options46"></l-geo-json>
      <l-geo-json v-if="to !== 'woerlitz' & distanceSlider.value[0] < length100 & distanceSlider.value[1] > length100" :geojson="geojson100" :options="options100"></l-geo-json>
      <l-marker :lat-lng="markerLeipzig">
       <l-popup content="Leipzig"></l-popup>
      </l-marker>
      <l-marker v-if="to !== 'woerlitz' & distanceSlider.value[0] < length100 & distanceSlider.value[1] > length100" :lat-lng="markerWerdau">
        <l-popup content="Werdau"></l-popup>
      </l-marker>
      <l-marker v-if="to !== 'werdau' & distanceSlider.value[0] < length46 & distanceSlider.value[1] > length46" :lat-lng="markerWoerlitz">
        <l-popup content="Wörlitz"></l-popup>
      </l-marker>
    </l-map>
  </div>
  <div class="menu">
    <div class="filter-switch">
      <button class="btn btn-primary" @click="showFilter = !showFilter"><i class="fa fa-filter"></i> Filter</button>
    </div>
    <div class="filter" v-show="showFilter">
      <h3>Abfahrt</h3>
      <select v-model="from">
        <option value="all">Alle Startorte</option>
        <option value="leipzig">Leipzig</option>
      </select>

      <h3>Distanz</h3>
      <div class="slider">
        <vue-slider v-bind="distanceSlider" v-model="distanceSlider.value" :show="showFilter"></vue-slider>
      </div>

      <h3>Ziel</h3>
      <select v-model="to">
        <option value="all">Alle Zielorte</option>
        <option value="werdau">Werdau</option>
        <option value="woerlitz">Wörlitz</option>
      </select>

      <h3>Touren</h3>
      <ul>
        <li>
          <router-link v-if="to !== 'werdau' & distanceSlider.value[0] < length46 & distanceSlider.value[1] > length46" :to="'/detail/46'">Leipzig - Dessau - Wörlitz</router-link>
        </li>
        <li>
          <router-link v-if="to !== 'woerlitz' & distanceSlider.value[0] < length100 & distanceSlider.value[1] > length100" :to="'/detail/100'">Leipzig - Altenburg - Werdau</router-link>
        </li>
      </ul>
    </div>
  </div>
</div>
</template>

<script>
import Vue from 'vue'
import {
  LMap,
  LTileLayer,
  LMarker,
  LGeoJson,
  LPopup
} from 'vue2-leaflet'
import vueSlider from 'vue-slider-component'
import router from '../router/index.js'
import {route46} from './Route46.js'
import {route100} from './Route100.js'

function onEachFeature (feature, layer) {
  let popupContent = Vue.extend({
    template: `<div><p><router-link :to="'/detail/${layer.options.id}'">Details zur Route ${layer.options.name}</router-link></p></div>`,
    router
  })
  let popup = new popupContent()
  layer.bindPopup(popup.$mount().$el)
}

export default {
  name: 'Tour',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LGeoJson,
    LPopup,
    vueSlider
  },
  data () {
    return {
      showFilter: false,
      distanceSlider: {
        value: [
          0,
          100
        ],
        formatter: '{value} km',
        max: 100
      },
      from: 'all',
      to: 'all',
      zoom: 9,
      center: [51.3391827, 12.3810549],
      geojson46: null,
      length46: 72.5,
      geojson100: null,
      length100: 79.6,
      bounds: null,
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution: 'openrouteservice.org | &copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      markerLeipzig: L.latLng(0, 0),
      markerWerdau: L.latLng(0, 0),
      markerWoerlitz: L.latLng(0, 0),
      options46: {
        style: function () {
          return {
            weight: 7,
            color: '#007bff',
            opacity: 1,
            fillColor: '007bff',
            fillOpacity: 1,
            id: 46,
            name: 'Leipzig - Dessau - Wörlitz'
          }
        },
        onEachFeature: onEachFeature
      },
      options100: {
        style: function () {
          return {
            weight: 7,
            color: '#0c2f2f',
            opacity: 1,
            fillColor: '0c2f2f',
            fillOpacity: 1,
            id: 100,
            name: 'Leipzig - Altenburg - Werdau'
          }
        },
        onEachFeature: onEachFeature
      }
    }
  },
  watch: {
    /*
    geojson: function (newGeojson, oldGeojson) {
      var bounds = L.latLngBounds(newGeojson.features[0].geometry.coordinates.map((o) => o))
      var correctedBounds = L.latLngBounds([[bounds._southWest.lng, bounds._southWest.lat], [bounds._northEast.lng, bounds._northEast.lat]])
      this.bounds = correctedBounds
    }
    */
  },
  created () {
    this.geojson46 = route46.route46
    this.geojson100 = route100.route100
    this.markerLeipzig = L.latLng(51.3391827, 12.3810549)
    this.markerWerdau = L.latLng(50.7361377, 12.3763847)
    this.markerWoerlitz = L.latLng(51.8481, 12.4233)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tour {
  display: flex;
  height: 100%;
  text-align: center;
}

.map {
  flex: 1 0 auto;
  max-width: 100%;
}

.vue2leaflet-map {
  z-index: 1;
}

.slider {
  margin-top: 2.5em;
}

.menu {
  font-family: 'Arapey';
  font-size: 18px;
  height: calc(100% - 100px);
  width: 250px;
  margin-left: -260px;
  position: relative;
  float: right;
  z-index: 2;
  pointer-events: none;
}

.filter-switch {
    margin-top: 2%;
    height: 10%;
    pointer-events: auto;
}

.tour ul {
  list-style-type: none;
  float: left;
  padding-left: 0;
}

.tour li {
  margin-bottom: 1em;
}

.tour a {
  color: #000;
}

.filter {
  height: 85%;
  background: rgba(208, 210, 211, .5);
  padding: 0 1em;
  pointer-events: auto;
}

select {
  width: 70%;
}

h3 {
  background-image: url('../assets/sign.jpg');
  background-repeat: no-repeat;
  background-position: 45px;
  background-size: 120px 40px;
  margin-top: 1.5rem;
}
</style>
