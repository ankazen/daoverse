import importlib
from sanic import Sanic
from sanic_cors import CORS
from jinja2 import Environment, FileSystemLoader, Template
from sanic_session import RedisSessionInterface
from strdata import sanic_utils
from strdata.redis import Redis


def make_apis(config, appname, routes, path=None):
    for route in routes:
        '''
        '/api/doc/<pk>/tt/<pk2>'
        '/api/doc/<pk>/tt/'
        '/api/doc/<pk>'
        '''
        params = []
        keys = route['path'].split('/')
        for key in keys:
            if '<' in key:
                key = key[1:-1]
                params.append(key)

        route['path'] = route['path'].replace('<', '\'+').replace('>','+\'')
        route['path'] = '\'' + route['path'] + '\''
        route['path'] = route['path'].replace('\'\'', '')
        if route['path'][-1] == '+':
            route['path'] = route['path'][:-1]
        route['params'] = ','.join(params)


    
    tpl='strdata/templates/api_js.tpl'
    jinja2_template_string = open(tpl, 'r').read()
    template = Template(jinja2_template_string)
    content = template.render({'BaseUrl': config.API_BASEURL, 'routes':routes })
    with open(appname.replace('.', '/') +'/api.js', 'w') as f:
        f.write(content)

def createApp(config):
    App = Sanic(config['NAME'], strict_slashes=True)
    CORS(App)
    for key in config:
        setattr(App.config, key, config[key])

    App.config.REAL_IP_HEADER = "x-real-ip"

    config = App.config

    App.ctx.jinja = Environment(loader=FileSystemLoader(config.TEMPLATE_PATH))
    App.ctx.redis = Redis()
    App.ctx.session_interface = RedisSessionInterface(App.ctx.redis.get_redis_pool, expiry=604800)
    App.ctx.models = {}

    for appname in config.apps:
        module_model = importlib.import_module(appname+'.models')
        for modelname in dir(module_model):
            item = getattr(module_model, modelname)
            clsname = item.__class__.__name__
            if clsname != 'ModelBase':
                continue
            if modelname in ['Model', 'BaseModel']:
                continue
            modelname = item._meta.table_name
            App.ctx.models[modelname]= {'model':item, 'app': appname}
        module_views = importlib.import_module(appname+'.views')
        App.blueprint(module_views.bp)

    for middleware in config.middlewares:
        module_middleware = importlib.import_module(middleware)
        for fname in dir(module_middleware):
            item = getattr(module_middleware, fname)
            if item.__class__.__name__ != 'function':
                continue
            if fname.startswith('request_'):
                App.register_middleware(item, "request")
            elif fname.startswith('response_'):
                App.register_middleware(item, "response")

    App.static('/static', config.STATIC_PATH)

    return App


def startApp(App):
    config = App.config
    sanic_utils.showapp(App)
    App.run(host=config.HOST, port=config.PORT, access_log=config.DEBUG, debug=config.DEBUG)
