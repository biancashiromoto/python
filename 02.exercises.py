# Exercício 01: Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida

name = input(str("Enter your name: "))


def print_name(name):
    # inicia o loop for no comprimento do nome e vai até 1, excluindo o 0, decrementando 1
    for i in range(len(name), 0, -1):
        # imprime até o índice i
        print(name[:i])


print_name(name)