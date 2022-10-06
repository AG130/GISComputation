<template>
  <div>
    <div>
      <el-table
        :data="
          testPlace_form.slice(
            (currentPage - 1) * pageSize,
            currentPage * pageSize
          )
        "
        style="width: 100%"
      >
        <el-table-column prop="t_id" label="序号" width="50"></el-table-column>
        <el-table-column
          prop="t_name"
          label="名称"
          width="150"
        ></el-table-column>
        <el-table-column
          prop="t_address"
          label="地址"
          width="400"
        ></el-table-column>
        <el-table-column prop="x" label="经度" width="180"></el-table-column>
        <el-table-column prop="y" label="纬度" width="180"></el-table-column>
        <el-table-column label="操作" width="145" fixed="right">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
              >编辑</el-button
            >
            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>
    <!-- 分页实现 -->
    <div align="right" style="line-height: 22px">
      <div style="display: inline-block">
        <el-button @click="addNewTestPlace" type="primary" size="mini"
          >新增</el-button
        >
      </div>
      <div style="display: inline-block">
        <el-pagination
          style="margin: 10px 0px"
          background
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[1, 5, 10, 20, 40]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="testPlace_form.length"
        >
        </el-pagination>
      </div>
    </div>

    <div>
      <el-dialog title="新增核酸采样点" :visible.sync="newTPForm_vis">
        <el-form :model="new_tP_form">
          <el-form-item label="序号" :label-width="new_tP_form_width">
            <el-input v-model="new_tP_form.t_id" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="名称" :label-width="new_tP_form_width">
            <el-input
              v-model="new_tP_form.t_name"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="地址" :label-width="new_tP_form_width">
            <el-input
              v-model="new_tP_form.t_address"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="经纬度" :label-width="new_tP_form_width">
            <div align="right">
              <el-input
                type="textarea"
                :autosize="{ minRows: 2 }"
                placeholder="核酸检测点坐标将自动匹配到此处"
                :disabled="true"
                v-model="newTestP_xy"
              ></el-input>
              <el-button type="primary" @click="chooseNewTestP"
                >选取核酸检测点</el-button
              >
            </div>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel_newTP_input">取消</el-button>
          <el-button type="primary" @click="conf_newTP_input">确认</el-button>
        </div>
      </el-dialog>
    </div>

    <div>
      <el-dialog title="修改核酸采样点" :visible.sync="tpForm_vis">
        <el-form :model="tP_form">
          <el-form-item label="序号" :label-width="new_tP_form_width">
            <el-input v-model="tP_form.t_id" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="名称" :label-width="new_tP_form_width">
            <el-input v-model="tP_form.t_name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="地址" :label-width="new_tP_form_width">
            <el-input
              v-model="tP_form.t_address"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="经纬度" :label-width="new_tP_form_width">
            <div align="right">
              <el-input
                type="textarea"
                :autosize="{ minRows: 2 }"
                placeholder="核酸检测点坐标将自动匹配到此处"
                :disabled="true"
                v-model="newTestP_xy"
              ></el-input>
              <el-button type="primary" @click="chooseNewTestP"
                >选取核酸检测点</el-button
              >
            </div>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel_tp_input">取消</el-button>
          <el-button type="primary" @click="conf_tp_input">确认</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import utils from "@/utils";
