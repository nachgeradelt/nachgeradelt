<template>
  <div id="app">
    <img src="./assets/logo.jpg">
    <div>
      <router-link v-bind:to="'/'">Toursuche</router-link>
      <router-link v-bind:to="'/list'">Tourenliste</router-link>
      <router-link v-bind:to="'/about'">Über uns</router-link>
      <router-link v-bind:to="'/contact'">Kontakt</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
