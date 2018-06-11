<template>
<div id="app">
  <div class="content">
    <div class="header">
      <router-link v-bind:to="'/'">
        <img src="./assets/header.svg" alt="Header" />
      </router-link>
    </div>
    <router-view/>
  </div>

  <footer class="footer">
    <div class="banner"></div>
    <ul class="list-unstyled quick-links">
      <li>
        <router-link v-bind:to="'/'"><i class="fa fa-angle-double-right"></i>Toursuche</router-link>
      </li>
      <li>
        <router-link v-bind:to="'/about'"><i class="fa fa-angle-double-right"></i>Über uns</router-link>
      </li>
      <!--li>
        <router-link v-bind:to="'/contact'"><i class="fa fa-angle-double-right"></i>Kontakt</router-link>
      </li-->
    </ul>
    <ul class="list-unstyled list-inline social text-center">
      <li class="list-inline-item"><a href="https://twitter.com/radfahrerwissen"><i class="fa fa-twitter"></i></a></li>
      <li class="list-inline-item"><a href="https://github.com/nachgeradelt/nachgeradelt"><i class="fa fa-github"></i></a></li>
    </ul>
  </footer>
</div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@import url('https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css');
html,
body {
  font-family: 'Lato';
  font-size: 18px;
  height: 100%;
}

#app {
  display: flex;
  flex-direction: column;
  height: 100%;
  text-align: center;
}

.content {
  flex: 1 0 auto;
}

.header {
  background: #179999;
  display: flex;
  padding: 15px 10px;
}


.header img {
  height: 75px;
  background: none;
  max-width: 100%;
}

.footer {
  flex-shrink: 0;
}

.list-unstyled {
  margin-bottom: 0;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  background: #F1F1F2;
}

p {
  margin: 0 0 20px 0;
}

.banner {
  background: transparent url("./assets/logo_banner.jpg") repeat scroll 0% 0%;
  max-width: 100%;
  height: 45px;
}

/* Footer */

footer {
  background: #0C2F2F !important;
}

footer a {
  color: #ffffff;
  text-decoration: none !important;
  background-color: transparent;
  -webkit-text-decoration-skip: objects;
}

footer ul.social li {
  padding: 3px 0;
}

footer ul.social li a i {
  margin-right: 5px;
  font-size: 25px;
  -webkit-transition: .5s all ease;
  -moz-transition: .5s all ease;
  transition: .5s all ease;
}

footer ul.social li:hover a i {
  font-size: 30px;
  margin-top: -10px;
}

footer ul.social li a,
footer ul.quick-links li a {
  color: #ffffff;
}

footer ul.social li a:hover {
  color: #eeeeee;
}

footer ul.quick-links li {
  padding: 5px 5px;
  -webkit-transition: .5s all ease;
  -moz-transition: .5s all ease;
  transition: .5s all ease;
  display: inline-block;
}

footer ul.quick-links li:hover {
  padding: 3px 0;
  margin-left: 5px;
  font-weight: 700;
}

footer ul.quick-links li a i {
  margin-right: 5px;
}

footer ul.quick-links li:hover a i {
  font-weight: 700;
}
</style>
