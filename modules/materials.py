from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout,  QPushButton,
QApplication, QWidget, QTableView, QStyledItemDelegate, QDateEdit, QSpinBox)
from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlQuery, QSqlRelationalDelegate, QSqlRelation
from PyQt5.QtCore import Qt, QDate, QSortFilterProxyModel
import sys


class ProductDelegate(QStyledItemDelegate):
    def __init__(self, column_number):
        super().__init__()
        self.col = column_number    
    def createEditor(self, parent, option, index):
        if index.column() == self.col:
            editor = QDateEdit(parent)
            editor.setDisplayFormat('dd.MM.yyyy')
            editor.date().toString('dd.MM.yyyy')
            editor.setCalendarPopup(True)
            return editor
        else:
            return QStyledItemDelegate.createEditor(self, parent, option, index)

class CustomDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QDateEdit(parent)
        editor.setDisplayFormat('dd.MM.yyyy')
        editor.date().toString('dd.MM.yyyy')
        editor.setCalendarPopup(True)
        return editor

class SpinBox(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        spin = QSpinBox(parent)
        #spin.textFromValue()
        return spin

class Materials(QWidget):

    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        self.setObjectName("Main window")
        self.resize(370, 300)
        self.setWindowTitle("Материалы")
        self.btn_add = QPushButton(self)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.setText("Добавить")
        self.btn_delete = QPushButton(self)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.setText("Удалить")
        self.btn_exit = QPushButton(self)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.setText("Выход")
        self.btn_refresh = QPushButton(self)
        self.btn_refresh.setText("Обновить")
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('ocenka.db')
        self.db.open()
        self.model = QSqlRelationalTableModel(self)
        self.model.setTable("v_materials")
        self.model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
        self.model.setJoinMode(QSqlRelationalTableModel.LeftJoin)
        self.model.setHeaderData(0, Qt.Horizontal, "Идентификатор")
        self.model.setHeaderData(1, Qt.Horizontal, "Наименование")
        self.model.setHeaderData(2, Qt.Horizontal, "Ед.изм.")
        self.model.setHeaderData(3, Qt.Horizontal, "Количество")
        self.model.setHeaderData(4, Qt.Horizontal, "Стоимость")
        self.model.setHeaderData(5, Qt.Horizontal, "Сумма")
        self.model.setHeaderData(6, Qt.Horizontal, "Выбрать")
        #self.proxyModel = QSortFilterProxyModel(self)
        #self.proxyModel.setSourceModel(self.model)
        self.view = QTableView(self)
        
        self.view.setSortingEnabled(True)
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()
        self.view.hideColumn(0)
        self.view.horizontalHeader().setStretchLastSection(True)
        #self.view.hideColumn(1)
        self.view.setItemDelegate(QSqlRelationalDelegate(self.model))
        self.model.select()
        

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.btn_delete)
        self.layout.addWidget(self.btn_exit)
        self.layout.addWidget(self.btn_refresh)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.view)
        vlayout.addLayout(self.layout)
        self.setLayout(vlayout)
        self.show()

        self.view.clicked.connect(self.findrow)
        self.btn_add.clicked.connect(self.addrow)
        self.btn_delete.clicked.connect(lambda: self.model.removeRow(self.view.currentIndex().row()))
        self.btn_exit.clicked.connect(self.close_event)
        self.btn_refresh.clicked.connect(lambda: self.model.select())

    def close_database(self):
        self.view.setModel(None)
        del self.model
        self.db.close()
        del self.db
        QSqlDatabase.removeDatabase('ocenka.db')
        self.close()

    def close_event(self, event):
        self.close_database()            
       

    def findrow(self, i):
        delrow = i.row()

    def addrow(self):
        print(self.model.rowCount())
        ret = self.model.insertRows(self.model.rowCount(), 1)
        return ret

if __name__ == '__main__':
    app = QApplication(sys.argv)
    con = Materials()
    delrow = -1
    sys.exit(app.exec_())