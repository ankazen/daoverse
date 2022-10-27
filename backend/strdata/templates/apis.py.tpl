import json
import urllib.parse
import requests

BaseUrl = '{{BaseUrl}}'
{% for route in routes %}
{% if route.params %}
def {{route.name}}({{route.params}}, args={}, data={}, headers={}):
{% else %}
def {{route.name}}(args={}, data={}, headers={}):
{% endif %}    url = BaseUrl + {{route.url}}
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.{{route.method}}(url, json.dumps(data), headers=headers)
    return r.json()
{% endfor %}