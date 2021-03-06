# На основе шаблона из https://github.com/zaharsk/pyqt_test
"""
Основной скрипт программы.
Запускает конфигуратор окна, подключает слоты и отображает окно.
"""
# Импортируем системый модуль для корректного закрытия программы
import sys
# Импортируем минимальный набор виджетов
# from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
# Импортируем созданный нами класс со слотами
from slots import MainWindowSlots

import signal


# Создаём ещё один класс, наследуясь от класса со слотами
class MainWindow(MainWindowSlots):

    # При инициализации класса нам необходимо выпонить некоторые операции
    def __init__(self, dialog):
        # Сконфигурировать интерфейс методом из базового класса Ui_Form
        self.setupUi(dialog)
        # Подключить созданные нами слоты к виджетам
        self.connect_slots()
        # Иницировать буфер обмена
        self.clip = QtWidgets.QApplication.clipboard()

        #Обработка ctrl+c в консоли
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Подключаем слоты к виджетам
    def connect_slots(self):
        self.start_program()

        self.pushButton.clicked.connect(self.generate_account)
        self.pushButton_2.clicked.connect(self.generate_key)

        self.checkBox.stateChanged.connect(self.reset1)
        self.lineEdit_3.textChanged.connect(self.reset1)
        self.lineEdit_2.textChanged.connect(self.reset1)
        self.lineEdit.textChanged.connect(self.reset1)

        self.checkBox_2.stateChanged.connect(self.reset2)
        self.lineEdit_5.textChanged.connect(self.reset2)
        self.lineEdit_7.textChanged.connect(self.reset2)

        return None

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    # Поверх всех окон
    # Window.setWindowFlags(Window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    ui = MainWindow(Window)
    Window.show()
    sys.exit(app.exec_())

