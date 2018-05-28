<template>
<div class="tour">
  <div class="map">
    <l-map style="height: calc(100% - 50px)" :zoom="zoom" :center="center" :bounds="bounds">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-geo-json :geojson="geojson" :options="options"></l-geo-json>
      <l-marker :lat-lng="marker">
       <l-popup content="Leipzig"></l-popup>
      </l-marker>
      <l-marker :lat-lng="marker2">
        <l-popup content="Hof"></l-popup>
      </l-marker>
    </l-map>
  </div>
  <div class="menu">
    <div class="filter-switch">
      <button class="btn btn-primary" @click="showFilter = !showFilter"><i class="fa fa-filter"></i> Filter</button>
    </div>
    <div class="filter" v-show="showFilter">
      <h3>Abfahrt</h3>
      <select>
        <option value="">Start</option>
        <option value="">Leipzig</option>
      </select>

      <h3>Distanz</h3>
      <div class="slider">
        <vue-slider v-bind="distanceSlider" v-model="distanceSlider.value" :show="showFilter"></vue-slider>
      </div>

      <h3>Ziel</h3>
      <select>
        <option value="">Ziel</option>
        <option value="">Dessau</option>
        <option value="">Werdau</option>
      </select>

      <h3>Touren</h3>
      <ul>
        <li>
          <router-link v-bind:to="'/detail'">Details zur Route 1</router-link>
        </li>
        <li>
          <router-link v-bind:to="'/detail'">Details zur Route 2</router-link>
        </li>
        <li>
          <router-link v-bind:to="'/detail'">Details zur Route 3</router-link>
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
import axios from 'axios'
import PopupContent from './TourPopup'

function onEachFeature (feature, layer) {
  let popupContent = Vue.extend(PopupContent)
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
        max: 250
      },
      zoom: 9,
      center: [51.3391827, 12.3810549],
      geojson: null,
      bounds: null,
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution: 'openrouteservice.org | &copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      // TODO: Add dynamic marker
      marker: L.latLng(51.3391827, 12.3810549),
      marker2: L.latLng(50.3219015, 11.9178807),
      options: {
        style: function () {
          return {
            weight: 5,
            color: '#007bff',
            opacity: 1,
            fillColor: '007bff',
            fillOpacity: 1
          }
        },
        onEachFeature: onEachFeature
      }
    }
  },
  watch: {
    geojson: function (newGeojson, oldGeojson) {
      var bounds = L.latLngBounds(newGeojson.features[0].geometry.coordinates.map((o) => o))
      var correctedBounds = L.latLngBounds([[bounds._southWest.lng, bounds._southWest.lat], [bounds._northEast.lng, bounds._northEast.lat]])
      this.bounds = correctedBounds
    }
  },
  created () {
    axios.get(
      'https://private-anon-e0b6bc4572-openrouteservice.apiary-proxy.com/directions?api_key=58d904a497c67e00015b45fceb5286746f824aea8ee12a074a6cdf47&coordinates=12.3810549%2C51.3391827%7C12.324152%2C51.2182735%7C12.45%2C51.1333%7C12.4340988%2C50.9852411%7C12.3890204%2C50.8153837%7C12.3763847%2C50.7361377%7C12.2008694%2C50.6562556%7C12.1679662%2C50.6082525%7C12.1346523%2C50.4950632%7C11.9178807%2C50.3219015&profile=cycling-tour&preference=recommended&format=geojson&units=km&language=de&geometry=true&geometry_format=geojson&geometry_simplify=true&instructions=false&elevation=true'
    ).then(response => {
      this.geojson = response.data
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tour {
  display: flex;
  height: 100%;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
}

.map {
  flex: 1 0 auto;
  z-index: 1;
  max-width: 100%;
}

.slider {
  margin-top: 2.5em;
}

.menu {
  height: calc(100% - 50px);
  width: 300px;
  margin-left: -350px;
  position: relative;
  float: right;
  z-index: 2;
  pointer-events: auto;
}

.filter-switch {
    margin-top: 2%;
    height: 10%;
}

.tour ul {
  list-style-type: none;
  float: left;
}

.tour a {
  color: #000;
}

.filter {
  height: 85%;
  background: rgba(255, 255, 255, .5);
  padding: 0 1em;
}

h3 {
}

select {
  width: 100%;
}
</style>
