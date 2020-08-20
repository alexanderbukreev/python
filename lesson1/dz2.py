time = int(input("Введите время в секундах: "))

hour = int(time / 3600)
time = time % 3600
min = int(time / 60)
sec = time % 60

print(f"{hour:02}:{min:02}:{sec:02}")
