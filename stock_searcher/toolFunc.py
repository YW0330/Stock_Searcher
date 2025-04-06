from selenium import webdriver
from selenium.webdriver import chrome, edge
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
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
        try:
            edge_options = edge.options.Options()
            edge_options.add_argument("headless")
            edge_service = edge.service.Service(
                EdgeChromiumDriverManager().install())
            edge_service.creation_flags = 0x08000000  # 關閉 console 視窗
            driver = webdriver.Edge(service=edge_service, options=edge_options)
        except Exception as e:
            print(e.msg)
            chrome_options = chrome.options.Options()
            chrome_options.add_experimental_option("detach", True)
            chrome_options.add_experimental_option(
                "excludeSwitches", ['enable-automation'])
            prefs = {"credentials_enable_service": False,
                     "profile.password_manager_enabled": False}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_service = chrome.service.Service(
                ChromeDriverManager().install())
            chrome_service.creation_flags = 0x08000000  # 關閉 console 視窗
            self.driver = webdriver.Chrome(
                service=chrome_service, options=chrome_options)
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
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    }
    cookies = {
        'CLIENT%5FID': '20250201215246820%5F220%2E136%2E161%2E233',
        'TW_STOCK_BROWSE_LIST': '8299%7C6129%7C2454%7C1459%7C3189%7C2337%7C1528%7C0050%7C6669%7C6142%7C4938%7C2357%7C3515%7C2401%7C3592%7C5289%7C2330%7C2308%7C2360%7C4906',
        'IS_TOUCH_DEVICE': 'F',
        'SCREEN_SIZE': 'WIDTH=1920&HEIGHT=1080',
    }
    r = requests.get(url, headers=headers, cookies=cookies)
    if r.status_code == requests.codes.ok:
        try:
            if websiteType == "台灣證卷交易所":
                df = pd.read_html(r.content)[0]
            else:
                r.encoding = 'utf-8'
                soup = BeautifulSoup(r.text, "lxml")
                data = soup.select_one(divID)
                df = pd.read_html(data.prettify())
                df = df[len(df)-1]
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
