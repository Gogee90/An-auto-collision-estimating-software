#!/usr/bin/python3
# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QDateEdit, QStyledItemDelegate, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlRelation, QSqlRelationalDelegate, QSqlRelationalTableModel
from modules.materials import Materials as Template
from modules.materials import ProductDelegate
from modules.materials import CustomDelegate
from modules.materials import SpinBox
from modules.calc import Ui_Dialog
import sys
import os


class StartScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menubar()

        self.resize(800, 300)
        self.setWindowTitle("Оценка ДТП")
        self.show() 

    def menubar(self):
        exitAct = QAction("Выход", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.triggered.connect(qApp.quit)

        openAuData = QAction("Дела", self)
        openAuData.setShortcut("Ctrl+I")
        openAuData.triggered.connect(self.open_aut_data)

        openCarsData = QAction("Транспортное средтство", self)
        openCarsData.setShortcut("Ctrl+U")
        openCarsData.triggered.connect(self.open_cars_data)

        openCounterAgents = QAction("Контрагенты", self)
        openCounterAgents.setShortcut("Ctrl+L")
        openCounterAgents.triggered.connect(self.open_coun_agents)

        mats = QAction("Материалы", self)
        mats.setShortcut("Ctrl+N")
        mats.triggered.connect(self.open_mats)

        works = QAction("Работы", self)
        works.setShortcut("Ctrl+B")
        works.triggered.connect(self.open_work_price)

        spare_parts = QAction("Запчасти", self)
        spare_parts.setShortcut("Ctrl+S")
        spare_parts.triggered.connect(self.open_spare_parts)

        worker_info = QAction("Информация о сотрудниках", self)
        worker_info.setShortcut("Ctrl+V")
        worker_info.triggered.connect(self.open_workers_info)

        smeta = QAction("Калькуляция", self)
        smeta.setShortcut("Ctrl+C")
        smeta.triggered.connect(self.open_calculation)

        calculator = QAction("Калькулятор", self)
        calculator.setShortcut("Ctrl+M")
        calculator.triggered.connect(self.open_calc)

        estimate = self.menuBar().addMenu("Автооценка")
        estimate.addAction(openAuData)
        estimate.addAction(openCarsData)

        counAgents = self.menuBar().addMenu("Справочник по контрагентам")
        counAgents.addAction(openCounterAgents)

        mats_and_works = self.menuBar().addMenu("Справочник по материалам и услугам")
        mats_and_works.addAction(mats)
        mats_and_works.addAction(works)
        mats_and_works.addAction(spare_parts)

        workers_list = self.menuBar().addMenu("Справочник по сотрудникам")
        workers_list.addAction(worker_info)

        report = self.menuBar().addMenu("Отчёт")
        report.addAction(smeta)
        report.addAction(calculator)
        exit_menu = self.menuBar().addMenu("Выход")
        exit_menu.addAction(exitAct)

    def open_calc(self):
        os.system("start calc.exe")
        return None

    def open_aut_data(self):
        dialog = Auto_marks_data()
        dialog.show()

    def open_cars_data(self):
        cars = Car_data()
        cars.show()

    def open_coun_agents(self):
        agents = Counteragents()
        agents.show()

    def open_mats(self):
        spare_parts = Template()
        spare_parts.show()

    def open_work_price(self):
        work_cost = Works()
        work_cost.show()

    def open_workers_info(self):
        workers = WorkersInfo()
        workers.show()

    def open_calculation(self):
        self.calcul = Ui_Dialog()
        self.calcul.show()

    def open_spare_parts(self):
        sp = Spares()
        sp.show()

class Works(Template):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Работы")
        self.model.setTable("v_works")
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "Код работы")
        self.model.setHeaderData(1, Qt.Horizontal, "Наименование")
        self.model.setHeaderData(2, Qt.Horizontal, "Ед.изм.")
        self.model.setHeaderData(3, Qt.Horizontal, "Кол-во")
        self.model.setHeaderData(4, Qt.Horizontal, "Стоимость")
        self.model.setHeaderData(5, Qt.Horizontal, "Сумма")
        self.view.resizeColumnsToContents()

class WorkersInfo(Template):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Информация о сотрудниках')
        self.model.setTable("workers_info")
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "Идентификатор счёта")
        self.model.setHeaderData(1, Qt.Horizontal, "ФИО Сотрудника")
        self.model.setHeaderData(2, Qt.Horizontal, "Дата рождения")
        self.model.setHeaderData(3, Qt.Horizontal, "Серия и номер паспорта")
        self.model.setHeaderData(4, Qt.Horizontal, "Адресс")
        self.model.setHeaderData(5, Qt.Horizontal, "Телефон")
        self.model.setHeaderData(6, Qt.Horizontal, "Когда и кем выдан")
        self.model.setHeaderData(7, Qt.Horizontal, "Населённый пункт")
        self.view.setItemDelegateForColumn(2, CustomDelegate())
        self.view.resizeColumnsToContents()

