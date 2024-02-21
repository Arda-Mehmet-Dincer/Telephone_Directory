from PyQt5.QtWidgets import *
from Telefon_Rehberi import Ui_MainWindow
from VeriTabaniIslemleri import *

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.qtDesign = Ui_MainWindow()
        self.qtDesign.setupUi(self)
        self.veritabani = VeriTabaniIslemleri()
        
        self.qtDesign.pushButton_ekle.clicked.connect(self.Ekle)
        self.qtDesign.pushButton_duzenle.clicked.connect(self.Duzenle)
        self.qtDesign.tableWidget.clicked.connect(self.satirSecmek)
        self.qtDesign.pushButton_temizle.clicked.connect(self.Temizle)
        self.qtDesign.pushButton_sil.clicked.connect(self.Sil)
        
        self.VerileriArayuzdeGoster()

    def Ekle(self):
        ad = self.qtDesign.lineEdit_ad.text()
        soyad = self.qtDesign.lineEdit_soyad.text()
        telefon = self.qtDesign.lineEdit_telefon.text()
        self.veritabani.VeriEkle(ad, soyad, telefon)
        self.VerileriArayuzdeGoster()
        self.Temizle()
    
    def satirSecmek(self):
        selected_row = self.qtDesign.tableWidget.currentRow()
        if selected_row >= 0:
            id = self.qtDesign.tableWidget.item(selected_row, 0).text()
            ad = self.qtDesign.tableWidget.item(selected_row, 1).text()
            soyad = self.qtDesign.tableWidget.item(selected_row, 2).text()
            telefon = self.qtDesign.tableWidget.item(selected_row, 3).text()
            
            self.qtDesign.lineEdit_ad.setText(ad)
            self.qtDesign.lineEdit_soyad.setText(soyad)
            self.qtDesign.lineEdit_telefon.setText(telefon)

    def Duzenle(self):
        selected_row = self.qtDesign.tableWidget.currentRow()
        if selected_row >= 0:
            id = self.qtDesign.tableWidget.item(selected_row, 0).text()
            ad = self.qtDesign.lineEdit_ad.text()
            soyad = self.qtDesign.lineEdit_soyad.text()
            telefon = self.qtDesign.lineEdit_telefon.text()

            self.veritabani.VeriGuncelle(id, ad, soyad, telefon)
            self.VerileriArayuzdeGoster()
            self.Temizle()
            
    def Temizle(self):
        self.qtDesign.lineEdit_ad.clear()
        self.qtDesign.lineEdit_soyad.clear()
        self.qtDesign.lineEdit_telefon.clear()
        
    def Sil(self):
        selected_row = self.qtDesign.tableWidget.currentRow()
        if selected_row >= 0:
            id = self.qtDesign.tableWidget.item(selected_row, 0).text()
            if id:
                self.veritabani.VeriSil(id)
                self.VerileriArayuzdeGoster()
                self.Temizle()
                
                
    def VerileriArayuzdeGoster(self):
        self.veritabani.VerileriGetirArayuz(self.qtDesign.tableWidget)
    
    def closeEvent(self, event):
        self.veritabani.connection.close()
        event.accept()


app = QApplication([])
window = main()
window.show()
app.exec_() # sonsuz dongu olusturur

