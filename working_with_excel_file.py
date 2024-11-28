import os
import openpyxl
from settings.settings import EXPANDED

test_direction: str = r"test direction\\"
file_name = r'Krasnopol'


# data = pd.read_excel(excel_file_old + expanded)
# data.to_excel(excel_file_old + '.2' + expanded)

class GetExpandedFile:
	def get_index_for_last_file(self, direction:str, file_check: str) -> int:
		"""
		direction - Директория в которой будут искаться файлы
		file_check - Файл который будут искать в direction
		:return: -1 if there is no file
			0 if file have not index
			else return the index of the last file
		"""
		set_files = set(os.listdir(direction))
		
		for index in range(101):
			if index != 0:
				file = file_check + f'.{index}' + expanded
			else:
				file = file_check + expanded
			if not file in set_files:
				return index - 1

class ModifyExistingExcelFile(GetExpandedFile):
	def __init__(self, path_by_directory:str, name_excel_file:str, name_sheet='Сопроводительный лист'):
		
		last_index_file = self.get_index_for_last_file(path_by_directory, name_excel_file)
		
		self.wb = openpyxl.load_workbook(name_excel_file)
		self.sheet = self.wb[name_sheet]
	
	def mode_excel_file(self, cell: str, value):
		self.sheet[cell].value = value
	
	def save_changed_excel_file(self, name_new_file):
		self.wb.save(name_new_file)


def test_start(object_class):
	excel_file = object_class(test_direction + file_name + expanded)
	# name_cells = (f'B{el}' for el in range(10, 18))
	# value_cells = ('05.015.09', '-B-C', 13560, '6R777', 660, '4M', 780, 777)
	# for index, name_cell in enumerate(name_cells):
	# 	change_excel_file.mode_excel_file(name_cell, value_cells[index])
	for index in range(1, 5):
		excel_file.save_changed_excel_file(test_direction + file_name + f'.{index}' + '.xlsx')


if __name__ == '__main__':
	# test_start(ModifyExistingExcelFile)
	# test = GetExpandedFile().get_index_for_last_file(test_direction, file_name)
	print(EXPANDED)
	# pass
