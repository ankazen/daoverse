import mitt from 'mitt';

let data = {
    name: '2222'
}

let userdata = {
    address: ''
}

const HOST = 'http://127.0.0.1:9000'
const emitter = mitt()



export {
    userdata,
    HOST,
    emitter
}