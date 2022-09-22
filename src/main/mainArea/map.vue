<template>
  <div>
    <div id="mapDiv">
      <div
        id="mouseP"
        style="
          color: #fff;
          position: absolute;
          bottom: 10px;
          right: 10px;
          z-index: 10000000;
          width: 200px;
          line-height: 30px;
          background: rgba(0, 0, 0, 0.5);
        "
      ></div>
    </div>
    <div>
      <el-button @click="addPoint()">添加点</el-button>
      <el-button @click="addLine()">添加线</el-button>
      <el-button @click="addBuffer()">添加缓冲区</el-button>
    </div>
  </div>
</template>
 
<script>
import "ol/ol.css";
import OSM from "ol/source/OSM";
import { Map, View, Feature, controls } from "ol";
import TileLayer from "ol/layer/Tile";
import { LineString, Point } from "ol/geom";
import { Style, Fill, Stroke, Circle as sCircle } from "ol/style";
import { Vector as VectorLayer } from "ol/layer";
import { Vector as VectorSource } from "ol/source";
import MousePosition from "ol/control/MousePosition";
import { createStringXY } from "ol/coordinate";
import {
  defaults as defaultControls,
  OverviewMap,
  ZoomSlider,
} from "ol/control";

export default {
  inject: ["locatePlace_form"],
  data() {
    return {
      //地图框架
      map: null,
      //初始中心点
      initCenter: [114.612, 30.4604],
      //初始缩放
      initZoom: 16,
      //测试数据开始
      line_point: [
        [114.625212, 30.46644],
        [114.619551, 30.466218],
        [114.617589, 30.466121],
      ],
      //测试数据结束
    };
  },
  mounted() {
    this.initMap();
    this.initMouse();
  },
  methods: {
    // 地图初始化
    initMap() {
      var OverviewMapControl = new OverviewMap({
        className: "ol-overviewmap ol-custom-overviewmap",
        layers: [
          new TileLayer({
            source: new OSM(),
          }),
        ],
        label: "\u00AB",
        collapsed: false,
      });
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
          center: this.initCenter,
          // 初始16倍
          zoom: this.initZoom,
        }),
        controls: defaultControls({ zoom: true }).extend([OverviewMapControl]),
      });
      this.map.addControl(new ZoomSlider());
    },
    // 地图复位
    resetMap() {
      var view = this.map.getView();
      view.animate({
        center: this.initCenter,
        zoom: this.initZoom,
      });
    },
    // 地图定位
    locatePlace(id) {
      var id = id;
      var view = this.map.getView();
      switch (id) {
        // 洪山区
        case 0:
          view.animate({
            center: [114.337837, 30.502241],
            zoom: 12,
          });
          break;
        // 东湖高新区
        case 1:
          view.animate({
            center: [114.525418, 30.489736],
            zoom: 12,
          });
          break;
        // 南望山
        case 2:
          view.animate({
            center: [114.395896, 30.521557],
            zoom: 16,
          });
          break;
        // 未来城
        case 3:
          view.animate({
            center: [114.612, 30.4604],
            zoom: 16,
          });
          break;
        default:
          view.animate({
            center: [this.locatePlace_form.x, this.locatePlace_form.y],
            zoom: 12,
          });
          break;
      }
    },
    //传地图中心点坐标
    sendCood() {
      var mapCenter = this.map.getView().getCenter();
      mapCenter[0] = mapCenter[0].toFixed(4);
      mapCenter[1] = mapCenter[1].toFixed(4);
      this.$emit("sendCood", mapCenter);
    },
    // 测试函数开始
    initMouse() {
      var MousePositionControl = new MousePosition({
        coordinateFormat: createStringXY(6),
        projection: "EPSG:4326",
        className: "custom-mouse-position",
        target: document.getElementById("mouseP"),
      });
      this.map.addControl(MousePositionControl);
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
    addBuffer() {},
    //测试函数结束
  },
};
</script>
 
<style>
#mapDiv {
  width: 100%;
  height: 500px;
}

#mapDiv .ol-zoom .ol-zoom-out {
  margin-top: 204px;
}
#mapDiv .ol-zoomslider {
  background-color: transparent;
  top: 2.3em;
}
#mapDiv .ol-touch .ol-zoom .ol-zoom-out {
  margin-top: 212px;
}
#mapDiv .ol-touch .ol-zoomslider {
  top: 2.75em;
}
#mapDiv .ol-zoom-in .ol.has-tooltip:hover[role="tooltip"],
#mapDiv .ol-zoom-in .ol-has-tooltip:focus[role="tooltip"] {
  top: 3px;
}
#mapDiv .ol-zoom-out .ol-has-tooltip:hover[role="tooltip"],
#mapDiv .ol-zoon-out .ol-has-out-tooltip:focus[role="tooltip"] {
  top: 232px;
}
#mapDiv .ol-zoom-extent {
  top: 280px;
}
#mapDiv .ol-custom-overviewmap .ol-overviewmap-box {
  border: 1px solid red;
}
</style>
