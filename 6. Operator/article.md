# Python Dasar - Operator

Operator di dalam Python adalah simbol khusus yang berfungsi untuk menjalankan suatu operasi tertentu, baik operasi aritmatika maupun operasi logika. Sedangkan nilai yang dioperasikan oleh operator dinamakan sebagai operan.

Berikut ini salah satu contoh paling sederhana dari operator aritmatika pada Python:

```py3
10 + 15
```

Output :

```
25
```

Pada kode program di atas, tanda ``+`` adalah sebuah operator. Sedangkan ``angka 10 dan 15`` keduanya merupakan operan.

Dari operasi tersebut, didapatkanlah sebuah hasil akhir berupa nilai integer yaitu 25.

## Jenis-jenis operator pada python

Ada enam jenis operator dalam pemrograman yang wajib diketahui:

- Operator Aritmatika
- Operator Pembanding/Relasi
- Operator Penugasan
- Opeartor Logika
- Operator Bitwise
- Operator Ternary

### A. Operator Aritmatika  
Operator matematika adalah operator yang kita gunakan untuk menghitung operasi matematika.

|   Operator  | Simbol |
|:-----------:|:------:|
| Penjumlahan |    +   |
| Pengurangan |    -   |
|  Perkalian  |    *   |
|  Pembagian  |    /   |
|  Sisa Bagi  |    %   |
| Pemangkatan |   **   |

Contoh :

```py3

# Ambil input untuk mengisi nilai
a = 20
b = 5

# Menggunakan operator penjumlahan
c = a + b
print ("Hasil dari", a, "+", b, "=", c)

# Operator Pengurangan
c = a - b
print ("Hasil dari", a, "-", b, "=", c)

# Operator Perkalian
c = a * b
print ("Hasil dari", a, "*", b, "=", c)

# Operator Pembagian
c = a / b
print ("Hasil dari", a, "/", b, "=", c)

# Operator Sisa Bagi
c = a % b
print ("Hasil dari", a, "%", b, "=", c)

# Operator Pangkat
c = a ** b
print ("Hasil dari", a, "pangkat", b, "=", c)

```

### B. Operator Penugasan
OPerator penugasan adalah operator yang berfungsi untuk memberikan nilai ke dalam sebuah variabel.

|   Operator  | Simbol |
|:-----------:|:------:|
|  Pengisian  |    =   |
| Penjumlahan |   +=   |
| Pengurangan |   -=   |
|  Perkalian  |   *=   |
|  Pembagian  |   /=   |
|  Sisa Bagi  |   %=   |
| Pemangkatan |   **=  |

Contoh :

```py3

# Ambil input dan cetak nilai awal
x = 5
print("Nilai x adalah", x)

# Coba kita jumlahkan nilai pada variable x dengan operator penugasan penjumlahan.
x += 5

# Setelah nilai pada variable x ditambah 5.
print("Nilai setelah ditambah 5 adalah", x)

# Kita coba penugasan yang lain
x -= 2
print("Nilai setelah dikurangi 2 adalah", x)

x *= 4
print("Nilai setelah dikali 4 adalah", x)

x %= 7
print("Sisa bagi 7, pada nilai x adalah", x)

x **= 2
print("Nilai x setelah dipangkatkan 2 adalah", x)

```

### C. Operator Perbandingan  
Operator perbandingan adalah operator yang bertugas untuk membandingkan antar dua operan. Apakah operan 1 lebih besar dari pada operan 2, atau apakah keduanya sama? Dan lain sebagainya.  

| Simbol |             Nama             |  Contoh  | Hasil |
|:------:|:----------------------------:|:--------:|:-----:|
| >      | Lebih dari                   | 5 > 5    | False |
| <      | Kurang dari                  | 2 < 4    | True  |
| ==     | Sama dengan                  | 10 == 10 | True  |
| !=     | Tidak sama dengan            | 5 != 5   | False |
| >=     | Lebih dari atau sama dengan  | 10 >= 10 | True  |
| <=     | Kurang dari atau sama dengan | 9 <= 10  | True  |

Contoh :

```py3

# Deklarasi Variable

a = 10
b = 12

# Apakah a lebih dari b
print(a > b)

# Apakah a kurang dari b
print(a < b)

# Apakah a sama dengan b
print(a == b)

# Apakah a tidak sama dengan b
print(a != b)

# Apakah a lebih dari sama dengan b
print(a >= b)

# Apakah a kurang dari sama dengan b
print(a <= b)

```

Output : 

```
False
True
False
True
False
True
```

### D. Operator logika  
Operator logika adalah operator yang sangat penting. Operator ini sangat berkaitan erat dengan operator perbandingan. Dan kedua-duanya juga mengembalikan nilai dengan tipe data yang sama yaitu boolean.

