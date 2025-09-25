from selenium import webdriver
from selenium.webdriver import edge
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QAbstractTableModel, Qt
from bs4 import BeautifulSoup
import pandas as pd
import os
import requests
from io import StringIO


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
            edge_options.add_argument("disable-gpu")
            driver = webdriver.Edge(options=edge_options)
        except Exception as e:
            print(e)
            return
        
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, features='lxml')
        select = soup.find('select', {'name': 'selectType'})
        self.options = [o.string for o in select.find_all('option')]
        self.combo_dict = {o.string: o['value']
                           for o in select.find_all('option')}
        
        url = 'https://goodinfo.tw/tw/index.asp'
        driver.get(url)
        self.cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
        driver.quit()


def getWebContent(url, **optional_type):
    checked = True
    df = None
    model = None
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    }

    try:
        r = requests.get(url, headers=headers, cookies=optional_type.get("cookies"))
        if r.status_code == requests.codes.ok:
            try:
                if optional_type.get("website") == "台灣證卷交易所":
                    df = pd.read_html(r.content)[0]
                else:
                    r.encoding = 'utf-8'
                    soup = BeautifulSoup(r.text, "lxml")
                    data = soup.select_one(optional_type.get("divID"))
                    df = pd.read_html(StringIO(data.prettify()))
                    df = df[len(df)-1]
                    if optional_type.get("type") == "獲利指標":
                        df.drop(df[df['年度', '年度'] == "年度"].index, inplace=True)
                model = pandasModel(df)
                checked = False
            except:
                print("解析失敗")
        else:
            print("連線至" + url + "發生錯誤")
    except Exception as e:
        print(e)
 
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
