<template>
<div class="tour">
  <div class="map">
    <l-map style="height: calc(100% - 100px)" :zoom="zoom" :center="center" :bounds="bounds">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-geo-json :geojson="geojson46" :options="options46"></l-geo-json>
      <l-geo-json :geojson="geojson100" :options="options100"></l-geo-json>
      <l-marker :lat-lng="markerLeipzig">
       <l-popup content="Leipzig"></l-popup>
      </l-marker>
      <l-marker :lat-lng="markerWerdau">
        <l-popup content="Werdau"></l-popup>
      </l-marker>
      <l-marker :lat-lng="markerWoerlitz">
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
      <select>
        <option value="">Alle Startorte</option>
        <option value="">Leipzig</option>
      </select>

      <h3>Distanz</h3>
      <div class="slider">
        <vue-slider v-bind="distanceSlider" v-model="distanceSlider.value" :show="showFilter"></vue-slider>
      </div>

      <h3>Ziel</h3>
      <select>
        <option value="">Alle Zielorte</option>
        <option value="">Werdau</option>
        <option value="">Wörlitz</option>
      </select>

      <h3>Touren</h3>
      <ul>
        <li>
          <router-link :to="{ name: 'detail', params: {id: 46, name: 'Leipzig - Dessau - Wörlitz' } }">Leipzig - Dessau - Wörlitz</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'detail', params: {id: 100, name: 'Leipzig - Altenburg - Werdau' } }">Leipzig - Altenburg - Werdau</router-link>
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
import router from '../router/index.js'

function onEachFeature (feature, layer) {
  let popupContent = Vue.extend({
    template: `<div><p><router-link :to="{ name: 'detail', params: {id: ${layer.options.id}, name: '${layer.options.name}' } }">Details zur Route ${layer.options.name}</router-link></p></div>`,
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
        max: 250
      },
      zoom: 9,
      center: [51.3391827, 12.3810549],
      geojson46: null,
      geojson100: null,
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
    function getRoute46 () {
      return axios.get('https://private-anon-e0b6bc4572-openrouteservice.apiary-proxy.com/directions?api_key=58d904a497c67e00015b45fceb5286746f824aea8ee12a074a6cdf47&coordinates=12.3811%2C51.3392%7C12.376742%2C51.35116%7C12.385%2C51.3686%7C12.38555%2C51.36883%7C12.38442%2C51.36959%7C12.3772%2C51.3844%7C12.375139%2C51.392931%7C12.3736%2C51.3944%7C12.3522%2C51.405483%7C12.354641%2C51.43436%7C12.34035%2C51.434929%7C12.34871197%2C51.4642334%7C12.343749%2C51.473375%7C12.345014284%2C51.473306515%7C12.343803717%2C51.473081294%7C12.335233574%2C51.516849639%7C12.33256%2C51.523136%7C12.3289%2C51.5234%7C12.342965%2C51.533736%7C12.337026736%2C51.546612394%7C12.33611111%2C51.55472222%7C12.337421908%2C51.55144916%7C12.336443078%2C51.55413301%7C12.336982159%2C51.555026303%7C12.335801%2C51.564666%7C12.3443198%2C51.5738505%7C12.324718%2C51.578363%7C12.335254%2C51.581803%7C12.3%2C51.6%7C12.300224%2C51.608563%7C12.2876557%2C51.6022269%7C12.27292778%2C51.64491389%7C12.26873%2C51.66122%7C12.262589%2C51.656583%7C12.268188%2C51.69029%7C12.261997%2C51.691148%7C12.229865%2C51.732304%7C12.2272%2C51.7567%7C12.240392%2C51.786642%7C12.2267%2C51.8392%7C12.2169%2C51.8564%7C12.23583%2C51.863944%7C12.237728%2C51.879187%7C12.27278%2C51.841041%7C12.2781%2C51.845%7C12.2721%2C51.8507%7C12.30247778%2C51.84348333%7C12.351422%2C51.847643%7C12.42138889%2C51.84611111%7C12.4233%2C51.8481&profile=cycling-tour&preference=recommended&format=geojson&units=km&language=de&geometry=true&geometry_format=geojson&geometry_simplify=true&instructions=false&elevation=true')
    }

    function getRoute100 () {
      return axios.get('https://private-anon-e0b6bc4572-openrouteservice.apiary-proxy.com/directions?api_key=58d904a497c67e00015b45fceb5286746f824aea8ee12a074a6cdf47&coordinates=12.3810549%2C51.3391827%7C12.324152%2C51.2182735%7C12.45%2C51.1333%7C12.4340988%2C50.9852411%7C12.3890204%2C50.8153837%7C12.3763847%2C50.7361377&profile=cycling-tour&preference=recommended&format=geojson&units=km&language=de&geometry=true&geometry_format=geojson&geometry_simplify=true&instructions=false&elevation=true')
    }

    axios.all([getRoute46(), getRoute100()])
      .then(axios.spread((route46, route100) => {
        // TODO: Add dynamic geojsons
        this.geojson46 = route46.data
        this.geojson100 = route100.data
        // TODO: Add dynamic marker
        this.markerLeipzig = L.latLng(51.3391827, 12.3810549)
        this.markerWerdau = L.latLng(50.7361377, 12.3763847)
        this.markerWoerlitz = L.latLng(51.8481, 12.4233)
      }))
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
  font-family: 'Arapey';font-size: 20px;
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

h3 {
}

select {
  width: 100%;
}
</style>
