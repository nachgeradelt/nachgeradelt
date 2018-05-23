<template>
  <div id="list">
  <h2>Liste der Touren</h2>
  <div class="tours">
    Leipzig Dessau Wörlitz Gräfenhainichen Leipzig 113.6 km<br>
    Leipzig Zwenkau Lobstädt Altenburg Crimmitschau Werdau Greiz Elsterberg Plauen Hof 150 km
  </div>
  </div>
</template>

<script>
export default {
  name: 'List'
}
</script>
<!-- styling for the component -->
<style>
#list {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.tours {
  padding-left: 15em;
  text-align: left;
}
</style>
