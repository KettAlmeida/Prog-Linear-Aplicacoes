#KETTNEY ALMEIDA DOS SANTOS - ADM - MANHÃ - AULA05-EX03
print("Matriz Inversa (a)A ")
a00 = 3
a01 = 4
a10 = 2
a11 = 3

print(a00, a01, )
print(a10, a11, )

print('-=' * 5)
total = a00 * a11 - a10 * a01

if total != 0:
    print("", a11 / total), ('', -a10 / total)
    print("", -a01 / total), ('', a00 / total)

else:
    print("Não existe Matriz Inversa")


