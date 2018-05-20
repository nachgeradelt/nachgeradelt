<template>
  <div id="app">
    <h1>Radfahrerwissen</h1>
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
  text-align: center;
  color: #2c3e50;
}
</style>
