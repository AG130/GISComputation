<template>
  <div>
    <div id="mapDiv"></div>
    <div>
      <el-button @click="addPoint()">添加点</el-button>
      <el-button @click="addLine()">添加线</el-button>
      <el-button @click="addBuffer()">添加缓冲区</el-button>
    </div>
  </div>
</template>
 
<script>
import "ol/ol.css";
import { Map, View, Feature } from "ol";
import TileLayer from "ol/layer/Tile";
import OSM from "ol/source/OSM";
import { LineString, Point } from "ol/geom";
import { Style, Fill, Stroke, Circle as sCircle } from "ol/style";
import { Vector as VectorLayer } from "ol/layer";
import { Vector as VectorSource } from "ol/source";

export default {
  data() {
    return {
      map: null,
      line_point: [
        [114.625212, 30.46644],
        [114.619551, 30.466218],
        [114.617589, 30.466121],
      ],
    };
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      this.map = new Map({
        target: "mapDiv",
        layers: [
          new TileLayer({
            // 使用OSM地图
            source: new OSM(),
          }),
        ],
        view: new View({
          // 使用WGS84坐标系
          projection: "EPSG:4326",
          center: [114.612, 30.4604],
          // 初始16倍
          zoom: 16,
        }),
      });
    },
    addPoint() {
      var new_style = new Style({
        image: new sCircle({
          radius: 10,
          stroke: new Stroke({
            color: "#fff",
          }),
          fill: new Fill({
            color: "#3399CC",
          }),
        }),
      });
      var point1 = new Feature({
        geometry: new Point([114.612, 30.4604]),
      });
      point1.setStyle(new_style);
      var new_marker = new VectorLayer({
        source: new VectorSource({
          features: [point1],
        }),
      });
      this.map.addLayer(new_marker);
    },
    addLine() {
      var marker1 = new Feature({
        type: "lineStyle",
        geometry: new LineString(this.line_point),
      });
      var lineStyle = new Style({
        stroke: new Stroke({
          color: "red",
          width: 4,
        }),
      });
      marker1.setStyle(lineStyle);
      var line = new VectorLayer({
        source: new VectorSource({
          features: [marker1],
        }),
      });
      this.map.addLayer(line);
    },
    addBuffer(){

    }
  },
};
</script>
 
<style scoped>
#mapDiv {
  width: 100%;
  height: 400px;
}
</style>
