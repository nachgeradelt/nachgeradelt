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
import axios from 'axios'
import router from '../router/index.js'

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
    function getRoute46 () {
      return axios.get('https://api.openrouteservice.org/directions?api_key=5b3ce3597851110001cf6248a7920b3eb8e3406eb56356c8fe69a904&coordinates=12.3811,51.3392|12.376742,51.35116|12.385,51.3686|12.38555,51.36883|12.38442,51.36959|12.3772,51.3844|12.375139,51.392931|12.3736,51.3944|12.3522,51.405483|12.354641,51.43436|12.34035,51.434929|12.34871197,51.4642334|12.343749,51.473375|12.345014284,51.473306515|12.343803717,51.473081294|12.335233574,51.516849639|12.33256,51.523136|12.3289,51.5234|12.342965,51.533736|12.337026736,51.546612394|12.33611111,51.55472222|12.337421908,51.55144916|12.336443078,51.55413301|12.336982159,51.555026303|12.335801,51.564666|12.3443198,51.5738505|12.324718,51.578363|12.335254,51.581803|12.3,51.6|12.300224,51.608563|12.2876557,51.6022269|12.27292778,51.64491389|12.26873,51.66122|12.262589,51.656583|12.268188,51.69029|12.261997,51.691148|12.229865,51.732304|12.2272,51.7567|12.240392,51.786642|12.2267,51.8392|12.2169,51.8564|12.23583,51.863944|12.237728,51.879187|12.27278,51.841041|12.2781,51.845|12.2721,51.8507|12.30247778,51.84348333|12.351422,51.847643|12.42138889,51.84611111|12.4233,51.8481&profile=cycling-road&preference=recommended&format=geojson&units=km&geometry=true&geometry_simplify=false&instructions=false')
    }

    function getRoute100 () {
      return axios.get('https://api.openrouteservice.org/directions?api_key=5b3ce3597851110001cf6248a7920b3eb8e3406eb56356c8fe69a904&coordinates=12.3810549,51.3391827|12.324152,51.2182735|12.45,51.1333|12.4340988,50.9852411|12.3890204,50.8153837|12.3763847,50.7361377&profile=cycling-road&preference=recommended&format=geojson&units=km&geometry=true&geometry_simplify=false&instructions=false')
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
