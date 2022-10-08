"""Main entry point"""
import cgitb 

import os
from PyQt5.Qt import QApplication
import qdarkstyle
from gui.prime import Prime

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
cgitb.enable(format = 'text', logdir = desktop)

APP = QApplication([])
APP.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
P = Prime()
os._exit(APP.exec_()) # pylint: disable=W0212
cle