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
