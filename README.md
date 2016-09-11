#Генератор банковских счетов QT-version 0.8
Программа для генерации банквоских счетов и генерации ключа проверки.

![ScreenShot](http://savepic.org/8372535.png)

## Установка для запуска из исходников
1. Установить [python 3.5](https://www.python.org/downloads/) записать в переменные среды(если ОС Windows)
2. Запустить в консоли pip3 install -r requirements.txt

##Запуск
В файловом менеджереЖ
Двойной щелчок по main.py (в зависимсоти от ОС будут разные способы настроить ассоциации файлов *py с python3)
В консоли:
python3 main.py

##Сборка под Windows
Сборка под Windows делается с помощью pyinstaller из develop ветки:
pip3 install https://github.com/pyinstaller/pyinstaller/zipball/develop

Сборка acc_gen.exe
pyinstaller --onefile --noconsole main.py --name acc_gen

На данный момент у сборки таким образом есть надостаток: https://github.com/fleytman/generator_bank_accounts/issues/2

Запускалось под Windows 8 и Windows 10, Linux Mint, OS X Captain
