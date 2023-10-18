# sys é um módulo que fornece acesso a variávies do niterpretador Python e para interagir com o ambiente em que o Python é executado
# import sys
# quando o Python executa um script diretamente, ele define o __name__ como __main__ - significa que o script está sendo executado como o programa principal
# if __name__ == "__main__":
    # sys.argv é uma lista que contém todos os argumentos passados para o script, e sys.argv[0] é o nome do próprio script
    # o loop itera sobre todos os argumentos passados na linha de comando e imprime cada um deles no console
    # for argument in sys.argv:
    #     print("Received: ", argument)

# -----------------------------------------------------

    # name = input("Name: ")

    # for letter in name:
    #     print(letter)

# -----------------------------------------------------

# # recebe os números
# numbers = input(
#     "Type a list of natural numbers, separated by an empty space: "
# )
# # cria um array contendo os números sem os espaços
# numbers_array = numbers.split(" ")

# sum = 0

# # para cada item no array
# for number in numbers_array:
#     # verifica se é um número
#     if not number.isdigit():
#         print(f"Error! {number} is not a natural number")
#     else:
#         # int converte uma string ou number para integer
#         sum += int(number)


# print(f"The sum of the numbers is: {sum}")

# -----------------------------------------------------

# a, b = "cd"
# print(a)  # saída: c
# print(b)  # saída: d

# head, *tail = (1, 2, 3)  # Quando um * está presente no desempacotamento, os valores são desempacotados em formato de lista.
# print(head)  # saída: 1
# print(tail)  # saída: [2, 3]

# -----------------------------------------------------

# while True:
#     try:
#         x = int(input("Por favor digite um número inteiro: "))
#         break
#     except ValueError:
#         # 'ValueError' é a exceção que ocorre quando a função int() recebe um
#         # valor que não pode ser traduzido para número inteiro
#         print("Oops! Esse não era um número inteiro. Tente novamente...")

# -----------------------------------------------------

# def get_students(file_name):
#     try:
#         with open(file_name, "r") as file:
#             students = []
#             for student in file:
#                 name, grade = student.split()
#                 students.append({"name": name, "grade": int(grade)})
#         return students
#     except FileNotFoundError:
#         print("File not found")


# def filter_students(students):
#     failed = []
#     for student in students:
#         if student["grade"] < 6:
#             failed.append(student["name"])
#     print(failed)
#     return failed


# students = get_students("students.txt")
# failed_students = filter_students(students)

# with open("failed_students.txt", "w") as failed_students_file:
#     for failed_student in failed_students:
#         failed_students_file.write(f"{failed_student}\n")

# -----------------------------------------------------


# import csv

# with open("graduacao_unb.csv", encoding="utf-8") as file:
#     graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')

#     header, *data = graduacao_reader

# print(data)

# -----------------------------------------------------

import csv

# Abre o arquivo CSV para leitura, especificando o delimitador (",") e o caractere de citação ('"')
with open("graduacao_unb.csv", encoding="utf8") as file:
    # Cria um objeto leitor de CSV
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
    # Usando o conceito de desempacotamento, lê o cabeçalho (primeira linha) e o restante dos dados (restantes das linhas)
    header, *data = graduacao_reader

# Cria um dicionário vazio para agrupar por departamento
group_by_department = {}

# Itera sobre as linhas de dados
for row in data:
    # Obtém o nome do departamento da coluna 16 (índice 15 no Python, pois a indexação começa em 0)
    department = row[15]
    
    # Se o departamento não está no dicionário, inicializa com 0
    if department not in group_by_department:
        group_by_department[department] = 0
    # Incrementa a contagem de cursos para o departamento
    group_by_department[department] += 1

# Escreve o relatório em um novo arquivo .csv

# Abre um arquivo para escrita
with open("department_report.csv", "w", encoding = "utf-8") as file:
    # Cria um objeto escritor de CSV
    writer = csv.writer(file)

    # Escreve o cabeçalho no arquivo
    headers = [
        "Departamento",
        "Total de Cursos",
    ]
    writer.writerow(headers)

    # Escreve as linhas de dados
    # método items() retorna uma visualização dos pares chave-valor no dicionário como uma sequência de tuplas
    for department, grades in group_by_department.items():
        row = [
            department,
            grades,
        ]
        writer.writerow(row)
