"""
Напишите генераторное выражения. Для генерации словаря где ключем выступают числа от 0 до 10. А значения эти же числа в 16чной системе счисления.
Работу с 16чной системой найдите в документации Python
"""
generator = {i:hex(i) for i in range(11)}
for i,j in generator.items():
    print(i,j)

generator = {i:hex(i) for i in range(11)}
print(generator)

generator = {i:hex(i) for i in range(11)}
print(*generator)