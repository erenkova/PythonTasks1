summa=int(input("Сумма к оплате:"))
hour=int(input("Текущий час:"))
if 10<=hour<=12:
    print(summa/2)
elif 20<=hour<=22:
    print(summa/4)
elif 8<hour<10 or 12<hour<20:
    print(summa)
else:
    print("Не часы работы")