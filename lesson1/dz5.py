rev = int(input("Укажите доходы фирмы: "))
exp = int(input("Укажите расходы фирмы: "))
profit = rev - exp

if profit > 0:
    print("Работаем с прибылью")
    rent = profit / rev
    qrent = str(rent * 100)
    print(f"Рентабельность: {qrent:.2} %")
elif profit == 0:
    print("Сработали в 0, без прибыли")
else:
    print("Работаем в убыток")
