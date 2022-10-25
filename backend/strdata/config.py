# config
import os
import yaml
import pprint


SANIC_ENV = os.environ.get("SANIC_ENV")
AUTO_RELOAD = True
CONF = 'config.yaml'
if SANIC_ENV == 'PROD':
    CONF = '/data/playerki/config.yaml'
    AUTO_RELOAD = False

with open(CONF) as f:
    data = yaml.load(f.read())
    pprint.pprint(data)

locals().update(data)