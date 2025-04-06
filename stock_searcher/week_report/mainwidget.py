from stock_searcher.ui.ui_widget_week_report import Ui_WidgetWeekReport
from stock_searcher.toolFunc import df2Excel, getWebContent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox
import time


class WidgetWeekReport(QObject):
    def __init__(self, widget, option, dict):
        super(WidgetWeekReport, self).__init__()
        self.ui = Ui_WidgetWeekReport()
        self.ui.setupUi(widget)
        self.setComboBox(option)
        self.ui.pushButton_search.clicked.connect(lambda: self.search(dict))
        self.ui.pushButton_export.clicked.connect(self.export)
        self.uiEnable(False)

    def search(self, dict):
        self.ui.label_status.setText("等待")
        week = self.ui.lineEdit_yy.text()
        week += self.ui.lineEdit_mm.text().zfill(2)
        week += self.ui.lineEdit_dd.text().zfill(2)
        selectType = dict[self.ui.comboBox.currentText()]
        url = "https://www.twse.com.tw/fund/TWT54U?response=html&date=" + \
            week+"&selectType="+selectType
        checked, self.df, model = getWebContent(url, "台灣證卷交易所")
        if checked:
            self.ui.label_status.setText("查無此資料!!")
            QMessageBox.warning(None, "提示", "年份請輸入'西元年'與'當週星期一'之日期")
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
            sheetName = "買賣超週表"
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
