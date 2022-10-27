import datetime
import json
from peewee import CharField, IntegerField, TextField, ForeignKeyField, BooleanField, DateTimeField
from strdata.db import DB, BaseModel, VIEW_CONFIG
from playhouse.shortcuts import model_to_dict, dict_to_model
from playhouse.signals import post_save


class Union(BaseModel):
    name = CharField(unique=True) 
    
    class Meta:
        table_name = 'union'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic

class User(BaseModel):
    identifier = CharField()

    class Meta:
        table_name = 'user'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class UnionUser(BaseModel):
    user = ForeignKeyField(User)
    union = ForeignKeyField(Union)
    is_admin = BooleanField(default=False)

    class Meta:
        table_name = 'union_user'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class Contract(BaseModel):
    name = CharField()
    union = ForeignKeyField(Union)
    creator = ForeignKeyField(User)

    class Meta:
        table_name = 'contract'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class UnionContract(BaseModel):
    user = ForeignKeyField(User)
    union = ForeignKeyField(Union)
    contract = ForeignKeyField(Contract)

    class Meta:
        table_name = 'union_contract'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class Apply(BaseModel):
    user = ForeignKeyField(User)
    union = ForeignKeyField(Union)
    desc = CharField()
    certified = BooleanField(default=False)
    certified_at = DateTimeField(null=True)
    certified_user = ForeignKeyField(User, null=True)

    class Meta:
        table_name = 'apply'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


DB.create_tables([Union, User, UnionUser, Contract, Apply, UnionContract])
