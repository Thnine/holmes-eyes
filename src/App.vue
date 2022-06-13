<template>
  <div id="app">
    <!--Mapshow id="map-comp"/-->
    <ShoppingTime/>
  </div>
</template>

<script>
import Mapshow from './components/Mapshow'
import MatchSankey from './components/MatchSankey.vue'
import ShoppingTime from './components/ShoppingTime.vue'

export default {
  name: 'App',
  components: {
    Mapshow,
    MatchSankey,
    ShoppingTime
}
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
  width:100%;
  height: 100%;

}
#map-comp{
    height:1150px;
    width: 2100px;
    border: black;
    border-width: 5px;
    display: flex;
    flex-direction: row;
  }


</style>
