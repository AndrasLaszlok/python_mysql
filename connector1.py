from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys, mysql.connector


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("connector1.ui",self)
        
        self.pushButton.pressed.connect(self.readMysqlTable)
        self.tableWidget.setColumnWidth(0,300)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,150)


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
        mysql_select_query = ("SELECT gazdalkodo.nev, karositas.faj,\
                            reszlet.kozseg, reszlet.tag, reszlet.reszlet, karositas.terulet, \
                            karositas.gyakorisag, karositas.karerely \
                            from gazdalkodo, karositas, reszlet \
                            where gazdalkodo.id = karositas.gazd_id \
                            and reszlet.id = karositas.reszlet_id \
                            and gazdalkodo.id = %s")
        c_id = self.spinBox.value()
        cursor.execute(mysql_select_query, (c_id,))
        records = cursor.fetchall()
        rows=len(records)
        self.tableWidget.setRowCount(rows)

        for row_number in enumerate(records):

                self.tableWidget.setItem(row_number[0],0, QTableWidgetItem(str(row_number[1][0])))
                self.tableWidget.setItem(row_number[0],1, QTableWidgetItem(str(row_number[1][1]))) 
                self.tableWidget.setItem(row_number[0],2, QTableWidgetItem(str(row_number[1][2]))) 
                self.tableWidget.setItem(row_number[0],3, QTableWidgetItem(str(row_number[1][3]))) 
                self.tableWidget.setItem(row_number[0],4, QTableWidgetItem(str(row_number[1][4]))) 
                self.tableWidget.setItem(row_number[0],5, QTableWidgetItem(str(row_number[1][5])))
                self.tableWidget.setItem(row_number[0],6, QTableWidgetItem(str(row_number[1][6]))) 
                self.tableWidget.setItem(row_number[0],7, QTableWidgetItem(str(row_number[1][7])))  

        cursor.close()
        mysqlConnection.close()

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
