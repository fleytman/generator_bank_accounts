import os, sys
from random import randrange
import configparser
import logging

if sys.platform == "win32":
    from UiMainWindow import Ui_MainWindow
elif sys.platform == "darwin":
    from UiMainWindow_OSX import Ui_MainWindow
elif sys.platform == "linux":
    # На данный момент не реализованно
    from UiMainWindow_Linux import Ui_MainWindow

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

logging_error = logging.getLogger('Error log')
logging_accounts = logging.getLogger('Accounts log')

# setup_logger by jpmc26: http://stackoverflow.com/a/17037016
def setup_logger(logger_name, log_file, level=logging.INFO, formatter_m='%(asctime)s : %(message)s'):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter(formatter_m)
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)

setup_logger('Error log', r'error.log', logging.ERROR)
setup_logger('Accounts log', r'accounts.log', logging.INFO, '%(message)s')

# Проверка ключа по номеру счёта
def check_key(account, RkeyC):
    RkeyC_key = "713"

    # account_key = "71371371371371371371"
    account_key = (RkeyC_key * 7)[:-1]

    multiplication = []
    i = 0
    while i < 3:
        multiplication.append(int(RkeyC[i]) * int(RkeyC_key[i]))
        i += 1
    i = 0
    while i < 20:
        multiplication.append(int(account[i]) * int(account_key[i]))
        i += 1
    key = 0
    for i in multiplication:
        key += i
    key = ((key % 10) * 3) % 10

    logging_accounts.info(u" Ключ = %s" % key)
    return key


