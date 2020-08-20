num = int(input("Введите произвольное число: "))
num2 = str(num)
num2 += num2
num3 = num2 + str(num)
sum = num + int(num2) + int(num3)
print(f"{num} + {num2} + {num3} = {sum}")
