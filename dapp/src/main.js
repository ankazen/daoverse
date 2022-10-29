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
    console.log('Complie', data)
    let compiler = data.compiler
    let contract = data.contract

    let sources = {}
    let source = ' '
    for (let f in data.contract.files) {
        let content = data.contract.files[f].content
        if (content.indexOf('contract') === -1) {
            continue
        }
        sources[f] = {content:data.contract.files[f].content};
        source = data.contract.files[f].content
    }

    let input = {
        language: 'Solidity',
        sources: sources
    }
    let optimize = 1;
    let result = compiler.compile(JSON.string, optimize);
    console.log(result);

    emitter.emit('ComplieDone', result)

    // BrowserSolc.loadVersion(this.version, function(compiler) {
    //             this.state = 'Compiling'
    //             console.log(this.contract)
                
    //         });
})



createApp(App).use(router).mount('#app')