export default {
  inject: ["changeView", "chooseNewTP"],
  mounted() {
    this.people_input()
    var that = this;
    utils.$on("newTestP", (data) => {
      that.newTestP_xy = data;
      that.new_tP_form.x = data[0];
      that.new_tP_form.y = data[1];
      that.tP_form.x = data[0];
      that.tP_form.y = data[1];
    });
  },
  data() {
    return {
      testPlace_form: [
      ],
      new_tP_form: {
        t_id: "",
        t_name: "",
        t_address: "",
        x: "",
        y: "",
      },
      newTestP_xy: "",
      new_tP_form_width: "60px",
      newTPForm_vis: false,
      tP_form: {
        t_id: "",
        t_name: "",
        t_address: "",
        x: "",
        y: "",
      },
      tpForm_vis: false,
      //分页有关（start）
      currentPage: 1,
      pageSize: 10,
      total: 0,
      //分页有关（end）
    };
  },
  methods: {
    people_input(){
      this.testPlace_form=[]
      const self=this;
      $.ajax({
        url: '/api/explore_all_check_point/',
        type: 'GET',
        dataType: 'json',
        data: {'type': "id", 'value': "1"},
        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          for (var i=0;i<dat.result.data.length;i++) {
            var will_append={
              t_id:dat.result.data[i].point_id,
              t_name:dat.result.data[i].point_name,
              t_address:dat.result.data[i].poind_address,
              x:dat.result.data[i].locate_x_float,
              y:dat.result.data[i].locate_y_float,
            }
            self.testPlace_form.push(will_append)
          }
        },
        error: function () {
          alert('服务器超时，请重试！');
        }
      })
    },

    //新增核酸检测点
    addNewTestPlace() {
      this.newTestP_xy=[]
      this.newTPForm_vis = true;
    },
    //选取新检测点
    chooseNewTestP() {
      this.changeView(0);
      this.chooseNewTP();
    },
    //编辑
    handleEdit(index, row) {
      this.tpForm_vis = true;
      this.tP_form = Object.assign({}, row);
      this.newTestP_xy =
        [this.testPlace_form[index].x , this.testPlace_form[index].y]
      utils.$emit("index", index);
    },
    //删除
    handleDelete(index, row) {
      const selfff=this;
      $.ajax({
        url: '/api/del_check_point/',
        type: 'GET',
        dataType: 'json',
        data: {'point_id': selfff.testPlace_form[index].t_id},
        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
        }
      })
      this.$notify({
            title:'成功',
            type:'success',
            message:'已删除该采样点'
          })
      this.testPlace_form.splice(index, 1);
    },
    //取消修改
    cancel_tp_input() {
      this.tP_form.t_id = "";
      this.tP_form.t_name = "";
      this.tP_form.t_address = "";
      this.tP_form.x = "";
      this.tP_form.y = "";
      this.tpForm_vis = false;
    },
    //确认修改
    conf_tp_input() {
      this.testPlace_form[this.tP_form.t_id - 1].x = this.tP_form.x;
      this.testPlace_form[this.tP_form.t_id - 1].y = this.tP_form.y;

      this.tpForm_vis = false;
    },
    //取消新增
    cancel_newTP_input() {
      this.new_tP_form.t_id = "";
      this.new_tP_form.t_name = "";
      this.new_tP_form.t_address = "";
      this.new_tP_form.x = "";
      this.new_tP_form.y = "";
      this.newTPForm_vis = false;
    },
    //确认新增
    conf_newTP_input() {
      let newTp = {
        t_id:this.new_tP_form.t_id,
        t_name:this.new_tP_form.t_name,
        t_address:this.new_tP_form.t_address,
        x:this.new_tP_form.x,
        y:this.new_tP_form.y
      }
      const selffff=this;
      $.ajax({
        url: '/api/add_check_point/',
        type: 'GET',
        dataType: 'json',
        // traditional: true,
        data: {'point_id': selffff.new_tP_form.t_id,
          'point_name':selffff.new_tP_form.t_name,
          'poind_address':selffff.new_tP_form.t_address,
          'locate_x_float':selffff.new_tP_form.x,
          'locate_y_float':selffff.new_tP_form.y,
        },
        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
        }
      })
      this.$notify({
            title:'成功',
            type:'success',
            message:'已添加新采样点'
          })
      this.testPlace_form.push(newTp)
      this.newTPForm_vis = false;

    },
    //分页有关（start）
    handleSizeChange(size) {
      this.pageSize = size;
    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;
    },
    //分页有关（end）
  },
};
</script>

<style>
</style>