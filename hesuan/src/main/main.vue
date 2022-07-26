<template>
  <div>
    <div>
      <el-container>
        <el-aside width="200px">
          <div class="asideBand">核酸检测助手</div>
          <div class="personalInf"><PersonalInf ref="personalInf"/></div>
          <el-menu :default-openeds="['1']" background-color="#66ccff" active-text-color="white">
            <el-submenu index="1">
              <template v-slot:title>地图功能控件</template>
              <el-menu-item-group>
                <el-menu-item index="1-1">地图复位</el-menu-item>
                <el-menu-item index="1-2">地图定位</el-menu-item>
                <el-menu-item index="1-3">切换地理底图</el-menu-item>
                <el-menu-item index="1-4">鹰眼开关</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-container>
          <el-header>Header</el-header>
          <el-main>
            <div v-show="this.tab==0"><Map ref="map"/></div>
            <div v-show="this.tab==1"><PInfDetail ref="pInfDetail"/></div>
          </el-main>
        </el-container>
      </el-container>
    </div>
  </div>
</template>

<script>
import PersonalInf from './aside/personalInf.vue';
import Map from "./mainArea/map.vue";
import PInfDetail from "./mainArea/pInfDetail.vue";
export default {
  components: { Map, PersonalInf,PInfDetail },
  provide(){
    return{
      username:this.username,
      changeView:this.changeView,
    }
  },
  data(){
    return{
      username:this.$route.params.username,
      tab:0,
    }
  },
  methods:{
    changeView(id){
      this.tab=id;
    }
  }
};
</script>

<style scoped>
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #6cf;
  color: #333;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
}
.asideBand {
  font-size: large;
  height: 60px;
  line-height: 60px;
}
.personalInf{
  background-color:white;
  height: 200px;
}
</style>