<template>
  <div class="container">
    <h3>个人信息完善</h3>
    <div class="formCss">
      <div>
      <span>用户名</span><br>
      <el-input v-model="pInfDetForm.username" style="width:220px"></el-input>
      </div>
            <div>
      <span>邮箱</span><br>
      <el-input v-model="pInfDetForm.useremail" style="width:220px"></el-input>
      </div>
            <div>
      <span>联系电话</span><br>
      <el-input v-model="pInfDetForm.userphone" style="width:220px"></el-input>
      </div>
      <div>
      <span>所在城市</span><br>
      <el-cascader v-model="pInfDetForm.usercity" :options="cityList"></el-cascader>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pInfDetForm: {
        username: "",
        useremail: "",
        userphone: "",
        usercity: "",
      },
      cityList:[{
        value:'BeiJing',
        label:'北京'
      },{
        value:'ShangHai',
        label:'上海'
      }]
    };
  },
};
</script>

<style scoped>
.container {
  width: 500px;
  height: 100%;
  margin-left: 300px;
}
.formCss{
  text-align: left;
}
</style>