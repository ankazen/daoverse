import datetime
import json
from peewee import CharField, IntegerField, TextField, ForeignKeyField, BooleanField, DateTimeField
from strdata.db import DB, BaseModel, VIEW_CONFIG
from playhouse.shortcuts import model_to_dict, dict_to_model
from playhouse.signals import post_save


class Union(BaseModel):
    name = CharField(unique=True) 

    class Meta:
        table_name = 'daoverse_union'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class UnionMember(BaseModel):
    address = CharField()
    union = ForeignKeyField(Union)
    is_admin = BooleanField(default=False)

    class Meta:
        table_name = 'daoverse_union_member'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class Contract(BaseModel):
    name = CharField()
    union = ForeignKeyField(Union)
    creator = CharField()

    class Meta:
        table_name = 'daoverse_contract'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class Apply(BaseModel):
    address = CharField()
    union = ForeignKeyField(Union)
    desc = CharField()
    certified = BooleanField(default=False)
    certified_at = DateTimeField(null=True)

    class Meta:
        table_name = 'daoverse_apply'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


DB.create_tables([Union, UnionMember, Contract, Apply])
