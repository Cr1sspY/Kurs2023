import sqlite3
import sys
from datetime import datetime

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLineEdit


class AuthWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("forms/auth.ui", self)
        self.ui.show()
        self.setWindowTitle('Авторизация')
