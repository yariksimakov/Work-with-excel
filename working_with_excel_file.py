import os
import openpyxl
from settings.settings import EXPANDED, MAX_INDEX_EXCEL_FILE

test_direction: str = r"test direction\\"
file_name = r'Krasnopol'


# data = pd.read_excel(excel_file_old + expanded)
# data.to_excel(excel_file_old + '.2' + expanded)

class GetExpandedFile:
	def get_index_for_last_file(self, direction: str, file_check: str) -> int:
		"""
		direction - Directory in whish files will be searched
		file_check - The name of the file whose last index we will search for
		:return: -1 if there is no file
			0 if file have not index
			else return the index of the last file
		"""
		set_files = set(os.listdir(direction))
		
		for index in range(MAX_INDEX_EXCEL_FILE + 1):
			if index == 1:
				""" Это необходимо так как индекс 1 у файлов небывает"""
				continue
			if index != 0:
				file = file_check + f'.{index}' + EXPANDED
			else:
				file = file_check + EXPANDED
			if not file in set_files:
				return index - 1


class ModifyExistingExcelFile(GetExpandedFile):
	def __init__(self, path_to_directory: str, template_excel_file: str,
	             name_new_file: str, name_sheet='Сопроводительный лист'):
		self.last_index_file = self.get_index_for_last_file(path_to_directory, name_new_file)
		self.path_to_create_new_file = path_to_directory + '\\' + name_new_file
		
		self.wb = openpyxl.load_workbook(template_excel_file)
		self.sheet = self.wb[name_sheet]
	
	def mode_excel_file(self, cell: str, value):
		self.sheet[cell].value = value
	
	def save_changed_excel_file(self) -> None:
		if self.last_index_file == -1:
			self.wb.save(self.path_to_create_new_file + EXPANDED)
		elif self.last_index_file == 0:
			self.wb.save(self.path_to_create_new_file + '.2' + EXPANDED)
		else:
			self.wb.save(self.path_to_create_new_file + f'.{self.last_index_file + 1}' + EXPANDED)


def test_start():
	create_excel_file = ModifyExistingExcelFile('test direction', 'test direction\\Krasnopol.xlsx',
	                                     '0001')
	create_excel_file.save_changed_excel_file()


if __name__ == '__main__':
	test_start()
	# test = GetExpandedFile().get_index_for_last_file(test_direction, file_name)
	# pass

# D:/Python Projects/Application/test direction/Krasnopol.xlsx
