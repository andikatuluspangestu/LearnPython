# Python Dasar - Sintaks Dasar

### Menjalankan Program Python  
Untuk menjalankan Python ada banyak cara yang bisa dilakukan. Anda bisa menggunakan shell, terminal atau menggunakan IDE (Integrated Development Environment). Di bawah ini adalah langkah-langkah menjalankan Python dengan cara yang paling mudah.

Seperti yang kita pelajari di halaman sebelumnya, sintaks Python dapat dieksekusi dengan menulis contoh kode berikut.

```python 
print("Hello, World!")
```

Dan membuat file python, menggunakan ekstensi file .py, dan menjalankannya di Command Line:

    C:>python hello.py


### Python Case Sensitivity  
Bahasa pemrograman python bersifat case sensitive. Ia akan membedakan antara huruf kecil dan huruf besar walaupun sebuah kata itu terlihat sama.
Sebagai contoh jika Anda menggunakan fungsi print dengan huruf kecil ```print()``` akan berhasil. Lain hal jika anda menggunakan huruf kapital ```Print() atau PRINT()``` , akan muncul pesan error.

Contoh:

```py
ibu_kota = 'Slawi'
print(iBu_kota)
```

Jika dijalankan, kita akan mendapatkan error:

```
Exception has occurred: NameError
name 'iBu_kota' is not defined
  File "case-sensitive.py", line 3, in <module>
    print(iBu_kota)
```

> Karena variabel yang kita definisikan adalah ibu_kota, dengan huruf kecil semuanya. Sedangkan variabel yang berusaha kita panggil adalah iBu_kota yang mana huruf B nya adalah huruf kapital, dan interpreter python menganggap keduanya berbeda

### Indentasi Python
Pada bahasa pemrograman lain, umumnya indentasi adalah sesuatu yang tidak penting. Bahkan cenderung diabaikan oleh mesin.
Indentasi hanya digunakan untuk mempermudah manusia dalam membaca kode program.

**Tapi tidak dengan python.**

Dalam python, indentasi adalah hal yang super-super penting, karena ia bertugas untuk mendefinisikan struktur blok kode program.
Sehingga, melakukan kesalahan indentasi juga bisa berujung pada sebuah error (yang mungkin akan sulit dipecahkan bagi yang belum terbiasa). Atau dalam istilah lain: kita menggunakan indentasi untuk mengelompokkan blok kode program di dalam python.

Indentasi adalah penulisan paragraf yang agak menjorok masuk ke dalam [3]. Biasanya jika kita membaca majalah atau koran, kita akan dapati indentasi pada kalimat awal setiap paragrafnya

Untuk memahami betapa pentingnya indentasi pada python, mari kita perhatikan contoh-contoh berikut tentang kesalahan indentasi yang umum terjadi pada bahasa pemrogrman python.

Perhatikan contoh berikut:

```py
print('Selamat')
  print('Pagi')
print('Dunia')
```

Kode program di atas, secara sekilas tidak ada masalah. Tapi, ketika kita eksekusi, ternyata interpreter python memberitahukan kita bahwa terdapat error yang disebabkan oleh indentasi yang tidak pada tempatnya:

``` 
IndentationError: unexpected indent
```

Yang benar harusnya tiga perintah print() berada pada satu indentasi, karena memang ketiganya berada dalam satu blok yang sama.

```py
print('Selamat')
print('Pagi')
print('Dunia')
```
--------------------------------

Contoh kode program yang benar ✅:

```py
a = 10

if a > 5:
  print('nilai a lebih dari 5')
```
Contoh yang salah ❌:

```py
a = 10

if a > 5:
print('nilai a lebih dari 5')
```

Pesan error:

```
IndentationError: expected an indented block
```

### Tanda Kutip dan Tanda Kutip Dua
Dalam bahasa pemrograman python, kita bisa mendefinisikan string dengan tanda kutip satu ' maupun tanda kutip dua ".

Contoh yang benar ✅:

```py
nama = 'Andika'
asal = "Slawi"
```

Contoh yang salah ❌:

```py
nama = 'Andika"
asal = "Slawi'
```

### Penulisan Komentar
Komentar adalah sebuah baris kode atau statemen yang diabaikan oleh interpreter python. Ia hanya ditulis dengan tujuan agar dibaca oleh manusia, bukan mesin.

Komentar juga sangat penting sebagai penjelasan alur dari kode program yang kita tulis. Jika tidak, kita sendiri (si penulis kode) bisa lupa dan kebingungan jika harus menjelaskan kode program lama yang pernah kita tulis pada masa lalu.

Penulisan komentar pada python terdiri dari 2 jenis:

- satu baris
- dan multi baris

Komentar satu baris ditulis dengan tanda #. 
Sedangkan komentar lebih dari satu baris ditulis dengan triple doublequote (tanda petik dua sebanyak 3x).

Contoh:

```py
# variabel a merepresentasikan panjang
a = 5
b = 10 # variabel b merepresentasikan tinggi
```

```python
"""
Dan variabel c merepresentasikan luas
persegi dari hasil perkalian
variabel a dan variabel b
"""
c = a * b
```


