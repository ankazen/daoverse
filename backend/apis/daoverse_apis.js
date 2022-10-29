import axios from 'axios';

var BaseUrl = 'http://127.0.0.1:9000';


function getCookie(cname) {
      var name = cname + "=";
      var ca = document.cookie.split(';');
      for(var i=0; i<ca.length; i++)
      {
        var c = ca[i].trim();
        if (c.indexOf(name)==0) return c.substring(name.length,c.length);
      }
      return "";
}


function gettoken() {
    let token = window.localStorage.getItem('token');
    if (!token) {
      return null;
    }
    return token;
}

function request(url, method, args, data) {
    const _url = BaseUrl + url
    const header = {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + gettoken()
    }
    return new Promise((resolve, reject) => {
        axios({
            method: method,
            url: _url,
            params: args,
            data: data,
            headers: header,
        }).then(res => {
            resolve(res.data)
        }).catch(err => {
            reject(err)
        })
    })
}



export function unionapply_create(args, data) {
    return request("/api/unionapply", 'post', args, data)
}


export function unoincontract_findOne(pk, args, data) {
    return request("/api/unoincontract/"+pk, 'get', args, data)
}


export function auth(args, data) {
    return request("/api/auth", 'post', args, data)
}


export function unoincontract_find(args, data) {
    return request("/api/unoincontract", 'get', args, data)
}


export function user_find(args, data) {
    return request("/api/user", 'get', args, data)
}


export function contract_find(args, data) {
    return request("/api/contract", 'get', args, data)
}


export function contract_findOne(pk, args, data) {
    return request("/api/contract/"+pk, 'get', args, data)
}


export function union_find(args, data) {
    return request("/api/union", 'get', args, data)
}


export function unionapply_find(args, data) {
    return request("/api/unionapply", 'get', args, data)
}


export function union_findOne(pk, args, data) {
    return request("/api/union/"+pk, 'get', args, data)
}


export function contract_create(args, data) {
    return request("/api/contract", 'post', args, data)
}


export function unionuser_find(args, data) {
    return request("/api/unionuser", 'get', args, data)
}


export function unoincontract_create(args, data) {
    return request("/api/unoincontract", 'post', args, data)
}


export function union_create(args, data) {
    return request("/api/union", 'post', args, data)
}


export function unionuser_create(args, data) {
    return request("/api/unionuser", 'post', args, data)
}


export function user_create(args, data) {
    return request("/api/user", 'post', args, data)
}


export function user_findOne(pk, args, data) {
    return request("/api/user/"+pk, 'get', args, data)
}


export function unionapply_patch(pk, args, data) {
    return request("/api/unionapply/"+pk, 'patch', args, data)
}


export function unionapply_findOne(pk, args, data) {
    return request("/api/unionapply/"+pk, 'get', args, data)
}


export function unionuser_findOne(pk, args, data) {
    return request("/api/unionuser/"+pk, 'get', args, data)
}
