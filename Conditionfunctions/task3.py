a=int(input("Введите цену товара:"))
b=int(input("Введите цену товара:"))
c=int(input("Введите цену товара:"))
if a<b<c:
    print("Акция!")
    print("Сумма к оплате:", (a+b+c)/2)
elif a>b>c:
    print("Акция!")
    print("Сумма к оплате:", (a + b + c) / 3)
else:
    print("Сумма к оплате:", (a+b+c))