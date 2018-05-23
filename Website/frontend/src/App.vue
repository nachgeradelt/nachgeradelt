<template>
  <div id="app">
    <h1>Radfahrerwissen</h1>
    <img src="./assets/logo.jpg">
    <div class="topnav">
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
/* Add a black background color to the top navigation */
.topnav {
    margin: 2em 0;
}

/* Style the links inside the navigation bar */
.topnav a {
    color: #000;
    text-align: center;
    text-decoration: none;
    font-size: 20px;
    padding: 1em;
}

.topnav a:not(:last-child) {
    margin-right: 10em;
  }

/* Change the color of links on hover */
.topnav a:hover {
    background-color: orange;
}

/* Add a color to the active/current link */
.topnav a.router-link-exact-active {
    background-color: orange;
}

</style>
