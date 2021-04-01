# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lamp_control.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets #khai báo thư viện pyqt5 phần này qt designer sẽ thêm sẵn những phần còn thiếu cho project
import image # khai báo file code của ảnh

# class dưới đây là giao diện cửa sổ chúng ta đã design bên QT code này là code theo giao giao diện đã tạo
class Ui_MainWindow(object): #class của sổ chinh của giao diện app
    def setupUi(self, MainWindow): # hàm setup các thành phần của giao diện
        MainWindow.setObjectName("MainWindow") #tên cửa sổ
        MainWindow.resize(523, 395) # kích thước cửa số chính
        MainWindow.setStyleSheet("")# stylesheet đi kèm
        self.centralwidget = QtWidgets.QWidget(MainWindow) 
        self.centralwidget.setObjectName("centralwidget")
        #code định dạng cho label 4
        self.label_4 = QtWidgets.QLabel(self.centralwidget) #khai báo cửa sổ cho label
        self.label_4.setGeometry(QtCore.QRect(10, 350, 501, 16)) # set kích thước và vị trí cho label
        self.label_4.setAlignment(QtCore.Qt.AlignCenter) # căn dòng
        self.label_4.setObjectName("label_4") # tên của label đó
        #code định dang cho btn_0ff
        self.btn_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_off.setGeometry(QtCore.QRect(290, 260, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_off.setFont(font)
        self.btn_off.setObjectName("btn_off")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 320, 501, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btn_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_on.setGeometry(QtCore.QRect(130, 260, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_on.setFont(font)
        self.btn_on.setObjectName("btn_on")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 481, 151))
        self.label_2.setStyleSheet("image: url(:/myimage/lamp_off.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # đoạn code kết nối nút nhấn với hàm on bên dưới
        self.btn_on.clicked.connect(self.on) # khi nút on lên mức 1 thì hàm on sẽ được gọi
        self.btn_off.clicked.connect(self.off) # tương tự nút on
         
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Nguyen Ngoc Hoang - Nguyen Pham Thanh Hung - Do Minh Toan - Truong Quang Phuc"))
        self.btn_off.setText(_translate("MainWindow", "OFF"))
        self.label.setText(_translate("MainWindow", "IOT LAMP CONTROL"))
        self.label_3.setText(_translate("MainWindow", "Program made by KMT Team"))
        self.btn_on.setText(_translate("MainWindow", "ON"))
        #hàm on off thay đổi hình ảnh khi nhấn nút
    def on(self):
        self.label_2.setStyleSheet("image: url(:/myimage/lamp_on);") #gọi ảnh đã lưu trong style sheet
    def off(self):
        self.label_2.setStyleSheet("image: url(:/myimage/lamp_off);")


if __name__ == "__main__": # hàm này là hàm main nhưng không nên viết code trong đây quá nhiều vì nó chủ yếu dùng để gọi và chaỵ hàm
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
