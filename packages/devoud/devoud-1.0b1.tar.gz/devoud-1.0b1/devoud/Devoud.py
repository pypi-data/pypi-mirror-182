#!/usr/bin/python3
from .lib import *
from .lib.devoud_data import __version__
import sys
import os


def main():
    print(f'''---------------------------------------------
  Добро пожаловать в
  _____  ________      ______  _    _ _____  
 |  __ \|  ____\ \    / / __ \| |  | |  __ \ 
 | |  | | |__   \ \  / / |  | | |  | | |  | |
 | |  | |  __|   \ \/ /| |  | | |  | | |  | |
 | |__| | |____   \  / | |__| | |__| | |__| |
 |_____/|______|   \/   \____/ \____/|_____/ 
    ({__version__}) by oneeyeddancer            
---------------------------------------------
''')
    os.environ["QT_FONT_DPI"] = "96"
    args = []
    app = QApplication(sys.argv + args)

    window = BrowserWindow()
    size = window.screen().availableGeometry()
    window.resize(size.width() * 2 / 3, size.height() * 2 / 3)
    window.show()
    ad = AdBlocker()
    if ad.load_file():
        interceptor = WebEngineUrlRequestInterceptor(ad.rules)
        QWebEngineProfile.defaultProfile().setUrlRequestInterceptor(interceptor)

    app.exec()


if __name__ == '__main__':
    main()
