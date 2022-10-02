const { defineConfig } = require('@vue/cli-service')
module.exports ={
    devServer: {
        proxy: {
            //一个代理
            '/api/*': {    //请求前缀，加上代表走代理，不加不走
                target: 'http://127.0.0.1:8000',    // 代理目标的基础路径
                // 必须加的配置，重写路径，转发给代理时取消请求前缀，
                //'^/api'（正则表达式）表示匹配所有以'/api'开头的接口
                pathRewrite:{'^/api':"/"},
                ws: true,   //用于支持websocket,默认true
                //用于控制请求头中的host值，默认true，
                //为true时，服务器收到请求头中的host为：localhost:5000，
                //为false时，服务器收到请求头中的host为：localhost:8080，
                changeOrigin: true
            },
        }
    },
    transpileDependencies: true,
    lintOnSave:false
}
