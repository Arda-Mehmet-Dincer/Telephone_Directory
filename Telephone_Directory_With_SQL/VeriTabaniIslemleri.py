import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem

class VeriTabaniIslemleri:
    def __init__(self):
        self.connection = sqlite3.connect("Telefon_Rehberi.db")
        self.cursor = self.connection.cursor()
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS rehber(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad VARCHAR(100),
            soyad VARCHAR(100),
            telefon VARCHAR(15)
            )
                            ''')
        self.connection.commit()
        
    def VerileriGetir(self):
        self.cursor.execute('SELECT * FROM rehber')
        return self.cursor.fetchall()
    
    def VeriEkle(self, ad, soyad, telefon):
        self.cursor.execute('INSERT INTO rehber(ad, soyad, telefon) VALUES(?,?,?)',(ad,soyad, telefon))
        self.connection.commit()
        
    def VeriSil(self, row_id):
        self.cursor.execute('DELETE FROM rehber WHERE id=?', (row_id,))
        self.connection.commit()
        
    def VeriGuncelle(self, row_id, ad, soyad, telefon):
        self.cursor.execute('UPDATE rehber SET ad=?, soyad=?, telefon=? WHERE id=?',(ad, soyad, telefon, row_id))
        self.connection.commit()
        
    def VerileriGetirArayuz(self, table_widget):
        table_widget.clearContents()
        data = self.VerileriGetir()

        table_widget.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                table_widget.setItem(i, j, QTableWidgetItem(str(value)))
        