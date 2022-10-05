<template>
  <div>
    <div class="user-header">
      <input
        type="file"
        name="image"
        accept="image/*"
        @change="changeAvatar"
        class="header-upload-btn user-header-com"
      />
      <el-avatar
        alt="更改头像"
        shape="square"
        :src="url"
        :size="100"
        fit="fill"
      ></el-avatar>
    </div>
    <div class="usernameInf">
      <span>欢迎:{{ username }}</span>
    </div>
    <div class="personalSelect">
      <!-- <div class="clickCss" @click="showPInfDetail">
        <div>
          <i class="el-icon-user-solid"></i>
        </div>
        <div class="inf">个人信息</div>
      </div> -->
      <div class="clickCss" @click="exitLoginConf">
        <div>
          <i class="el-icon-switch-button"></i>
        </div>
        <div class="inf">退出登录</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  inject: ["username", "changeView"],
  data() {
    return {
      url: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
    };
  },
  methods: {
    changeAvatar(e) {
      var file = e.target.files[0];
      var that = this;
      var reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onloadend = function () {
        var dataURL = reader.result;
        that.url = dataURL;
      };
    },
    showPInfDetail() {
      this.changeView("1");
    },
    exitLogin() {
      window.sessionStorage.clear();
      this.$router.replace("/login")
    },
    exitLoginConf(){
       this.$confirm('确定退出登录吗?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(action => {
          if (action == 'confirm') {
            this.exitLogin()
          }
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消退出'
          });          
        });
    }
  },
};
</script>

<style scoped>
.user-header {
  position: relative;
  display: inline-block;
}
.user-header-com {
  width: 100px;
  height: 100px;
  display: inline-block;
}
.header-upload-btn {
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
  /* 通过定位把input放在img标签上面，通过不透明度隐藏 */
  cursor:pointer;
}
.personalSelect {
  display: flex;
  justify-content: space-around;
  font-size: 30px;
  line-height: 60px;
}
.usernameInf {
  height: 10px;
  font-size: 10px;
}
.clickCss{
cursor: pointer;
}
.inf {
  height: 10px;
  font-size: 10px;
  line-height: 10px;
}
</style>