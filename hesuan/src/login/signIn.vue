<template>
    <div>
        <el-form ref="loginform" :model="form" :rules="rules" label-width="80px" class="login-box">
            <h3 class="login-title">欢迎使用核酸检测助手</h3>
            <el-form-item label="用户名" prop="username">
                <el-input v-model="form.username"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm()">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    data(){
        return{
            form:{
                username:'',
                password:''
            }
        }
    },
    methods:{}
}
</script>

<style>
    .login-box{
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

    .login-title{
        text-align: center;
    }
</style>