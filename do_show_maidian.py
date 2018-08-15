#coding=utf8
#Author:Guo Xiangchen

import pymysql
from time import sleep
import global_list


def select_datacenter(sql):
    ###mysql connect###
    db = pymysql.connect("","root","","data_center",charset='utf8')
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception:
        return False
    # 关闭数据库连接
    db.close()
    return data

def watch_mysql(process_name, tasks, results, stop_flag):
    # cnt_db = select_datacenter()
    cnt_db = 50
    cnt_db_now = 45
    while True:
        #cnt_db_now = select_datacenter()
        print(cnt_db_now)
        if cnt_db_now > cnt_db:
            print ("!!")
            cnt_db = cnt_db_now
            results = -1
            return results
        cnt_db_now = cnt_db_now + 1
        sleep(1)


def match_result(process_name, tasks, results, stop_flag):
    while True:
        print("$$$")
        if len(global_list.maidian_all) != 0:
            sleep(1)
            print("mmm")
            print(global_list.maidian_all)
            global_list.maidian_all = []
            print("!" + global_list.maidian_all)
        sleep(1)