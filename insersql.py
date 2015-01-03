#/usr/bin/python
#coding:utf-8

__author__='zmj'

import MySQLdb
import random

def insert(n,table):
    conn=MySQLdb.connect(user='root',passwd='tigerwith',host='127.0.0.1')
    conn.select_db("testmysql")
    course=conn.cursor()
    sqli="insert into "+table+"(name,sex,resume) values(%s,%s,%s)"
    for i in range(n):
        array=[]
        for j in range(5):
            ar=(suizi(5),suishu(4),suizi(100))
            array.append(ar)
        course.executemany(sqli,array)
    course.close()
    conn.commit()
    conn.close()

def suizi(n):
    a=''
    for i in range(n):
        a+=chr(random.randint(67,99))
    return a

def suishu(n):
    return random.randint(0,n)

if __name__=="__main__":
    insert(10000,"testmysql2")

