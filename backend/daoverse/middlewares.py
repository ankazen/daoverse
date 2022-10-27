import jwt
from daoverse.models import User

async def request_get_user(request):
    user = None
    token = request.token
    if not token:
        token = request.cookies.get('token')
    if not token:
        request.ctx.user = user
        return

    token = token.encode('utf-8')
    payload = {}
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except Exception as e:
        print(e)
        request.ctx.user = user
        return

    if payload and 'user_id' in payload:
        user_id = payload['user_id']
        try:
            user = User.get(User.identifier == user_id)
        except Exception as e:
            print(e)
    request.ctx.user = user