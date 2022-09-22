<template>
  <div>
    <div>
      <el-container>
        <!-- 侧边栏 -->
        <el-aside width="200px">
          <div class="asideBand">核酸检测助手</div>
          <div class="personalInf"><PersonalInf ref="personalInf" /></div>
          <el-menu background-color="#66ccff" active-text-color="white">
            <el-submenu index="1">
              <template v-slot:title>地图功能控件</template>
              <el-menu-item-group>
                <el-menu-item index="1-1" @click="showMap"
                  >地图展示</el-menu-item
                >
                <el-menu-item index="1-2" @click="resetMap"
                  >地图复位</el-menu-item
                >
                <el-menu-item index="1-3" @click="showLocatePlace"
                  >地图定位</el-menu-item
                >
                <el-menu-item index="1-4" @click="chooseMap"
                  >切换地图</el-menu-item
                >
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
                <el-menu-item index="4-2" @click="testPlaceM"
                  >采样点管理</el-menu-item
                >
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-aside>
        <!-- 主页面 -->
        <el-container>
          <!-- 标头 -->
          <el-header>Header</el-header>
          <!-- 显示区域 -->
          <el-main>
            <div v-show="this.tab == 0">
              <Map ref="map" @sendCood="getCood" />
            </div>
            <div v-show="this.tab == 1"><PInfDetail ref="pInfDetail" /></div>
            <div v-show="this.tab == 2">
              <PeopleManage ref="peopleManage" />
            </div>
            <div v-show="this.tab == 3"><DiagnoseP ref="diagnoseP" /></div>
            <div v-show="this.tab == 4"><TestPlace ref="testPlace" /></div>
          </el-main>
        </el-container>
      </el-container>
    </div>
    <!-- 弹窗 -->
    <div>
      <!-- 地图定位 -->
      <div>
        <el-dialog
          title="地图跳转选择"
          :visible.sync="locatePlace_vis"
          :height="'50px'"
        >
          <div style="text-align: left">
            <h3>快速定位</h3>
            <el-button @click="locatePlace(0)">洪山区</el-button>
            <el-button @click="locatePlace(1)">东湖高新区</el-button>
            <el-button @click="locatePlace(2)">南望山校区</el-button>
            <el-button @click="locatePlace(3)">未来城校区</el-button>
          </div>
          <div style="text-align: left">
            <h3>经纬度定位</h3>
            <span>当前经纬度为：{{ map_center[0] }},{{ map_center[1] }}</span>
            <el-form :model="locatePlace_form">
              <el-form-item label="请输入经度" :label-width="'85px'">
                <el-input
                  v-model="locatePlace_form.x"
                  autocomplete="off"
                ></el-input>
              </el-form-item>
              <el-form-item label="请输入纬度" :label-width="'85px'">
                <el-input
                  v-model="locatePlace_form.y"
                  autocomplete="off"
                ></el-input>
              </el-form-item>
            </el-form>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button @click="locatePlace_vis = false">取消</el-button>
            <el-button @click="locatePlace(10)" type="primary">确定</el-button>
          </div>
        </el-dialog>
      </div>
      <!-- 切换地理底图 -->
      <div>
        <el-dialog title="选择要展示的地图" :visible.sync="chooseMap_vis">
          <el-select v-model="chosenMap" placeholder="选择地图">
            <el-option
              v-for="map in choosedMap"
              :key="map.value"
              :label="map.label"
              :value="map.value"
            >
            </el-option>
          </el-select>
          <div slot="footer" class="dialog-footer">
            <el-button @click="chooseMap_vis = false">取消</el-button>
            <el-button @click="conf_chosenMap" type="primary">确定</el-button>
          </div>
        </el-dialog>
      </div>
      <!-- 未作核酸人员查询 -->
      <div>
        <el-dialog title="未检核酸人员查询" :visible.sync="p_s_vis">
          <el-form :model="p_s_form">
            <el-form-item label="连续未做核酸天数：" :label-width="p_s_width">
              <el-input v-model="p_s_form.data" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="p_s_vis = false">取消</el-button>
            <el-button @click="conf_p_s" type="primary">确定</el-button>
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
  components: {
    Map,
    PersonalInf,
    PInfDetail,
    PeopleManage,
    DiagnoseP,
    TestPlace,
  },
  provide() {
    return {
      username: this.username,
      changeView: this.changeView,
      locatePlace_form: this.locatePlace_form,
    };
  },
  data() {
    return {
      //用户名
      username: this.$route.params.username,
      //页面代码
      tab: 0,
      //定位窗口显示
      locatePlace_vis: false,
      //定位数据表单
      locatePlace_form: {
        x: "",
        y: "",
      },
      //地图中心点
      map_center: "",
      //地图切换窗口展示
      chooseMap_vis: false,
      //地图待选
      choosedMap: [
        {
          value: 0,
          label: "OSM地图",
        },
        {
          value: 1,
          label: "天地图矢量地图",
        },
        {
          value: 2,
          label: "天地图影像地图",
        },
      ],
      //选定地图
      chosenMap: "",
      //核酸人员搜索可视化
      p_s_vis: false,
      //核酸人员搜索参数表单
      p_s_form: {
        data: "",
      },
      //行宽
      p_s_width: "150px",
    };
  },
  methods: {
    //改变主页面显示
    changeView(id) {
      this.tab = id;
    },
    //地图功能控件->地图展示
    showMap() {
      this.tab = 0;
    },
    //地图功能控件->地图复位
    resetMap() {
      this.$refs.map.resetMap();
    },
    //地图功能控件->地图定位->显示表单
    showLocatePlace() {
      this.$refs.map.sendCood();
      this.locatePlace_vis = true;
    },
    //地图功能控件->地图定位->定位区域
    locatePlace(id) {
      this.$refs.map.locatePlace(id);
      this.locatePlace_vis = false;
      this.locatePlace_form.x = "";
      this.locatePlace_form.y = "";
    },
    //地图功能控件->地图定位->展示当前地图中心点
    getCood(msg) {
      this.map_center = msg;
    },
    //地图功能控件->地图定位->显示地图切换窗口
    chooseMap() {
      this.chooseMap_vis = true;
    },
    //地图功能控件->地图定位->地图切换
    conf_chosenMap() {
      this.$refs.map.changeMap(this.chosenMap)
      this.chooseMap_vis=false
    },
    //核酸人员管理->人员录入
    peopleManage() {
      this.tab = 2;
    },
    //核酸人员管理->未检核酸人员查询
    showSearchPeople() {
      if (this.tab != 0) {
        this.tab = 0;
        this.p_s_vis = true;
      } else {
        this.p_s_vis = true;
      }
    },
    //轨迹分析->阳性轨迹点展示
    showDiagnoseP() {
      this.tab = 3;
    },
    //核酸采样辅助->采样点管理
    testPlaceM() {
      this.tab = 4;
    },
    //核酸人员管理->未检核酸人员查询->确认查询
    conf_p_s() {
      // 查询未检核酸人员
      alert("查询完成");
    },
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