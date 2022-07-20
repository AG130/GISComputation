<template>
    <div>
        <div id="map" class="map"></div>
    </div>
</template>

<script>
import { Map, View } from "ol";//地图,视图
import OSM from "ol/source/OSM"; //可以理解为数据源,就是一张图片
import TileLayer from "ol/layer/Tile"; //可以理解为图层
import { fromLonLat } from "ol/proj";//将坐标从经度/纬度转换为不同的投影。
export default {
  data() {
    return {
      map: null,
    };
  },
  methods: {
    createMap() {
      this.map = new Map({
        target: "map",
        layers: [
          new TileLayer({
            source: new OSM({}),
          }),
        ],
        view: new View({
          center: [114.624, 30.4634],
          projection: "EPSG:3857",
          zoom: 8,
          maxZoom: 20,
        }),
      });
    },
  },
  mounted() {
    this.createMap();
  },
};
</script>

<style>
.map{
    height: 400px;
    width: 100%;
}
</style>