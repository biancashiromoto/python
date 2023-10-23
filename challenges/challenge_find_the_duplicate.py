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
