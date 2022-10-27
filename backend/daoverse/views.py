# ankazen@qq.com
import jwt
import json
from sanic import Blueprint
from playhouse.shortcuts import dict_to_model
from strdata.sanic_utils import json_ok, json_fail
from daoverse.models import Union, UnionUser, Contract, Apply, User
from strdata.restful import attachRoutes
from sanic.exceptions import SanicException
import datetime


bp = Blueprint(
    'daoverse',
    url_prefix='/api'
)


@bp.route('/auth', methods=['POST'])
async def auth(request):
    data = dict(request.json)    
    identifier = data['identifier']
    
    qs = User.select().where(User.identifier==identifier)
    if qs.count() == 0:
        user = User.create(**{'identifier': identifier})
    else:
        user = qs[0]

    token = jwt.encode({'user_id': user.identifier}, 'secret', algorithm='HS256')
    dic = {}
    dic['id'] = user.id
    try:
        dic['token'] = str(token, encoding='utf-8')
    except Exception as e:
        dic['token'] = token

    dic['me'] = user.m2d()
    return json_ok(dic)


def fill_user(request):
    request.ctx.json['user'] = request.ctx.user


def apply_patch_check(request, pk):
    row = Apply.get(id=pk)
    union = row.union
    user = request.ctx.user
    qs = UnionUser.select().where(UnionUser.union==union, UnionUser.is_admin==True)
    if qs.count() == 0:
        raise SanicException("权限不足", status_code=501)

    request.ctx.json['certified_at'] = datetime.datetime.now()
    request.ctx.json['certified_user'] = user



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
        '_name': 'contract',
        '_model': Contract,
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
            'auth': True,
            'request_done': fill_user
        },
        'patch': {
            'auth': True,
            'request_done': apply_patch_check
        }
    },
]

attachRoutes(bp, routes_config)