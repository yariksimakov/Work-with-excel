# ИЗМЕНИТЬ В СЛУЧАЕ СМЕНЫ ДИРРЕКТОРИИ ФАЙЛА
DIRECTION_BY_SAVE = 'settings' # Папка где лежат настройки приложения

# Для работы с экселем
SHEET_NAME: str = 'Сопроводительный лист'
EXPANDED_EXCEL_FILE = '.xlsx' # Расширение эксель файлов
MAX_INDEX_EXCEL_FILE = 30 # Максимальный индекс эксель файла

# Файл для сохранения настроек пути
path_to_file_save_lineEdit = DIRECTION_BY_SAVE + r'\\' + 'linEdit_excel_file.pkl'

# Файл для сохранения табличных данных
path_to_file_save_table_data = DIRECTION_BY_SAVE + r'\\' + 'tableData.json'