width=float(input("Ширина поверхности:"))
high=float(input("Высота поверхности:"))
exp=float(input("Расход краски:"))
volume=int(input("Объем банки:"))
percent=int(input("Процент запаса:"))
S = width*high
liters = S/exp + S/exp/100*percent
cans = liters//volume + 1
remain = volume*cans-liters
print("Площадь окрашивания:", round(S, 2))
print("Количество литров:", round(liters, 2))
print("Количество банок:", cans)
print("Неиспользуемые литры:", round(remain, 2))