<template>
  <div>
    <div id="miniMapDiv2" ref="miniMapDiv2"></div>
  </div>
</template>
  
  <script>
import "ol/ol.css";
import GeoJSON from "ol/format/GeoJSON";
import OSM from "ol/source/OSM";
import { Map, View, Feature, Tile } from "ol";
import { LineString, Point } from "ol/geom";
import { Style, Fill, Stroke, Icon, Circle } from "ol/style";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import { Vector as VectorSource, XYZ } from "ol/source";
import { createStringXY } from "ol/coordinate";
import { Select, Draw } from "ol/interaction";
import {
  defaults as defaultControls,
  OverviewMap,
  ZoomSlider,
  ScaleLine,
} from "ol/control";
import utils from "@/utils";
import * as turf from "@turf/turf";
export default {
  data() {
    return {
      //地图框架
      map: null,
      OSMLayer: null,
      //绘制轨迹
      draw: null,
      drawSource: null,
      drawLayer: null,
      //初始中心点
      initCenter: [114.612, 30.4604],
      //初始缩放
      initZoom: 16,
    };
  },
  mounted() {
    let self = this;
    self.initMap();
  },
  methods: {
    initMap() {
      //鹰眼
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
      //OSM地图
      this.OSMLayer = new TileLayer({
        source: new OSM(),
      });
      //绘制图层
      this.drawSource = new VectorSource({ wrapX: false });
      this.drawLayer = new VectorLayer({
        source: this.drawSource,
      });
      this.map = new Map({
        target: "miniMapDiv2",
        layers: [this.OSMLayer, this.drawLayer],
        view: new View({
          // 使用WGS84坐标系
          projection: "EPSG:4326",
          center: this.initCenter,
          // 初始16倍
          zoom: this.initZoom,
        }),
        controls: defaultControls({ zoom: true }).extend([OverviewMapControl]),
      });
      //导航条
      this.map.addControl(new ZoomSlider());
      //比例尺
      this.map.addControl(
        new ScaleLine({
          units: "metric",
        })
      );
    },
    //绘图线工具
    onAddInteraction(type) {
      let self = this;
      //勾绘矢量图形的类
      this.draw = new Draw({
        //source代表勾绘的要素属于的数据集
        source: self.drawSource,
        //type 表示勾绘的要素包含的 geometry 类型
        type: type,
      });
      //绘制结束时触发的事件
      this.draw.on("drawend", function (e) {
        const geometry = e.feature.getGeometry();
        let pointArr = geometry.getCoordinates();
        utils.$emit("trailPoint", pointArr);
        self.coordinate = [];
        self.$emit("changeVis",true)
        self.drawLayer.getSource().clear()
        self.removeDraw();
      });
      self.map.addInteraction(this.draw);
    },
    //删除交互
    removeDraw() {
      this.map.removeInteraction(this.draw);
    },
    //绘制轨迹线
    addTrail() {
      // 获取点击地图的坐标(选中样式)
      let selectedStyle = new Style({
        fill: new Fill({
          color: "rgba(1, 210, 241, 0.2)",
        }),
        stroke: new Stroke({
          color: "yellow",
          width: 4,
        }),
      });
      // 选择线的工具类
      this.selectTool = new Select({
        multi: true,
        hitTolerance: 10, // 误差
        style: selectedStyle, // 选中要素的样式
      });
      //添加交互
      this.map.addInteraction(this.selectTool);
      //调用绘图工具并传递类型为线，其他类型有Point,LineString,Polygon,Circle
      this.onAddInteraction("LineString");
    },
  },
};
</script>
  
  <style>
#miniMapDiv2 {
  width: 100%;
  height: 600px;
  padding: 0;
  margin: 0;
  z-index: 10;
}

#miniMapDiv2 .ol-zoom .ol-zoom-out {
  margin-top: 204px;
}
#miniMapDiv2 .ol-zoomslider {
  background-color: transparent;
  top: 2.3em;
}
#miniMapDiv2 .ol-touch .ol-zoom .ol-zoom-out {
  margin-top: 212px;
}
#miniMapDiv2 .ol-touch .ol-zoomslider {
  top: 2.75em;
}
#miniMapDiv2 .ol-zoom-in .ol.has-tooltip:hover[role="tooltip"],
#miniMapDiv2 .ol-zoom-in .ol-has-tooltip:focus[role="tooltip"] {
  top: 3px;
}
#miniMapDiv2 .ol-zoom-out .ol-has-tooltip:hover[role="tooltip"],
#miniMapDiv2 .ol-zoon-out .ol-has-out-tooltip:focus[role="tooltip"] {
  top: 232px;
}
#miniMapDiv2 .ol-zoom-extent {
  top: 280px;
}
#miniMapDiv2 .ol-custom-overviewmap,
.ol-custom-overviewmap.ol-uncollapsible {
  bottom: auto;
  left: auto;
  /* 右侧显示 */
  right: 0;
  /* 顶部显示 */
  top: 0;
}
/* 鹰眼控件展开时控件外框的样式 */
.ol-custom-overviewmap:not(.ol-collapsed) {
  border: 1px solid black;
}
/* 鹰眼控件中地图容器样式 */
.ol-custom-overviewmap .ol-overviewmap-map {
  border: none;
  width: 200px;
}
/* 鹰眼控件中显示当前窗口中主图区域的边框 */
.ol-custom-overviewmap .ol-overviewmap-box {
  border: 1px solid red;
}
/* 鹰眼控件展开时其控件按钮图标的样式 */
.ol-custom-overviewmap:not(.ol-collapsed) button {
  bottom: auto;
  left: auto;
  right: 1px;
  top: 1px;
}
</style>
  
  