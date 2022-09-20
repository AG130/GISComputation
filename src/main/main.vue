<template>
  <div>
    <div>
      <el-container>
        <el-aside width="200px">
          <div class="asideBand">核酸检测助手</div>
          <div class="personalInf"><PersonalInf ref="personalInf" /></div>
          <el-menu
            background-color="#66ccff"
            active-text-color="white"
          >
            <el-submenu index="1">
              <template v-slot:title>地图功能控件</template>
              <el-menu-item-group>
                <el-menu-item index="1-1" @click="showMap"
                  >地图展示</el-menu-item
                >
                <el-menu-item index="1-2">地图复位</el-menu-item>
                <el-menu-item index="1-3">地图定位</el-menu-item>
                <el-menu-item index="1-4">切换地理底图</el-menu-item>
                <el-menu-item index="1-5">鹰眼开关</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
              <template v-slot:title>核酸人员管理</template>
              <el-menu-item-group>
                <el-menu-item index="2-1" @click="peopleManage"
                  >人员录入</el-menu-item
                >
                <el-menu-item index="2-2" @click="showSearchPeople"
                  >未检核酸人员查询</el-menu-item
                >
                <el-menu-item index="2-3">人员导出</el-menu-item>
              </el-menu-item-group>
            </el-submenu>

            <el-submenu index="3">
              <template v-slot:title>轨迹分析</template>
              <el-menu-item-group>
                <el-menu-item index="3-1" @click="showDiagnoseP"
                  >阳性轨迹点</el-menu-item
                >
                <el-menu-item index="3-2">生成路径</el-menu-item>
                <el-menu-item index="3-3">密接区域范围</el-menu-item>
              </el-menu-item-group>
            </el-submenu>

            <el-submenu index="4">
              <template v-slot:title>核酸采样辅助</template>
              <el-menu-item-group>
                <el-menu-item index="4-1">现有采样点查询</el-menu-item>
                <el-menu-item index="4-2" @click="testPlaceM">采样点管理</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-container>
          <el-header>Header</el-header>
          <el-main>
            <div v-show="this.tab == 0"><Map ref="map" /></div>
            <div v-show="this.tab == 1"><PInfDetail ref="pInfDetail" /></div>
            <div v-show="this.tab == 2">
              <PeopleManage ref="peopleManage" />
            </div>
            <div v-show="this.tab == 3"><DiagnoseP ref="diagnoseP" /></div>
            <div v-show="this.tab==4"><TestPlace ref="testPlace"/></div>
          </el-main>
        </el-container>
      </el-container>
    </div>
    <div>
      <!-- 未作核酸人员查询 -->
      <div>
        <el-dialog title="未检核酸人员查询" :visible.sync="this.p_s_vis">
          <el-form :model="p_s_form">
            <el-form-item label="连续未做核酸天数：" :label-width="p_s_width">
              <el-input v-model="p_s_form.data" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="p_s_vis = false">取消</el-button>
            <el-button @click="conf_p_s">确定</el-button>
          </div>
        </el-dialog>
      </div>
    </div>
  </div>
</template>

<script>
import PersonalInf from "./aside/personalInf.vue";
import Map from "./mainArea/map.vue";
import PInfDetail from "./mainArea/pInfDetail.vue";
import PeopleManage from "./mainArea/peopleManage.vue";
import DiagnoseP from "./mainArea/diagnoseP.vue";
import TestPlace from "./mainArea/testPlace.vue";
export default {
  components: { Map, PersonalInf, PInfDetail, PeopleManage, DiagnoseP, TestPlace },
  provide() {
    return {
      username: this.username,
      changeView: this.changeView,
    };
  },
  data() {
    return {
      username: this.$route.params.username,
      tab: 0,
      p_s_vis: false,
      p_s_form: {
        data: "",
      },
      p_s_width:"150px",
    };
  },
  methods: {
    changeView(id) {
      this.tab = id;
    },
    showMap() {
      this.tab = 0;
    },
    peopleManage() {
      this.tab = 2;
    },
    showSearchPeople() {
      if (this.tab != 0) {
        this.tab = 0;
        this.p_s_vis = true;
      } else {
        this.p_s_vis = true;
      }
    },
    showDiagnoseP() {
      this.tab = 3;
    },
    testPlaceM(){
      this.tab = 4;
    },
    conf_p_s(){
      // 查询未检核酸人员
      alert("查询完成")
    }
  },
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
.personalInf {
  background-color: white;
  height: 200px;
}
</style>