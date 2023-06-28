number=int(input("Введите число для проверки:"))
last=number%10
summa=0
while number>0:
    summa += number%10
    number//=10
if summa%3==0 and last%2==0:
    print("Число кратно 6")
else:
    print("Число не кратно 6")