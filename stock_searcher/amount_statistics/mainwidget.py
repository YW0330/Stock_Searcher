from stock_searcher.ui.ui_widget_amount_statistics import Ui_WidgetAmountStatistics
from stock_searcher.toolFunc import df2Excel, getWebContent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox
import time


class WidgetAmountStatistics(QObject):
    def __init__(self, widget):
        super(WidgetAmountStatistics, self).__init__()
        self.ui = Ui_WidgetAmountStatistics()
        self.ui.setupUi(widget)
        self.ui.pushButton_search.clicked.connect(self.search)
        self.ui.pushButton_export.clicked.connect(self.export)
        self.uiEnable(False)

    def search(self):
        self.ui.label_status.setText("等待")
        if self.ui.radioButton_day.isChecked():
            day = self.ui.lineEdit_day_yy.text()
            day += self.ui.lineEdit_day_mm.text().zfill(2)
            day += self.ui.lineEdit_day_dd.text().zfill(2)
            url = "https://www.twse.com.tw/fund/BFI82U?response=html&dayDate="+day+"&type=day"
        elif self.ui.radioButton_week.isChecked():
            week = self.ui.lineEdit_week_yy.text()
            week += self.ui.lineEdit_week_mm.text().zfill(2)
            week += self.ui.lineEdit_week_dd.text().zfill(2)
            url = "https://www.twse.com.tw/fund/BFI82U?response=html&weekDate="+week+"&type=week"
        elif self.ui.radioButton_month.isChecked():
            month = self.ui.lineEdit_month_yy.text()
            month += self.ui.lineEdit_month_mm.text().zfill(2) + '01'
            url = "https://www.twse.com.tw/fund/BFI82U?response=html&monthDate="+month+"&type=month"
        checked, self.df, model = getWebContent(url, "台灣證卷交易所")
        if checked:
            self.ui.label_status.setText("查無此資料!!")
            QMessageBox.warning(None, "提示", "年份請輸入'西元年'<br>週報表請輸入'當週星期一'之日期")
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
            sheetName = "買賣金額表"
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
