sumSell = float(input("Введите сумму продажи:"))
discount = 0

if sumSell > 0 and sumSell <= 5000:
    discount = (sumSell / 100) * 5
elif sumSell > 5000 and sumSell <= 15000:
    discount = (sumSell / 100) * 12
elif sumSell > 15000 and sumSell <= 25000:
    discount = (sumSell / 100) * 20
else:
    discount = (sumSell / 100) * 30

finalSum = sumSell - discount
print("Скидка:", discount)
print("Сумма с учетом скидки :", finalSum)
