m=int(input("Масса тела в килограммах:"))
h=int(input("Рост в сантиметрах:"))
i=m/((h/100)**2)
print(round(i,2))