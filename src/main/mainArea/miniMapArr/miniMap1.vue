<template>
  <div>
    <div id="miniMapDiv1" ref="miniMapDiv1"></div>
  </div>
</template>

<script>
import "ol/ol.css";
import OSM from "ol/source/OSM";
import { Map, View, Feature, Tile } from "ol";
import { Style, Fill, Stroke, Icon, Circle } from "ol/style";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import { Vector as VectorSource, XYZ } from "ol/source";
import { Select, Draw } from "ol/interaction";
import {
  defaults as defaultControls,
  OverviewMap,
  ZoomSlider,
  ScaleLine,
} from "ol/control";
import utils from "@/utils";
export default {
  data() {
    return {
      //地图框架
      map1: null,
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
    var that =this
    setTimeout(()=>{
      that.initMap()
    },6000)
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
      this.map1 = new Map({
        target: "miniMapDiv1",
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
      this.map1.addControl(new ZoomSlider());
      //比例尺
      this.map1.addControl(
        new ScaleLine({
          units: "metric",
        })
      );
    },
    //删除交互
    removeDraw() {
      this.map1.removeInteraction(this.draw);
    },
    //绘制人员
    onAddPeople(type,t) {
      let self = this;
      //勾绘矢量图形的类
      this.draw = new Draw({
        //source代表勾绘的要素属于的数据集
        source: self.drawSource,
        //type 表示勾绘的要素包含的 geometry 类型
        type: type,
      });
      this.draw.on("drawend", function (e) {
        const geometry = e.feature.getGeometry();
        let pointArr = geometry.getCoordinates();
        utils.$emit("newPeopleP", pointArr);
        self.coordinate = [];
        if(t==0){
          self.$emit("changeVis",0)
        }else{
          self.$emit("changeVis",1)
        }
        self.drawLayer.getSource().clear()
        self.removeDraw();
      });
      self.map1.addInteraction(this.draw);
    },
    //绘制点
    addPeoplePoint(t) {
      let selectedStyle = new Style({
        image: new Circle({
          radius: 5,
          stroke: new Stroke({
            color: "#fff",
          }),
          fill: new Fill({
            color: "#66ccff",
          }),
        }),
      });
      this.selectTool = new Select({
        multi: true,
        hitTolerance: 10, // 误差
        style: selectedStyle, // 选中要素的样式
      });
      this.map1.addInteraction(this.selectTool);
      //调用绘图工具并传递类型为线，其他类型有Point,LineString,Polygon,Circle
      this.onAddPeople("Point", t);
    },
  },
};
</script>

<style>
#miniMapDiv1 {
  width: 100%;
  height: 600px;
  padding: 0;
  margin: 0;
  z-index: 0;
}

#miniMapDiv1 .ol-zoom .ol-zoom-out {
  margin-top: 204px;
}
#miniMapDiv1 .ol-zoomslider {
  background-color: transparent;
  top: 2.3em;
}
#miniMapDiv1 .ol-touch .ol-zoom .ol-zoom-out {
  margin-top: 212px;
}
#miniMapDiv1 .ol-touch .ol-zoomslider {
  top: 2.75em;
}
#miniMapDiv1 .ol-zoom-in .ol.has-tooltip:hover[role="tooltip"],
#miniMapDiv1 .ol-zoom-in .ol-has-tooltip:focus[role="tooltip"] {
  top: 3px;
}
#miniMapDiv1 .ol-zoom-out .ol-has-tooltip:hover[role="tooltip"],
#miniMapDiv1 .ol-zoon-out .ol-has-out-tooltip:focus[role="tooltip"] {
  top: 232px;
}
#miniMapDiv1 .ol-zoom-extent {
  top: 280px;
}
#miniMapDiv1 .ol-custom-overviewmap,
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

