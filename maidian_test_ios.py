#coding=utf-8
import os
import signal
import subprocess
import time
import MySQLdb
 
 
logFile = "maidian.txt"

def insert(sql):
    db = MySQLdb.connect("localhost","root","test","guo_db",charset='utf8')
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        db.close()
    except:
        # Rollback in case there is any error
        # print sql
        db.rollback()
        db.close()

 
def monitorLog(logFile):
    print '监控的日志文件 是%s' % logFile
    #stoptime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 10))
    popen = subprocess.Popen('tail -f ' + logFile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = popen.pid
    print('Popen.pid:' + str(pid))
    line_temp = ""
    model = ""
    sdk = ""
    appinfo = ""
    while True:
        line = popen.stdout.readline().strip()
        # 判断内容是否为空
        if "*******" not in line:
            if "model:" in line:
		#print (line)
            	model = line.split('model:')[1].split(',')[0]
		sdk = line.split('sdk:')[1].split(';')[0]
		appinfo = line.split('appVersion:')[1].split(';')[0]
	    	#print ("model:" + model)
    		#print ("sdk:" + sdk)
	    else:
	    	line_temp = line_temp + "|||" + line
	else:
	    time_now = line_temp.split("|||")[0]
            #print (time_now)
            #print (line_temp)
            sql = "INSERT INTO maidian_log (No, model, sdk, appinfo, log) VALUES (0, '%s', '%s', '%s', '%s');" %(model, sdk, appinfo, line_temp)
	    #print("sql=" + sql)
	    insert(sql)
	    line_temp = ""
 
if __name__ == '__main__':
    monitorLog(logFile)
