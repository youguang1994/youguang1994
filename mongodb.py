#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on 2020-3-10
@author: lihua
Project:mongo的基本操作
"""
from pymongo import MongoClient
_DB = "wisteria_assets"


class MyMongo:

    def __init__(self, conf):

        host = conf.get("host")
        port = conf.get("port")
        user = conf.get("user")
        password = conf.get("password")
        if user is not None:
            url = 'mongodb://' + user + ':' + \
                  password + '@' + host + ':' + str(port)
        else:
            url = 'mongodb://' + host + ':' + port
        self.mongoclient = MongoClient(url, w=1)  # w=1表示需要等待写入完成后才进行后续操作

    def find(self, db=_DB, tb='default', cond={}):
        rt = self.mongoclient[db].get_collection(tb).find(cond)
        return [i for i in rt]

    def find_ids(self, db=_DB, tb='default', cond={}):
        rt = self.mongoclient[db].get_collection(tb).find(cond)
        return [i.get("_id") for i in rt]

    def find_one(self, db=_DB, tb='default', cond={}):
        rt = self.mongoclient[db].get_collection(tb).find_one(cond)
        # print "db %s tb %s cond %s data %s" % (db, tb, cond, rt)
        return rt

    def aggregate(self, db=_DB, tb="default", cond={}):
        rt = self.mongoclient[db].get_collection(tb).aggregate(cond)
        return rt

    def insertone(self, db=_DB, tb='default', mdata={}):
        try:
            rt = self.mongoclient[db].get_collection(tb).insert_one(mdata)
            return rt.inserted_id
        except Exception as e:
            print(e)

    def insertmany(self, db=_DB, tb='default', mdatas=[]):
        try:
            rt = self.mongoclient[db].get_collection(tb).insert_many(mdatas)
            return rt.inserted_ids
        except Exception as e:
            print(e)

    def delete(self, db=_DB, tb='default', cond={}):
        try:
            rt = self.mongoclient[db].get_collection(tb).delete_many(cond)
            return rt
        except Exception as e:
            print(e)

    def update_many(self, db=_DB, tb='default', cond={}, data={}):
        self.mongoclient[db].get_collection(tb).update_many(cond, data)

    def update(self, db=_DB, tb='default', cond={}, data={}):
        self.mongoclient[db].get_collection(tb).update(cond, data)

    def close(self):
        self.mongoclient.close()
