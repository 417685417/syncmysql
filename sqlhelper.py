#!/bin/env python
#_*_coding:utf-8_*_
import conf
import MySQLdb
class MySqlHelper():
    def __init__(self):
        self.mysql_str =conf.mysql_str
    def installsql(self,sql,dbname=""):
        try:
            self.mysql_str["db"]=dbname
            conn = MySQLdb.Connect(**self.mysql_str)
            cur = conn.cursor()
            Recoue=cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
        except Exception,e:
            pass
    def showsql(self,sql,dbname="mysql"):
        try:
            self.mysql_str["db"]=dbname
            conn = MySQLdb.Connect(**self.mysql_str)
            cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            Recoue=cur.execute(sql)
            data= cur.fetchall()
            return data
            cur.close()
            conn.close()
        except Exception,e:
            pass
    def select(self,sql,dbname="mysql"):
        try:
            self.mysql_str["db"]=dbname
            conn = MySQLdb.Connect(**self.mysql_str)
            cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            Recoue=cur.execute(sql)
            data= cur.fetchone()
            return data
            cur.close()
            conn.close()
        except Exception,e:
            pass