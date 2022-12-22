from PyQt5.QtWidgets import QMainWindow
from stock_searcher.ui.ui_mainwindow import Ui_MainWindow
from stock_searcher.amount_statistics import WidgetAmountStatistics
from stock_searcher.day_report import WidgetDayReport
from stock_searcher.week_report import WidgetWeekReport
from stock_searcher.month_report import WidgetMonthReport
from stock_searcher.goodinfo import WidgetGoodinfo
from stock_searcher.toolFunc import setComboBox


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        parma = setComboBox()
        self.Amount = WidgetAmountStatistics(self.tabAmountStatistics)
        self.Day = WidgetDayReport(
            self.tabDayReport, parma.options, parma.combo_dict)
        self.Week = WidgetWeekReport(
            self.tabWeekReport, parma.options, parma.combo_dict)
        self.Month = WidgetMonthReport(
            self.tabMonthReport, parma.options, parma.combo_dict)
        self.Profit = WidgetGoodinfo(self.tabGoodinfo)
