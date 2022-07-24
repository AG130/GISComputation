<template>
  <div>
    <div>
      <el-container>
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
          <el-menu :default-openeds="['1']">
            <el-submenu index="1">
              <template slot="title">地图功能控件</template>
              <el-menu-item-group>
                <el-menu-item index="1-1">地图复位</el-menu-item>
                <el-menu-item index="1-2">地图定位</el-menu-item>
                <el-menu-item index="1-3">切换地理底图</el-menu-item>
                <el-menu-item index="1-3">鹰眼开关</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-container>
          <el-header>Header</el-header>
          <el-main>
            <Map ref="map"></Map>
          </el-main>
        </el-container>
      </el-container>
    </div>
  </div>
</template>

<script>
import Map from "./mapArea/map.vue";
export default {
  components: { Map },
};
</script>

<style>
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}
</style>