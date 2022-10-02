<template>
  <div>
    <div>
      <el-table
        :data="
          dia_form.slice((currentPage - 1) * pageSize, currentPage * pageSize)
        "
        border
        style="width: 100%"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column prop="name" label="姓名" width="85"></el-table-column>
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
          prop="n"
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
    <div>
      <el-dialog title="核酸人员录入" :visible.sync="newDiaPInput_vis">
        <el-form :model="newDIaP_form">
          <el-form-item label="序号" :label-width="form_width">
            <el-input v-model="newDIaP_form.id" auto-complete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel_new_p_input">取 消</el-button>
          <el-button type="primary" @click="conf_new_p_input">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      //人员轨迹表
      dia_form: [
        {
          name: "张三",
          p_id: "320410123412341234",
          dia_time: "2021-09-01",
          n: ["肉夹馍->", "车友驾校->", "胖哥面馆"],
        },
      ],
      //多选框
      multipleSelection: [],
      //新增人员窗口查看
      newDiaPInput_vis:false,
      //行宽
      form_width:"120px",
      //新增轨迹表
      newDIaP_form:{
        id:''
      },
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
      this.newDiaPInput_vis=true
    },
    // 删除行
    handleDelete(index, row) {
      this.$confirm('是否删除该人员轨迹？','提示',{
        confirmButtonText:'确定',
        cancelButtonText:'取消',
        type:'warning'
      }).then(()=>{
        this.dia_form.splice(index, 1);
      }).catch(()=>{
        this.$message({
          type:'info',
          message:'已取消删除'
        })
      })
    },

    toggleSelection(rows) {
      if (rows) {
        rows.forEach((row) => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
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