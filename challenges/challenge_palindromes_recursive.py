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
