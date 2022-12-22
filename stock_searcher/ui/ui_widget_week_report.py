# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\widget_week_report.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetWeekReport(object):
    def setupUi(self, WidgetWeekReport):
        WidgetWeekReport.setObjectName("WidgetWeekReport")
        WidgetWeekReport.resize(601, 576)
        self.verticalLayout = QtWidgets.QVBoxLayout(WidgetWeekReport)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(WidgetWeekReport)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_mm = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_mm.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_mm.setObjectName("lineEdit_mm")
        self.gridLayout.addWidget(self.lineEdit_mm, 1, 2, 1, 1)
        self.lineEdit_dd = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_dd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_dd.setObjectName("lineEdit_dd")
        self.gridLayout.addWidget(self.lineEdit_dd, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_yy = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_yy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_yy.setObjectName("lineEdit_yy")
        self.gridLayout.addWidget(self.lineEdit_yy, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 2)
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 3, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(WidgetWeekReport)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_status = QtWidgets.QLabel(self.groupBox_2)
        self.label_status.setObjectName("label_status")
        self.gridLayout_2.addWidget(self.label_status, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.pushButton_export = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_export.setObjectName("pushButton_export")
        self.verticalLayout_3.addWidget(self.pushButton_export)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(WidgetWeekReport)
        QtCore.QMetaObject.connectSlotsByName(WidgetWeekReport)

    def retranslateUi(self, WidgetWeekReport):
        _translate = QtCore.QCoreApplication.translate
        WidgetWeekReport.setWindowTitle(_translate("WidgetWeekReport", "Form"))
        self.groupBox.setTitle(_translate("WidgetWeekReport", "查詢條件"))
        self.label.setText(_translate("WidgetWeekReport", "日期："))
        self.label_2.setText(_translate("WidgetWeekReport", "分類項目："))
        self.pushButton_search.setText(_translate("WidgetWeekReport", "查詢"))
        self.groupBox_2.setTitle(_translate("WidgetWeekReport", "結果"))
        self.label_4.setText(_translate("WidgetWeekReport", "當前狀態："))
        self.label_3.setText(_translate("WidgetWeekReport", "工作表名稱(sheet name)："))
        self.label_status.setText(_translate("WidgetWeekReport", "等待"))
        self.pushButton_export.setText(_translate("WidgetWeekReport", "匯出"))
