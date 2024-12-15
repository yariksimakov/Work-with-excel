from PySide6.QtWidgets import QMainWindow, QFileDialog, QLineEdit, QMessageBox
from PySide6.QtCore import Qt, QEvent, QThreadPool
from PySide6.QtCore import QObject, Slot, Signal, QThreadPool, QRunnable
from MainWidget_by_working_excel import Ui_MainWindow

from settings.settings import DIRECTION_BY_SAVE, LINE_EDIT
from working_with_excel_file import ModifyExistingExcelFile
import pickle, os, re, traceback, sys


class WorkerSignals(QObject):
	finished = Signal()
	error = Signal(tuple)
	progress = Signal(int)


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
	def __init__(self, parent):
		Table = parent.tableWidget_CC
		column = Table.columnCount()
		for i in range(column):
			if i % 2 == 0:
				Table.horizontalHeaderItem(i).setToolTip('Номер клетки')
			else:
				Table.horizontalHeaderItem(i).setToolTip('Данные')


class MainWindow(QMainWindow, Ui_MainWindow):
	__path_to_file_save_lineEdit = DIRECTION_BY_SAVE + r'\\' + LINE_EDIT

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)

		self.load_data_for_lineEdit()

		self.pushButton_excel_template.clicked.connect(self.open_dialog_box_excel_template)
		self.pushButton_path_creating_file.clicked.connect(self.open_dialog_box_path_creating_file)
		self.pushButton_plate_info.clicked.connect(self.open_dialog_box_plate_info)
		self.pushButton_save_default_settings.clicked.connect(self.save_default_settings)

		self.threadpool = QThreadPool()
		# print(f"Multithreading with maxim {self.threadpool.maxThreadCount()} threads")
		TableForWorkExcelFile(self)
		self.tableWidget_CC.installEventFilter(self)
		self.pushButton_add_new_line.clicked.connect(self.add_new_line)
		self.pushButton_del_last_line.clicked.connect(self.del_last_line)

		self.pushButton_create_CC.clicked.connect(self.create_excel_file_by_template_using_external_thread)

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
	def create_excel_file_by_template_using_external_thread(self):
		data_table_CC = self.get_data_from_table_CC()
		name_new_excel_file = self.lineEdit_number_CC.text()

		match = re.fullmatch(r'\d{5,}', name_new_excel_file)
		if not match:
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

	def create_excel_file_by_template(self, path_creating_file, excel_template, name_new_excel_file, data_table_CC):
		create_new_excel_file = ModifyExistingExcelFile(path_creating_file, excel_template, name_new_excel_file)
		if data_table_CC:
			for cell, data in data_table_CC:
				create_new_excel_file.mode_excel_file(cell, data)

		create_new_excel_file.save_changed_excel_file()


	def print_output(self, *args, **kwargs) -> None:
		print(args)
		print(kwargs)

	def thread_complete(self):
		print("Thread complete successful!")

	@Slot()
	def add_new_line(self) -> None:
		row_podition = self.tableWidget_CC.rowCount()
		self.tableWidget_CC.insertRow(row_podition)

	@Slot()
	def del_last_line(self) -> None:
		max_row = self.tableWidget_CC.rowCount()
		if max_row == 0:
			item = QMessageBox.warning(self, 'Внимание', "<b style='color: red;'> Нельзя удалить то чего нету!</b>")
			self.listWidget_result.addItem(item)
		else:
			self.tableWidget_CC.removeRow(max_row-1)

	def get_data_from_table_CC(self) -> list:
		"""
		:return: [(cell, data_cell),(cell, data_cell), ...]
		"""
		table = self.tableWidget_CC
		row, column = table.rowCount(), table.columnCount()
		data = list()
		column_i = 0
		while column_i <= column:
			for row_i in range(row):
				cell = table.item(row_i, column_i)
				cell_data = table.item(row_i, column_i + 1)
				if cell is not None and cell_data is not None:
					data.append((cell.text(), cell_data.text()))
			column_i += 2
		return data

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
	def save_default_settings(self):
		data_line = (self.lineEdit_excel_template.text(),
					 self.lineEdit_path_creating_file.text(),
					 self.lineEdit_plate_info.text())
		with open(self.__path_to_file_save_lineEdit, 'wb') as file:
			pickle.dump(data_line, file)

	def load_data_for_lineEdit(self):
		if not self.get_bool_checking_directory(DIRECTION_BY_SAVE):
			self.save_default_settings()

		with open(self.__path_to_file_save_lineEdit, 'rb') as file:
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
