# 股票查詢器 Stock Searcher
本專案提供使用者一個 GUI 介面查詢臺灣的股票資訊。另外，本專案僅供使用者自行使用，不可進行任何商業用途。
## 如何使用? How to use?
- 複製專案到本地端 git clone
    ```shell
    git clone https://github.com/YW0330/Stock_Searcher.git
    ```
- 下載相關套件 Download depenaencies packages in Python `v3.10.7`
    ```shell
    pip install -r requirement.txt
    ```
- 執行專案 Execute this project from source code
    ```shell
    python -m stock_searcher
    ```
- PyInstaller 製作執行檔 Create executable file
    ```shell
    python scripts/build_exec.py
    ```
    - [Install Windows SDK](https://developer.microsoft.com/zh-tw/windows/downloads/windows-sdk/)
## 功能 Functions
- 搜尋`三大法人買賣金額統計表`、`三大法人買賣超日報`、`三大法人買賣超週報`、`三大法人買賣超月報`\
    :notes: `年`請輸入西元 (yyyy)，`週`請輸入該週的星期一 (Week start from  Monday)
- 搜尋`獲利指標`、`現金流量`、`資產負載比例`\
    :notes: 輸入股票代碼 (Stock ID)
- 資料匯出至 Excel (Export data to Excel)
## 資料來源 References
- [臺灣證卷交易所](https://www.twse.com.tw/zh/)
- [Goodinfo!台灣股市資訊網](https://goodinfo.tw/tw/)
