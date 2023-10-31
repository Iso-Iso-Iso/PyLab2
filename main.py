from random import randint
# Fill arrays
def fill_array_by_random(size):
    return [randint(1, 9) for _ in range(size)]
# Sum up arrays
def sum_up_arrays(first_array, second_array):
    max_length = max(len(first_array), len(second_array))

    first_array = [0] * (max_length - len(first_array)) + first_array
    second_array = [0] * (max_length - len(second_array)) + second_array

    rest = 0
    result = []
    
    # Sum up loop
    for i in range(max_length - 1, -1, -1):
        total = first_array[i] + second_array[i] + rest
        rest = total // 10
        result.insert(0, total % 10)

    if rest:
        result.insert(0, rest)

    return result
# Subtract arrays
def subtract_arrays(first_array, second_array):
    result = []
    rest = 0
    # Substract loop
    for i in range(len(first_array) - 1, -1, -1):
        diff = first_array[i] - rest
        # clear delete wihtout rest
        if i < len(second_array):
            diff -= second_array[i]
        rest = 0
        # Take chunck from neighbour if we need
        if diff < 0:
            diff += 10
            rest = 1

        result.insert(0, diff)

    while result[0] == 0 and len(result) > 1:
        result.pop(0)

    return result
# Request data for arrays and operator
first_arr_length = int(input("Введите размер 1 массива: "))

second_arr_length = int(input("Введите размер 2 массива: "))

operation = input("Введите операцию. 1 - сложение, 2 - вычитание")
# Fill arrays
first_array = fill_array_by_random(first_arr_length)

second_array = fill_array_by_random(second_arr_length)
# Validate operator
if operation == "1":
    result_array = sum_up_arrays(first_array, second_array)
elif operation == "2":
    result_array = subtract_arrays(first_array, second_array)

print(f"1 массив: {first_array}")
print(f"2 массив: {second_array}")
print(f"\nРезультат: {result_array}")