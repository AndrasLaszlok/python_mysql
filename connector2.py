from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys, mysql.connector


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("connector2.ui",self)
        
        self.pushButton.pressed.connect(self.insertMysqlTable)

    def insertMysqlTable(self):

        config = {
        'user': 'yourusername',
        'password': 'yourpassword',
        'host': '127.0.0.1',
        'database': 'karositok',
        'raise_on_warnings': True
        }

        mysqlConnection = mysql.connector.connect(**config)
        cursor = mysqlConnection.cursor()    
        mysql_insert_query = ("INSERT INTO gazdalkodo (nev, cim) \
                                VALUES \
                                (%s, %s);")
        v_nev = self.textEdit.toPlainText()
        v_cim = self.textEdit_2.toPlainText()
        v_egyben = (v_nev, v_cim)

        cursor.execute(mysql_insert_query, v_egyben)
        
        mysqlConnection.commit()
        self.label_3.setText(f'Sikeres feltöltés: {v_nev}')
        cursor.close()
        mysqlConnection.close()

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
