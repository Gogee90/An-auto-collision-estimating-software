# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculation.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlRelation
from PyQt5.QtCore import Qt
from docxtpl import DocxTemplate
from .materials import Materials as Sum_table
import sqlite3
from docx.shared import Pt
import sys
import os


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def autocomplete(self, table, base,  model):
        con = sqlite3.connect('ocenka.db')
        c = con.cursor()
        query = ("SELECT {} FROM {}").format(table, base)
        c.execute(query)
        result = c.fetchall()
        table_list = []
        for column in result:
            for mark in column:
                table_list.append(str(mark))
        model.setStringList(table_list)
        c.close()

    def queries(self, table, column):
        summary = ("SELECT sum({}) FROM {}").format(table, column)
        return summary
        
    def connection(self, query):
        con = sqlite3.connect('ocenka.db')
        c = con.cursor()
        c.execute(query)
        result = c.fetchall()
        c.close()
        return result

    def open_table(self, base):
        shit = []
        for number, columns in enumerate(self.connection(base)):
            for count, data in enumerate(columns):
                shit.append(str(data))
        return shit

    def make_dict(self, view):
        contents = []
        for row, columns in enumerate(self.connection(view)):
            rows = ['cols'*len(str(row))]
            col = [columns]
            records = dict(zip(rows, col))
            contents.append(records)
        return contents

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(506, 401)
        self.header_label = QtWidgets.QLabel(self)
        self.header_label.setGeometry(QtCore.QRect(100, 10, 303, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.header_label.setFont(font)
        self.header_label.setObjectName("header_label")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 360, 300, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exit_button = QtWidgets.QPushButton(self.layoutWidget)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout.addWidget(self.exit_button)
        self.report_button = QtWidgets.QPushButton(self.layoutWidget)
        self.report_button.setObjectName("report_button")
        self.summary_button = QtWidgets.QPushButton(self.layoutWidget)
        self.summary_button.setObjectName("smmary_button")
        self.sum_button = QtWidgets.QPushButton(self.layoutWidget)
        self.horizontalLayout.addWidget(self.summary_button)
        self.horizontalLayout.addWidget(self.report_button)
        self.horizontalLayout.addWidget(self.sum_button)
        self.layoutWidget1 = QtWidgets.QWidget(self)
        self.layoutWidget1.setGeometry(QtCore.QRect(28, 33, 451, 261))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.case_number = QtWidgets.QLabel(self.layoutWidget1)
        self.case_number.setObjectName("case_number")
        self.verticalLayout.addWidget(self.case_number)
        self.car_name = QtWidgets.QLabel(self.layoutWidget1)
        self.car_name.setObjectName("car_name")
        self.verticalLayout.addWidget(self.car_name)
        self.act_number = QtWidgets.QLabel(self.layoutWidget1)
        self.act_number.setObjectName("act_number")
        self.verticalLayout.addWidget(self.act_number)
        self.act_date = QtWidgets.QLabel(self.layoutWidget1)
        self.act_date.setObjectName("act_date")
        self.verticalLayout.addWidget(self.act_date)
        self.hour_cost = QtWidgets.QLabel(self.layoutWidget1)
        self.hour_cost.setObjectName("hour_cost")
        self.verticalLayout.addWidget(self.hour_cost)
        self.estimator_name = QtWidgets.QLabel(self.layoutWidget1)
        self.estimator_name.setObjectName("estimator_name")
        self.verticalLayout.addWidget(self.estimator_name)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 7, 1)
        self.act_edit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.act_edit.setObjectName("act_edit")
        self.gridLayout.addWidget(self.act_edit, 0, 1, 1, 1)
        self.car_mark_edit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.car_mark_edit.setObjectName("car_mark_edit")

        self.gridLayout.addWidget(self.car_mark_edit, 1, 1, 1, 1)
        self.act_number_edit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.act_number_edit.setObjectName("act_number_edit")
        self.gridLayout.addWidget(self.act_number_edit, 2, 1, 1, 1)
        self.act_date_edit = QtWidgets.QDateEdit(self.layoutWidget1)
        self.act_date_edit.setObjectName("act_date_edit")
        self.act_date_edit.setCalendarPopup(True)
        self.gridLayout.addWidget(self.act_date_edit, 3, 1, 1, 1)
        self.hour_cost_edit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.hour_cost_edit.setObjectName("hour_cost_edit")
        self.gridLayout.addWidget(self.hour_cost_edit, 4, 1, 1, 1)
        self.estimator_edit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.estimator_edit.setObjectName("estimator_edit")
        self.gridLayout.addWidget(self.estimator_edit, 5, 1, 1, 1)

        self.sum_lbl = QtWidgets.QLabel(self.layoutWidget1)
        self.sum_lbl.setObjectName("sum_lbl")
        self.verticalLayout.addWidget(self.sum_lbl)

        
        
        self.sum_edit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.sum_edit.setObjectName("sum_edit")
        self.gridLayout.addWidget(self.sum_edit, 6, 1, 1, 1)

        self.setWindowTitle("Калькуляция")
        self.header_label.setText("Калькуляция для возмещения ущерба")
        self.exit_button.setText( "Выход")
        self.report_button.setText("Отчёт")
        self.summary_button.setText("Калькуляция")
        self.sum_button.setText("Подсчитать")
        self.case_number.setText("Введите номер договора")
        self.car_name.setText("Марка автомобиля")
        self.act_number.setText("Номер акта")
        self.act_date.setText("Дата акта")
        self.hour_cost.setText("Стоимость норма-часа")
        self.estimator_name.setText("Оценщик")
        self.sum_lbl.setText("Сумма составляет:")
        self.show()

        #autocompletion
        self.completer = QtWidgets.QCompleter()
        self.model = QtCore.QStringListModel()
        self.completer.setModel(self.model)
        self.autocomplete('car_mark', 'car_data', self.model)
        self.car_mark_edit.setCompleter(self.completer)

        self.completion1 = QtWidgets.QCompleter()
        self.data = QtCore.QStringListModel()
        self.completion1.setModel(self.data)
        self.autocomplete('nomer_dogovora', 'auto_marks_data', self.data)
        self.act_edit.setCompleter(self.completion1)

        self.completion3 = QtWidgets.QCompleter()
        self.data = QtCore.QStringListModel()
        self.completion3.setModel(self.data)
        self.autocomplete('case_number', 'auto_marks_data', self.data)
        self.act_number_edit.setCompleter(self.completion3)

        self.completion4 = QtWidgets.QCompleter()
        self.data = QtCore.QStringListModel()
        self.completion4.setModel(self.data)
        self.autocomplete('cost', 'works', self.data)
        self.hour_cost_edit.setCompleter(self.completion4)

        self.completion5 = QtWidgets.QCompleter()
        self.data = QtCore.QStringListModel()
        self.completion5.setModel(self.data)
        self.autocomplete('FIO', 'workers_info', self.data)
        self.estimator_edit.setCompleter(self.completion5)

        self.exit_button.clicked.connect(self.close)
        self.report_button.clicked.connect(self.report)
        self.summary_button.clicked.connect(self.open_work_list)
        self.sum_button.clicked.connect(self.sum_clicked)

    def sum_clicked(self):
        value4 = self.open_table(self.queries('sum', 'works_sum'))[0]
        value5 = self.open_table(self.queries('sum', 'spare_sum'))[0]
        value6 = self.open_table(self.queries('sum', 'mat_sum'))[0]
        result_number = str(self.summa(value4, value5, value6))
        self.sum_edit.setText(result_number)
        print(value4, value5, value6)


    def summa(self, *args):
        err2 = QtWidgets.QMessageBox(self)
        err2.setIcon(err2.Critical)
        err2.setText("Введите данные в таблицу 'Калькуляция'!")
        err2.setWindowTitle("Ошибка!")
        err2.setStandardButtons(err2.Ok)                      
        total_cost = []
        dup_items = set()
        for arg in args:
            dup_items.add(arg)
            if 'None' in dup_items:
                dup_items.remove('None')
        try:
            total = [float(x) for x in dup_items]
        except ValueError:
            err2.show()
        else:
            sum_value = sum(total)
            return sum_value 

    def error_handler(self, method, message, i):
        message.setIcon(message.Information)
        message.setText("Введите название автомобиля!")
        message.setWindowTitle("Ошибка!")
        message.setStandardButtons(message.Ok)
        try:
            method[i]
        except IndexError:
            message.show()
        else:
            return method[i]

    def report(self):
        data_act = self.act_date_edit.date().toString('dd.MM.yyyy')
        car = self.car_mark_edit.text()
        case_number = self.act_number_edit.text()
        act_number = self.act_edit.text()
        norm_hour = self.hour_cost_edit.text()
        estimator = self.estimator_edit.text()
        err = QtWidgets.QMessageBox()
        err1 = QtWidgets.QMessageBox(self)
        err1.setIcon(err1.Critical)
        err1.setText("Закройте созданный документ")
        err1.setWindowTitle("Ошибка!")
        err1.setStandardButtons(err1.Ok)

        car_mark = ("""SELECT * FROM car_data
        WHERE car_mark = '{}' """).format(car)
        v_works = ("""SELECT name_of_work,measurement,norma_hour,cost,sum
        FROM works_sum""")
        materials = ("""select material,measure,quantity,cost,sum
        from mat_sum""")
        spare_sum = ("""select spare_name,measure_name,quantity,cost,sum
        from spare_sum""")

        doc = DocxTemplate(docx=os.path.join(os.getcwd(), 'default.docx'))

        value1 = self.open_table(self.queries('sum', 'works_sum'))[0]
        value2 = self.open_table(self.queries('sum', 'spare_sum'))[0]
        value3 = self.open_table(self.queries('sum', 'mat_sum'))[0]
   
        
        context = {'carmark': self.error_handler(self.open_table(car_mark), err, 1),
                    'reg_number': self.error_handler(self.open_table(car_mark), err, 2), 
                    'color': self.error_handler(self.open_table(car_mark), err, 3), 
                    'probeg': self.error_handler(self.open_table(car_mark), err, 4), 
                    'production_year': self.error_handler(self.open_table(car_mark), err, 5), 
                    'seria_and_pts': self.error_handler(self.open_table(car_mark), err, 6), 
                    'vin': self.error_handler(self.open_table(car_mark), err, 7), 
                    'engine_number': self.error_handler(self.open_table(car_mark), err, 8), 
                    'chassis_number': self.open_table(car_mark)[9], 
                    'table2': self.make_dict(v_works), 
                    'summary': value1, 
                    'headers': ['Наименование работ', 'Ед.\nизм', 'Кол-во', 'Стоимость\nчас', 'Сумма в\nруб.'],
                    'headers2': ['Наименвание запасных частей', 'Ед.\nизм', 'Кол-во', 'Стоимость\nв руб.', 'Сумма в\nруб.'],
                    'headers3': ['Наименование материалов', 'Ед.\nизм', 'Кол-во', 'Стоимость\nв руб.', 'Сумма в\nруб.'], 
                    'table3': self.make_dict(spare_sum), 
                    'table4': self.make_dict(materials), 
                    'summary2': value2, 
                    'summary3': value3, 
                    'estimator': estimator, 
                    'case_number': case_number, 
                    'data_act': data_act, 
                    'total_price': self.summa(value1, value2, value3), 
                    'act_number': act_number, 
                    'data_act': data_act, }
        doc.render(context)
        try:
            doc.save("generated_doc.docx")
        except PermissionError:
            err1.show()
        else:
            print("nothing happenned")
            print(os.getcwd())
            current_dir = os.getcwd()
            doc.save("generated_doc.docx")
            open_file = os.path.join(current_dir, "generated_doc.docx")
            os.startfile(open_file)
        

    def open_work_list(self):
        li = Summarized()
        li.show()

class Summarized(Sum_table):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькуляция')
        self.model.setTable('calculation')
        self.model.setRelation(1, QSqlRelation('auto_marks_data', 'am_data_id', 'case_number'))
        self.model.setRelation(2, QSqlRelation('materials', 'materials_id', 'material'))
        self.model.setRelation(3, QSqlRelation('spare_parts', 'spare_id', 'spare_name'))
        self.model.setRelation(4, QSqlRelation('works', 'work_id', 'name_of_work'))
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "Идентификатор")
        self.model.setHeaderData(1, Qt.Horizontal, "Номер дела")
        self.model.setHeaderData(2, Qt.Horizontal, "Hаименование материала")
        self.model.setHeaderData(3, Qt.Horizontal, "Наименование запчасти")
        self.model.setHeaderData(4, Qt.Horizontal, "Наименование работ")
        self.view.resizeColumnsToContents()
        self.view.hideColumn(0)
        self.view.hideColumn(5)
        

               
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    sys.exit(app.exec_())
    
