<template>
  <div>
    <div>
      <el-table
        :data="
          dia_form.slice((currentPage - 1) * pageSize, currentPage * pageSize)
        "
        border
        style="width: 100%"
        ref="dia_table"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column
          prop="id"
          label="序号"
          width="50"
        ></el-table-column>
        <el-table-column
          prop="p_name"
          label="姓名"
          width="85"
        ></el-table-column>
        <el-table-column
          prop="p_id"
          label="身份证"
          width="180"
          align="center"
        ></el-table-column>
        <el-table-column
          prop="dia_time"
          label="确诊时间"
          width="150"
          align="center"
        ></el-table-column>
        <el-table-column
          prop="dia_trail"
          label="轨迹路径"
          align="center"
        ></el-table-column>
        <el-table-column fixed="right" label="操作" width="145" align="center">
          <template slot-scope="scope">
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
        <el-button @click="addNewDiaP" type="primary" size="mini"
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
          :total="dia_form.length"
        >
        </el-pagination>
      </div>
    </div>
    <!-- 新增信息弹窗 -->
    <div ref="newDiaP">
      <el-dialog title="核酸人员录入" :visible.sync="newDiaPInput_vis">
        <el-form :model="newDIaP_form">
          <el-form-item label="序号" :label-width="form_width">
            <el-input
              v-model="newDIaP_form.id"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="姓名" :label-width="form_width">
            <el-input
              v-model="newDIaP_form.p_name"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="身份证" :label-width="form_width">
            <el-input
              v-model="newDIaP_form.p_id"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="确诊时间" :label-width="form_width">
            <el-input
              v-model="newDIaP_form.dia_time"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="轨迹路径" :label-width="form_width">
            <el-input
              v-model="newDIaP_form.dia_trail"
              auto-complete="off"
              placeholder="请填写人员行动轨迹"
            ></el-input>
            <div align="right">
              <el-input
                type="textarea"
                :autosize="{ minRows: 2 }"
                placeholder="轨迹线坐标将自动匹配到此处"
                :disabled="true"
                v-model="dia_trail_xy"
              ></el-input>
              <el-button type="primary" @click="chooseTrailPoint"
                >选取轨迹线</el-button
              >
            </div>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel_DiaP_input">取 消</el-button>
          <el-button type="primary" @click="conf_DiaP_input">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import utils from "@/utils";
export default {
  inject: ["changeView", "chooseTrail"],
  mounted() {
    var that = this;
    utils.$on("trailPoint", (data) => {
      that.dia_trail_xy = data;
    });
  },
  data() {
    return {
      //人员轨迹表
      dia_form: [
        {
          id:'1',
          p_name: "张三",
          p_id: "320410123412341234",
          dia_time: "2021-09-01",
          dia_trail: "肉夹馍->车友驾校->胖哥面馆",
        },
        {
          id:'2',
          p_name: "张三",
          p_id: "320410123412341234",
          dia_time: "2021-09-01",
          dia_trail: "肉夹馍->车友驾校->胖哥面馆",
        },
        {
          id:'3',
          p_name: "张三",
          p_id: "320410123412341234",
          dia_time: "2021-09-01",
          dia_trail: "肉夹馍->车友驾校->胖哥面馆",
        },
      ],
      //多选框
      multipleSelection: [],
      //新增人员窗口查看
      newDiaPInput_vis: false,
      //行宽
      form_width: "80px",
      //新增轨迹表
      newDIaP_form: {
        id:'',
        p_name: "",
        p_id: "",
        dia_time: "",
        dia_trail: "",
      },
      dia_trail_xy: "",
      //分页有关（start）
      currentPage: 1,
      pageSize: 10,
      total: 0,
      //分页有关（end）
    };
  },
  methods: {
    //新增阳性轨迹点
    addNewDiaP() {
      this.newDiaPInput_vis = true;
    },
    //选取路径轨迹点
    chooseTrailPoint() {
      this.changeView(0);
      this.chooseTrail();
    },
    //取消轨迹录入
    cancel_DiaP_input() {
      this.newDIaP_form.p_name = "";
      this.newDIaP_form.p_id = "";
      this.newDIaP_form.dia_time = "";
      this.dia_trail = "";
      this.dia_trail_xy = "";
      this.newDiaPInput_vis = false;
    },
    //确认轨迹输入
    conf_DiaP_input() {
      this.newDIaP_form.p_name = "";
      this.newDIaP_form.p_id = "";
      this.newDIaP_form.dia_time = "";
      this.dia_trail = "";
      this.dia_trail_xy = "";
      this.newDiaPInput_vis = false;
    },
    // 删除行
    handleDelete(index, row) {
      this.$confirm("是否删除该人员轨迹？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.dia_form.splice(index, 1);
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
    handleSelectionChange(val) {
      this.multipleSelection=val.map(item=>item.id)
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