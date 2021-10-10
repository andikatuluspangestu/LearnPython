# Python Dasar - Perulangan for

### Struktur Sintaks

```py

for nilai in sequence:
  # blok kode for

```

Jadi, ada 3 bagian penting.  

- ``sequence``: adalah sebuah nilai yang bersifat iterable alias bisa diulang-ulang.  
- ``nilai``: adalah setiap item yang diekstrak dari sequence  
- **Blok kode**: yaitu statemen-statemen atau perintah-perintah tertentu yang akan dieksekusi secara berulang.

--------------------------------------------------------------------------------------

**Contoh Pertama :**  

```py

for indek in range(banyak_perulangan):
    # jalankan kode ini
    # jalankan juga kode ini
#kode ini tidak akan diulang karena berada di luar for

```

```py3

ulang = 10

for i in range(ulang):
    print(f"Perulangan ke-{i}")

```

Pertama kita menentukan banyak perulangannya sebanyak 10x.  

```py
ulang = 10
```

Variabel ``i`` berfungsi **untuk menampung indeks**, dan fungsi ``range()`` berfungsi **untuk membuat list dengan range dari 0-10**. Fungsi ``str()`` berfungsi **merubah tipe data ineger ke string**.

Output :  

```
Perulangan ke-0
Perulangan ke-1
Perulangan ke-2
Perulangan ke-3
Perulangan ke-4
Perulangan ke-5
Perulangan ke-6
Perulangan ke-7
Perulangan ke-8
Perulangan ke-9
```

--------------------------------------------------------------------------------------

**Contoh kedua :**

Kita akan membuat program untuk menampilkan buah yang berada di dalam kerajang.  

```py
keranjang = ['jeruk','apel','anggur','pisang']

for buah in keranjang:
    print(buah)
```

Output :  
```
jeruk
apel
anggur
pisang
```

--------------------------------------------------------------------------------------

### For dengan fungsi range()  

Selain dengan list, kita juga bisa menggunakan for dengan fungsi range().  

```py

## 0 sampai 4
for i in range(5):
  print("Perulangan ke -", i)

```

Output :
```py
Perulangan ke - 0
Perulangan ke - 1
Perulangan ke - 2
Perulangan ke - 3
Perulangan ke - 4
```

> Dengan fungsi range, kita bisa melakukan perulangan dari 0, sampai kurang dari nilai 
  range yang kita definisikan (yaitu 5 dalam contoh di atas).  
  Sehingga hasil perulangan yang didapatkan adalah 0 sampai 4.

**Kita juga bisa mendefinisikan kelipatannya:**  

```py

## Bilangan genap kelipatan 2
for i in range(2, 12, 2):
  print('i =', i)

```

Output :  

```
i = 2
i = 4
i = 6
i = 8
i = 10
```

> Pada contoh di atas, sistem akan melakukan perulangan dimulai dari angka 2,  
  hingga kurang dari 12 dengan interval/kelipatan sebanyak 2.


## Break dan continue

Pada python, kita bisa menginterupsi dan juga men-skip suatu iterasi pada perulangan.

Terdapat 2 perintah yang bisa kita gunakan, yaitu:

- ``break`` untuk interupsi (memberhentikan paksa) sebuah perulangan
- ``continue`` untuk menskip ke iterasi selanjutnya

```py

for i in range(10, 20):
  # skip jika i == 15
  if (i == 15):
    continue
  
  print(i)

```

```
Output:

10
11
12
13
14
16  <-- Habis 14 langsung 16
17
18
19
```

Perhatikan output di atas, pada saat i == 15, perintah print(i) tidak dieksekusi dan justru di-skip ke iterasi berikutnya.

Atau…

Kita justru bisa memberhentikan paksa suatu perulangan sekalipun belum sampai ke iterasi yang terakhir.

```py

for i in range(10, 20):
  # hentikan jika i == 15
  if (i == 15):
    break
  
  print(i)

```

Output :

```
10
11
12
13
14 <-- print terakhir sebelum terjadi break pada i == 15
```

Sistem akan memberhentikan perulangan ketika i == 15 dan belum sempat melakukan perintah ``print()``

