from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt, QEvent
from PySide6.QtCore import QObject, Slot, Signal, QThreadPool, QRunnable
from MainWidget import Ui_MainWindow
import pickle, os, re, traceback, sys
import json

# Мои файлы
from settings.settings import DIRECTION_BY_SAVE, path_to_file_save_lineEdit, path_to_file_save_table_data
from working_with_excel_file import ModifyExistingExcelFile


class WorkerSignals(QObject):
	finished = Signal()
	error = Signal(tuple)
	result = Signal(object)


class WorkerThreads(QRunnable):
	def __init__(self, fn, *args, **kwargs):
		super().__init__()
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.signals = WorkerSignals()

	# self.kwargs['progress_callback'] = self.signals.progress

	@Slot()
	def run(self):
		try:
			self.fn(*self.args, **self.kwargs)
		except:
			traceback.print_exc()
			exctype, value = sys.exc_info()[:2]
			self.signals.error.emit((exctype, value, traceback.format_exc()))
		finally:
			self.signals.finished.emit()


class TableForWorkExcelFile():
	def __init__(self, main_window):
		Table = main_window.tableWidget_CC
		column = Table.columnCount()
		for i in range(column):
			if i % 2 == 0:
				Table.horizontalHeaderItem(i).setToolTip('Номер клетки')
			else:
				Table.horizontalHeaderItem(i).setToolTip('Данные')

		try:
			with open(path_to_file_save_table_data, 'r') as file:
				information_about_table = json.load(file)
			table_contents: str = information_about_table['data_table_save']
			rows: int = len(table_contents)

			if Table.rowCount() <= rows:
				Table.setRowCount(rows + 1)
			if table_contents:
				for row in range(rows):
					column: int = 0
					for cell_location, data_for_cell in table_contents[row]:
						if cell_location is not None:
							Table.setItem(row, column, QTableWidgetItem(cell_location))
						if data_for_cell is not None:
							Table.setItem(row, column+1, QTableWidgetItem(data_for_cell))
						column += 2
		except FileNotFoundError('Таблица пуста') as err:
			print(err)
			if Table.rowCount() < 6:
				Table.setRowCount(6)


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.load_data_for_lineEdit()

		self.signals = WorkerSignals()
		self.signals.result.connect(self.print_output)
		# self.signals.finished.connect(self.thread_complete)

		self.pushButton_excel_template.clicked.connect(self.open_dialog_box_excel_template)
		self.pushButton_path_creating_file.clicked.connect(self.open_dialog_box_path_creating_file)
		self.pushButton_plate_info.clicked.connect(self.open_dialog_box_plate_info)
		self.pushButton_save_default_settings.clicked.connect(self.save_by_default_paths)

		self.threadpool = QThreadPool()
		# print(f"Multithreading with maxim {self.threadpool.maxThreadCount()} threads")
		TableForWorkExcelFile(self)
		self.tableWidget_CC.installEventFilter(self)
		self.pushButton_add_new_line.clicked.connect(self.add_new_line)
		self.pushButton_del_last_line.clicked.connect(self.del_last_line)
		self.pushButton_save_cell.clicked.connect(self.save_default_table_data)
		self.pushButton_create_CC.clicked.connect(self.create_file_by_template_using_external_thread)

		self.pushButton_create_files.clicked.connect(self.create_files_by_template_using_external_thread)

	def eventFilter(self, source, event):
		if (event.type() == QEvent.KeyPress and event.key() in (Qt.Key_Return, Qt.Key_Enter)):
			current = self.tableWidget_CC.currentIndex()
			nextIndex = current.sibling(current.row() + 1, current.column())
			nextIndexColumn = current.sibling(0, current.column() + 1)

			if nextIndex.isValid():
				self.tableWidget_CC.setCurrentIndex(nextIndex)
			# self.tableWidget_CC.edit(nextIndex)
			elif nextIndexColumn.isValid():
				# self.tableWidget_CC.closeEditor(current)
				self.tableWidget_CC.setCurrentIndex(nextIndexColumn)
			# self.tableWidget_CC.edit(nextIndexColumn)
			return super().eventFilter(source, event)
		return super().eventFilter(source, event)

	@Slot()
	def create_file_by_template_using_external_thread(self):
		data_table_CC = self.get_data_from_table_CC_without_None()
		name_new_excel_file = self.lineEdit_number_CC.text()

		match = re.fullmatch(r'\d{5,}', name_new_excel_file)
		if not match:
			self.signals.result.emit("Неправильный номер КП")
			raise ValueError('Неправильно набран номер эксель файла')

		excel_template = self.lineEdit_excel_template.text()
		path_creating_file = self.lineEdit_path_creating_file.text()

		worker = WorkerThreads(self.create_excel_file_by_template,
							   path_creating_file, excel_template,
							   name_new_excel_file, data_table_CC)

		worker.signals.error.connect(self.print_output)
		worker.signals.finished.connect(self.thread_complete)
		self.threadpool.start(worker)

	# worker.signals.result.connect(self.print_output)

	@Slot()
	def create_files_by_template_using_external_thread(self):
		name_from_excel_file = self.lineEdit_from.text()
		name_to_excel_file = self.lineEdit_to.text()
		path_creating_file = self.lineEdit_path_creating_file.text()
		excel_template = self.lineEdit_excel_template.text()

		match_from = re.fullmatch(r'\d{5,}', name_from_excel_file)
		match_to = re.fullmatch(r'\d{5,}', name_from_excel_file)
		if not match_from or not match_to or int(name_from_excel_file) >= int(name_to_excel_file):
			self.signals.result.emit("Неправильный номер КП")
			raise ValueError('Неправильно набран номер эксель файла')

		# count_zero_from_excel_file = next(i for i, el in enumerate(name_from_excel_file) if el != '0')
		length_name_file = len(name_from_excel_file)
		# Это не разумно - переделать логику создание множества ексель файлов
		for number_file in range(int(name_from_excel_file), int(name_to_excel_file) + 1):
			length_name_creating_file = len(str(number_file))
			if length_name_creating_file < length_name_file:  # Проверка есть ли в номере файла нули перед цифрами
				difference = length_name_file - length_name_creating_file
				name_creating_file = '0' * difference + str(number_file)
			else:
				name_creating_file = str(number_file)

			worker = WorkerThreads(self.create_excel_file_by_template,
								   path_creating_file, excel_template,
								   name_creating_file, [])
			worker.signals.error.connect(self.print_output)
			self.threadpool.start(worker)
			worker.signals.finished.connect(self.thread_complete)

	def create_excel_file_by_template(self, path_creating_file, excel_template, name_new_excel_file, data_table_CC):
		create_new_excel_file = ModifyExistingExcelFile(path_creating_file, excel_template, name_new_excel_file)
		if data_table_CC:
			for cell, data in data_table_CC:
				create_new_excel_file.mode_excel_file(cell, data)

		create_new_excel_file.save_changed_excel_file()

	def print_output(self, *args, **kwargs) -> None:
		# item = QMessageBox.warning(self, 'Внимание', "<b style='color: green;'>Сохранение прошло успешно</b>")
		# self.listWidget_result.addItem(item)
		# self.listWidget_result.addItems(args)
		print(*args)

	def thread_complete(self):
		print('Работа внешнего потока завершена')
		# print("Thread complete successful!")

	@Slot()
	def add_new_line(self) -> None:
		row_position = self.tableWidget_CC.rowCount()
		self.tableWidget_CC.insertRow(row_position)
		# self.tableWidget_CC.setVerticalHeaderItem(row_position-1, QTableWidgetItem())

	@Slot()
	def del_last_line(self) -> None:
		max_row = self.tableWidget_CC.rowCount()
		if max_row == 0:
			item = QMessageBox.warning(self, 'Внимание', "<b style='color: red;'> Нельзя удалить то, чего нету!</b>")
			self.tableWidget_CC.editItem(item)
		else:
			self.tableWidget_CC.removeRow(max_row - 1)

	@Slot()
	def save_default_table_data(self):
		data_table_CC = self.get_data_from_table_CC()
		dictionary = {'data_table_save': data_table_CC}
		with open(path_to_file_save_table_data, 'w') as file:
			json.dump(dictionary, file)
		self.signals.result.emit("Таблица сохранена")

	def get_data_from_table_CC_without_None(self) -> list:
		"""
		:return: [(cell, data_cell),(cell, data_cell), ...]
		"""
		table = self.tableWidget_CC
		rows, columns = table.rowCount(), table.columnCount()
		data = list()
		column_i = 0
		while column_i <= columns:
			for row_i in range(rows):
				cell = table.item(row_i, column_i)
				data_for_cell = table.item(row_i, column_i + 1)
				if cell is not None and data_for_cell is not None:
					cell_text = cell.text()
					data_for_cell_text = data_for_cell.text()
					if cell_text and data_for_cell_text:
						data.append((cell_text, data_for_cell_text))
			column_i += 2
		return data

	def get_data_from_table_CC(self) -> list:
		"""
		:return:[
		[(cell, data_cell),  (cell, None), ...],
		[(cell, data_cell),  (cell, None), ...],
		...
		]
		"""
		table = self.tableWidget_CC
		rows, columns = table.rowCount(), table.columnCount()
		data_table_save = []
		for row in range(rows):
			row_table_save = []
			for column in range(0, columns, 2):
				cell_location = table.item(row, column)
				data_for_cell = table.item(row, column + 1)
				if cell_location is not None and data_for_cell is not None:
					row_table_save.append((cell_location.text(), data_for_cell.text()))
				elif cell_location is not None:
					row_table_save.append((cell_location.text(), None))

			if row_table_save:
				data_table_save.append(row_table_save)
		return data_table_save

	@Slot()
	def open_dialog_box_excel_template(self) -> None:
		filename = QFileDialog.getOpenFileName()
		self.lineEdit_excel_template.setText(filename[0])

	@Slot()
	def open_dialog_box_path_creating_file(self) -> None:
		filename = QFileDialog.getExistingDirectory()
		self.lineEdit_path_creating_file.setText(filename)

	@Slot()
	def open_dialog_box_plate_info(self):
		filename = QFileDialog.getOpenFileName()
		self.lineEdit_plate_info.setText(filename[0])

	def get_bool_checking_directory(self, path_directory: str) -> bool:
		if path_directory in set(os.listdir()):
			return True
		return False

	@Slot()
	def save_by_default_paths(self):
		data_line = (self.lineEdit_excel_template.text(),
					 self.lineEdit_path_creating_file.text(),
					 self.lineEdit_plate_info.text())
		with open(path_to_file_save_lineEdit, 'wb') as file:
			pickle.dump(data_line, file)
		self.signals.result.emit("Настройки путей сохранены успешно")

	def load_data_for_lineEdit(self) -> None:
		"""
		Подгружает в настройки сохраненые пути.
		:return: None
		"""
		if not self.get_bool_checking_directory(DIRECTION_BY_SAVE):
			self.save_by_default_paths()

		with open(path_to_file_save_lineEdit, 'rb') as file:
			path_by_settings: tuple = pickle.load(file)
			lineEdit_object: tuple = (
				self.lineEdit_excel_template, self.lineEdit_path_creating_file, self.lineEdit_plate_info)

			for index, path in enumerate(path_by_settings):
				if path:
					lineEdit_object[index].setText(path)


if __name__ == '__main__':
	"""https://ru.stackoverflow.com/questions/1538874/%D0%9D%D0%B0%D0%B6%D0%B0%D1%82%D0%B8%D0%B5-%D0%BA%D0%BB%D0%B0%D0%B2%D0%B8%D1%88%D0%B8-enter-%D0%B2-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B5-qtablewidget"""
	with open('save_params/linEdit_excel_file.pkl', 'rb') as file:
		param = pickle.load(file)
	print(param)
