#coding=utf8
#Author:Guo Xiangchen

import test_change_503
import pymysql
from time import sleep
import global_list
import re


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

def match_result(data):
    result_temp = ""
    for key, value in global_list.excel_dict_temp.items():
        match_key = key + ";"
        match_temp = re.search(match_key, data)
        if match_temp != None:
            #sleep(1)
            print(data)
            print(value)
            result_temp = result_temp + data + "\n" + value + "\n"
    #print(result_temp)
    return result_temp



#if __name__ == '__main__':
def make_data():
    result = ""
    with open("maidian.txt", encoding='utf8') as f:
        line = f.readline()
        while line:
            #print (line)
            result_match = match_result(line)
            line = f.readline()
            if result_match != "":
                result = result + result_match
    print(result)
    return result