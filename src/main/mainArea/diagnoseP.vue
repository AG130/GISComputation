<template>
  <div>
    <el-table :data="dia_form" border style="width: 100%">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="p_id" label="身份证"></el-table-column>
      <el-table-column prop="n1" label="路径1"></el-table-column>
      <el-table-column prop="n2" label="路径2"></el-table-column>
      <el-table-column prop="n3" label="路径3"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dia_form: [
        {
          name: "张三",
          p_id: "320410123412341234",
          n1: "肉夹馍",
          n2: "车友驾校",
          n3: "胖哥面馆",
        },
      ],
      multipleSelection:[]
    };
  },
  methods:{
    toggleSelection(rows){
        if(rows){
            rows.forEach(row => {
            this.$refs.multipleTable.toggleRowSelection(row);
          });
        } else{
            this.$refs.multipleTable.clearSelection();
        }
    },
    handleSelectionChange(val) {
        this.multipleSelection = val;
      }
  }
};
</script>

<style>
</style>