#Генератор банковских счетов QT-version 0.8
Программа для генерации банквоских счетов и генерации ключа проверки.

![ScreenShot](http://savepic.org/8372535.png)

## Установка для запуска из исходников
1. Установить [python 3.5](https://www.python.org/downloads/) (записать в переменные среды, если ОС Windows)
2. Запустить в консоли
```bash
pip3 install -r requirements.txt
```

##Запуск
1. В файловом менеджере: двойной щелчок по main.py (в зависимсоти от ОС будут разные способы настроить ассоциации файлов *py с python3)
2. В консоли:
```bash
python3 main.py
```

##Сборка под свою ОС
Сборка под свою ОС делается с помощью pyinstaller из develop ветки:
```bash
pip3 install https://github.com/pyinstaller/pyinstaller/zipball/develop
```
Сборка acc_gen
```bash
pyinstaller --onefile --noconsole main.py --name acc_gen
```

В директории dist будет лежать бинарник acc_gen

##Известные проблемы
1. Сборка собранная на Windows 10 не работает в Windows 7: https://github.com/fleytman/generator_bank_accounts/issues/2

Запускалось под Windows 8 и Windows 10, Linux Mint, OS X Captain
