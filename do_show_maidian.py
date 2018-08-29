#coding=utf8
#Author:Guo Xiangchen

import test_change_503
import pymysql
from time import sleep
import global_list
import re


def select_guo_db(sql):
    ###mysql connect###
    db = pymysql.connect("10.134.96.54", "root", "test", "guo_db", charset='utf8')
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

def match_result(data):
    result_temp = ""
    for key, value in global_list.excel_dict.items():
        match_key = key + ";"
        match_temp = re.search(match_key, data)
        if match_temp != None:
            result_temp = result_temp + data + "\n" + value + "\n" + "\n"
    return result_temp


#if __name__ == '__main__':
def make_data(cnt_log):
#    print("appinfo=" + global_list.appinfo)
    result = ""
    sql = "SELECT * FROM maidian_log order by No DESC limit %d;" %cnt_log
    #sql = "SELECT * FROM maidian_log order by No DESC limit 5;"
    data = select_guo_db(sql)
    for i in range(0, cnt_log):
        if data[i][1] == global_list.device and data[i][3] == global_list.appinfo:
            data_log = data[i][4].split("|||")
            #print(data[i][4])
            for line in data_log:
                #print(line)
                result_match = match_result(line)
                if result_match != "":
                    result = result + result_match
    #print(result)
    return result