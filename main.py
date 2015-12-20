from random import randrange
import pyperclip
import ConfigParser

def loadConfig():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    bic = config.get('connect', 'bic')
    valuta = config.get('connect', 'valuta')
    first_group = config.get('connect', 'first_group')

    return {'bic':bic,'valuta':valuta, 'first_group':first_group}

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
    print final_acc

    pyperclip.copy(final_acc)

if __name__ == '__main__':
    main()
