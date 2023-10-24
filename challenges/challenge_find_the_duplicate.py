# Desafio 05: Dado um array nums de números inteiros contendo n + 1 itens, em que cada inteiro está no intervalo [1, n], retorne apenas um número duplicado em nums. Caso não seja passado nenhum valor, ou seja passada uma string, ou não haja valores repetidos, retorne False.
# Challenge 05: Given an array nums of integers containing n + 1 items, in which each integer is within the interval [1, n], return only a duplicate number in nums. In case no value is passed, or a string is given, or there are no repeated values, return False.


def find_duplicate(nums):
    # criação de dois sets vazios - sets não permitem números repetidos
    numbers = set()
    duplicates = 0

    # itera sobre o array
    for num in nums:
        if (isinstance(num, str)) or (num < 0):
            return False
        # caso o número esteja nos números do set
        if num in numbers:
            # adiciona o número ao set de duplicatas
            duplicates = num
        # caso contrário, adiciona aos números que já foram passados
        else:
            numbers.add(num)

    if (duplicates == 0) or (len(nums) <= 1) or (isinstance(nums, str)):
        return False
    return duplicates
