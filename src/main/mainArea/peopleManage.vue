<template>
  <div>
    <div align="left">
      <el-button @click="addLine" type="primary">新增</el-button>
    </div>
    <div>
      <el-table :data="db_p_info">
        <el-table-column
          property="id"
          label="序号"
          width="50"
        ></el-table-column>
        <el-table-column
          property="name"
          label="姓名"
          width="100"
        ></el-table-column>
        <el-table-column
          property="p_id"
          label="身份证"
          width="180"
        ></el-table-column>
        <el-table-column
          property="p_address"
          label="住址"
          width="300"
        ></el-table-column>
        <el-table-column
          property="x"
          label="经度"
          width="100"
        ></el-table-column>
        <el-table-column
          property="y"
          label="纬度"
          width="100"
        ></el-table-column>
        <el-table-column
          property="p_phone"
          label="联系方式"
          width="150"
        ></el-table-column>
        <el-table-column
          property="testData"
          label="核酸检测日期"
          width="150"
        ></el-table-column>
        <el-table-column
          property="testResult"
          label="结果"
          width="100"
        ></el-table-column>
        <el-table-column fixed="right"
        label="操作" width="145">
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

    <div>
      <el-dialog title="核酸人员录入" :visible.sync="new_p_input_vis">
        <el-form :model="new_p_form">
          <el-form-item label="序号" :label-width="p_form_width">
            <el-input v-model="new_p_form.id" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="姓名" :label-width="p_form_width">
            <el-input v-model="new_p_form.name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="身份证" :label-width="p_form_width">
            <el-input v-model="new_p_form.p_id" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="住址" :label-width="p_form_width">
            <el-input
              v-model="new_p_form.p_address"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="经度" :label-width="p_form_width">
            <el-input v-model="new_p_form.x" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="纬度" :label-width="p_form_width">
            <el-input v-model="new_p_form.y" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="联系方式" :label-width="p_form_width">
            <el-input
              v-model="new_p_form.p_phone"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="核酸检测日期" :label-width="p_form_width">
            <el-input
              v-model="new_p_form.testData"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="核酸结果" :label-width="p_form_width">
            <el-input
              v-model="new_p_form.testResult"
              auto-complete="off"
            ></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel_new_p_input">取 消</el-button>
          <el-button type="primary" @click="conf_new_p_input">确 定</el-button>
        </div>
      </el-dialog>
    </div>

    <div>
      <el-dialog title="核酸人员录入" :visible.sync="dialogFormVisible">
        <el-form :model="p_form">
          <el-form-item label="序号" :label-width="p_form_width">
            <el-input v-model="p_form.id" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="姓名" :label-width="p_form_width">
            <el-input v-model="p_form.name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="身份证" :label-width="p_form_width">
            <el-input v-model="p_form.p_id" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="住址" :label-width="p_form_width">
            <el-input v-model="p_form.p_address" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="经度" :label-width="p_form_width">
            <el-input v-model="p_form.x" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="纬度" :label-width="p_form_width">
            <el-input v-model="p_form.y" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="联系方式" :label-width="p_form_width">
            <el-input v-model="p_form.p_phone" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="核酸检测日期" :label-width="p_form_width">
            <el-input v-model="p_form.testData" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="核酸结果" :label-width="p_form_width">
            <el-input
              v-model="p_form.testResult"
              auto-complete="off"
            ></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel_p_input">取 消</el-button>
          <el-button type="primary" @click="conf_p_input">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      db_p_info: [
        {
          id: 1,
          name: "张三",
          p_id: "320410200104011234",
          p_address: "中国地质大学未来城校区",
          x: "114.624",
          y: "30.4634",
          p_phone: "12300001234",
          testData: "2022-04-01",
          testResult: "阴性",
        },
        {
          id: 2,
          name: "李四",
          p_id: "320410200104011234",
          p_address: "中国地质大学未来城校区",
          x: "114.624",
          y: "30.4634",
          p_phone: "12300001234",
          testData: "2022-04-01",
          testResult: "阴性",
        },
      ],
      new_p_input_vis: false,
      dialogFormVisible: false,
      p_form: {
        id: "",
        name: "",
        p_id: "",
        p_address: "",
        x: "",
        y: "",
        p_phone: "",
        testData: "",
        testResult: "",
      },
      new_p_form: {
        id: "",
        name: "",
        p_id: "",
        p_address: "",
        x: "",
        y: "",
        p_phone: "",
        testData: "",
        testResult: "",
      },
      p_form_width: "120px",
    };
  },
  methods: {
    addLine() {
      this.new_p_input_vis = true;
    },
    // 编辑
    handleEdit(index, row) {
      this.dialogFormVisible = true;
      this.p_form = Object.assign({}, row);
    },
    // 删除行
    handleDelete(index, row) {
      this.db_p_info.splice(index, 1);
    },
    cancel_p_input() {
      this.dialogFormVisible = false;
      this.p_form.id = "";
      this.p_form.name = "";
      this.p_form.p_id = "";
      this.p_form.p_address = "";
      this.p_form.x = "";
      this.p_form.y = "";
      this.p_form.p_phone = "";
      this.p_form.testData = "";
      this.p_form.testResult = "";
    },
    conf_p_input() {
      this.dialogFormVisible = false;
    },
    cancel_new_p_input() {
      this.new_p_input_vis = false;
      this.new_p_form.id = "";
      this.new_p_form.name = "";
      this.new_p_form.p_id = "";
      this.new_p_form.p_address = "";
      this.new_p_form.x = "";
      this.new_p_form.y = "";
      this.new_p_form.p_phone = "";
      this.new_p_form.testData = "";
      this.new_p_form.testResult = "";
    },
    conf_new_p_input() {
      let row = {
        id: this.new_p_form.id,
        name: this.new_p_form.name,
        p_id: this.new_p_form.p_id,
        p_address: this.new_p_form.p_address,
        x: this.new_p_form.x,
        y: this.new_p_form.y,
        p_phone: this.new_p_form.p_phone,
        testData: this.new_p_form.testData,
        testResult: this.new_p_form.testResult,
      };
      this.db_p_info.push(row);
      this.new_p_input_vis = false;
    },
  },
};
</script>

<style>
</style>