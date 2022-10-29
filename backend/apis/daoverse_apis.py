import json
import urllib.parse
import requests

BaseUrl = 'http://127.0.0.1:9000'


def unionapply_create(args={}, data={}, headers={}):
    url = BaseUrl + "/api/unionapply"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.post(url, json.dumps(data), headers=headers)
    return r.json()


def unoincontract_findOne(pk, args={}, data={}, headers={}):
    url = BaseUrl + "/api/unoincontract/"+pk
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def auth(args={}, data={}, headers={}):
    url = BaseUrl + "/api/auth"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.post(url, json.dumps(data), headers=headers)
    return r.json()


def unoincontract_find(args={}, data={}, headers={}):
    url = BaseUrl + "/api/unoincontract"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def user_find(args={}, data={}, headers={}):
    url = BaseUrl + "/api/user"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def contract_find(args={}, data={}, headers={}):
    url = BaseUrl + "/api/contract"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def contract_findOne(pk, args={}, data={}, headers={}):
    url = BaseUrl + "/api/contract/"+pk
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def union_find(args={}, data={}, headers={}):
    url = BaseUrl + "/api/union"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def unionapply_find(args={}, data={}, headers={}):
    url = BaseUrl + "/api/unionapply"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def union_findOne(pk, args={}, data={}, headers={}):
    url = BaseUrl + "/api/union/"+pk
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def contract_create(args={}, data={}, headers={}):
    url = BaseUrl + "/api/contract"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.post(url, json.dumps(data), headers=headers)
    return r.json()


def unionuser_find(args={}, data={}, headers={}):
    url = BaseUrl + "/api/unionuser"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def unoincontract_create(args={}, data={}, headers={}):
    url = BaseUrl + "/api/unoincontract"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.post(url, json.dumps(data), headers=headers)
    return r.json()


def union_create(args={}, data={}, headers={}):
    url = BaseUrl + "/api/union"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.post(url, json.dumps(data), headers=headers)
    return r.json()


def unionuser_create(args={}, data={}, headers={}):
    url = BaseUrl + "/api/unionuser"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.post(url, json.dumps(data), headers=headers)
    return r.json()


def user_create(args={}, data={}, headers={}):
    url = BaseUrl + "/api/user"
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.post(url, json.dumps(data), headers=headers)
    return r.json()


def user_findOne(pk, args={}, data={}, headers={}):
    url = BaseUrl + "/api/user/"+pk
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def unionapply_patch(pk, args={}, data={}, headers={}):
    url = BaseUrl + "/api/unionapply/"+pk
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.patch(url, json.dumps(data), headers=headers)
    return r.json()


def unionapply_findOne(pk, args={}, data={}, headers={}):
    url = BaseUrl + "/api/unionapply/"+pk
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()


def unionuser_findOne(pk, args={}, data={}, headers={}):
    url = BaseUrl + "/api/unionuser/"+pk
    query_string = urllib.parse.urlencode(args)
    if query_string:
        url += '?' + query_string
    r = requests.get(url, json.dumps(data), headers=headers)
    return r.json()
