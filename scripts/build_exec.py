import PyInstaller.__main__
import os
import shutil

# NOTE you need to change the path if you want to build it.
# A path to search for imports (like using PYTHONPATH).
# If it has been include in yout system PATH, you don't have to add it.
PATH = [
    # NOTE Need libs in package PyQt5.
    'C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages/PyQt5/Qt5/bin',
    'C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages/PyQt5/Qt5/plugins',

    # NOTE Need Windows Kits 10 to support win10.
    'C:/Program Files (x86)/Windows Kits/10/Redist/10.0.22621.0/ucrt/DLLs/x86',
    'C:/Program Files (x86)/Windows Kits/10/Redist/10.0.22621.0/ucrt/DLLs/x64',
]

HIDEEN_IMPORT = [
    'PyQt5.sip'
]


def build_exec():
    opts = [
        # program to package
        'stock_searcher/__main__.py',

        # exe name
        '--name=上市三大法人買賣超與Goodinfo',

        # NOTE Clean PyInstaller cache and remove temporary files before building.
        # will slow down the speed
        # '--clean',

        # NOTE '--onefile' Create a one-file bundled executable.
        # maybe not stable in some environment, need more test.
        '--onefile',

        # NOTE if you want exe not to print info to I/O, use '-w' .
        '-w'

        # NOTE if ypu want to extra debug info, use the '-debug'.
        # '--debug'
    ]
    opts += [f'--paths={path}' for path in PATH]
    opts += [f'--hidden-import={path}' for path in HIDEEN_IMPORT]

    PyInstaller.__main__.run(opts)


def rmPreFiles():
    TARGET_DIR = 'dist/'
    if (os.path.isdir(TARGET_DIR)):
        shutil.rmtree(TARGET_DIR)
    os.mkdir(TARGET_DIR)


def run():
    rmPreFiles()
    build_exec()


if __name__ == '__main__':
    run()
