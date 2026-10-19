"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput

#1
def count_vowels(data: TextInput) -> int:
    text = data.value.lower()
    count = 0
    for a in text:
        if a in "aeiou":
            count += 1
    return count

#2
def has_unique_characters(data: TextInput) -> bool:
    text = data.value
    return len(set(text)) == len(text)

#3
def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count

#4
def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    steps = 0
    while number >= 10:
        product = 1
        while number:
            product *= number % 10
            number //= 10
        number = product
        steps += 1
    return steps

#5
def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    n = len(predicted)
    return sum((p - e) ** 2 for p, e in zip(predicted, expected)) / n

#6
def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    parts = []
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            power = 0
            while number % divisor == 0:
                number //= divisor
                power += 1
            if power == 1:
                parts.append(f"({divisor})")
            else:
                parts.append(f"({divisor}**{power})")
        divisor += 1
    if number > 1:
        parts.append(f"({number})")
    return "".join(parts)

#7
def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    total = 0
    k = 0
    while total < cube_count:
        k += 1
        total += k * k
    if total == cube_count:
        return k
    return "It is impossible"

#8
def is_balanced_number(data: PositiveIntegerInput) -> bool:
    digits = [int(d) for d in str(data.value)]
    n = len(digits)
    mid = n // 2
    left_sum = sum(digits[:mid])
    right_start = mid if n % 2 == 0 else mid + 1
    right_sum = sum(digits[right_start:])
    return left_sum == right_sum

#1
print(count_vowels(TextInput("AEIOU")))
print(count_vowels(TextInput("bcdfg")))
print(count_vowels(TextInput("")))
print(count_vowels(TextInput("aAeEiIoOuU")))
print(count_vowels(TextInput("python")))

#2
print(has_unique_characters(TextInput("Aa")))
print(has_unique_characters(TextInput("abcde")))
print(has_unique_characters(TextInput("abcdefghijklmnopqrstuvwxyz")))
print(has_unique_characters(TextInput("")))
print(has_unique_characters(TextInput("abca")))

#3
print(count_one_bits(PositiveIntegerInput(255)))
print(count_one_bits(PositiveIntegerInput(1)))
print(count_one_bits(PositiveIntegerInput(1024)))
print(count_one_bits(PositiveIntegerInput(3)))
print(count_one_bits(PositiveIntegerInput(10)))

#4
print(multiplicative_persistence(PositiveIntegerInput(3)))
print(multiplicative_persistence(PositiveIntegerInput(999)))
print(multiplicative_persistence(PositiveIntegerInput(352)))
print(multiplicative_persistence(PositiveIntegerInput(39)))
print(multiplicative_persistence(PositiveIntegerInput(77)))

#5
print(mse(VectorPairInput([2, 4], [0, 0])))
print(mse(VectorPairInput([1], [1])))
print(mse(VectorPairInput([-1, 1], [1, -1])))
print(mse(VectorPairInput([0, 0], [1, 1])))
print(mse(VectorPairInput([1, 2, 3], [1, 2, 5])))

#6
print(prime_factorization(PositiveIntegerInput(100)))
print(prime_factorization(PositiveIntegerInput(862)))
print(prime_factorization(PositiveIntegerInput(97)))
print(prime_factorization(PositiveIntegerInput(862404)))
print(prime_factorization(PositiveIntegerInput(4)))

#7
print(pyramid(PositiveIntegerInput(30)))
print(pyramid(PositiveIntegerInput(4)))
print(pyramid(PositiveIntegerInput(1)))
print(pyramid(PositiveIntegerInput(9)))
print(pyramid(PositiveIntegerInput(55)))

#8
print(is_balanced_number(PositiveIntegerInput(12345)))
print(is_balanced_number(PositiveIntegerInput(1)))
print(is_balanced_number(PositiveIntegerInput(12021)))
print(is_balanced_number(PositiveIntegerInput(12)))
print(is_balanced_number(PositiveIntegerInput(1122)))