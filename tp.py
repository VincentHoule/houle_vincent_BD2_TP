# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tp.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 894)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_creer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_creer.setGeometry(QtCore.QRect(10, 50, 71, 28))
        self.pushButton_creer.setObjectName("pushButton_creer")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 221, 41))
        self.label_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(690, 20, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_chapitre = QtWidgets.QLabel(self.centralwidget)
        self.label_chapitre.setGeometry(QtCore.QRect(220, 160, 221, 71))
        self.label_chapitre.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.label_chapitre.setObjectName("label_chapitre")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 800, 121, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_destination = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_destination.setGeometry(QtCore.QRect(230, 800, 131, 22))
        self.comboBox_destination.setObjectName("comboBox_destination")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(680, 50, 160, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_kai_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_kai_4.setObjectName("comboBox_kai_4")
        self.gridLayout_2.addWidget(self.comboBox_kai_4, 4, 0, 1, 1)
        self.comboBox_kai_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_kai_3.setObjectName("comboBox_kai_3")
        self.gridLayout_2.addWidget(self.comboBox_kai_3, 2, 0, 1, 1)
        self.comboBox_kai_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_kai_2.setObjectName("comboBox_kai_2")
        self.gridLayout_2.addWidget(self.comboBox_kai_2, 1, 0, 1, 1)
        self.comboBox_kai_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_kai_5.setObjectName("comboBox_kai_5")
        self.gridLayout_2.addWidget(self.comboBox_kai_5, 5, 0, 1, 1)
        self.comboBox_kai_1 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_kai_1.setObjectName("comboBox_kai_1")
        self.gridLayout_2.addWidget(self.comboBox_kai_1, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(710, 250, 341, 521))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit_equipement = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_equipement.setObjectName("textEdit_equipement")
        self.gridLayout_3.addWidget(self.textEdit_equipement, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.textEdit_speciaux = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_speciaux.setObjectName("textEdit_speciaux")
        self.gridLayout_3.addWidget(self.textEdit_speciaux, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.textEdit_repas = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_repas.setObjectName("textEdit_repas")
        self.gridLayout_3.addWidget(self.textEdit_repas, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(260, 10, 401, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_argent = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_argent.setObjectName("lineEdit_argent")
        self.gridLayout_4.addWidget(self.lineEdit_argent, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 2, 1, 1)
        self.lineEdit_nom = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.gridLayout_4.addWidget(self.lineEdit_nom, 0, 1, 1, 1)
        self.spinBox_endurance = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_endurance.setObjectName("spinBox_endurance")
        self.gridLayout_4.addWidget(self.spinBox_endurance, 1, 3, 1, 1)
        self.spinBox_habilite = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_habilite.setObjectName("spinBox_habilite")
        self.gridLayout_4.addWidget(self.spinBox_habilite, 0, 3, 1, 1)
        self.pushButton_sauvegarder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sauvegarder.setGeometry(QtCore.QRect(10, 90, 111, 31))
        self.pushButton_sauvegarder.setObjectName("pushButton_sauvegarder")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(870, 20, 55, 16))
        self.label_6.setObjectName("label_6")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(870, 50, 160, 80))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox_arme_1 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_arme_1.setObjectName("comboBox_arme_1")
        self.gridLayout_5.addWidget(self.comboBox_arme_1, 0, 0, 1, 1)
        self.comboBox__arme_2 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox__arme_2.setObjectName("comboBox__arme_2")
        self.gridLayout_5.addWidget(self.comboBox__arme_2, 1, 0, 1, 1)
        self.plainTextEdit_chapitre = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_chapitre.setGeometry(QtCore.QRect(40, 270, 591, 491))
        self.plainTextEdit_chapitre.setObjectName("plainTextEdit_chapitre")
        self.comboBox_charger = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_charger.setGeometry(QtCore.QRect(120, 130, 131, 21))
        self.comboBox_charger.setObjectName("comboBox_charger")
        self.pushButton_charger = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_charger.setGeometry(QtCore.QRect(10, 130, 93, 28))
        self.pushButton_charger.setObjectName("pushButton_charger")
        self.pushButton_chapitre = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chapitre.setGeometry(QtCore.QRect(400, 800, 131, 28))
        self.pushButton_chapitre.setObjectName("pushButton_chapitre")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_creer.setText(_translate("MainWindow", "Créer"))
        self.label_2.setText(_translate("MainWindow", "Nouveau personnage"))
        self.label_5.setText(_translate("MainWindow", "Disciplines Kaï"))
        self.label_chapitre.setText(_translate("MainWindow", "Chapitre"))
        self.label_7.setText(_translate("MainWindow", "Prochain Chapitre"))
        self.label_10.setText(_translate("MainWindow", "Équipement"))
        self.label_11.setText(_translate("MainWindow", "Objets spéciaux"))
        self.label_9.setText(_translate("MainWindow", "Repas"))
        self.label_4.setText(_translate("MainWindow", "Endurance"))
        self.label.setText(_translate("MainWindow", "Nom :"))
        self.label_8.setText(_translate("MainWindow", "Argent :"))
        self.label_3.setText(_translate("MainWindow", "Points d\'habilité"))
        self.pushButton_sauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.label_6.setText(_translate("MainWindow", "Arme"))
        self.pushButton_charger.setText(_translate("MainWindow", "Charger"))
        self.pushButton_chapitre.setText(_translate("MainWindow", "Prochain Chapitre"))
