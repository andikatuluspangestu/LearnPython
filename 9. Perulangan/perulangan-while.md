## Perulangan While

Perulangan menggunakan while akan menjalankan blok pernyataan terus menerus selama
kondisi bernilai benar.

## Struktur Sintaks

```py

while <kondisi>:
  # blok kode yang akan diulang-ulang

```

Terdapat 3 bagian utama:  

- keyword ``while``, ini harus kita isi.  
- ``<kondisi>:`` ini bisa berupa variabel boolean atau ekspresi logika.  
- **blok** (atau kumpulan baris) kode yang akan diulang-ulang kondisi terpenuhi.

## Perulangan Tanpa Batas ( Infinity Loop )  

Perulangan while sangat berkaitan dengan variabel boolean, atau logical statement. Karena penentuan kapan suatu blok kode akan diulang-ulang ditinjau dari True or False dari suatu pernyataan logika.

Sehingga jika suatu kondisi itu selalu benar, maka perulangannya pun akan selalu di eksekusi.  

```py

while (1 + 2 == 3):
  print('Hello World!')

```

Output :

```

Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!

```

Jika kode tadi dieksekusi, sistem akan mencetak tulisan “Hello World!” berkali-kali tanpa henti.

> Kita bisa memaksanya berhenti dengan menekan tombol Ctr + C jika menggunakan CLI, atau dengan cara menekan tombol stop jika menggunakan IDE atau sejenisnya.

**Kenapa perulangan di atas dieksekusi terus menerus?**

Karena kita memerintahkan komputer untuk menulis “Hello World” selama satu ditambah dua sama dengan tiga.  

Pertanyaannya: apakah satu ditambah dua sama dengan tiga terus-menerus atau tidak?
Jawabannya iya! Oleh karena itu sistem melakukan iterasi tak terbatas.

--------------------------------------------------------------------------------------

**Contoh Pertama :**  

```py

jawab = 'ya'
hitung = 0

while(True):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    if jawab == 'tidak':
        break

print(f"Total perulagan: {hitung}")

```

Pertama menentukan variabel untuk menghitung, dan menentukan kapan perulangan berhenti. kalau pengguna menjawab tidak maka perulangan akan terhenti.

```py

jawab = 'ya'
hitung = 0

```

Melakukan perulangan dengan while, kemudian menambah satu variabel hitung setiap kali mengulang. lalu menanyakan kepada pengguna, apakah mau berhenti mengulang atau tidak?

```py

while(jawab == 'ya'):
  hitung += 1
  jawab = input("Ulang lagi tidak? ")

```

Setelah selesai mengulang, cetak berapa kali perulangan tersebut terjadi.

```py
print(f"Total perulagan: {hitung}")
```

Output :  

```
Ulang lagi tidak? ya
Ulang lagi tidak? ya
Ulang lagi tidak? ya
Ulang lagi tidak? ya
Ulang lagi tidak? ya
Ulang lagi tidak? ya
Ulang lagi tidak? tidak
Total perulagan: 7
```

--------------------------------------------------------------------------------------

## Perulangan while untuk list  

Untuk menampilkan semua item pada list, cara yang paling clean adalah dengan menggunakan metode for seperti yang telah kita bahas sebelumnya.

Meskipun begitu, kita tetap bisa menggunakan perulangan while untuk bermain-main dengan list.

```py

listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

# bermain index
i = 0
while i < len(listKota):
  print(listKota[i])
  i += 1

```

Output :

```
Jakarta
Surabaya
Depok
Bekasi
Solo
Jogjakarta
Semarang
Makassar
```

--------------------------------------------------------------------------------------

## Perulangan while dengan inputan  

Kita juga bisa menggunakan while dengan inputan.

Perhatikan contoh di bawah. Pada contoh ini kita akan meminta user untuk memasukkan angka ganjil lebih dari 50. Jika user justru memasukkan nilai genap atau nilai yang kurang dari 50, maka sistem akan meminta user untuk menginputkan kembali.

```py

a = int(input('Masukkan bilangan ganjil lebih dari 50: '))

while a % 2 != 1 or a <= 50:
  a = int(input('Salah, masukkan lagi: '))

print('Benar')

```

Output :  

```
Masukkan bilangan ganjil lebih dari 50: 1
Salah, masukkan lagi: 2
Salah, masukkan lagi: 3
Salah, masukkan lagi: 10
Salah, masukkan lagi: 50
Salah, masukkan lagi: 52
Salah, masukkan lagi: 54
Salah, masukkan lagi: 55
Benar
```

------------------------------------------------------------------------------------

## Perulangan while dengan continue  

Sama dengan perulangan for, kita juga bisa menggunakan perintah ``continue`` pada perulangan while.

Apa itu perintah ``continue``?

Perintah ``continue`` berfungsi untuk men-skip iterasi sekarang ke iterasi selanjutnya.

```py3

listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

# skip jika i adalah bilangan genap
# dan i lebih dari 0
i = -1
while i < len(listKota):
  i += 1
  if i % 2 == 0 and i > 0:
    print('skip')
    continue

  # tidak dieksekusi ketika continue dipanggil
  print(listKota[i])

```

Output :  

```

Jakarta
Surabaya
skip         <-- i sama dengan 2
Bekasi
skip         <-- i sama dengan 4
Jogjakarta  
skip         <-- i sama dengan 6
Makassar
skip         <-- i sama dengan 8

```

> Pada output di atas, ketika i-nya adalah bilangan genap yang lebih dari satu, perintah print(listKota[i]) tidak dieksekusi dan justru di-skip.

----------------------------------------------------------------------------------

## Perulangan while dengan break  

Kita juga bisa menggunakan perintah ``break`` pada perulangan while.

Perintah ``break`` itu sebenarnya mirip dengan perintah continue.

Bedanya:

Ketika perintah ``break`` dipanggil, maka perulangan akan dihentikan secara paksa.

```py

listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

kotaYangDicari = input('Masukkan nama kota yang dicari: ')

i = 0
while i < len(listKota):
  if listKota[i].lower() == kotaYangDicari.lower():
    print('Ketemu di index', i)
    break

  print('Bukan', listKota[i])
  i += 1

```

Output :

```
Masukkan nama kota yang dicari: bekasi
Bukan Jakarta
Bukan Surabaya
Bukan Depok
Ketemu di index 3
```

----------------------------------------------------------------------------------

## Kapan harus menggunakan for, dan kapan harus menggunakan while?  

Sebenarnya tidak ada acuan yang sangat baku, karena banyak sekali kasus-kasus yang bisa diselesaikan dengan menggunakan keduanya.  

Tapi, kalau memang ingin sebuah jawaban:  

- Kalian bisa menggunakan for untuk kasus-kasus yang berkaitan dengan data sequence pada python, atau untuk kasus yang sudah jelas jumlah perulangannya berapa.  
- Dan kalian bisa menggunakan while jika memang perulangannya tidak jelas akan dilakukan berapa banyak

