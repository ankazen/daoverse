import datetime
import json
from peewee import CharField, IntegerField, TextField, ForeignKeyField, BooleanField, DateTimeField
from strdata.db import DB, BaseModel, VIEW_CONFIG
from playhouse.shortcuts import model_to_dict, dict_to_model
from playhouse.signals import post_save
from pathlib import Path


ContractPath = './contracts'
AbiPath = './abis'


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
        dic['union'] = self.union.m2d()
        return dic


class Contract(BaseModel):
    name = CharField()
    path = CharField()
    desc = CharField()

    class Meta:
        table_name = 'contract'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        # dic['content'] =
        path = Path('{}/{}'.format(ContractPath, self.path))
        print(path)
        dic['files'] = {}
        dic['file_summary'] = ''
        for file in path.iterdir():
            print(file)
            dic['files'][file.name] = {'path': path.name, 'content': file.read_text()}
            dic['file_summary'] += file.name +'\n' + file.read_text()
        return dic


class UnionContract(BaseModel):
    user = ForeignKeyField(User)
    union = ForeignKeyField(Union)
    contract = ForeignKeyField(Contract)
    address = CharField()
    abi = CharField()
    name = CharField()
    network = CharField()

    class Meta:
        table_name = 'union_contract'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        dic['contract'] = self.contract.m2d()

        path = Path(self.abi)
        print(path)
        dic['interface'] = path.read_text()
        return dic


class UnionApply(BaseModel):
    user = ForeignKeyField(User)
    union = ForeignKeyField(Union)
    desc = CharField()
    certified = BooleanField(default=False)
    certified_at = DateTimeField(null=True)
    certified_user = ForeignKeyField(User, null=True)

    class Meta:
        table_name = 'union_apply'

    def m2d(self):
        dic = model_to_dict(self, backrefs=False, recurse=False)
        return dic


@post_save(sender=UnionApply)
def on_unionapply_save_handler(model_class, instance, created):
    if instance.certified:
        user = instance.user
        union = instance.union
        qs = UnionUser.select().where(UnionUser.user==user, UnionUser.union==union)
        if qs.count() > 0:
            return
        UnionUser.create(**{'user':instance.user,'union':instance.union})
    

DB.create_tables([Union, User, UnionUser, Contract, UnionApply, UnionContract])


