# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'z:\Qt\PyQtTools\Python\components\ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.TabbedView)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.qAction_RawImageEditor = QtWidgets.QAction(MainWindow)
        self.qAction_RawImageEditor.setObjectName("qAction_RawImageEditor")
        self.qAction_clear_cache = QtWidgets.QAction(MainWindow)
        self.qAction_clear_cache.setObjectName("qAction_clear_cache")
        self.qAction_DebugMK = QtWidgets.QAction(MainWindow)
        self.qAction_DebugMK.setObjectName("qAction_DebugMK")
        self.menutest.addAction(self.qAction_RawImageEditor)
        self.menutest.addAction(self.qAction_clear_cache)
        self.menuTest.addAction(self.qAction_DebugMK)
        self.menubar.addAction(self.menutest.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menutest.setTitle(_translate("MainWindow", "文件"))
        self.menuTest.setTitle(_translate("MainWindow", "Test"))
        self.qAction_RawImageEditor.setText(_translate("MainWindow", "raw分析工具"))
        self.qAction_clear_cache.setText(_translate("MainWindow", "清理缓存"))
        self.qAction_DebugMK.setText(_translate("MainWindow", "Debug"))