class Counteragents(Template):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Контрагенты")
        self.model.setTable('counter_agents')
        self.model.select()
        self.model.setHeaderData(1, Qt.Horizontal, "Имя в списке")
        self.model.setHeaderData(2, Qt.Horizontal, "Руководитель")
        self.model.setHeaderData(3, Qt.Horizontal, "Тип")
        self.model.setHeaderData(4, Qt.Horizontal, "Адресс")
        self.model.setHeaderData(5, Qt.Horizontal, "Телефон")
        self.model.setHeaderData(6, Qt.Horizontal, "Расчётный счёт")
        self.view.resizeColumnsToContents()

class Car_data(Template):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Транспортное средство")
        self.model.setTable('car_data')
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "Номер ТС")
        self.model.setHeaderData(1, Qt.Horizontal, "Марка автомобиля")
        self.model.setHeaderData(2, Qt.Horizontal, "Регистрационный номер")
        self.model.setHeaderData(3, Qt.Horizontal, "Цвет")
        self.model.setHeaderData(4, Qt.Horizontal, "Пробег")
        self.model.setHeaderData(5, Qt.Horizontal, "Год выпуска")
        self.model.setHeaderData(6, Qt.Horizontal, "Серия и ПТС")
        self.model.setHeaderData(7, Qt.Horizontal, "VIN")
        self.model.setHeaderData(8, Qt.Horizontal, "Номер двигателя")
        self.model.setHeaderData(9, Qt.Horizontal, "Номер кузова")
        self.view.resizeColumnsToContents()
        self.view.setItemDelegateForColumn(5, ProductDelegate(5))
       
class Auto_marks_data(Template):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Автооценка')
        self.model.setTable('auto_marks_data')
        self.model.setRelation(4, QSqlRelation("car_data", "car_data_id", "car_mark"))
        self.model.setRelation(5, QSqlRelation("car_data", "car_data_id", "car_reg_number"))
        self.model.setRelation(6, QSqlRelation("counter_agents", "counter_agent_id", "manager"))
        self.model.setRelation(7, QSqlRelation("counter_agents", "counter_agent_id", "manager"))
        self.model.setRelation(8, QSqlRelation('workers_info', 'worker_info_id', 'FIO'))
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "id")
        self.model.setHeaderData(1, Qt.Horizontal, "Дата оценки")
        self.model.setHeaderData(2, Qt.Horizontal, "Номер дела")
        self.model.setHeaderData(3, Qt.Horizontal, "Номер договора")
        self.model.setHeaderData(4, Qt.Horizontal, "Транспортное средство")
        self.model.setHeaderData(5, Qt.Horizontal, "Регистрационный номер")
        self.model.setHeaderData(6, Qt.Horizontal, "Владелец ТС")
        self.model.setHeaderData(7, Qt.Horizontal, "Заказчик")
        self.model.setHeaderData(8, Qt.Horizontal, "Оценщик")
        self.view.resizeColumnsToContents()
        self.view.setItemDelegateForColumn(4, QSqlRelationalDelegate(self.view))
        self.view.setItemDelegateForColumn(6, QSqlRelationalDelegate(self.view))
        self.view.setItemDelegateForColumn(7, QSqlRelationalDelegate(self.view))
        self.view.setItemDelegateForColumn(8, QSqlRelationalDelegate(self.view))
        self.view.setItemDelegate(ProductDelegate(1))
        self.view.setItemDelegateForColumn(5, QSqlRelationalDelegate(self.view))

class Spares(Template):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Запчасти')
        self.model.setTable('v_spare_parts')
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "Идентификатор")
        self.model.setHeaderData(1, Qt.Horizontal, "Наименование")
        self.model.setHeaderData(2, Qt.Horizontal, "Ед.изм.")
        self.model.setHeaderData(3, Qt.Horizontal, "Количество")
        self.model.setHeaderData(4, Qt.Horizontal, "Стоимость")
        self.model.setHeaderData(5, Qt.Horizontal, "Сумма")
        self.view.resizeColumnsToContents()
        self.view.setItemDelegateForColumn(3, SpinBox())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    st = StartScreen()
    sys.exit(app.exec_())
