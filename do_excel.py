#coding=utf-8
#Author:Guo Xiangchen

import xlrd
import global_list


def do_excel(path):
	ExcelFile = xlrd.open_workbook(path)
	try:
		if len(ExcelFile.sheet_names()) > 1:
			if "iOS" in ExcelFile.sheet_names():
				sheet = ExcelFile.sheet_by_name('iOS')
				print ("!")
		else:
			sheet = ExcelFile.sheet_by_index()
		name_rows = sheet.row_values(1)
		if '友盟埋点' in name_rows:
			key_index = name_rows.index("友盟埋点")
		if '事件' in name_rows:
			value_index = name_rows.index("事件")
		for i in range(2, int(sheet.nrows)):
			global_list.excel_dict[sheet.cell_value(i, key_index)] = sheet.cell_value(i, value_index)
		#print (global_list.excel_dict)
	except:
		print ("Excel炸了")


if __name__ == '__main__':
	path = "D:/04 code/maidiancheck/App-搜索需求-V6.5埋点-V1.0.xlsx"
	do_excel(path)
