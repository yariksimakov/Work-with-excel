from PySide6.QtWidgets import QApplication
import sys
from MainWindow import MainWindow


	# """https://ru.stackoverflow.com/questions/1538874/%D0%9D%D0%B0%D0%B6%D0%B0%D1%82%D0%B8%D0%B5-%D0%BA%D0%BB%D0%B0%D0%B2%D0%B8%D1%88%D0%B8-enter-%D0%B2-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B5-qtablewidget"""
	# with open('save_params\\linEdit_excel_file.pkl', 'rb') as file:
	# 	param = pickle.load(file)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()
# direction_path = os.path.dirname(os.path.abspath(__file__))
# generate_from_ui_by_py(direction_path)
