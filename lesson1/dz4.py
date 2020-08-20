num = int(input("Введите целое положительное число: "))
max = 0

while num > 0:
    last_digit = num % 10
    if max < last_digit:
        max = last_digit
    if (max == 9):
        break
    num = num // 10

print(f"Максимальная цифра в числе: {max}")
