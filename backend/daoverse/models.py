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


class User(BaseModel):
    address = CharField(unique = True)
    name = CharField()

    class Meta:
        table_name = 'daoverse_user'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class UnionUser(BaseModel):
    user = ForeignKeyField(User)
    union = ForeignKeyField(Union)

    class Meta:
        table_name = 'daoverse_union_user'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class State(BaseModel):
    type = CharField()
    name = CharField()

    class Meta:
        table_name = 'daoverse_state'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class Tran(BaseModel):
    state = ForeignKeyField(State)
    name = CharField()

    class Meta:
        table_name = 'daoverse_tran'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class Order(BaseModel):
    creator = ForeignKeyField(User)
    type = CharField() # apply invite
    state = ForeignKeyField(State)

    class Meta:
        table_name = 'daoverse_order'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


class TranLog(BaseModel):
    order = ForeignKeyField(Order)
    user = ForeignKeyField(User)
    tran = ForeignKeyField(Tran)

    class Meta:
        table_name = 'daoverse_tranlog'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)


class Apply(BaseModel):
    order = ForeignKeyField(Order)
    class Meta:
        table_name = 'daoverse_apply'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)



DB.create_tables([Union, User, UnionUser, State, Tran, Order, TranLog, Apply])
