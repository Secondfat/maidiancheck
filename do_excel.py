#coding=utf-8
#Author:Guo Xiangchen

import xlrd
import global_list


def do_excel(path):
	ExcelFile = xlrd.open_workbook(path)
	print (ExcelFile.sheet_names())
	#try:
	if len(ExcelFile.sheet_names()) > 1:
		for name_test in ExcelFile.sheet_names():
			print (name_test)
			if "iOS" == name_test or "ios" == name_test:
				os_name = "iOS"
			if "Android" ==name_test or "android" == name_test:
				os_name = "Android"
			sheet = ExcelFile.sheet_by_name(os_name)
			#print(os_name)
			store_dic(os_name, sheet)
	else:
		print("Excel no sheet")
	print(global_list.excel_dict)
		# name_rows = sheet.row_values(1)
		# if '友盟埋点' in name_rows:
		# 	key_index = name_rows.index("友盟埋点")
		# if '事件' in name_rows:
		# 	value_index = name_rows.index("事件")
		# for i in range(2, int(sheet.nrows)):
		# 	global_list.excel_dict['iOS'][sheet.cell_value(i, key_index)] = sheet.cell_value(i, value_index)
		# print (global_list.excel_dict)

	#except:
		#print ("Excel炸了")

def store_dic(os_name, sheet):
	name_rows = sheet.row_values(1)
	if '友盟埋点' in name_rows:
		key_index = name_rows.index("友盟埋点")
	if '事件' in name_rows:
		value_index = name_rows.index("事件")
	if '主id' in name_rows:
		id_fathere = name_rows.index("主id")
	if '子id' in name_rows:
		id_son = name_rows.index("子id")
	if os_name == "iOS":
		for i in range(2, int(sheet.nrows)):
			global_list.excel_dict[os_name][sheet.cell_value(i, key_index)] = sheet.cell_value(i, value_index)
	elif os_name == "Android":
		for i in range(2, int(sheet.nrows)):
			id_all = str(int(sheet.cell_value(i, id_fathere))) + ";" + str(int(sheet.cell_value(i, id_son)))
			global_list.excel_dict[os_name][id_all] = sheet.cell_value(i, value_index)



#if __name__ == '__main__':
	#path = "D:/04 code/maidiancheck/App-搜索需求-V6.5埋点-V1.0.xlsx"
	#do_excel(path)
