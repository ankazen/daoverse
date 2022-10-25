from sanic.response import json, html
from orjson import dumps as json_dumps
from strdata import common
import urllib.parse
from functools import wraps
import operator


comparison_operators = {
    "$lt": operator.lt,
    "$le": operator.le,
    "$eq": operator.eq,
    "$ne": operator.ne,
    "$gt": operator.gt,
    "$ge": operator.ge
}

PAGE_COUNT = 10


def showapp(app):
    for name in app.blueprints:
        bp = app.blueprints[name]
        for u in bp.routes:
            print(u.uri, u.methods)


def template_render(app, templatename, data):
    jinja = app.ctx.jinja
    template = jinja.get_template(templatename)
    html_content = template.render(data)
    return html(html_content)


def get_object(app, row):
    models = app.ctx.models
    Model = models[row.object_type]['model']
    obj = Model.get(id=row.object_pk)
    return obj


def json_data(data):
    return json(data, dumps=json_dumps)


def json_ok(data, extend={}, msg="success"):
    dic = {}
    dic['data'] = data
    dic['message'] = msg
    dic['status'] = 200
    dic.update(extend)
    return json(dic, dumps=json_dumps)


def json_fail(msg="fail"):
    dic = {}
    dic['description'] = msg
    dic['status'] = 200
    dic['message'] = msg
    return json(dic, dumps=json_dumps)


async def query_pager(qs, request):
    page = int(request.args.get('page', 1))
    count = int(request.args.get('count', PAGE_COUNT))
    if type(qs).__name__ == 'coroutine':
        qs = await qs
    total = qs.count()
    page_total = int((total - 1)/PAGE_COUNT) + 1

    if count != -1:
        qs = qs.paginate(page, count)

    count = qs.count()
    extend_dic = {
        'total': total,
        'page_total': page_total,
        'page': page,
        'count': count
    }

    return qs, extend_dic


def query_filter(qs, request, Model):
    import json
    args_filter = request.args.get('filter', None)
    if not args_filter:
        return qs
    dic_filter = json.loads(args_filter)
    for col_name in dic_filter:
        if not hasattr(Model, col_name):
            continue
        field = getattr(Model, col_name)
        ops = dic_filter[col_name]
        for op in ops:
            val = ops[op]
            exp = comparison_operators[op](field, val)
            qs = qs.where(exp)
    return qs


def view_pager(request, extends, length=3):
    page = int(request.args.get('page', 1))
    total = extends['total']
    total = int((total - 1)/PAGE_COUNT) + 1
    start = page - length
    end = page + length

    if start <=0:
        start = 1
    if end > total:
        end = total

    pre = page - 1
    nt = page + 1

    pages =  list(range(start, end+1))
    pages = list(map(lambda x: {'text':x, 'path': request_url(request, {'page':x})}, pages))

    pre = request_url(request, {'page': pre}) if pre > 0 else None
    nt = request_url(request, {'page': nt}) if nt <= total else None
    return {'pages': pages, 'pre':pre, 'next':nt, 'curr': page}


def json_list(qs, pagenum=1, count=-1, extend=None):
    result = []
    total_count = qs.count()
    if count != -1:
        qs = qs.paginate(pagenum, count)

    for entry in qs:
        result.append(entry.m2d())
    count_qs = len(result)

    dic = {
        'count': count_qs,
        'total': total_count,
        'page': pagenum,
    }
    if extend:
        dic.update(extend)

    return json_ok(result, extend=dic)


def request_file(request, savepath):
    file = request.files.get('file')
    try:
        ftype = file.type.split('/')[1]
    except Exception as e:
        print(e)
        return None, None

    fname = file.name
    ftype = fname.split('.')[-1]

    filename = common.uuid() +'.' + ftype
    filepath = savepath + '/' + filename
    filedata = file.body
    with open(filepath, 'wb') as f:
        f.write(filedata)

    return file, filename


# 装饰器
def authorized():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_authorized = request.ctx.user
            if is_authorized:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return json_fail('需要登录')
        return decorated_function
    return decorator


def request_url(request, extend):
    args = {}
    for arg, val in request.query_args:
        args[arg] = val

    args.update(extend)
    return '{}?{}'.format(request.path, urllib.parse.urlencode(args))