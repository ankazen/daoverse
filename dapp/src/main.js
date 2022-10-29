import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import {emitter} from './global.js'
import {auth} from './daoverse_apis'

emitter.on('signer', data=>{
    console.log(data)
    auth({}, {identifier: data.data})
    .then(res=>{
    	console.log(res);
    	window.localStorage.setItem('token', res.data.token);
    })
})


emitter.on('Complie', data=>{
    let compiler = data.compiler
    let contract = data.contract

    let source = 'contract x { function g() {} }';
    let optimize = 1;
    let result = compiler.compile(source, optimize);
    console.log(result);

    emitter.emit('ComplieDone', result)

    // BrowserSolc.loadVersion(this.version, function(compiler) {
    //             this.state = 'Compiling'
    //             console.log(this.contract)
                
    //         });
})


createApp(App).use(router).mount('#app')
