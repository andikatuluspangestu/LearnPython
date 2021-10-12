# Pattern Segitiga Sama Kaki - 12210940 Andika Tulus Pangestu

#-------------------------------------#

print('\n\n1. Jawaban Soal Pertama')
print("")

a = int(input("Masukan Angka : "))
print("")
s = a - 1
for i in range(0, a):
    for j in range(0, s):
        print(' ', end='')
    s -= 1
    for j in range(0, i + 1):
        print('A ', end='')

    print('')

#-------------------------------------#

print('\n\n2. Jawaban Soal kedua')
print("")

a = int(input("Masukan Angka : "))
print("")
s = a - 1
for i in range(0, a):
    for j in range(0, s):
        print(' ', end='')
    s -= 1
    for j in range(0, i + 1):
        print('$ ', end='')

    print('')

print("")