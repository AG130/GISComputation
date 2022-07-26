<template>
  <div class="container">
    <h3>个人信息完善</h3>
    <div>
      <el-form ref="pInfDetForm" :model="pInfDetForm" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="pInfDetForm.username"></el-input>
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="pInfDetForm.useremail"></el-input>
        </el-form-item>
        <el-form-item label="联系电话">
          <el-input v-model="pInfDetForm.userphone"></el-input>
        </el-form-item>
      </el-form>
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
      },
    };
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  height: 100%;
}
</style>