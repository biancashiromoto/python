# Desafio 03: Desenvolva uma função que recebe uma string de parâmetro e verifica, retornando um valor booleano, se a string é um palíndromo, respeitando as seguintes regras:
# - O algoritmo deve ser feito usando uma solução recursiva
# - Caso seja passada uma string vazia, retorne False
# Challenge 03: Develop a function that takes a string as a parameter and checks, returning a boolean, if the string is a palindrome, following the conditions:
# - The algoritm must use a recursive solution
# - If the string is empty, return False


def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    # condição de parada
    # a função para de chamar a si mesma quando chegar ao meio da palavra
    if low_index >= high_index:
        return True

    if word[low_index] == word[high_index]:
        # se as letras forem iguais,
        # a função é chamada com os index progredindo, um em cada direção
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return False
