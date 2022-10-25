# from sanic import Sanic
# from sanic.response import text
# from sanic_utils import showapp
# import config
# from daoverse.views import bp

# app = Sanic(config.NAME)
# app.blueprint(bp)


# @app.get("/t")
# async def foo_handler(request):
#     return text("I said foo!")

# showapp(app)

# app.run(host=config.HOST, port=config.PORT, access_log=config.DEBUG, debug=config.DEBUG)
import yaml
from strdata import strdata


apps = [
    'daoverse'
]

middlewares = [
]

with open('config.yaml') as f:
    config = yaml.load(f.read())

config.update({'apps': apps, 'middlewares': middlewares})

print(config)
App = strdata.createApp(config)
strdata.startApp(App)