from stock_searcher.ui.ui_widget_month_report import Ui_WidgetMonthReport
from stock_searcher.toolFunc import df2Excel, getWebContent
from PyQt5.QtCore import QObject
import time


class WidgetMonthReport(QObject):
    def __init__(self, widget, option, dict):
        super(WidgetMonthReport, self).__init__()
        self.ui = Ui_WidgetMonthReport()
        self.ui.setupUi(widget)
        self.setComboBox(option)
        self.ui.pushButton_search.clicked.connect(lambda: self.search(dict))
        self.ui.pushButton_export.clicked.connect(self.export)
        self.uiEnable(False)

    def search(self, dict):
        self.ui.label_status.setText("等待")
        month = self.ui.lineEdit_yy.text()
        month += self.ui.lineEdit_mm.text().zfill(2)
        month += '01'
        selectType = dict[self.ui.comboBox.currentText()]
        url = "https://www.twse.com.tw/fund/TWT47U?response=html&date=" + \
            month+"&selectType="+selectType
        checked, self.df, model = getWebContent(url, "台灣證卷交易所")
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
            sheetName = "買賣超月表"
        self.ui.label_status.setText("匯出進行中...")
        checked = df2Excel(self.df, sheetName)
        if not checked:
            self.ui.lineEdit.setText('')
            self.ui.label_status.setText("匯出完成!")
        else:
            self.ui.label_status.setText("發生錯誤，請確認Excel檔案已關閉。")

    def setComboBox(self, option):
        self.ui.comboBox.addItems(option)

    def uiEnable(self, bool):
        self.ui.pushButton_export.setEnabled(bool)
        self.ui.lineEdit.setEnabled(bool)
