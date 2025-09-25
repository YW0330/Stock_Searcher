# Fix PyInstaller packaged pip_system_certs https://gitlab.com/alelec/pip-system-certs
import pip_system_certs.wrapt_requests; pip_system_certs.wrapt_requests.inject_truststore()
from stock_searcher import run
import sys
import os

if __name__ == "__main__":
    # Fix PyInstaller v5.7.0 issue https://github.com/pyinstaller/pyinstaller/issues/7325
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w")
    run()
