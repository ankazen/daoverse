# ankazen@qq.com
import jwt
import json
from sanic import Blueprint
from playhouse.shortcuts import dict_to_model
from strdata.sanic_utils import json_ok, json_fail
from daoverse.models import Union, UnionMember, Contract, Apply
from strdata.restful import attachRoutes


bp = Blueprint(
    'daoverse',
    url_prefix='/api'
)


routes_config = [
    {
        '_name': 'union',
        '_model': Union,
        'find': {
            'auth': False,
        },
        'findOne': {
            'auth': False,
        },
        'create': {
            'auth': False,
        },
    },
    {
        '_name': 'unionmember',
        '_model': UnionMember,
        'find': {
            'auth': False,
        },
        'findOne': {
            'auth': False,
        },
        'create': {
            'auth': False,
        },
    }
]

attachRoutes(bp, routes_config)