# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QTableView, QHBoxLayout, QVBoxLayout
from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlQuery, QSqlRelation, QSqlRelationalDelegate
from PyQt5.QtCore import QRect, Qt
import sys

class Cars_data(QWidget):

    def __init__(self):
        super().__init__()        
        self.setObjectName("Main window")
        self.setGeometry(QRect(500, 300, 430, 300))
        self.setWindowTitle("Транспортное средство")
        self.btn_add = QPushButton(self)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.setText("Добавить")
        self.btn_delete = QPushButton(self)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.setText("Удалить")
        self.btn_exit = QPushButton(self)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.setText("Выход")
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('ocenka.db')
        self.model = QSqlRelationalTableModel(self)
        self.model.setTable('car_data')
        self.model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "Номер ТС")
        self.model.setHeaderData(1, Qt.Horizontal, "Марка автомобиля")
        self.model.setHeaderData(2, Qt.Horizontal, "Регистрационный номер")
        self.model.setHeaderData(3, Qt.Horizontal, "Цвет")
        self.model.setHeaderData(4, Qt.Horizontal, "Пробег")
        self.model.setHeaderData(5, Qt.Horizontal, "Год выпуска")
        self.model.setHeaderData(6, Qt.Horizontal, "Страна производства")
        self.model.setHeaderData(7, Qt.Horizontal, "Место использования")
        self.model.setHeaderData(8, Qt.Horizontal, "Страна импортёр")
        self.model.setHeaderData(9, Qt.Horizontal, "Серия и ПТС")
        self.model.setHeaderData(10,Qt.Horizontal, "VIN")
        self.model.setHeaderData(11,Qt.Horizontal, "Номер двигателя")
        self.model.setHeaderData(12,Qt.Horizontal, "Номер кузова")


        self.view1 = self.createView("Table Model (View 1)", self.model)
        self.query = QSqlQuery(self.db)
        self.query.exec_("PRAGMA Foreign_keys = ON")

        layout = QHBoxLayout()
        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_delete)
        layout.addWidget(self.btn_exit)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.view1)
        vlayout.addLayout(layout)
        self.setLayout(vlayout)

        self.show()

        self.view1.clicked.connect(self.findrow)
        self.btn_add.clicked.connect(self.addrow)
        self.btn_delete.clicked.connect(lambda: self.model.removeRow(self.view1.currentIndex().row()))
        self.btn_exit.clicked.connect(self.close)

    def findrow(self, i):
        delrow = i.row()

    def addrow(self):
        print (self.model.rowCount())
        ret = self.model.insertRows(self.model.rowCount(), 1)
        return ret

    def createView(self, title, model):
        self.model = model
        self.title = title
        view = QTableView(self)
        view.setModel(self.model)
        view.setWindowTitle(self.title)
        view.resizeColumnsToContents()
        view.setGeometry(25, 25, 380, 200)
        view.hideColumn(0)
        view.setItemDelegate(QSqlRelationalDelegate(view))
        return view


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cars = Cars_data()
    delrow = -1
    sys.exit(app.exec_())
