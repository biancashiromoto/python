# Desafio 02: Esta função veio pronta no projeto - Desenvolva os testes para a função encrypt_message. O teste está no diretório /tests
# Challenge 02: This function came ready in the project - Develop the tests for the encrypt_message function. The test file is in the directory /tests

def encrypt_message(message: str, key: int):

    if not isinstance(key, int):
        raise TypeError("tipo inválido para key")

    if not isinstance(message, str):
        raise TypeError("tipo inválido para message")

    if key not in range(1, len(message)):
        return "".join(reversed(message))

    part_one = reversed(message[:key])
    part_two = reversed(message[key:])

    if not key % 2:
        part_two, part_one = part_one, part_two

    return "".join(part_one) + "_" + "".join(part_two)
