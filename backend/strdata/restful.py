from sanic import Blueprint
from strdata.sanic_utils import json_ok, json_fail, json_list
from jinja2 import Template
import re
from sanic import exceptions
import operator


def need_auth(request):
    user = request.ctx.user
    if not user:
        raise exceptions.Forbidden(f'需要登录')
    return user


def attachRoutes(bp, config):
    for item in config:
        routes = createRoutes(item)
        for route in routes:
            bp.add_route(route['handler'], route['path'], methods=[route['method']], name=route['name'])


def createRoutes(data):
    result = []
    name = data['_name']
    model = data['_model']
    if 'findOnly' in data:
        def findOnly(request):
            cfg = data['findOnly']
            if 'auth' in cfg and cfg['auth']:
                need_auth(request)
            if 'request_done' in cfg:
                cfg['request_done'](request)

            qs = model.select()
            if 'db_done' in cfg:
                qs = cfg['db_done'](request, qs)
            if qs.count() == 0:
                dic = {}
            else:
                dic = qs[0].m2d()
            return json_ok(dic)
        result.append({'handler': findOnly, 'path': '/'+name, 'method': 'get', 'name': name +'_findOnly'})

    if 'find' in data:
        def find(request):
            cfg = data['find']
            if 'auth' in cfg and cfg['auth']:
                need_auth(request)
            if 'request_done' in cfg:
                cfg['request_done'](request)

            qs = model.select()
            if 'db_done' in cfg:
                qs = cfg['db_done'](request, qs)
            
            sorts = []
            filters = []

            for (item, val) in request.query_args:
                if 'sort' in item:
                    group = val.split(':')
                    if len(group) == 2:
                        field, flg = group
                    else:
                        field = val
                        flg = 'asc'
                    field = getattr(model, field)
                    if flg == 'desc':
                        field = field.desc()
                    sorts.append(field)
                if 'filters' in item:
                    item = item.replace('[', ' ').replace(']', ' ')
                    group = item.split(' ')
                    field = group[1]
                    op = group[3]
                    if op == '$eq':
                        op = operator.eq
                    elif op == '$ne':
                        op = operator.ne
                    elif op == '$le':
                        op = operator.le
                    elif op == '$lt':
                        op = operator.lt
                    elif op == '$ge':
                        op = operator.ge
                    elif op == '$gt':
                        op = operator.gt
                    field = getattr(model, field)
                    filters.append(op(field, val))
                
                if 'pagination[start]' == item:
                    qs = qs.offset(int(val))
                if 'pagination[limit]' == item:
                    qs = qs.limit(int(val))

            for query in filters:
                qs = qs.where(query)
            if sorts:
                qs = qs.order_by(*sorts)            
                
            dic = []
            for row in qs:
                dic.append(row.m2d())
            return json_ok(dic)
        result.append({'handler': find, 'path': '/'+name, 'method': 'get', 'name': name +'_find'})

    if 'findOne' in data:
        def findOne(request, pk):
            cfg = data['findOne']
            if 'auth' in cfg and cfg['auth']:
                need_auth(request)
            if 'request_done' in cfg:
                cfg['request_done'](request, pk)

            row = model.get(id=pk)
            if 'db_done' in cfg:
                row = cfg['db_done'](request, row)

            return json_ok(row.m2d())
        result.append({'handler': findOne, 'path': '/'+ name +'/<pk>', 'method': 'get', 'params':'pk', 'name':name+'_findOne'})
    
    if 'create' in data:
        def create(request):
            request.ctx.json = request.json
            
            cfg = data['create']
            if 'auth' in cfg and cfg['auth']:
                need_auth(request)
            if 'request_done' in cfg:
                cfg['request_done'](request)
            
            row = model.create(**request.ctx.json)

            if 'db_done' in cfg:
                row = cfg['db_done'](request, row)

            return json_ok(row.m2d())
        result.append({'handler': create, 'path': '/' + name, 'method': 'post', 'name': name+'_create'})
    
    if 'patch' in data:
        def patch(request, pk):
            request.ctx.json = request.json

            cfg = data['patch']
            if 'auth' in cfg and cfg['auth']:
                need_auth(request)
            if 'request_done' in cfg:
                cfg['request_done'](request, pk)
            
            q = model.update(request.ctx.json).where(id==pk)
            q.execute()

            row = model.get(id=pk)
            if 'db_done' in cfg:
                row = cfg['db_done'](request, row)

            return json_ok(row.m2d())
        result.append({'handler': patch, 'path': '/'+name +'/<pk>', 'method': 'patch', 'params':'pk', 'name':name + '_patch'})

    return result


def createApis(bp, BaseUrl, tplname):
    routes_list = []
    for route in bp.routes:
        method = list(route.methods)[0].lower()
        name = route.name.split('.')[-1]
        urls = []
        param = None
        url_parts = ['']
        for part in route.parts:
            if ':' not in part:
                url_parts.append(part)
            else:
                if url_parts:
                    urls.append('"' + '/'.join(url_parts) + '/"')
                url_parts = []
                ret = re.match(r'\<(.+):.+\>', part)
                param = ret.groups()[0]
                urls.append(param)
        else:
            if url_parts:
                urls.append('"' + '/'.join(url_parts) + '"')
        
        url =  '+'.join(urls)
        routes_list.append({'name':name, 'method': method, 'url': url, 'params': param})
    
    tpl='strdata/templates/{}.tpl'.format(tplname)
    jinja2_template_string = open(tpl, 'r').read()
    template = Template(jinja2_template_string)
    content = template.render({'BaseUrl': BaseUrl, 'routes':routes_list })
    with open('apis/{}_{}'.format(bp.name, tplname), 'w') as f:
        f.write(content)