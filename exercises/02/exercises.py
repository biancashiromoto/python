import random
import re

# # Exercício 01: Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida

# name = input(str("Enter your name: "))


# def print_name(name):
#     # inicia o loop for no comprimento do nome e vai até 1, excluindo o 0, decrementando 1
#     for i in range(len(name), 0, -1):
#         # imprime até o índice i
#         print(name[:i])


# print_name(name)

# -----------------------------------------------------

# Exercício 02: Dado o seguinte arquivo no formato JSON, leia seu conteúdo e calcule a porcentagem de livros em cada categoria em relação ao número total de livros.

# import json
# import csv


# def get_books(file_name):
#     with open(file_name, "r") as file:
#         return json.load(file)


# def count_by_category(books):
#     categories = {}
#     # itera sobre os livros
#     for book in books:
#         # itera sobre as categorias de cada livro
#         for category in book["categories"]:
#             # verifica se a categoria já existe no dicionário - o get retorna None se a categoria não existir
#             if not categories.get(category):
#                 # caso não exista, é adicionada com valor inicial 0, porque quando uma nova categoria é criada, ainda não tem nenhum livro que a tenha
#                 categories[category] = 0
#             # independentemente de a categoria ter sido criada agora ou não, é incrementada uma unidade para essa categoria, já que o livro analisado nessa iteração é dessa categoria 
#             categories[category] += 1
#     return categories


# books = get_books("books.json")
# categories = count_by_category(books)


# def get_books_list(books_by_category, total_books):
#     return [
#         # percorre o dicionário books_by_category e descompacta os pares chave-valor em category e num_books
#         # cria uma lista com dois elementos - o nome da categoria e porcentagem de livros
#         [category, num_books / total_books]
#         # o método items() retorna uma lista de tuplas com pares chave-valor do dicionário
#         for category, num_books in books_by_category.items()
#     ]


# def write_csv(file_name):
#     with open(file_name, "w", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         headers = [
#             "Category",
#             "%"
#         ]
#         writer.writerow(headers)

#         rows = get_books_list(categories, len(books))
#         for category, percentage in rows:
#             row = [
#                 category,
#                 f"{percentage:.2%}",
#             ]
#             writer.writerow(row)


# write_csv("categories.csv")

# -----------------------------------------------------

def fizz_buzz(n):
    result = []
    # começa a iterar do index 1 e v ai até n + 1
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


print(fizz_buzz(5))

# -----------------------------------------------------


def validate_email(email):
    valid_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(valid_email, email) is None:
        raise ValueError(
            "Invalid email"
        )
    

print(validate_email("email@email.com"))