<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import login from "./login/login.vue";

export default {
  name: "app",
  components: { login },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: auto;

  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
