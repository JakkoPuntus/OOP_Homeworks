n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Создаем список строк для вывода
numbers_per_column = n//k if n/k == n//k else n//k + 1  # округление вверх

lines = ['' for _ in range(numbers_per_column)]

for i, word in enumerate(numbers): # перечисление по числам и их индексам
    formatted_word = f'{word:4}'
    lines[i % len(lines)] += formatted_word

for line in lines:
    print(line)