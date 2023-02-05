# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(490, 270, 121, 51))
        self.button1.setObjectName("button1")
        self.output_box_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_box_1.setGeometry(QtCore.QRect(470, 20, 521, 241))
        self.output_box_1.setObjectName("output_box_1")
        self.graph_widget = PlotWidget(self.centralwidget)
        self.graph_widget.setGeometry(QtCore.QRect(20, 360, 971, 291))
        self.graph_widget.setObjectName("graph_widget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 451, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.button3 = QtWidgets.QPushButton(self.tab)
        self.button3.setGeometry(QtCore.QRect(330, 40, 75, 24))
        self.button3.setObjectName("button3")
        self.file_location_box = QtWidgets.QPlainTextEdit(self.tab)
        self.file_location_box.setGeometry(QtCore.QRect(10, 40, 281, 61))
        self.file_location_box.setObjectName("file_location_box")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.button4 = QtWidgets.QPushButton(self.tab)
        self.button4.setGeometry(QtCore.QRect(330, 80, 75, 24))
        self.button4.setObjectName("button4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 63, 20))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 63, 20))
        self.label_7.setObjectName("label_7")
        self.button6 = QtWidgets.QPushButton(self.tab_2)
        self.button6.setGeometry(QtCore.QRect(300, 10, 121, 21))
        self.button6.setObjectName("button6")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(20, 37, 401, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.slider1 = QtWidgets.QSlider(self.widget)
        self.slider1.setMinimum(1)
        self.slider1.setMaximum(100)
        self.slider1.setProperty("value", 1)
        self.slider1.setOrientation(QtCore.Qt.Horizontal)
        self.slider1.setObjectName("slider1")
        self.horizontalLayout.addWidget(self.slider1)
        self.slider1_box = QtWidgets.QSpinBox(self.widget)
        self.slider1_box.setMinimum(1)
        self.slider1_box.setMaximum(100)
        self.slider1_box.setObjectName("slider1_box")
        self.horizontalLayout.addWidget(self.slider1_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.slider2 = QtWidgets.QSlider(self.widget)
        self.slider2.setMinimum(1)
        self.slider2.setMaximum(200)
        self.slider2.setOrientation(QtCore.Qt.Horizontal)
        self.slider2.setObjectName("slider2")
        self.horizontalLayout_2.addWidget(self.slider2)
        self.slider2_box = QtWidgets.QSpinBox(self.widget)
        self.slider2_box.setMinimum(1)
        self.slider2_box.setMaximum(200)
        self.slider2_box.setObjectName("slider2_box")
        self.horizontalLayout_2.addWidget(self.slider2_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(25)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.slider5 = QtWidgets.QSlider(self.widget)
        self.slider5.setMinimum(1)
        self.slider5.setMaximum(200)
        self.slider5.setOrientation(QtCore.Qt.Horizontal)
        self.slider5.setObjectName("slider5")
        self.horizontalLayout_6.addWidget(self.slider5)
        self.slider5_box = QtWidgets.QSpinBox(self.widget)
        self.slider5_box.setMinimum(1)
        self.slider5_box.setMaximum(200)
        self.slider5_box.setObjectName("slider5_box")
        self.horizontalLayout_6.addWidget(self.slider5_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.widget1 = QtWidgets.QWidget(self.tab_2)
        self.widget1.setGeometry(QtCore.QRect(20, 190, 401, 111))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.slider3 = QtWidgets.QSlider(self.widget1)
        self.slider3.setMinimum(1)
        self.slider3.setMaximum(100)
        self.slider3.setProperty("value", 1)
        self.slider3.setOrientation(QtCore.Qt.Horizontal)
        self.slider3.setObjectName("slider3")
        self.horizontalLayout_3.addWidget(self.slider3)
        self.slider3_box = QtWidgets.QDoubleSpinBox(self.widget1)
        self.slider3_box.setObjectName("slider3_box")
        self.horizontalLayout_3.addWidget(self.slider3_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(25)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.slider4 = QtWidgets.QSlider(self.widget1)
        self.slider4.setMinimum(1)
        self.slider4.setMaximum(200)
        self.slider4.setOrientation(QtCore.Qt.Horizontal)
        self.slider4.setObjectName("slider4")
        self.horizontalLayout_4.addWidget(self.slider4)
        self.slider4_box = QtWidgets.QSpinBox(self.widget1)
        self.slider4_box.setMinimum(1)
        self.slider4_box.setMaximum(200)
        self.slider4_box.setObjectName("slider4_box")
        self.horizontalLayout_4.addWidget(self.slider4_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.slider6 = QtWidgets.QSlider(self.widget1)
        self.slider6.setMinimum(1)
        self.slider6.setMaximum(100)
        self.slider6.setProperty("value", 1)
        self.slider6.setOrientation(QtCore.Qt.Horizontal)
        self.slider6.setObjectName("slider6")
        self.horizontalLayout_5.addWidget(self.slider6)
        self.slider6_box = QtWidgets.QDoubleSpinBox(self.widget1)
        self.slider6_box.setObjectName("slider6_box")
        self.horizontalLayout_5.addWidget(self.slider6_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 40, 91, 24))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 70, 91, 24))
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setTristate(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 131, 20))
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(800, 280, 71, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(802, 310, 71, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(890, 280, 91, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(890, 310, 91, 20))
        self.label_11.setObjectName("label_11")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(490, 330, 121, 21))
        self.button5.setObjectName("button5")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(660, 270, 115, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button2 = QtWidgets.QPushButton(self.layoutWidget)
        self.button2.setIconSize(QtCore.QSize(20, 20))
        self.button2.setObjectName("button2")
        self.verticalLayout.addWidget(self.button2)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1006, 26))
        self.menubar.setObjectName("menubar")
        self.menuHRV = QtWidgets.QMenu(self.menubar)
        self.menuHRV.setObjectName("menuHRV")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHRV.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "Run"))
        self.button3.setText(_translate("MainWindow", "Browse:"))
        self.label.setText(_translate("MainWindow", "File:"))
        self.button4.setText(_translate("MainWindow", "Load"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Data input"))
        self.label_4.setText(_translate("MainWindow", "BP"))
        self.label_7.setText(_translate("MainWindow", "ECG"))
        self.button6.setText(_translate("MainWindow", "Reset to Default"))
        self.label_2.setText(_translate("MainWindow", "Height        "))
        self.label_3.setText(_translate("MainWindow", "Distance     "))
        self.label_14.setText(_translate("MainWindow", "Prominence"))
        self.label_5.setText(_translate("MainWindow", "Height        "))
        self.label_6.setText(_translate("MainWindow", "Distance     "))
        self.label_13.setText(_translate("MainWindow", "Prominence"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Param adj"))
        self.checkBox_2.setText(_translate("MainWindow", "Raw ECG"))
        self.checkBox_3.setText(_translate("MainWindow", "RRI"))
        self.label_12.setText(_translate("MainWindow", "Plots to generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Run config"))
        self.label_8.setText(_translate("MainWindow", "Start Time:"))
        self.label_9.setText(_translate("MainWindow", "End Time"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "0"))
        self.button5.setText(_translate("MainWindow", "new window"))
        self.button2.setText(_translate("MainWindow", "Get Region"))
        self.checkBox.setText(_translate("MainWindow", "Show Marker"))
        self.menuHRV.setTitle(_translate("MainWindow", "HRV"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
