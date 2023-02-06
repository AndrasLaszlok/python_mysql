import sys
import mysql.connector
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

"""Adatbáziskapcsolat konfigurálása"""
config = {
'user': 'yourusername',
'password': 'yourpassword',
'host': '127.0.0.1',
'database': 'karositok',
'raise_on_warnings': True
}

class GazdLekerdWindow(QWidget):
    """Erdőgazdálkodók adatainak lekérése"""

    def __init__(self, *args, **kwargs):
        super(GazdLekerdWindow,self).__init__(*args, **kwargs)
        uic.loadUi(
            os.path.join(os.path.dirname(__file__),
            "connector_lekerd_gazd.ui"),self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.pushButton.pressed.connect(self.readMysqlTable)
        self.tableWidget.setColumnWidth(1,450)
        self.tableWidget.setColumnWidth(2,450)


    def readMysqlTable(self):

        mysqlConnection = mysql.connector.connect(**config)
        cursor = mysqlConnection.cursor()    
        mysql_select_query_one = ("SELECT * from gazdalkodo \
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

                self.tableWidget.setItem(
                    row_number[0],0, QTableWidgetItem(str(row_number[1][0])))
                self.tableWidget.setItem(
                    row_number[0],1, QTableWidgetItem(str(row_number[1][1]))) 
                self.tableWidget.setItem(
                    row_number[0],2, QTableWidgetItem(str(row_number[1][2]))) 

        cursor.close()
        mysqlConnection.close()

class ReszlLekerdWindow(QWidget):
    """Erdőrészletek adatainak lekérése"""

    def __init__(self, *args, **kwargs):
        super(ReszlLekerdWindow,self).__init__(*args, **kwargs)
        uic.loadUi(
            os.path.join(os.path.dirname(__file__),
            "connector_lekerd_reszl.ui"),self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.pushButton.pressed.connect(self.readMysqlTable)
        self.tableWidget.setColumnWidth(1,200)


    def readMysqlTable(self):

        mysqlConnection = mysql.connector.connect(**config)
        cursor = mysqlConnection.cursor()    
        mysql_select_query_one = ("SELECT * from reszlet \
                                  where reszlet.id = %s")
        c_id = self.spinBox.value()
        
        mysql_select_query_all = ("SELECT * from reszlet")
        
        if self.checkBox.isChecked():
            cursor.execute(mysql_select_query_all)
        else:
            cursor.execute(mysql_select_query_one, (c_id,))
        
        records = cursor.fetchall()
        rows=len(records)
        self.tableWidget.setRowCount(rows)

        for row_number in enumerate(records):

                self.tableWidget.setItem(
                    row_number[0],0, QTableWidgetItem(str(row_number[1][0])))
                self.tableWidget.setItem(
                    row_number[0],1, QTableWidgetItem(str(row_number[1][1]))) 
                self.tableWidget.setItem(
                    row_number[0],2, QTableWidgetItem(str(row_number[1][2])))
                self.tableWidget.setItem(
                    row_number[0],3, QTableWidgetItem(str(row_number[1][3]))) 
                self.tableWidget.setItem(
                    row_number[0],4, QTableWidgetItem(str(row_number[1][4]))) 
                self.tableWidget.setItem(
                    row_number[0],5, QTableWidgetItem(str(row_number[1][5]))) 

        cursor.close()
        mysqlConnection.close()

class KarLekerdWindow(QWidget):
    """Erdőkárok adatainak lekérése"""

    def __init__(self, *args, **kwargs):
        super(KarLekerdWindow,self).__init__(*args, **kwargs)
        uic.loadUi(
            os.path.join(os.path.dirname(__file__),
            "connector_lekerd_kar.ui"),self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.pushButton.pressed.connect(self.readMysqlTable)
        self.tableWidget.setColumnWidth(1,200)


    def readMysqlTable(self):

        mysqlConnection = mysql.connector.connect(**config)
        cursor = mysqlConnection.cursor()    
        mysql_select_query_one = ("SELECT * from karositas\
                                  where karositas.id = %s")
        c_id = self.spinBox.value()
        
        mysql_select_query_all = ("SELECT * from karositas")
        
        if self.checkBox.isChecked():
            cursor.execute(mysql_select_query_all)
        else:
            cursor.execute(mysql_select_query_one, (c_id,))
        
        records = cursor.fetchall()
        rows=len(records)
        self.tableWidget.setRowCount(rows)

        for row_number in enumerate(records):

                self.tableWidget.setItem(
                    row_number[0],0, QTableWidgetItem(str(row_number[1][0])))
                self.tableWidget.setItem(
                    row_number[0],1, QTableWidgetItem(str(row_number[1][1]))) 
                self.tableWidget.setItem(
                    row_number[0],2, QTableWidgetItem(str(row_number[1][2])))
                self.tableWidget.setItem(
                    row_number[0],3, QTableWidgetItem(str(row_number[1][3]))) 
                self.tableWidget.setItem(
                    row_number[0],4, QTableWidgetItem(str(row_number[1][4]))) 
                self.tableWidget.setItem(
                    row_number[0],5, QTableWidgetItem(str(row_number[1][5])))
                self.tableWidget.setItem(
                    row_number[0],6, QTableWidgetItem(str(row_number[1][6]))) 

        cursor.close()
        mysqlConnection.close()

class GazdFeltoltWindow(QWidget):
    """Erdőgazdálkodók adatainak feltöltése"""

    def __init__(self, *args, **kwargs):
        super(GazdFeltoltWindow,self).__init__(*args, **kwargs)
        uic.loadUi(
            os.path.join(os.path.dirname(__file__),
            "connector_feltolt_gazd.ui"),self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.pushButton.pressed.connect(self.insertMysqlTable)

    def insertMysqlTable(self):

        try:

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

        except mysql.connector.Error as error:
            print(f'Sikertelen feltöltés: {error}')

class ReszlFeltoltWindow(QWidget):
    """Erdőrészlek adatainak feltöltése"""

    def __init__(self, *args, **kwargs):
        super(ReszlFeltoltWindow,self).__init__(*args, **kwargs)
        uic.loadUi(
            os.path.join(os.path.dirname(__file__),
            "connector_feltolt_reszl.ui"),self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.pushButton.pressed.connect(self.insertMysqlTable)

    def insertMysqlTable(self):
        
        try:

            mysqlConnection = mysql.connector.connect(**config)
            cursor = mysqlConnection.cursor()    
            mysql_insert_query = ("INSERT INTO reszlet (kozseg, tag,\
                                  reszlet, gazd_id, faallomany) \
                                  VALUES \
                                  (%s, %s, %s, %s, %s);")
            v_kozseg = self.textEdit.toPlainText()
            v_tag = self.spinBox.value()
            v_reszlet = self.textEdit_3.toPlainText()
            v_gazd_id = self.spinBox_2.value()
            v_faallomany = self.textEdit_2.toPlainText()
            v_egyben = (v_kozseg, v_tag, v_reszlet, v_gazd_id, v_faallomany)

            cursor.execute(mysql_insert_query, v_egyben)
            
            mysqlConnection.commit()
            message = (f'Sikeres feltöltés: {v_kozseg} {v_tag} {v_reszlet}')
            self.label_3.setText(message)
            cursor.close()
            mysqlConnection.close()

        except mysql.connector.Error as error:
            print(f'Sikertelen feltöltés: {error}')

class KarFeltoltWindow(QWidget):
    """Erdőkárok adatainak feltöltése"""

    def __init__(self, *args, **kwargs):
        super(KarFeltoltWindow,self).__init__(*args, **kwargs)
        uic.loadUi(
            os.path.join(os.path.dirname(__file__),
            "connector_feltolt_kar.ui"),self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.pushButton.pressed.connect(self.insertMysqlTable)

    def insertMysqlTable(self):
        
        try:

            mysqlConnection = mysql.connector.connect(**config)
            cursor = mysqlConnection.cursor()    
            mysql_insert_query = ("INSERT INTO karositas (faj, reszlet_id, \
                                  gazd_id, terulet, gyakorisag, karerely) \
                                  VALUES \
                                  (%s, %s, %s, %s, %s, %s);")
            v_faj = self.textEdit.toPlainText()
            v_reszlet_id = self.spinBox.value()
            v_gazd_id = self.spinBox_2.value()
            v_terulet = self.doubleSpinBox.value()
            v_gyakorisag = self.spinBox_3.value()
            v_karerely = self.spinBox_4.value()
            v_egyben = (v_faj, v_reszlet_id, v_gazd_id,
                        v_terulet, v_gyakorisag, v_karerely)

            cursor.execute(mysql_insert_query, v_egyben)
            
            mysqlConnection.commit()
            self.label_3.setText(f'Sikeres feltöltés: {v_faj}')
            cursor.close()
            mysqlConnection.close()

        except mysql.connector.Error as error:
            print(f'Sikertelen feltöltés: {error}')

class OsszLekerdWindow(QWidget):
    """Összevont lekérdezés a három tábla legfontosabb adataival"""

    def __init__(self, *args, **kwargs):
        super(OsszLekerdWindow,self).__init__(*args, **kwargs)
        uic.loadUi(
            os.path.join(os.path.dirname(__file__),
            "connector_lekerd_ossz.ui"),self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.pushButton.pressed.connect(self.readMysqlTable)
        self.tableWidget.setColumnWidth(0,300)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,150)

    def readMysqlTable(self):

        mysqlConnection = mysql.connector.connect(**config)
        cursor = mysqlConnection.cursor()    
        mysql_select_query = ("SELECT gazdalkodo.nev, karositas.faj, \
                              reszlet.kozseg, reszlet.tag, reszlet.reszlet, \
                              karositas.terulet, karositas.gyakorisag, \
                              karositas.karerely \
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

                self.tableWidget.setItem(
                    row_number[0],0, QTableWidgetItem(str(row_number[1][0])))
                self.tableWidget.setItem(
                    row_number[0],1, QTableWidgetItem(str(row_number[1][1]))) 
                self.tableWidget.setItem(
                    row_number[0],2, QTableWidgetItem(str(row_number[1][2]))) 
                self.tableWidget.setItem(
                    row_number[0],3, QTableWidgetItem(str(row_number[1][3]))) 
                self.tableWidget.setItem(
                    row_number[0],4, QTableWidgetItem(str(row_number[1][4]))) 
                self.tableWidget.setItem(
                    row_number[0],5, QTableWidgetItem(str(row_number[1][5])))
                self.tableWidget.setItem(
                    row_number[0],6, QTableWidgetItem(str(row_number[1][6]))) 
                self.tableWidget.setItem(
                    row_number[0],7, QTableWidgetItem(str(row_number[1][7])))  

        cursor.close()
        mysqlConnection.close()

class MainWindow(QMainWindow):
    """Főablak"""

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        uic.loadUi(
            os.path.join(os.path.dirname(__file__),
            "connector_inventory_main.ui"),self)
        self.pushButton.pressed.connect(self.show_gazdlekerd_window)
        self.pushButton_2.pressed.connect(self.show_reszllekerd_window)
        self.pushButton_3.pressed.connect(self.show_karlekerd_window)
        self.pushButton_4.pressed.connect(self.show_gazdfeltolt_window)
        self.pushButton_5.pressed.connect(self.show_reszlfeltolt_window)
        self.pushButton_6.pressed.connect(self.show_karfeltolt_window)
        self.pushButton_7.pressed.connect(self.show_osszlekerd_window)

    def show_gazdlekerd_window(self):
        self.gl = GazdLekerdWindow()
        self.gl.show()
        
    def show_reszllekerd_window(self):
        self.rl = ReszlLekerdWindow()
        self.rl.show()
        
    def show_karlekerd_window(self):
        self.kl = KarLekerdWindow()
        self.kl.show()
    
    def show_gazdfeltolt_window(self):
        self.gf = GazdFeltoltWindow()
        self.gf.show()
        
    def show_reszlfeltolt_window(self):
        self.rf = ReszlFeltoltWindow()
        self.rf.show()
        
    def show_karfeltolt_window(self):
        self.kf = KarFeltoltWindow()
        self.kf.show()

    def show_osszlekerd_window(self):
        self.ol = OsszLekerdWindow()
        self.ol.show()

def run():
    """Modul futtatása"""
    
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()
