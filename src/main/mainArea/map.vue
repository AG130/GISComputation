<template>
  <div id="mapDiv"></div>
</template>
 
<script>
import "ol/ol.css";
import {Map, View} from "ol";
import TileLayer from "ol/layer/Tile";
import OSM from "ol/source/OSM";
 
export default {
  data() {
    return {
      map: null
    };
  },
  mounted() {
    new Map({
      target: "mapDiv",
      layers: [new TileLayer({
        // 使用OSM地图
        source: new OSM()
      })],
      view: new View({
        // 使用WGS84坐标系
        projection: "EPSG:4326",
        center: [114.612, 30.4604],
        // 初始16倍
        zoom: 16
      })
    });
  }
};
</script>
 
<style scoped>
 
#mapDiv {
  width: 100%;
  height: 400px;
}
 
</style>
