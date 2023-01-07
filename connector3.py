from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys, mysql.connector


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("connector3.ui",self)
        
        self.pushButton.pressed.connect(self.readMysqlTable)
        self.tableWidget.setColumnWidth(1,450)
        self.tableWidget.setColumnWidth(2,450)


    def readMysqlTable(self):

        config = {
        'user': 'yourusername',
        'password': 'yourpassword',
        'host': '127.0.0.1',
        'database': 'karositok',
        'raise_on_warnings': True
        }

        mysqlConnection = mysql.connector.connect(**config)
        cursor = mysqlConnection.cursor()    
        mysql_select_query_one = ("SELECT * from gazdalkodo\
                            where gazdalkodo.id = %s")
        c_id = self.spinBox.value()
        
        mysql_select_query_all = ("SELECT * from gazdalkodo")
        
        if self.checkBox.isChecked():
            cursor.execute(mysql_select_query_all)
        else:
            cursor.execute(mysql_select_query_one, (c_id,))
        
        records = cursor.fetchall()
        rows=len(records)
        self.tableWidget.setRowCount(rows)

        for row_number in enumerate(records):

                self.tableWidget.setItem(row_number[0],0, QTableWidgetItem(str(row_number[1][0])))
                self.tableWidget.setItem(row_number[0],1, QTableWidgetItem(str(row_number[1][1]))) 
                self.tableWidget.setItem(row_number[0],2, QTableWidgetItem(str(row_number[1][2]))) 

        cursor.close()
        mysqlConnection.close()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
