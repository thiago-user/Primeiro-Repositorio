# Script que simula um sorteio de uma loteria tradiconal. O usuário escolhe 6 números de 1 à 60 e espera acertar algo
# Decidi não usar algumas funções que facilitem a construção do script


# O módulo 'time' será usada para contar o tempo para o script fazer a quantidade de sorteios desejada
from time import time
from random import randint


# 'user', guarda os números escolhidos pelo usuário
# 'sorteio', guarda os números sorteados
user = list()
sorteio = list()
cont = 1

# Esse 'print' é uma forma de "limpar a tela"
print("\n" * 250)
print("Escolha 1 numero e dê enter, faça isso 6 vezes... ou digite 0 para escolher aleatoriamente\n")

while len(user) < 6:
    n = int(input(f" {cont}=> "))

    # Se o número escolhido não estiver no intevalo esperado...
    if n < 1 or n > 60:
        # Verificamos se o número é igual à zero. Se sim, valores aleatórios serão atribuídos à 'user' até que 'user' tenha um total de 6 valores.
        if n == 0:
            while len(user) < 6:
                n = randint(1, 60)
                if n not in user:
                    user.append(n)
        else:
            print("\n" * 250)
            print(f"{n} Não esta entre 1 e 60\n")
    elif n in user:
        print("\n" * 250)
        print(f"Não, {n} ja fora escolhido\n")
    else:
        user.append(n)
        cont += 1

# Agora, precisamos colocar em ordem crescente os números escolhidos ('user')
for a in range(5):
    # Vamos comparar um elemento da lista com o (próximo elemento) elemento vizinho. Se o elemento à esquerda for maior que o (próximo elemento) elemento à direita, vamos inverter as posições desses elementos.
    for n in range(5):
        if user[n] > user[n + 1]:
            user[n], user[n + 1] = user[n + 1], user[n]

denovo = "S"
while denovo == "S":
    print("\n" * 250)
    # Aqui, o usuário escolherá quantos sorteios ele quer que o script realize e quantos números ele espera acertar
    qs = int(input("Quantos Sorteios? "))
    qa = int(input("Quantos Acertos?  "))
    print(
        f"\nSeus Números: {user[0]:2}, {user[1]:2}, {user[2]:2}, {user[3]:2}, {user[4]:2}, {user[5]:2}"
    )

    tempo = time()
    for sortear in range(qs):
        sorteio.clear()
        while len(sorteio) < 6:
            n = randint(1, 60)
            if n not in sorteio:
                sorteio.append(n)

        # 'acertos', guarda o total de acertos do usuário (comparado aos números sorteados) no sorteio atual
        acertos = 0
        for n in range(6):
            if user[n] in sorteio:
                acertos += 1

        if acertos >= qa:
            qs = sortear + 1
            for a in range(5):
                for n in range(5):
                    if sorteio[n] > sorteio[n + 1]:
                        sorteio[n], sorteio[n + 1] = sorteio[n + 1], sorteio[n]

            tempo = str(int(time() - tempo))
            print(
                f"Números Sort: {sorteio[0]:2}, {sorteio[1]:2}, {sorteio[2]:2}, {sorteio[3]:2}, {sorteio[4]:2}, {sorteio[5]:2}"
            )
            print(
                f"\nVocê ACERTOU {acertos} número(s) em {qs} sorteios! em {tempo} segundos"
            )
            print("----------------------------------------------------------")
            denovo = str(input("\nTentar Novamente? [S/N]")).upper()
            break

    if not acertos >= qa:
        # O tempo foi convertido para str() porque o resultado não estava sendo o esperado, quando "printado" an tela
        tempo = str(int(time() - tempo))
        denovo = str(
            input(
                f"\n{tempo} segundos\nVocê NÃO acertou o mínimo desejado. Tentar Novamente? [S/N]"
            )
        ).upper()
