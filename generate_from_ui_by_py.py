import re
import os

path_to_directory = 'D:\Work with excel\Work-with-excel'

def generate_from_ui_by_py(path: str):
	files = os.listdir(path)
	ui_list = []
	pattern = re.compile(r".*\.ui")
	for file in files:
		if pattern.match(file):
			ui_list.append(file)
	
	for file in ui_list:
		file_path = os.path.join(path, file)
		file_name_without_extension = file_path.split(os.sep)[-1].removesuffix(".ui")
		cmd = f"pyside6-uic {file_path} -o {path}{os.sep}{file_name_without_extension}.py"
		os.popen(cmd)

if __name__ == '__main__':
	generate_from_ui_by_py(path_to_directory)
