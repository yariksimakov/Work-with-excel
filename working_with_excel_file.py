import openpyxl, os
from win32file import GetFileSize

# import xlwings as xw
# from adodbapi.examples.xls_read import sheet

# from win32lz import GetExpandedName
from settings.settings import EXPANDED_EXCEL_FILE, MAX_INDEX_EXCEL_FILE


class GetExpandedFile:
	def get_index_for_last_file(self, direction: str, file_check: str) -> int:
		"""
		direction - Путь до директории в которой будем искать файл
		file_check - Имя файла у которого будем искать последний индекс
		:return: -1 Если нету файла
			0 если файл без индекса
			else возвращаем последний индекс файла
		"""
		set_files = set(os.listdir(direction))

		for index in range(MAX_INDEX_EXCEL_FILE + 1):
			if index == 1:
				""" Это необходимо так как индекс 1 у файлов небывает"""
				continue

			if index != 0:
				file = file_check + f'.{index}'
			else:
				file = file_check

			if not file + EXPANDED_EXCEL_FILE in set_files:
				return index - 1


class ModifyExcelFileCreatedUsingTemplate(GetExpandedFile):
	def __init__(self, path_to_directory: str, template_excel_file: str,
	             name_new_file: str, name_sheet='Сопроводительный лист'):

		self.last_index_file = self.get_index_for_last_file(path_to_directory, name_new_file)
		self.path_to_create_new_file = path_to_directory + r'\\' + name_new_file

		self.wb = openpyxl.load_workbook(template_excel_file)
		self.sheet = self.wb[name_sheet]

	def mode_excel_file(self, cell: str, value):
		self.sheet[cell].value = value

	@property
	def save_excel_file(self) -> None:
		if self.last_index_file == -1:
			self.wb.save(self.path_to_create_new_file + EXPANDED_EXCEL_FILE)
		elif self.last_index_file == 0:
			self.wb.save(self.path_to_create_new_file + '.2' + EXPANDED_EXCEL_FILE)
		else:
			self.wb.save(self.path_to_create_new_file + f'.{self.last_index_file + 1}' + EXPANDED_EXCEL_FILE)


class CreateManyExcelFilesByTemplate(GetExpandedFile):
	"""
	При инициализации сразу создает эксель файлы
	"""
	def __init__(self, path_to_directory: str, template_excel_file: str, list_of_names: list,
	             name_sheet='Сопроводительный лист'):
		self.wb = openpyxl.load_workbook(template_excel_file)
		self.sheet = self.wb[name_sheet]
		for name in list_of_names:
			self.last_index_file = self.get_index_for_last_file(path_to_directory, name)
			path_to_create_new_file = path_to_directory + r'\\' + name
			self.save_excel_file(path_to_create_new_file)

	def save_excel_file(self, path_to_create_new_file) -> None:
		if self.last_index_file == -1:
			self.wb.save(path_to_create_new_file + EXPANDED_EXCEL_FILE)
		elif self.last_index_file == 0:
			self.wb.save(path_to_create_new_file + '.2' + EXPANDED_EXCEL_FILE)
		else:
			self.wb.save(path_to_create_new_file + f'.{self.last_index_file + 1}' + EXPANDED_EXCEL_FILE)


def test_start():
	create_excel_file = ModifyExcelFileCreatedUsingTemplate(r'D:\Work with excel\Work-with-excel\test direction',
	                                                        r'test direction/Krasnopol.xlsm',
	                                                        '00010')
	create_excel_file.mode_excel_file("A20", 'Na montag')
	create_excel_file.save_excel_file


if __name__ == '__main__':
	path_test_file = r'test direction\\Krasnopol.xlsm'
# test_start()

# test = GetExpandedFile().get_index_for_last_file(test_direction, file_name)
# pass

# D:/Python Projects/Application/test direction/Krasnopol.xlsx
