import sqlite3
from PySide6.QtWidgets import (QWidget, QLabel,
                               QLineEdit, QHBoxLayout,
                               QPushButton, QGroupBox,
                               QVBoxLayout, QTableWidget)


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        #https://www.youtube.com/watch?v=6Q0h8FNaB7U

        self.setWindowTitle("SQLite DataBase")
        self.setGeometry(700, 500, 700, 150)

        #Create QLabel
        name_label = QLabel("Name")
        profession_label = QLabel("Profession")
        time_worked_by_month_label = QLabel("Time worked")
        salaries_label = QLabel("Salaries")

        #Create QLine Edit
        self.name_line_edit = QLineEdit()
        self.profession_label = QLineEdit()
        self.time_worked_by_month_label = QLineEdit()
        self.salaries_label = QLineEdit()

        #Push buttons for manipulating with data
        button_add_data = QPushButton("Add new row")
        button_add_data.clicked.connect(self.add_data)

        button_update_data = QPushButton("Update selected row")
        button_update_data.clicked.connect(self.update_data)

        button_insert_data = QPushButton("Insert demo data")
        button_insert_data.clicked.connect(self.insert_data)

        button_load_data = QPushButton("Load data")
        button_load_data.clicked.connect(self.load_data)

        button_call_data = QPushButton("Extra data")
        button_call_data.clicked.connect(self.call_data)

        button_delete_data = QPushButton("Delete data")
        button_delete_data.clicked.connect(self.delete_data)

        #Name QLabel and Name Qlineedit form horizontal layout
        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(name_label)
        h_layout1.addWidget(self.name_line_edit)

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(profession_label)
        h_layout2.addWidget(self.profession_label)

        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(time_worked_by_month_label)
        h_layout3.addWidget(self.time_worked_by_month_label)

        h_layout4 = QHBoxLayout()
        h_layout4.addWidget(salaries_label)
        h_layout4.addWidget(self.salaries_label)

        #QPushButtons horizontal layout
        h_layout5 = QHBoxLayout()
        h_layout5.addWidget(button_add_data)
        h_layout5.addWidget(button_update_data)

        #Grouplabels, edits and pushbuttons
        add_form = QGroupBox("ADD NEW EMPLOYEE")

        #Lay out all items in group vertically
        form_layout = QVBoxLayout()

        form_layout.addLayout(h_layout1)
        form_layout.addLayout(h_layout2)
        form_layout.addLayout(h_layout3)
        form_layout.addLayout(h_layout4)
        form_layout.addLayout(h_layout5)
        add_form.setLayout(form_layout)

        #Create Table
        self.table = QTableWidget(self)
        self.table.setMaximumWidth(700)

        self.table.setColumnCount(4)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 100)

        self.table.setHorizontalHeaderLabels(["NAME", "PROFESSION", "TIME WORKED", "SALARIES"])


        #Display all elements vertically
        layout = QVBoxLayout()
        layout.addWidget(add_form)
        layout.addWidget(self.table)
        layout.addWidget(button_insert_data)
        layout.addWidget(button_load_data)
        layout.addWidget(button_call_data)
        layout.addWidget(button_delete_data)
        self.setLayout(layout)


    def create_connection(self):
        return sqlite3.connect("employers.db")


    def insert_data(self):
        self.cursor = self.create_connection().cursor()

        self.cursor.execute("create table employees_list (Name text, Profession text, TimeWorked float, Salaries integer)")

        self.list_of_employers = [
            ('Olga', 'Engineer', 160, 80000),
            ('Dima', 'Product placement', 180, 100000),
            ('Marina', 'Eichar', 100, 65000)
        ]


    def add_data(self):
        pass

    def load_data(self):
        pass

    def call_data(self):
        pass

    def update_data(self):
        pass

    def delete_data(self):
        pass