| Simbol |                            Tugas                            |     Contoh     |
|:------:|:-----------------------------------------------------------:|:--------------:|
| and    | Mengembalikan True jika dua statement sama-sama benar       | True and True  |
| or     | Mengembalikan True jika salah satu statement bernilai benar | 2 > 5 or 1 < 3 |
| not    | Menegasikan hasil. True menjadi False dan sebaliknya        | not(1 > 5)     |

Contoh :

```py3

a = 5
b = 2

print(True and True)
print(5 + 2 == 7 and True)
print('----')
print(False or b > a)
print(False or a > b)
print('----')
print(not(b > a))
print(not(b < a))

```

Output :

```
True
True
----
False
True
----
True
False
```

### E. Operator Bitwise  
Operator bitwise adalah operator yang berhubungan dengan angka-angka biner.  
Angka-angka biner adalah angka 0 dan 1. Dan pada hakikatnya hanya ini lah angka yang dipahami oleh mesin.

|       Nama       | Simbol |
|:----------------:|:------:|
|        AND       |    &   |
|        OR        |    |   |
|        XOR       |    ^   |
| Negasi/kebalikan |    ~   |
|    Left Shift    |    «   |
|    Right Shift   |    »   |

Contoh :

```py3

a = 5
b = 2

# Operasi AND
c = a & b
print(c)

# Operasi OR
c = a | b
print(c)

# Operasi XOR
c = a ^ b
print(c)

# Operasi Not
c = ~a
print(c)

# Operasi shift left (tukar posisi biner)
c = a << b
print(c)

# Operasi shift right (tukar posisi biner)
c = a >> b 
print(c)

```

Output :

```
0
7
7
-6
20
1
```

### F. Operator identitas
Operator ini didefinisikan dengan is dan is not.  
Tugasnya adalah untuk mengetahui apakah dua buah variabel memiliki nilai yang sama dan posisi yang sama di dalam memori. Karena tidak semua nilai yang sama memiliki tempat / posisi yang sama di dalam memori.

| Simbol | Tugas |
|:---:|:---:|
| is | Bernilai true jika dua variabel bersifat identik baik dari segi nilai mau pun penempatan lokasi di memory |
| is not | Bernilai false jika dua variabel tidak identik baik dari segi nilai mau pun penempatan lokasi di memory |

Contoh :

```py3
x = ["apel", "jeruk"]
y = ["apel", "jeruk"]
z = x

# mengembalikan False karena x bukan objek yang sama dengan y, meskipun memiliki konten yang sama
print(x is y)

# untuk menunjukkan perbedaan antara "adalah" dan "==": perbandingan ini mengembalikan True karena x sama dengan y
print(x == y)

# mengembalikan False karena z adalah objek yang sama dengan x
print(x is not z)

# mengembalikan True karena x bukan objek yang sama dengan y, meskipun keduanya memiliki konten yang sama
print(x is not y)

# Untuk menunjukkan perbedaan antara "bukan" dan "!=": perbandingan ini mengembalikan False karena x sama dengan y
print(x != y)

```

Output :

```
False
True
False
True
False
```

### G. Operator keanggotaan  
Operator keanggotaan adalah operator yang digunakan untuk memeriksa
apakah suatu nilai atau variabel merupakan anggota atau ditemukan di dalam suatu
data (string, list, tuple, set, dan dictionary)

| Simbol |                            Tugas                            |
|:------:|:-----------------------------------------------------------:|
| in     | Bernilai true jika suatu nilai ada di dalam sequence        |
| not in | Bernilai false jika suatu nilai tidak ada di dalam sequence |

Contoh :

```py3

x = ["apel", "jeruk"]

# mengembalikan True karena nilai "jeruk" ada dalam daftar
print("Apakah jeruk ada di dalam x ?", "jeruk" in x)

# mengembalikan True karena nilai "anggur" tidak ada dalam daftar
print("Apakah anggur ada di dalam x ?", "anggur" not in x)


```

Output :

```

Apakah jeruk ada di dalam x ? True
Apakah anggur ada di dalam x ? True

```

### H. Operator Ternary  
Operator ternary juga dikenal dengan operator kondisi, karena digunakan untuk membuat sebuah ekspresi kondisi seperti percabangan IF/ELSE.  

Operator ternary sebenarnya tidak ada dalam Python, tapi python punya cara lain untuk menggantikan operator ini.  

Pada bahasa pemrograman lain operator ternary menggunakan tanda tanya (?) dan titik dua (:).

```js
kondisi ? <nilai true> : <nilai false>
```

Dalam Python bentuknya berbeda, yaitu menggunakann IF/ELSE dalam satu baris.

```py3

<Nilai True> if Kondisi else <Nilai False>
```

Contoh :

```py3

nilai = 80
keputusan = "lulus" if nilai >= 80 else "tidak lulus"
print(keputusan)

```
