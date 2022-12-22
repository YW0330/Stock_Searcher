from stock_searcher.ui.ui_widget_goodinfo import Ui_WidgetGoodinfo
from stock_searcher.toolFunc import df2Excel, getWebContent
from PyQt5.QtCore import QObject
import time


class WidgetGoodinfo(QObject):
    def __init__(self, widget):
        super(WidgetGoodinfo, self).__init__()
        self.ui = Ui_WidgetGoodinfo()
        self.ui.setupUi(widget)
        self.ui.pushButton_search.clicked.connect(self.search)
        self.ui.pushButton_export.clicked.connect(self.export)
        self.uiEnable(False)

    def search(self):
        self.ui.label_status.setText("等待")
        self.stockID = self.ui.lineEdit_stockID.text()
        if self.ui.radioButton_profit.isChecked():
            url = "https://goodinfo.tw/tw/StockBzPerformance.asp"
            self.type = "獲利指標"
            divID = "#txtFinDetailData"
        elif self.ui.radioButton_cash.isChecked():
            url = "https://goodinfo.tw/tw/StockCashFlow.asp"
            self.type = "現金流量"
            divID = "#txtFinDetailData"
        elif self.ui.radioButton_debt.isChecked():
            url = "https://goodinfo.tw/tw/StockAssetsStatus.asp"
            self.type = "資產負載比例"
            divID = "#divDetail"
        url += "?STOCK_ID=" + self.stockID

        checked, self.df, model = getWebContent(url, self.type, divID)
        if checked:
            self.ui.label_status.setText("查無此資料!!")
            self.uiEnable(False)
        else:
            self.uiEnable(True)
        self.ui.tableView.setModel(model)
        self.ui.pushButton_search.setEnabled(False)
        time.sleep(3)
        self.ui.pushButton_search.setEnabled(True)

    def export(self):
        sheetName = self.ui.lineEdit.text()
        if sheetName == '':
            sheetName = self.stockID + self.type
        self.ui.label_status.setText("匯出進行中...")
        checked = df2Excel(self.df, sheetName)
        if not checked:
            self.ui.lineEdit.setText('')
            self.ui.label_status.setText("匯出完成!")
        else:
            self.ui.label_status.setText("發生錯誤，請確認Excel檔案已關閉。")

    def uiEnable(self, bool):
        self.ui.pushButton_export.setEnabled(bool)
        self.ui.lineEdit.setEnabled(bool)
