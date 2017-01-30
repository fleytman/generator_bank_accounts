"""
Основной скрипт программы.
Запускает конфигуратор окна, подключает слоты и отображает окно.
"""
# Импортируем системый модуль для корректного закрытия программы
import sys
# Импортируем минимальный набор виджетов
#from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
# Импортируем созданный нами класс со слотами
from slots import MainWindowSlots

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
        self.clip_x11 = QtWidgets.QApplication.clipboard().Selection

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
    # Должно делать поверх всех окон, но не делает
    # Window.setWindowFlags(Window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    ui = MainWindow(Window)
    Window.show()
    sys.exit(app.exec_())

