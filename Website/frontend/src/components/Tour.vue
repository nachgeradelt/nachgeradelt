<template>
  <div class="tour">
    <h1>{{ msg }}</h1>
    <h2>Abfahrt</h2>

    <h2>Distanz</h2>

    <h2>Ziel</h2>

    <h2>Touren</h2>
    <ul>
      <li>
        <a
          href="https://vuejs.org"
          target="_blank"
        >
          Tour 1
        </a>
      </li>
      <li>
        <a
          href="https://forum.vuejs.org"
          target="_blank"
        >
          Tour 2
        </a>
      </li>
      <li>
        <a
          href="https://chat.vuejs.org"
          target="_blank"
        >
          Tour 3
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Tour',
  data () {
    return {
      msg: 'Radfahrerwissen'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
