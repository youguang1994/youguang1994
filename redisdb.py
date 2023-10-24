#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on 2019-6-11
@author: lhhuang
Project:redis的基本操作
"""
import redis
from rediscluster import RedisCluster
from loguru import logger


class Redis:

    def __init__(self, conf, is_cluster=False):
        host = conf.get("host")
        port = conf.get("port")
        db = int(conf.get("db"))
        password = conf.get("password")
        if is_cluster:
            self.redis_con = RedisCluster(host=host, port=port, password=password)
        else:
            self.redis_con = redis.Redis(host=host, port=port, db=db, password=password)

    def get_keys(self, key="test"):
        """
        获取当前数据库中所有的"key"
        :param key:
        :return:
        """
        keys = self.redis_con.keys(key)
        return keys

    def hgetall(self, name):
        # 获取name对应hash的所有键值
        keys = self.redis_con.hgetall(name)
        return keys

    def hset(self, name, key, value):
        rt = self.redis_con.hset(name, key, value)
        print(rt)

    def hget(self, name, key):
        # 在name对应的hash中根据key获取value
        value = self.redis_con.hget(name, key)
        return value

    def hmget(self, name, keys):
        # 在name对应的hash中获取多个key的值
        values = self.redis_con.hmget(name, keys)
        return values

    def set(self, name, value):
        # 在Redis中设置值，默认不存在则创建，存在则修改
        self.redis_con.set(name, value)

    def delete(self, keys):
        try:
            for key in keys:
                self.redis_con.delete(key)
        except Exception as e:
            logger.error(e)

    def deletes(self, *keys):
        self.redis_con.delete(*keys)

    def expire(self, name, expire_seconds):
        self.redis_con.expire(name, expire_seconds)

    def mset(self, key_values):
        for key in key_values.keys():
            value = key_values[key]
            self.redis_con.set(key, value)

    def get(self, name):
        value = self.redis_con.get(name)
        return value

    def keys(self, pattern):
        return self.redis_con.keys(pattern)

    def mget(self, keys):
        values = self.redis_con.mget(keys)
        return values

    def lpush(self, name, value):
        # 在Redis中从左侧推入元素
        value = self.redis_con.lpush(name, value)
        return value

    def rpop(self, name):
        # 获取name的值
        value = self.redis_con.rpop(name)
        if value:
            return value.decode('utf8')
        else:
            return value

    def shutdown(self):
        if self.redis_con is not None:
            self.redis_con.shutdown()

    # def zadd(self, keyname, key_values):
    #    self.redis_con.zadd(keyname, key_values)

    def zadd(self, keyname, name, score):
        self.redis_con.zadd(keyname, name, score)

    def zcard(self, keyname):
        return self.redis_con.zcard(keyname)

    def zremrangebyrank(self, keyname, min, max):
        return self.redis_con.zremrangebyrank(keyname, min, max)

    def zrem_allmember(self, keyname):
        member_num = self.zcard(keyname)
        return self.zremrangebyrank(keyname, 0, member_num)
