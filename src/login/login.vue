<template>
  <div class="login-register">
    <div class="contain">
      <div class="big-box" :class="{ active: isLogin }">
        <div class="big-contain" key="bigContainLogin" v-if="isLogin">
          <div class="btitle">账户登录</div>
          <div class="bform">
            <input type="email" placeholder="用户名" v-model="form.useremail" />
            <span class="errTips" v-if="eEmpty">* 邮箱不能为空！ *</span>
            <input type="password" placeholder="密码" v-model="form.userpwd" />
            <span class="errTips" v-if="pEmpty">* 密码不能为空！ *</span>
          </div>
          <button class="bbutton" @click="login">登录</button>
        </div>
        <div class="big-contain" key="bigContainRegister" v-else>
          <div class="btitle">创建账户</div>
          <div class="bform">
            <input type="text" placeholder="用户名" v-model="form.username" />
            <input type="email" placeholder="邮箱" v-model="form.useremail" />
            <span class="errTips" v-if="existed">* 该邮箱已被使用！ *</span>
            <input type="password" placeholder="密码" v-model="form.userpwd" />
          </div>
          <button class="bbutton" @click="register">注册</button>
        </div>
      </div>
      <div class="small-box" :class="{ active: isLogin }">
        <div class="small-contain" key="smallContainRegister" v-if="isLogin">
          <div class="stitle">核酸检测</div>
          <p class="scontent">一个都不能少!</p>
          <button class="sbutton" @click="changeType">注册</button>
        </div>
        <div class="small-contain" key="smallContainLogin" v-else>
          <div class="stitle">已有账户？</div>
          <p class="scontent">登录查看核酸状态!</p>
          <button class="sbutton" @click="changeType">登录</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login-register",
  data() {
    return {
      isLogin: true,
      eEmpty: false,
      pEmpty: false,
      existed: false,
      form: {
        username: "",
        useremail: "",
        userpwd: "",
      },
    };
  },
  methods: {
    changeType() {
      this.isLogin = !this.isLogin;
      this.form.username = "";
      this.form.useremail = "";
      this.form.userpwd = "";
    },
    login() {
      const that = this;
      if (that.form.useremail != "" && that.form.userpwd != "") {
        that.eEmpty = false;
        that.pEmpty = false;

        $.ajax({
          url: "/api/index.html/",
          type: "GET",
          dataType: "json",
          data: { username: that.form.useremail, password: that.form.userpwd },

          success: function (dat) {
            var jsonData = JSON.stringify(dat); // 转成JSON格式
            if (dat.result == "success") {
              window.sessionStorage.setItem("isLogin", "true"); //登陆成功
              that.$router.push({
                name: "main",
                params: { username: that.form.useremail },
              });
            } else {
              that.$message.error("账号或密码错误！");
            }
          },
        });
      } else if (that.form.useremail == "" && that.form.userpwd == "") {
        that.eEmpty = true;
        that.pEmpty = true;
      } else if (that.form.useremail == "") {
        that.eEmpty = true;
        that.pEmpty = false;
      } else {
        that.eEmpty = false;
        that.pEmpty = true;
      }
    },

    register() {
      const that = this;
      if (
        that.form.username != "" &&
        that.form.useremail != "" &&
        that.form.userpwd != ""
      ) {
        //ajax register
        $.ajax({
          url: "/api/register.html/",
          type: "GET",
          dataType: "json",
          data: {
            username: that.form.username,
            useremail: that.form.useremail,
            password: that.form.userpwd,
          },

          success: function (dat) {
            var jsonData = JSON.stringify(dat); // 转成JSON格式
            // alert(jsonData);
            alert(dat.result);

            if (dat.result == "可以注册") {
              window.sessionStorage.setItem("isLogin", "true"); //登陆成功
              that.$router.push({
                name: "main",
                params: { username: that.form.useremail },
              });
            } else {
              alert("用户名已存在或其它问题");
            }
          },
        });
      } else {
        alert("填写不能为空！");
      }
    },
  },
};
</script>

<style scoped>
.login-register {
  width: 100vw;
  height: 100vh;
  box-sizing: border-box;
}

.contain {
  width: 60%;
  height: 60%;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 0 3px #f0f0f0, 0 0 6px #f0f0f0;
}

.big-box {
  width: 70%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 30%;
  transform: translateX(0%);
  transition: all 1s;
}

.big-contain {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.btitle {
  font-size: 1.5em;
  font-weight: bold;
  color: rgb(57, 167, 176);
}

.bform {
  width: 100%;
  height: 40%;
  padding: 2em 0;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.bform .errTips {
  display: block;
  width: 50%;
  text-align: left;
  color: red;
  font-size: 0.7em;
  margin-left: 1em;
}

.bform input {
  width: 50%;
  height: 30px;
  border: none;
  outline: none;
  border-radius: 10px;
  padding-left: 2em;
  background-color: #f0f0f0;
}

.bbutton {
  width: 20%;
  height: 40px;
  border-radius: 24px;
  border: none;
  outline: none;
  background-color: rgb(57, 167, 176);
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}

.small-box {
  width: 30%;
  height: 100%;
  background: linear-gradient(135deg, rgb(57, 167, 176), rgb(56, 183, 145));
  position: absolute;
  top: 0;
  left: 0;
  transform: translateX(0%);
  transition: all 1s;
  border-top-left-radius: inherit;
  border-bottom-left-radius: inherit;
}

.small-contain {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.stitle {
  font-size: 1.5em;
  font-weight: bold;
  color: #fff;
}

.scontent {
  font-size: 0.8em;
  color: #fff;
  text-align: center;
  padding: 2em 4em;
  line-height: 1.7em;
}

.sbutton {
  width: 60%;
  height: 40px;
  border-radius: 24px;
  border: 1px solid #fff;
  outline: none;
  background-color: transparent;
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}

.big-box.active {
  left: 0;
  transition: all 0.5s;
}

.small-box.active {
  left: 100%;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  border-top-right-radius: inherit;
  border-bottom-right-radius: inherit;
  transform: translateX(-100%);
  transition: all 1s;
}
</style>