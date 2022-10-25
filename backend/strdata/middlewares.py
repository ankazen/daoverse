from sanic import Sanic, response

async def request_session_open(request):
    app = Sanic.get_app()
    session_interface = app.ctx.session_interface
    await session_interface.open(request)

async def response_session_save(request, response):
    app = Sanic.get_app()
    session_interface = app.ctx.session_interface
    await session_interface.save(request, response)

async def request_check_hosts(request):
    app = Sanic.get_app()
    config = app.config
    host = request.headers.get('host', None)
    if not host or host not in config.ALLOW_HOSTS:
        return response.redirect('https://www.baidu.com')
