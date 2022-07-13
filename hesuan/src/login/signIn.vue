<template>
  <div>
    <div>
      <el-form
        ref="signInForm"
        :model="signInForm"
        :rules="signInRules"
        label-width="80px"
        class="login-box"
      >
        <h3 class="login-title">欢迎使用核酸采样助手</h3>
        <el-form-item label="用户名" prop="username">
          <el-input v-model="signInForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="signInForm.password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="confirmSignIn()">登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      signInForm: {
        username: "",
        password: "",
      },
      signInRules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
      },
    };
  },
  methods: {
    confirmSignIn() {
      this.$refs.signInForm.validate((valid) => {
        if (valid) {
          window.sessionStorage.setItem("isLogin", "true");
          this.$router.push({
            name: "main",
            params: { username: this.signInForm.username },
          });
        } else {
          alert("用户名、密码不能为空！");
          return false;
        }
      });
    },
  },
};
</script>

<style>
.login-box {
  background-image: url("../assets/image.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  width: 400px;
  margin: 200px auto;
  border: 1px solid #66ccff;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 0 30px #dcdfe6;
}

.login-title {
  text-align: center;
}
</style>