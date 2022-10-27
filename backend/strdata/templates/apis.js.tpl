import axios from 'axios';

var BaseUrl = '{{BaseUrl}}';


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

{% for route in routes %}
{% if route.params %}
export function {{route.name}}({{route.params}}, args, data) {
    return request({{route.url}}, '{{route.method}}', args, data)
}{% else %}
export function {{route.name}}(args, data) {
    return request({{route.url}}, '{{route.method}}', args, data)
}{% endif %}
{% endfor %}
