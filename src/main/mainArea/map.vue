<template>
  <div>
    <div id="mapDiv" ref="mapDiv">
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
      <el-button @click="addPoint">添加点</el-button>
      <el-button @click="addBuffer">添加缓冲区</el-button>
      <el-button @click="testButtonClick">测试</el-button>
    </div>
  </div>
</template>
 
<script>
import html2canvas from "html2canvas";
import "ol/ol.css";
import GeoJSON from 'ol/format/GeoJSON';
import OSM from "ol/source/OSM";
import { Map, View, Feature, Tile } from "ol";
import { LineString, Point } from "ol/geom";
import { Style, Fill, Stroke, Circle as sCircle } from "ol/style";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import { TileWMS, Vector as VectorSource } from "ol/source";
import { createStringXY } from "ol/coordinate";
import { Select, Draw } from "ol/interaction";
import {
  defaults as defaultControls,
  OverviewMap,
  ZoomSlider,
  ScaleLine,
  MousePosition,
} from "ol/control";
import utils from "@/utils";
import * as turf from '@turf/turf'

export default {
  inject: ["locatePlace_form"],
  data() {
    return {
      //地图框架
      map: null,
      mapLayer: null,
      trailLayer: null,
      //绘制轨迹
      draw: null,
      trailSource: null,
      //单条轨迹线
      coordinate: [],
      //所有轨迹线
      pTrail: [
        [
          [114.625212, 30.46644],
          [114.619551, 30.466218],
          [114.617589, 30.466121],
        ],
        [
          [114.625, 30.466],
          [114.619, 30.466],
          [114.617, 30.466],
        ],
        [
          [114.67, 30.48],
          [114.69, 30.4],
          [114.5, 30.4],
        ],
      ],
      //初始中心点
      initCenter: [114.612, 30.4604],
      //初始缩放
      initZoom: 16,
    };
  },
  mounted() {
    this.initMap();
    this.initMouse();
  },
  methods: {
    // 地图初始化
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
      //线图层
      this.trailSource = new VectorSource({ wrapX: false });
      this.trailLayer = new VectorLayer({
        source: this.trailSource,
      });
      //主地图
      this.mapLayer = new TileLayer({
        source: new OSM(),
      });
      this.map = new Map({
        target: "mapDiv",
        layers: [this.mapLayer, this.trailLayer],
        logo: false,
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
      mapCenter[0] = parseFloat(mapCenter[0]).toFixed(4);
      mapCenter[1] = parseFloat(mapCenter[1]).toFixed(4);
      this.$emit("sendCood", mapCenter);
    },
    //切换地图展示
    changeMap(id) {
      switch (id) {
        case 0:
          alert("1");
          //展示OSM地图
          break;
        case 1:
          alert("2");
          //展示天地图矢量地图
          break;
        case 2:
          alert("3");
          //展示天地图影像地图
          break;
      }
    },
    //地图导出
    saveMap() {
      html2canvas(this.$refs.mapDiv, { backgroundColor: null }).then(
        (canvas) => {
          this.saveFile(
            canvas.toDataURL("image/png"),
            new Date().toLocaleString()
          );
        }
      );
    },
    saveFile(data, filename) {
      const save_link = document.createElementNS(
        "http://www.w3.org/1999/xhtml",
        "a"
      );
      save_link.href = data;
      save_link.download = filename;

      const event = document.createEvent("MouseEvents");
      event.initMouseEvent(
        "click",
        true,
        false,
        window,
        0,
        0,
        0,
        0,
        0,
        false,
        false,
        false,
        false,
        0,
        null
      );
      save_link.dispatchEvent(event);
    },
    //绘图工具
    onAddInteraction(type) {
      let self = this;
      //勾绘矢量图形的类
      this.draw = new Draw({
        //source代表勾绘的要素属于的数据集
        source: self.trailSource,
        //type 表示勾绘的要素包含的 geometry 类型
        type: type,
      });

      //绘制结束时触发的事件
      this.draw.on("drawend", function (e) {
        const geometry = e.feature.getGeometry();
        let pointArr = geometry.getCoordinates();
        self.coordinate.push(pointArr);
        utils.$emit("trailPoint", pointArr);
        self.pTrail.push(self.coordinate);
        self.coordinate = [];
        self.removeDraw();
      });
      self.map.addInteraction(this.draw);
    },
    //删除交互
    removeDraw() {
      this.map.removeInteraction(this.draw);
    },
    //添加轨迹线
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
    //生成路径（轨迹线展示）
    addLineMarker(arr) {
      var lineStyle = new Style({
        stroke: new Stroke({
          color: "red",
          width: 4,
        }),
      });
      for (let i = 0; i < arr.length; i++) {
        var marker = new Feature({
          type: "lineStyle",
          geometry: new LineString(arr[i]),
        });
        marker.setStyle(lineStyle);
        var line = new VectorLayer({
          source: new VectorSource({
            features: [marker],
          }),
        });
        this.map.addLayer(line);
      }
    },
    //生成密接范围
    createDiaPArea(arr, meters) {
      var line = turf.lineString(arr)
      var buffered=turf.buffer(line,meters,{units:'meters'})
      var format = new GeoJSON();
      var source = new VectorSource({ wrapX: false });
      // //读取geojson数据
      var lineFeature  = format.readFeature(line);
      var bufferFeature = format.readFeature(buffered);
      // //将数据添加数据源的
      source.addFeature(lineFeature);
      source.addFeature(bufferFeature);
      var test = new VectorLayer({ source: source })
      this.map.addLayer(test)
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
    addBuffer() {},
    testButtonClick() {
      console.log('test')
    },
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
#mapDiv .ol-custom-overviewmap,
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
