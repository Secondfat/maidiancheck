#coding:utf-8
#Author:Guo Xiangchen

import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import do_excel
import global_list
import pymysql
import do_show_maidian


# global show_flag
# show_flag = 0

#"""更新数据类"""
class UpdateData(QThread):
    print("update!!!")
    update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring

    def run(self):
        cnt_db = 50
        cnt_db_now = 49
        while True:
            if cnt_db_now < cnt_db:
                tt = do_show_maidian.make_data()
                print(tt)
                self.update_date.emit(str(tt)) # 发射信号
            else:
                self.update_date.emit(str(cnt_db_now))  # 发射信号
            cnt_db_now = cnt_db_now + 1
            time.sleep(1)

    def select_datacenter(self, sql):
        ###mysql connect###
        db = pymysql.connect("", "root", "", "data_center", charset='utf8')
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

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gfox_test')
        self.setWindowIcon(QIcon('xdbcb8.ico'))
        self.resize(1000, 800)
        self.initUI()
        self.show()

    def initUI(self):

        #定义变量
        self.title_name = []
        #self.change_value = []

        #定义控件
        self.json_file_path = QLineEdit('D:/04 code/maidiancheck/App-搜索需求-V6.5埋点-V1.0.xlsx', self)
        self.json_file_path.selectAll()
        self.json_file_path.setFocus()
        self.bt = QPushButton('选择文件')
        self.bt.clicked.connect(self.choose_file_dic)
        self.bt1 = QPushButton('解析文件')
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        #执行使用的文件
        self.bt1.clicked.connect(lambda:do_excel.do_excel(self.json_file_path.text()))
        self.bt1.clicked.connect(self.show_port)
        self.bt1.clicked.connect(self.pull_phone_info)



        #self.bt2.setGeometry(620, 50, 200, 30)

        #将光标至于框内
        #self.url_change.setFocus()
        #self.json_file_path.setGeometry(80, 50, 150 ,30)
        #self.url_change.setGeometry(450, 50, 150, 30)


        self.main_layout = QVBoxLayout(self)
        up = QHBoxLayout()

        self.middle = QVBoxLayout()
        self.middle_up = QHBoxLayout()
        device_info_text = QLabel('选择手机')
        self.app_info = QLineEdit('', self)
        app_info_text = QLabel('选择APP版本')

        self.device_info = QComboBox()
        self.device_info.setMinimumWidth(150)#设置最小长度

        #self.device_info.setModel("QAbstractItemView{min-width:400px;height:200px}")
        self.middle_up.addWidget(device_info_text)
        self.middle_up.addWidget(self.device_info)
        self.middle_up.addWidget(app_info_text)
        self.middle_up.addWidget(self.app_info)


        self.title_confirm = QPushButton("开始测试埋点", self)
        #self.title_confirm.clicked.connect(lambda:do_show_maidian.watch_mysql())
        self.title_confirm.clicked.connect(self.update_thread)



        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(0, 0, 400, 400)
        self.scroll_area.setAutoFillBackground(True)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_bar = self.scroll_area.verticalScrollBar()

        self.scroll_contents = QWidget()
        self.scroll_contents.setGeometry(100, 1000, 10, 20)
        self.scroll_contents.setMinimumSize(1, 1000)

        self.show_editor = QTextEdit()
        self.update_data_thread = UpdateData()
        self.update_data_thread.update_date.connect(self.update_text_data)  # 链接信号


        self.last = QHBoxLayout()
        self.last.addWidget(self.scroll_area)
        self.last.addWidget(self.show_editor)

        up.addWidget(self.json_file_path)
        up.addWidget(self.bt)
        up.addWidget(self.bt1)
        #self.middle_left.addWidget(self.result_lb0)
        #last.addWidget(self.url_change)
        #last.addWidget(self.bt2)
        self.middle.addLayout(self.middle_up)
        self.middle.addWidget(self.title_confirm)

        self.main_layout.addLayout(up)
        self.main_layout.addLayout(self.middle)
        self.main_layout.addLayout(self.last)

        self.show()
        
    def choose_file_dic(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         "D:/",
                                                         "Text Files (*.json)");
        if filename != '':
            self.json_file_path.setText(filename)
        
    #展示每一个接口
    def show_port(self):
        source = self.sender()

        self.scroll_contents = QWidget()  
        self.scroll_contents.setGeometry(100, 1000, 10, 20)  
        self.scroll_contents.setMinimumSize(1, 10000)
        self.last.addWidget(self.scroll_area)

        self.cb = {}
        mm = 0
        #print(global_list.port_name)
        for key, value in global_list.excel_dict.items():
            self.cb[key] = QPushButton(value, self.scroll_contents)
            self.cb[key].clicked.connect(self.button_delete_dic)
            #self.cb[key].setText(value)
            self.cb[key].move(10, 10+mm*30)
            mm = mm + 1
        self.scroll_area.setWidget(self.scroll_contents)

    #取数据库中的数据放在下拉栏里
    def pull_phone_info(self):
        # 添加下拉框的数据
        self.device_info.addItem("iPhone 6s plus")
        self.device_info.addItem("女性")
        print ("!!!")


    #隐藏已经展示的埋点
    def button_delete_dic(self):
        sender = self.sender()
        remove_value = sender.text()
        for key_match, value_match in global_list.excel_dict.items():
            if value_match == remove_value:
                global_list.excel_dict.pop(key_match)
                break
        self.cb[key_match].hide()

    def update_text_data(self, data):
        # cursor = self.show_editor.textCursor()
        # cursor.movePosition(QTextCursor.End)
        # self.show_editor.setTextCursor(cursor)
        # self.show_editor.ensureCursorVisible()
        #print("item")
        if data != "":
            self.show_editor.insertPlainText(data)
            self.show_editor.insertPlainText("\n")
        else:
            pass


    #启动跟踪线程
    def update_thread(self):
        print("start")
        self.update_data_thread.start()

    def store_title(self):
        if len(self.title_name) > 0:
            self.title_name = []
        for i in range(0, len(self.cb)):
            if self.cb[i].isChecked():
                self.title_name.append(self.cb[i].text())

    def mul_file(self):
        source = self.sender()
        #self.file_make.clicked.connect(lambda:do_file.do_file(self.json_file_path.text()))
        if len(self.title_name) > 0:
            self.title_name = []
        for i in range(0, len(self.cb)):
            if self.cb[i].isChecked():
                self.title_name.append(self.cb[i].text())
        
    def openfile(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         "D:/",
                                                         "Text Files (*.txt)");
        print (filename, filetype)
        if filename != '':
            self.r_text=open(filename,'r').read()
            self.show_editor.setPlainText(self.r_text)
    

    def closeEvent(self, event):
        #我们显示一个带有两个按钮的消息框：Yes和No。
        #第一个字符串出现在标题栏上。
        #第二个字符串是对话框显示的消息文本。
        #第三个参数指定出现在对话框中的按钮的组合。
        #最后一个参数是默认按钮。
        #它是初始键盘焦点的按钮。 返回值存储在答复变量中
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()        
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
