# -*- coding: utf-8 -*-
__author__ = 'tz'
__date__ = '2017-09-29 15:19'

import pymysql

conn = pymysql.connect("localhost", "root", "123456", "flaskdemo")
cur = conn.cursor()


def addUser(id,name,password):
    sql = "insert into t_user (id,name,password) values ('%s', '%s', '%s')" %(id, name,password)
    cur.execute(sql)
    conn.commit()
    conn.close()


#addUser('1', 'tz','123')


def isExisted(name,password):
    sql = "select * from t_user where name = '%s' and password = '%s'" %(name,password)
    cur.execute(sql)
    result = cur.fetchall()
    if(len(result) == 0):
        return False
    else:
        return True