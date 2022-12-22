from stock_searcher import run
import sys
import os

if __name__ == "__main__":
    # 修正 PyInstaller v5.7.0 問題 https://github.com/pyinstaller/pyinstaller/issues/7325
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w")
    run()
