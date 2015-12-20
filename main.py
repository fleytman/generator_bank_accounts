from random import randrange
import pyperclip
import ConfigParser
import logging

logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.ERROR, filename = u'erroe.log')
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO, filename = u'accounts.log')

def loadConfig():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    try:
        bic = config.getint('connect', 'bic')
    except ValueError:
        logging.error(u"Неверно указано значение бик. Значение бик должно быть числом, работа программы будет завершена, проверьте config.ini")
        print u"Неверно указано значение бик. Значение бик должно быть числом, работа программы будет завершена, проверьте config.ini"
        exit()
    try:
        valuta = config.getint('connect', 'valuta')
    except ValueError:
        logging.error(u"Неверно указано значение валюты. Значение валюты должно быть числом, работа программы будет завершена, проверьте config.ini")
        print u"Неверно указано значение валюты. Значение валюты должно быть числом, работа программы будет завершена, проверьте config.ini"
        exit()
    try:
        first_group = config.getint('connect', 'first_group')
    except ValueError:
        logging.error(u"Неверно указано значение первой группы. Значение первой группы должно быть числом, работа программы будет завершена, проверьте config.ini")
        print u"Неверно указано значение первой группы. Значение первой группы должно быть числом, работа программы будет завершена, проверьте config.ini"
        exit()

    return {'bic':str(bic),'valuta':str(valuta), 'first_group':str(first_group)}

def main():
    '''Скрипт, генерирующий счёт и ключ к счёту по указанному бику
by fleytman, velichkin'''
    config = loadConfig()

    bic = config['bic']
    valuta = config['valuta']
    first_group = config['first_group']

    RkeyC = bic[6:9]
    RkeyC_key="713"

    account = first_group + valuta + "0"
    rand_acc = str(randrange(0,100000000000))

    if len(rand_acc) <= 11:
        account = account + '0'*(11-len(rand_acc)) + rand_acc
    print account

    account_key = "71371371371371371371"
    multiplication=[]

    i=0
    while i <3:
        multiplication.append(int(RkeyC[i])*int(RkeyC_key[i]))
        i+=1
    i=0
    while i <20:
        multiplication.append(int(account[i])*int(account_key[i]))
        i+=1
    key=0
    for i in multiplication:
        key+=i
    key= ((key%10) * 3)%10
    print u" Ключ =", key
    final_acc= account[0:8] + str(key) + account[9:20]
    logging.INFO(final_acc)
    print final_acc

    pyperclip.copy(final_acc)

if __name__ == '__main__':
    main()
