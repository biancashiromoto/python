# Desafio 01: Desenvolva uma função que receba como parâmetros uma lista de tuplas contendo o período de permanência de um grupo de pessoas estudantes em um sistema com o horário de entrada em saída (permanence_period) e um horário (target_time). A função deve retornar quantas pessoas estudantes estão ativas no target_time dado, respeitando os seguintes requisitos:
# - O algoritmo deve utilizar uma solução iterativa
# - Caso o target_time seja nulo, ou haja alguma entrada inválida em permanence_period, o valor retornado deve ser None

# Challenge 01: Design a function that takes a list of tuples representing the time intervals when students are present (permanence_period) and a target time. The function should compute and return the count of active students at the specified target_time. Adhere to the following conditions:
# - The algorithm must implement an iterative approach.
# - If the target_time is null or there are any invalid entries in permanence_period, the function should return None.

# Exemplos de lista de tuplas/Tuples list example:
# [
#     ([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)], 5, 3),
#     ([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 1, 2),
#     ([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5)], 3, 2),
#     ([(1, 1), (2, 2), (3, 3), (4, 4)], 1, 1),
#     ([(1, 2), (1, 3), (2, 3)], 2, 3),
# ]


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    for student_permanence in permanence_period:
        entry_time = student_permanence[0]
        out_time = student_permanence[1]
        if (
            entry_time is None or not isinstance(entry_time, int)
          ) or (
            out_time is None or not isinstance(out_time, int)
          ):
            return None
        if (int(entry_time) <= target_time <= int(out_time)):
            counter += 1
    return counter
