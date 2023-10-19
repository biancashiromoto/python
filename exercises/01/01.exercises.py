# Exercício 01: Crie uma função que receba dois números e retorne o maior
# deles.
# Exercise 01: Create a function that takes two numbers and return the greater
# one

def biggest_number(a, b):
    if a > b:
        return a
    else:
        return b


# print(biggest_number(90, 25))

# Exercício 02: Calcule a média aritmética dos valores contidos em uma lista.
# Exercise 02: Calculate the average of the values in a list


def calculate_average(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum / len(numbers)


# print(calculate_average([2, 3, 4, 5, 6]))

# Exercício 03: Faça uma função que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.
# Exercise 03: Create a function that, given any value n such that n > 1,
# prints on the screen a square made of asterisks with side length of size n.


def print_square(n):
    for row in range(n):
        print(n * '* ')


# print(print_square(5))

#  Exercício 04: Crie uma função que receba uma lista de nomes e retorne o nome
# com a maior quantidade de caracteres.
# Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Caio", "Joana"], 
# o retorno deve ser "Fernanda".
# Exercise 04: Create a function that takes a list of names and returns the 
# name with the biggest length.
# For example, for ["José", "Lucas", "Nádia", "Fernanda", "Caio", "Joana"],
# the return must be "Fernanda"


def get_biggest_name(names):
    # para cada name no array de names
    for name in names:
        # retorna o elemento máximo, utilizando len como critério
        return max(names, key=len)


names = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
# print(get_biggest_name(names))

# Exercício 05: Considere que a cobertura da tinta é de 1 litro para cada 3
# metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
# R$80,00. Crie uma função que retorne dois valores em uma tupla contendo a
# quantidade de latas de tinta a serem compradas e o preço total a partir do
# tamanho de uma parede (em m²).
# Exercise 05: Given that the paint coverage is 1 liter for every 3 square
# meters and that the paint is sold in 18-liter cans, priced at R$80.00 each.
# Create a function that returns two values in a tuple containing the quantity
# of paint cans to be purchased and the total price based on the size of a
# wall (in square meters).


def get_values(sq_meters):
    paint_for_m2 = 1 / 3
    price_for_m2 = 80 / 3

    total_price = sq_meters * price_for_m2
    total_paint = sq_meters * paint_for_m2

    return (round(total_price, 2), round(total_paint, 2))


# print(get_values(1))

# Exercício 06: Crie uma função que receba os três lados de um triângulo e
# informe qual o tipo de triângulo formado ou "Not a triangle", caso não seja
# possível formar um triângulo.
# Exercise 06: Create a function that takes three sides of a triangle and
# informs what type of triangle it is or "Not a triangle" in case it is not a
#  triangle.


def check_triangle(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a):
        return "Not a triangle"
    if (a == b == c):
        return "Equilateral Triangle"
    elif (a == b) or (a == c) or (b == c):
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


# print(check_triangle(5, 6, 7))

# Exercício 07: Crie uma função que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um triângulo retângulo com n asteriscos de base.
# Exercise 07: Create a function  that, given any value n such that n > 1, 
# prints on the screen a right triangle made of asterisks with the base length of size n

def print_triangle(n):
    # o loop itera de 1 até n
    for row in range(1, n + 1):
        print(row * '* ')


print_triangle(5)
