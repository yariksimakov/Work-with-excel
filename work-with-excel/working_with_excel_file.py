from pprint import pprint
import xlwings as xw
import pandas as pd
import openpyxl

excel_file_old: str = 'Krasnopol'
expanded: str = '.xlsm'
sheet_name = 'Сопроводительный лист'


# data = pd.read_excel(excel_file_old + expanded)
# data.to_excel(excel_file_old + '.2' + expanded)


class ModifyExistingExcelFile:
	def __init__(self, name_excel_file, name_sheet='Сопроводительный лист'):
		self.wb = openpyxl.load_workbook(name_excel_file)
		self.sheet = self.wb[name_sheet]
	
	def mode_excel_file(self, cell: str, value):
		self.sheet[cell].value = value
	
	def save_changed_excel_file(self, name_new_file):
		self.wb.save(name_new_file)


def test_start(object_class):
	change_excel_file = object_class(excel_file_old + expanded)
	name_cells = (f'B{el}' for el in range(10, 18))
	value_cells = ('05.015.09', '-B-C', 13560, '6R777', 660, '4M', 780, 777)
	for index, name_cell in enumerate(name_cells):
		change_excel_file.mode_excel_file(name_cell, value_cells[index])
	change_excel_file.save_changed_excel_file(excel_file_old + '.2' + '.xlsx')


class CreateNewExcelFileByTemplate:
	def __init__(self, path_to_directory_where_file_will_be_created:str,  path_to_template:str = r"D:\Python Projects\Application\work-with-excel\Krasnopol.xlsx"):
		wb = xw.Book(path_to_template)
		sheet = wb.sheets[sheet_name]
		print(sheet['B10'])




if __name__ == '__main__':
	CreateNewExcelFileByTemplate('pass')
