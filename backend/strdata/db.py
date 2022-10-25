from peewee import *
from playhouse.signals import Model
import datetime
from playhouse.shortcuts import model_to_dict
from strdata import config

DB = SqliteDatabase(config.DB_PATH)


VIEW_CONFIG = {
    'id': {'show':True, 'readonly':True, 'v_type': 'text-field', 'cols': 1},
    'created_at': {'readonly':True, 'v_type': 'datetime', 'cols': 3, 'd_value': 0},
    'updated_at': {'readonly':True, 'v_type': 'datetime', 'cols': 3, 'd_value': 0},
    'deleted_at': {'readonly':True, 'v_type': 'datetime', 'cols': 3, 'd_value': 0},
    'is_deleted': {'readonly':False, 'v_type': 'checkbox', 'cols': 1},
}



class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(null=True)
    deleted_at = DateTimeField(null=True)
    is_deleted = BooleanField(default=False)

    class Meta:
        database = DB

    def m2d(self):
        return model_to_dict(self, backrefs=False, max_depth=3)
