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


createApp(App).use(router).mount('#app')
