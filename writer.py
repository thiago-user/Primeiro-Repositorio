# Esse script lê as próprias linhas do seu código e as imprime na tela

import os
from random import randint
from time import sleep


arq = open(r"D:\scripts\Python\algorithms\flights_.py", "r")
conteudo = arq.readlines()
arq.close()

for linha in conteudo:
    for carac in linha:
        x = randint(-45, 45)/100
        if x < 0.1:
            x = 0.1
        sleep(x)
        print(carac, end="")

# << FINALIZADO! >>
