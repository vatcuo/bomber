import os
import time
import sys


def main():
    os.system("cls")
    print(
        "Обратите внимание, всю ответственность за совершенные вами действия берете вы. Автор форка (бомбера) предоставляет его (бомбер) лишь в ознакомительных или образовательных целях. Выбрав язык вы автоматически соглашаетесь с тем, что прочитали это сообщение. "
    )
    print(
        "\nPlease note that you are all responsible for the actions you have taken. The author of the fork (bomber) provides it (bomber) for informational or educational purposes only. By choosing a language, you automatically agree that you have read this message."
    )
    print(
        "\nВыбери язык | Choose language \n 1. English \n 2. Русский"
    )

    oss = input(">> ")

    if oss == "1":
        from language import eng
    elif oss == "2":
        from language import ru
    else:
        time.sleep(3)
        main()
main()