# Создаём собственный класс, наследуясь от автоматически сгенерированного
class MainWindowSlots(Ui_MainWindow):

    def start_program(self):

        regex = QRegExp("[0-9]+")

        self.lineEdit_3.setValidator(QRegExpValidator(regex))
        self.lineEdit_2.setValidator(QRegExpValidator(regex))
        self.lineEdit.setValidator(QRegExpValidator(regex))

        self.lineEdit_5.setValidator(QRegExpValidator(regex))
        self.lineEdit_7.setValidator(QRegExpValidator(regex))

        if not os.path.isfile('config.ini'):
            self.save_Config()

        config = self.loadConfig()

        # Данные для генерации счёта
        logging_accounts.info("-------------------------------------")
        bic1 = config['bic1']
        self.lineEdit_3.setText(bic1)
        logging_accounts.info(u"Бик банка: %s" % bic1)
        print(type(bic1))
        valuta = config['valuta']
        self.lineEdit_2.setText(valuta)
        logging_accounts.info(u"Валюта банка: %s" % valuta)
        first_group = config['first_group']
        self.lineEdit.setText(first_group)
        logging_accounts.info(u"Первая группа счёта: %s" % first_group)

        #Данные для ключевания счёта
        bic2 = config['bic2']
        self.lineEdit_5.setText(bic2)
        logging_accounts.info(u"Бик банка: %s" % bic2)
        account = config['account']
        self.lineEdit_7.setText(account)
        logging_accounts.info(u"Счёт для ключевания: %s" % account)

    def save_Config(self):
        configfile = open('config.ini', 'w')
        config = configparser.ConfigParser()
        config.add_section('tab1')
        config.set('tab1', 'bic', self.lineEdit_3.text())
        config.set('tab1', 'valuta', self.lineEdit_2.text())
        config.set('tab1', 'first_group', self.lineEdit.text())
        config.set('tab1', 'corr_enabled', str(self.checkBox.checkState()))

        config.add_section('tab2')
        config.set('tab2', 'bic', self.lineEdit_5.text())
        config.set('tab2', 'account', self.lineEdit_7.text())
        config.set('tab2', 'corr_enabled', str(self.checkBox_2.checkState()))

        config.write(configfile)
        configfile.close()

    def loadConfig(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        # tab1
        try:
            bic1 = config.get('tab1', 'bic')
        except ValueError:
            logging_error.error(
                "В config.ini неверно указано значение бик. Значение бик должно быть числом, работа программы будет завершена, проверьте config.ini")
            bic1 = ""
        try:
            valuta = config.get('tab1', 'valuta')
        except ValueError:
            logging_error.error(
                "В config.ini неверно указано значение валюты. Значение валюты должно быть числом, работа программы будет завершена, проверьте config.ini")
            valuta = ""
        try:
            first_group = config.get('tab1', 'first_group')
        except ValueError:
            logging_error.error(
                "В config.ini неверно указано значение первой группы. Значение первой группы должно быть числом, работа программы будет завершена, проверьте config.ini")
            first_group = ""
        try:
            corr_enabled = config.getint('tab1', 'corr_enabled')
        except ValueError:
            logging_error.error("В config.ini неверно указано значение corr_enabled. Значение corr_enabled должно быть числом, работа программы будет завершена, проверьте config.ini")
            corr_enabled = 0

        if corr_enabled == 2:
            self.checkBox.setChecked(1)

        # tab2
        try:
            config.getint('tab2', 'bic')
            bic2 = config.get('tab2', 'bic')
        except ValueError:
            logging_error.error(
                u"В config.ini неверно указано значение бик. Значение бик должно быть числом, работа программы будет завершена, проверьте config.ini")
            bic2 = ""
        try:
            config.getint('tab2', 'account')
            account = config.get('tab2', 'account')
        except ValueError:
            logging_error.error(
                u"В config.ini неверно указано значение счёта. Значение счёта должно быть числом, работа программы будет завершена, проверьте config.ini")
            account = ""
        try:
            corr_enabled2 = config.getint('tab2', 'corr_enabled')
        except ValueError:
            logging_error.error("В config.ini неверно указано значение corr_enabled. Значение corr_enabled должно быть числом, работа программы будет завершена, проверьте config.ini")
            corr_enabled2 = 0

        if corr_enabled2 == 2:
            self.checkBox_2.setChecked(1)

        return {'bic1': str(bic1), 'valuta': str(valuta), 'first_group': str(first_group), 'bic2': str(bic2), 'account': str(account)}

    def generate_key(self):
        self.save_Config()
        bic = self.lineEdit_5.text()
        account = self.lineEdit_7.text()[0:8] + "0" + self.lineEdit_7.text()[9:20]

        if len(bic) < 9:
            self.statusBar.showMessage("В поле \"БИК\" меньше 9 символов")
            return None
        if len(account) < 20:
            self.statusBar.showMessage("Счёт для ключевания < 20 символов")
            return None

        if self.checkBox_2.isChecked():
            # Значение условного номера кредитной организации
            RkeyC = bic[6:9]
        else:
            # Значение трехзначного условного номера РКЦ
            RkeyC = "0" + bic[4:6]

        key = check_key(account, RkeyC)

        final_acc = account[0:8] + str(key) + account[9:20]
        logging_accounts.info(u"Сключёванный счёт:\n%s" % final_acc)

        logging_accounts.info("-------------------------------------")
        # pyperclip.copy(final_acc)

        # Реализовать нормальный способ показывать ключ над 10 разрядом сключеванного счета
        if sys.platform == "win32":
            self.label_12.setText("  " + str(key))
        elif sys.platform == "darwin":
            self.label_12.setText(str(key))

        self.lineEdit_8.setEnabled(True)
        self.lineEdit_8.setText(final_acc)

        self.clip.setText(final_acc)

    def generate_account(self):
        """Скрипт, генерирующий счёт и ключ к счёту по указанному бику
    by fleytman, velichkin"""

        self.save_Config()
        bic = self.lineEdit_3.text()
        valuta = self.lineEdit_2.text()
        first_group = self.lineEdit.text()

        if len(bic) < 9:
            self.statusBar.showMessage("В поле \"БИК\" меньше 9 символов")
            return None
        if len(valuta) < 3:
            self.statusBar.showMessage("В поле \"Валюта\" меньше 3 символов")
            return None
        if len(first_group) < 5:
            self.statusBar.showMessage("В поле \"Группа\" меньше 5 символов")
            return None

        if self.checkBox.isChecked():
            # Значение условного номера кредитной организации
            RkeyC = bic[6:9]
        else:
            # Значение трехзначного условного номера РКЦ
            RkeyC = "0" + bic[4:6]

        account = first_group + valuta + "0"
        rand_acc = str(randrange(0, 100000000000))

        if len(rand_acc) <= 11:
            account = account + '0' * (11 - len(rand_acc)) + rand_acc
        # print account
        logging_accounts.info(account)

        key = check_key(account, RkeyC)

        final_acc = account[0:8] + str(key) + account[9:20]
        logging_accounts.info(u"Сключёванный счёт:\n%s" % final_acc)

        logging_accounts.info("-------------------------------------")

        self.clip.setText(final_acc)

        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setText(final_acc)
        return None

    #Сбросить результат на странице генерации ключа
    def reset1(self):
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setText("")

    #Сбросить результат на странице ключевания ключа
    def reset2(self):
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setText("")
        self.label_12.setText("")