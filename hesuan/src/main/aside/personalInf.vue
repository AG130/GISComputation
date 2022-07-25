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
      <el-avatar alt="更改头像" shape="square" :src="url" :size="100" fit="fill"></el-avatar>
    </div>
    <div class="usernameInf">
      <span>欢迎:{{username}}</span>
    </div>
    <div class="personalSelect">
      <div><i class="el-icon-user-solid"></i></div>
      <div><i class="el-icon-message"></i></div>
      <div><i class="el-icon-switch-button" @click="exitLogin"></i></div>
    </div>
  </div>
</template>

<script>
export default {
  inject:['username'],
  data() {
    return {
      url: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
      
    };
  },
  methods: {
    changeAvatar(e) {
      var file = e.target.files[0];
      var _this = this;
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = function () {
          var dataURL = reader.result;
          _this.url = dataURL;
      }
    },
    exitLogin(){
        this.$router.push({
            name:'login'
        })
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
}
.personalSelect {
  display: flex;
  justify-content: space-around;
  font-size: 30px;
  line-height: 60px;
}
.usernameInf{
height: 10px;
}
</style>