#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on 2019-7-2
@author: lh.huang
Project:mysql的基本操作
"""
import pymysql
from loguru import logger


class MySqlHelper:
    """
    操作mysql数据库
    """

    def __init__(self, conf, database):
        """
        mysql数据库初始化连接
        :param conf: {'database': 'qt_titan', 'host': '172.16.13.65', 'port': 3306, 'user': 'root', 'password': 'H56q4vDzD270i3hj'}
        :param database:
        """
        try:
            # 注意mysql_conf中默认database=qt_titan, 如果有切换到其他database，需要更新database
            user_conf = {
                "database": database
            }
            user_conf.update(conf)
            self.conn = pymysql.connect(**user_conf)  # 加**后表示传入的是字典里的数据，否则报错
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except pymysql.Error as e:
            logger.error('连接数据库失败：{}'.format(e))

    def getOne(self, table, cond):
        data = ""
        sql = "select * from %s where %s" % (table, cond)
        logger.info(sql)
        try:
            self.cur.execute(sql)
            data = self.cur.fetchone()
        except pymysql.Error as e:
            logger.error("Uable to fetch one key data!")
        return data

    def getKeys(self, table, key, cond):
        data = ""
        sql = "select %s from %s where %s" % (key, table, cond)
        logger.info(sql)
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
        except pymysql.Error as e:
            logger.error(e)
            logger.error("Uable to fetch One data!")
        return data

    def getMany(self, table, cond=None):
        data = ""
        if cond is None:
            sql = "select * from %s" % table
        else:
            sql = "select * from %s where %s" % (table, cond)
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
        except BaseException:
            logger.error("Uable to fetch all data!")
        return data

    def execute(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.error("execute error %s" % e)

    def delete(self, sql):
        try:
            data = self.cur.execute(sql)
            return data
        except Exception as e:
            logger.error(e)

    def insert_data(self, sql, *args):
        """ 插入单行数据"""
        try:
            result = self.cur.execute(sql, args)
            self.conn.commit()
            return result
        except Exception as e:
            logger.error(e.args)

    def insert_datas(self, sql, list_datas):
        """
        批量插入数据
        :param sql:
        :param list_datas:
        :return:
        """
        try:
            result = self.cur.executemany(sql, list_datas)
            logger.info('insert data effects nums：{}'.format(result))
            self.conn.commit()
            return result
        except Exception as e:
            logger.error(e.args)

    def update_data(self, sql):
        """
        更新数据
        :param sql:
        :return:
        """
        try:
            result = self.cur.execute(sql)
            logger.info('update data effects nums：{}'.format(result))
            self.conn.commit()
            return result
        except Exception as e:
            print(e.args)

    def update_datas(self, sql, list_datas):
        """
        批量更新数据
        :param sql:
        :param list_datas:
        :return:
        """
        try:
            result = self.cur.executemany(sql, list_datas)
            logger.info('update data effects nums：{}'.format(result))
            self.conn.commit()
            return result
        except Exception as e:
            logger.error(e.args)

    def delete_datas(self, sql, list_datas):
        """
        批量更新数据
        :param sql:
        :param list_datas:
        :return:
        """
        try:
            result = self.cur.executemany(sql, list_datas)
            logger.info('update data effects nums：{}'.format(result))
            self.conn.commit()
            return result
        except Exception as e:
            logger.error(e.args)

    def close_conn(self):
        """关闭数据库"""
        try:
            if self.conn:
                self.cur.close()
                self.conn.close()
        except pymysql.Error as e:
            logger.error(e)
