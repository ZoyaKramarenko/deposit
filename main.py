money = int(input("Введите сумму вклада: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = list(per_cent.values())
i = 0
while i < len(deposit):
    deposit[i] = int(deposit[i] * money / 100)
    i += 1
print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit))
