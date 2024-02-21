from PyQt5.QtWidgets import *
from Telefon_Rehberi import Ui_MainWindow


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.qtDesign = Ui_MainWindow()
        self.qtDesign.setupUi(self)
        self.qtDesign.pushButton_Add.clicked.connect(self.Add)
        self.qtDesign.pushButton_Edit.clicked.connect(self.Edit)
        self.qtDesign.tableWidget.clicked.connect(self.satirSecmek)
        self.qtDesign.pushButton_Clear.clicked.connect(self.Clear)
        self.qtDesign.pushButton_Delete.clicked.connect(self.Delete)

    def Add(self):
        Name = self.qtDesign.lineEdit_Name.text()
        Surname = self.qtDesign.lineEdit_Surname.text()
        Phone = self.qtDesign.lineEdit_Phone.text()
        rowPosistion = self.qtDesign.tableWidget.rowCount()
        self.qtDesign.tableWidget.insertRow(rowPosistion)
        self.qtDesign.tableWidget.setItem(rowPosistion, 0, QTableWidgetItem(Name))
        self.qtDesign.tableWidget.setItem(rowPosistion, 1, QTableWidgetItem(Surname))
        self.qtDesign.tableWidget.setItem(rowPosistion, 2, QTableWidgetItem(Phone))
        
        self.qtDesign.lineEdit_Name.clear()
        self.qtDesign.lineEdit_Surname.clear()
        self.qtDesign.lineEdit_Phone.clear()
    
    def satirSecmek(self):
        selected_row = self.qtDesign.tableWidget.currentRow()
        if selected_row >= 0:
            Name = self.qtDesign.tableWidget.item(selected_row, 0).text()
            Surname = self.qtDesign.tableWidget.item(selected_row, 1).text()
            Phone = self.qtDesign.tableWidget.item(selected_row, 2).text()
            
            self.qtDesign.lineEdit_Name.setText(Name)
            self.qtDesign.lineEdit_Surname.setText(Surname)
            self.qtDesign.lineEdit_Phone.setText(Phone)

    def Edit(self):
        selected_row = self.qtDesign.tableWidget.currentRow()
        if selected_row >= 0:
            Name = self.qtDesign.lineEdit_Name.text()
            Surname = self.qtDesign.lineEdit_Surname.text()
            Phone = self.qtDesign.lineEdit_Phone.text()

            self.qtDesign.tableWidget.setItem(selected_row, 0, QTableWidgetItem(Name))
            self.qtDesign.tableWidget.setItem(selected_row, 1, QTableWidgetItem(Surname))
            self.qtDesign.tableWidget.setItem(selected_row, 2, QTableWidgetItem(Phone))

            self.qtDesign.lineEdit_Name.clear()
            self.qtDesign.lineEdit_Surname.clear()
            self.qtDesign.lineEdit_Phone.clear()
            
    def Clear(self):
        self.qtDesign.lineEdit_Name.clear()
        self.qtDesign.lineEdit_Surname.clear()
        self.qtDesign.lineEdit_Phone.clear()
        
    def Delete(self):
        selected_row = self.qtDesign.tableWidget.currentRow()
        if selected_row >= 0:
            self.qtDesign.tableWidget.removeRow(selected_row)
            self.Clear()


app = QApplication([])
window = main()
window.show()
app.exec_() # sonsuz dongu olusturur

