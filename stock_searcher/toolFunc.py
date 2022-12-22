from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QAbstractTableModel, Qt
from bs4 import BeautifulSoup
import pandas as pd
import os
import requests


class pandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data.copy()
        self._data.columns = [c[1] for c in self._data.columns.values]

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class setComboBox():
    def __init__(self):
        self.catch()

    def catch(self):
        url = 'https://www.twse.com.tw/zh/page/trading/fund/T86.html'
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 啟動無痕模式
        chrome_options.add_argument('--disable-gpu')  # windows必須加入此行
        service = ["hide_console"]
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options, service_args=service)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, features='lxml')
        select = soup.find('select', {'name': 'selectType'})
        self.options = [o.string for o in select.find_all('option')]
        self.combo_dict = {o.string: o['value']
                           for o in select.find_all('option')}
        driver.quit()


def getWebContent(url, websiteType, divID=""):
    checked = False
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        try:
            if websiteType == "台灣證卷交易所":
                df = pd.read_html(r.content)[0]
            else:
                r.encoding = 'utf-8'
                soup = BeautifulSoup(r.text, "lxml")
                data = soup.select_one(divID)
                df = pd.read_html(data.prettify())[0]
                if websiteType == "獲利指標":
                    df.drop(df[df['年度', '年度'] == "年度"].index, inplace=True)
            model = pandasModel(df)
        except:
            checked = True
            df = None
            model = None
    else:
        print("連線失敗")
    return checked, df, model


def df2Excel(dataframe, sheetName):
    checked = False
    name, _ = QFileDialog.getSaveFileName(
        filter='All Files (*);;Excel File(*.xlsx)', initialFilter='Excel File(*.xlsx)')
    if name != '':
        if os.path.exists(name):
            with pd.ExcelWriter(name, engine='openpyxl', mode='a') as writer:
                wb = writer.book
                try:
                    wb.remove(wb[sheetName])
                except:
                    pass
                finally:
                    dataframe.to_excel(writer, sheet_name=sheetName)
        else:
            dataframe.to_excel(name, sheet_name=sheetName)
    else:
        checked = True
    return checked
