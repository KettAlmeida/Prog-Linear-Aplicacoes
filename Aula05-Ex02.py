#KETTNEY ALMEIDA DOS SANTOS - ADM - MANHÃ - AULA05-EX02
print("Matriz Inversa (a)A ")
a00 = 1
a01 = 2
a10 = 4
a11 = -1


print(a00, a01, )
print(a10, a11, )

print('-=' * 5)
total = a00 * a11 - a10 * a01

if total != 0:
    print("", a11 / total), ('', -a10 / total)
    print("", -a01 / total), ('', a00 / total)

else:
    print("Não existe Matriz Inversa")
