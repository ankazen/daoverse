var API_BASE_URL = "{{BaseUrl}}";

const generateQueryString = (params) => {
    if (!params) {
        return null;
    }
  return Object.keys(params)
    .map((v, i) => (i !== 0 ? "&" : "?") + `${v}=${o[v]}`)
    .join("");
};

let request = (url, method, args, data) => {
    const queryString = generateQueryString(args)
    let _url = API_BASE_URL + url;
    if (queryString) {
        _url += '?' + queryString
    }
    const header = {
        'Content-Type': 'application/application/json',
        'Authorization': 'Token ' + wx.getStorageSync('token')
    }
    return new Promise((resolve, reject) => {
        wx.request({
            url: _url,
            method: method,
            data: data,
            header,
            success(request) {
                resolve(request.data)
            },
            fail(error) {
                reject(error)
            },
            complete(aaa) {
                // 加载完成
            }
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
