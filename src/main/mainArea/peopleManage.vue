<template>
  <div>
    <!-- 人员管理表格 -->
    <div>
      <el-table
        :data="
          db_p_info.slice((currentPage - 1) * pageSize, currentPage * pageSize)
        "
      >
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
        <el-table-column fixed="right" label="操作" width="145">
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
        <el-button @click="addNewPInfo" type="primary" size="mini"
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
          :total="db_p_info.length"
        >
        </el-pagination>
      </div>
    </div>
    <!-- 新增信息弹窗 -->
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
            <el-select v-model="new_p_form.testResult" placeholder="结果">
              <el-option
                v-for="i in testResult"
                :key="i.value"
                :label="i.label"
                :value="i.label"
              >
              </el-option
            ></el-select>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel_new_p_input">取 消</el-button>
          <el-button type="primary" @click="conf_new_p_input">确 定</el-button>
        </div>
      </el-dialog>
    </div>
    <!-- 修改信息弹窗 -->
    <div>
      <el-dialog title="核酸人员录入" :visible.sync="changePInfo_vis">
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
            <el-select v-model="p_form.testResult" placeholder="结果">
              <el-option
                v-for="i in testResult"
                :key="i.value"
                :label="i.label"
                :value="i.label"
              >
              </el-option
            ></el-select>
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
      //人员信息表
      db_p_info: [
      ],
      //新增信息窗口可视
      new_p_input_vis: false,
      //修改信息窗口可视
      changePInfo_vis: false,
      //修改行对应号
      changePInfo_row: 0,
      //新增人员信息
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
      //修改人员信息
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
      testResult: [
        {
          value: 0,
          label: "阴性",
        },
        {
          value: 1,
          label: "阳性",
        },
      ],
      //行宽
      p_form_width: "120px",
      //分页有关（start）
      currentPage: 1,
      pageSize: 10,
      total: 0,
      //分页有关（end）
    };
  },

  mounted() {
    this.people_input();
  },

  methods: {
    //人员信息表初始化
    people_input(){
      this.db_p_info=[]
      const self=this;
      $.ajax({
        url: '/api/all_post_type_value/',
        type: 'GET',
        dataType: 'json',
        data: {'type': "id", 'value': "1"},

        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          for (var i=0;i<dat.result.data.length;i++) {
            var will_append={
              id:dat.result.data[i].id,
              name:dat.result.data[i].name,
              p_id:dat.result.data[i].id_card,
              p_address:dat.result.data[i].address,
              x:dat.result.data[i].lon,
              y:dat.result.data[i].lat,
              p_phone:dat.result.data[i].phone,
              testData:dat.result.data[i].checkdata,
              testResult:dat.result.data[i].result,


            }
            self.db_p_info.push(will_append)
          }
        },
        error: function () {
          alert('服务器超时，请重试！');
        }
      })
    },
    //新增人员信息
    addNewPInfo() {
      this.new_p_input_vis = true;
    },
    // 编辑
    handleEdit(index, row) {
      this.changePInfo_vis = true;
      this.p_form = Object.assign({}, row);
      this.changePInfo_row = row;
    },
    // 删除行
    handleDelete(index, row) {
      const selfff=this;
      $.ajax({
        url: '/api/delete_from_db/',
        type: 'GET',
        dataType: 'json',
        data: {'value': selfff.db_p_info[index].p_id},

        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          alert("删除成功")
        }
      })

      this.db_p_info.splice(index, 1);
    },
    //取消修改
    cancel_p_input() {
      this.changePInfo_vis = false;
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
    //确认修改
    conf_p_input() {
      //依据changePInfo_row(即id)修改数据库中对应内容
      //用户所填内容存于p_form中

      $.ajax({
        url: '/api/change_from_db/',
        type: 'GET',
        dataType: 'json',
        data: {'id': this.p_form.id, 'type': "name", 'value': this.p_form.name},

        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          // alert(jsonData);
          // alert(dat.result);

        }
      })

      $.ajax({
        url: '/api/change_from_db/',
        type: 'GET',
        dataType: 'json',
        data: {'id': this.p_form.id, 'type': "id_card", 'value': this.p_form.p_id},

        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          // alert(jsonData);
          // alert(dat.result);

        }
      })

      $.ajax({
        url: '/api/change_from_db/',
        type: 'GET',
        dataType: 'json',
        data: {'id': this.p_form.id, 'type': "address", 'value': this.p_form.p_address},

        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          // alert(jsonData);
          // alert(dat.result);

        }
      })

      $.ajax({
        url: '/api/change_from_db/',
        type: 'GET',
        dataType: 'json',
        data: {'id': this.p_form.id, 'type': "lon", 'value': this.p_form.x},

        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          // alert(jsonData);
          // alert(dat.result);

        }
      })

      $.ajax({
        url: '/api/change_from_db/',
        type: 'GET',
        dataType: 'json',
        data: {'id': this.p_form.id, 'type': "lat", 'value': this.p_form.y},

        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          // alert(jsonData);
          // alert(dat.result);

        }
      })

      $.ajax({
        url: '/api/change_from_db/',
        type: 'GET',
        dataType: 'json',
        data: {'id': this.p_form.id, 'type': "phone", 'value': this.p_form.p_phone},

        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          // alert(jsonData);
          // alert(dat.result);

        }
      })

      $.ajax({
        url: '/api/change_from_db/',
        type: 'GET',
        dataType: 'json',
        data: {'id': this.p_form.id, 'type': "checkdata", 'value': this.p_form.testData},

        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          // alert(jsonData);
          // alert(dat.result);

        }
      })

      $.ajax({
        url: '/api/change_from_db/',
        type: 'GET',
        dataType: 'json',
        data: {'id': this.p_form.id, 'type': "result", 'value': this.p_form.testResult},

        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          // alert(jsonData);
          // alert(dat.result);

        }
      })

      this.changePInfo_vis = false;

    },
    //取消新增
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
    //确认新增
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

      $.ajax({
        url: '/api/add_to_db/',
        type: 'GET',
        dataType: 'json',
        data: {'value':
              [
                {'name': row.name, 'sex': ' ',
                  'id_card': row.p_id, 'checkdata': row.testData,
                  'result': row.testResult, 'responsibilityman': ' ',
                  'lon': row.x, 'lat': row.y ,'phone':row.p_phone,
                  'address':row.p_address},
              ]
        }

        ,
        success: function (dat) {
          var jsonData = JSON.stringify(dat);// 转成JSON格式
          alert("success")
        },

      })

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