# ankazen@qq.com
import jwt
import json
from sanic import Blueprint
from playhouse.shortcuts import dict_to_model
from strdata.sanic_utils import json_ok, json_fail
from daoverse.models import Union, User, UnionUser, State, Tran, Order, TranLog, Apply
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
        '_name': 'user',
        '_model': User,
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
        '_name': 'unionuser',
        '_model': UnionUser,
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
        '_name': 'state',
        '_model': State,
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
        '_name': 'tran',
        '_model': Tran,
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
        '_name': 'order',
        '_model': Order,
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
        '_name': 'tranlog',
        '_model': TranLog,
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
        '_name': 'apply',
        '_model': Apply,
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
]

attachRoutes(bp, routes_config)