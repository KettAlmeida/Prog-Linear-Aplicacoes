#KETTNEY ALMEIDA DOS SANTOS - ADM - MANHÃ - AULA05-EX01
print("Matriz Inversa (a)A ")
a00 = 0
a01 = 1
a02 = 0
a10 = 1
a11 = 0
a12 = 0
a20 = 0
a21 = 0
a22 = 1

print(a00, a01, a02)
print(a10, a11, a12)
print(a20, a21, a22)
print('-=' * 5)
total = a00 * a11 * a22 + a10 * a21 * a02 + a20 * a01 * a12
total = total + (a02 * a11 * a20) * -1 + (a12 * a21 * a00) * -1 + (a22 * a01 * a10) * -1

if total != 0:
    print(" ", (a11 * a22 - a21 * a12) / total, ' ', ((a01 * a22 - a21 * a02) * -1) / total, ' ', (
                a01 * a12 - a11 * a02) / total)
    print(" ", ((a10 * a22 - a20 * a12) * -1) / total, ' ', ((a00 * a22 - a20 * a02)) / total, ' ', (
                (a00 * a12 - a10 * a02) * -1) / total)
    print(" ", ((a10 * a21 - a20 * a11)) / total, ' ', ((a00 * a21 - a20 * a01) * -1) / total, ' ', (
                a00 * a11 - a10 * a01) / total)

else:
    print("Não existe Matriz Inversa")

print('-=' * 5)
print('-=' * 5)
print("Matriz Inversa(b)A")
b00 = 1
b01 = 1
b02 = 1
b10 = 0
b11 = 2
b12 = 3
b20 = 5
b21 = 5
b22 = 1
print(b00, b01, b02)
print(b10, b11, b12)
print(b20, b21, b22)
print('-=' * 5)
total = b00 * b11 * b22 + b10 * b21 * b02 + b20 * b01 * b12
total = total + (b02 * b11 * b20) * -1 + (b12 * b21 * b00) * -1 + (b22 * b01 * b10) * -1

if total != 0:
    print(" ", (b11 * b22 - b21 * b12) / total, ' ', ((b01 * b22 - b21 * b02) * -1) / total, ' ', (
                b01 * b12 - b11 * b02) / total)
    print(" ", ((b10 * b22 - b20 * b12) * -1) / total, ' ', ((b00 * b22 - b20 * b02)) / total, ' ', (
                (b00 * b12 - b10 * b02) * -1) / total)
    print(" ", ((b10 * b21 - b20 * b11)) / total, ' ', ((b00 * b21 - b20 * b01) * -1) / total, ' ', (
                b00 * b11 - b10 * b01) / total)

else:
    print("Não existe Matriz Inversa")

print('-=' * 5)
print('-=' * 5)
print("Matriz Inversa(c)A")
c00 = 1
c01 = -2
c02 = -3
c10 = 0
c11 = -4
c12 = 4
c20 = 0
c21 = 0
c22 = 0
print(c00, c01, c02)
print(c10, c11, c12)
print(c20, c21, c22)
print('-=' * 5)
total = c00 * c11 * c22 + c10 * c21 * c02 + c20 * c01 * c12
total = total + (c02 * c11 * c20) * -1 + (c12 * c21 * c00) * -1 + (c22 * c01 * c10) * -1

if total != 0:
    print(" ", (c11 * c22 - c21 * c12) / total, ' ', ((c01 * c22 - c21 * c02) * -1) / total, ' ', (
                c01 * c12 - c11 * c02) / total)
    print(" ", ((c10 * c22 - c20 * c12) * -1) / total, ' ', ((c00 * c22 - c20 * c02)) / total, ' ', (
                (c00 * c12 - c10 * c02) * -1) / total)
    print(" ", ((c10 * c21 - c20 * c11)) / total, ' ', ((c00 * c21 - c20 * c01) * -1) / total, ' ', (
                c00 * c11 - c10 * c01) / total)

else:
    print("Não existe Matriz Inversa")