# Desafio 04: Desenvolva um algoritmo que receba duas strings, as ordene e identifique se uma é anagrama da outra. O retorno da função deve ser uma tupla (com as duas strings ordenadas) e um booleano indicando se são anagramas ou não. O algoritmo deve ser case insensitive.
# Challenge 04: Develop an algorithm that takes two strings, sort them and identify if they are an anagram of the other. The return must be a tuple (containing the two sorted strings) and a boolean, indicating if they are anagrams or not. The algorithm must be case insensitive.


def is_anagram(first_string, second_string):
    sorted_first_string = sort_string(first_string.lower())
    sorted_second_string = sort_string(second_string.lower())
    third_element = False
    if (first_string == "" or second_string == ""):
        third_element = False
    elif (sorted_first_string != sorted_second_string):
        third_element = False
    else:
        third_element = True
    return sorted_first_string, sorted_second_string, third_element


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # divide o array pela metade e as nomeia left e right
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # divide os dois arrays novamente em dois, de forma recursiva
    left = merge_sort(left)
    right = merge_sort(right)

    # retorna o array ordenado
    return merge(left, right)


# recebe dois arrays como parâmetro
def merge(left, right):
    # cria um array vazio que vai armazenar os números ordenados
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # se o elemento left[i] < right[j], ele deve ser adicionado ao result
        # e o i é incrementado para passarmos para o próximo elemento
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        # caso contrário, o elemento de right deve ser adicionado ao result
        # e j é incrementado para passarmos para o próximo elemento
        else:
            result.append(right[j])
            j += 1

    # ao final, os elementos de left a partir do index i até o final do array
    # são adicionados a result
    result.extend(left[i:])
    # ao final, os elementos de right a partir do index j até o final do array
    # são adicionados a result
    result.extend(right[j:])
    return result


def sort_string(input_string):
    # converte a string de entrada em uma lista de caracteres
    char_list = list(input_string)
    # ordena os caracteres e retorna uma nova lista contendo os caracteres
    # ordenados
    sorted_chars = merge_sort(char_list)
    # concatena os caracteres da lista sorted_charts em uma única string
    sorted_string = ''.join(sorted_chars)
    return sorted_string

