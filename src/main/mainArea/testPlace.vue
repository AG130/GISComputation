<template>
    <div>
        <div>
            <el-dialog title="新增核酸采样点" :visible.sync="new_tP_vis">
                <el-form :model="new_tP_form">
                    <el-form-item label="序号" :label-width="new_tP_form_width">
                        <el-input v-model="new_tP_form.t_id" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="名称" :label-width="new_tP_form_width">
                        <el-input v-model="new_tP_form.t_name" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="地址" :label-width="new_tP_form_width">
                        <el-input v-model="new_tP_form.t_address" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="经度" :label-width="new_tP_form_width">
                        <el-input v-model="new_tP_form.x" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="纬度" :label-width="new_tP_form_width">
                        <el-input v-model="new_tP_form.y" auto-complete="off"></el-input>
                    </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <el-button @click="cancel_tp_input">取消</el-button>
                    <el-button type="primary" @click="conf_tp_input">确认</el-button>
                </div>
            </el-dialog>
        </div>
        <div align="left">
            <el-button @click="addLine" type="primary">新增空白行</el-button>
        </div>
        <div>
            <el-table :data="testPlace">
                <el-table-column prop="t_id" label="序号" width="50"></el-table-column>
                <el-table-column prop="t_name" label="名称" width="200"></el-table-column>
                <el-table-column prop="t_address" label="地址" width="300"></el-table-column>
                <el-table-column prop="x" label="经度" width="200"></el-table-column>
                <el-table-column prop="y" label="纬度" width="200"></el-table-column>
                <el-table-column label="操作">
                    <template slot-scope="scope">
                        <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                        <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            testPlace:[
                {
                    t_id:'1',
                    t_name:'地大核酸采样点',
                    t_address:"未来城体育馆",
                    x:'114.627855',
                    y:'30.464929'
                }
            ],
            new_tP_form:{
                t_id:'',
                t_name:'',
                t_address:"",
                x:'',
                y:''
            },
            new_tP_form_width:"120px",
            new_tP_vis:false,
        }
    },
    methods:{
        addLine(){
            let row={
                t_id:'',
                t_name:'',
                t_address:'',
                x:"",
                y:""
            }
            this.testPlace.push(row)
        },
        handleEdit(index, row) {
            this.new_tP_vis=true;
            this.new_tP_form = Object.assign({},row);
        },
        handleDelete(index, row) {
            this.testPlace.splice(index, 1)
        },
        cancel_tp_input(){
            this.new_tP_vis=false;
            this.testPlace.t_id=""
            this.testPlace.t_name=""
            this.testPlace.t_address=""
            this.testPlace.x=""
            this.testPlace.y=""
        },
        conf_tp_input(){
            this.new_tP_vis=false
        }
    }
}
</script>

<style>

</style>