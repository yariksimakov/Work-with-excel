from PySide6.QtWidgets import QMainWindow, QFileDialog, QLineEdit
from PySide6.QtCore import Slot, Signal, Qt, QEvent
import pickle, os
from MainWidget_by_working_excel import Ui_MainWindow
from settings.settings import DIRECTION_BY_SAVE, LINE_EDIT
from working_with_excel_file import ModifyExistingExcelFile


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
	__path_to_file_save_lineEdit = DIRECTION_BY_SAVE + '/' + LINE_EDIT
	
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		
		self.load_data_for_lineEdit()
		
		self.pushButton_excel_template.clicked.connect(self.open_dialog_box_excel_template)
		self.pushButton_path_creating_file.clicked.connect(self.open_dialog_box_path_creating_file)
		self.pushButton_plate_info.clicked.connect(self.open_dialog_box_plate_info)
		self.pushButton_save_default_settings.clicked.connect(self.save_default_settings)
		
		TableForWorkExcelFile(self)
		self.tableWidget_CC.installEventFilter(self)
		self.pushButton_create_CC.clicked.connect(self.create_new_excel_by_template)
		
		
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
	
	def create_new_excel_by_template(self):
		data_table_CC = self.get_data_by_table_CC()
		
		print(data_table_CC)
	
	def get_data_by_table_CC(self) -> list:
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
		if not self.get_bool_checking_directory(DIRECTION_BY_SAVE):
			os.mkdir(DIRECTION_BY_SAVE)
		
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
			
			del path_by_settings, lineEdit_object


if __name__ == '__main__':
	"""https://ru.stackoverflow.com/questions/1538874/%D0%9D%D0%B0%D0%B6%D0%B0%D1%82%D0%B8%D0%B5-%D0%BA%D0%BB%D0%B0%D0%B2%D0%B8%D1%88%D0%B8-enter-%D0%B2-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B5-qtablewidget"""
	with open('save_params/linEdit_excel_file.pkl', 'rb') as file:
		param = pickle.load(file)
	
	print(param)
