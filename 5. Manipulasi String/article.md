# Python Dasar - Manipulasi String Sederhana

### A. String
String adalah salah satu tipe data yang berfungsi untuk menyimpan kumpulan dari karakter. Karakter-karakter tersebut tersusun menjadi satu-kesatuan membentuk sebuah kata, kalimat, atau paragraf yang bahkan bisa terbentuk dari digit dan juga angka.

Pada python, String dibuat dengan kombinasi tanda petik tunggal ('') atau tanda petik dua ("")

Contoh :

```py

nama = "Andika"
negara = "Indonesia"

```

### B. Escape String

Beberapa karakter bisa memutus sebuah string pada Python. Seperti misalnya karakter tanda petik tunggal mau pun ganda.  
Karakter backslash (\) bisa kita gunakan untuk meng-escape karakter-karakter yang bisa memutus string dan membuat sintaks menjadi error.

Contoh. Kita akan menampilkan beberapa output seperti ini:

- `Dia berkata: "Ayolah!"`
- `Aku menimpali: "Apakah kamu ingin diriku 'angkat kaki'?!"`
- Atau menampilkan karakter `\(^_^ \) (/ -_-/)`

**Contoh pertama :**
Jika kita membuat string dengan tanda petik 2 (""), kita akan medapatkan error karena sintaks terputus.

Sintaks yang salah: ❌  

```py
print("Dia berkata: "Ayolah!"")
```

Output :  
```py
 print("Dia berkata: "Ayolah!"")
                         ^
SyntaxError: invalid syntax
```  

Nah, coba perhatikan. Dari sususan warnanya saja sudah kelihatan kalau sintaks di atas bermasalah. Jadi, solusi yang benar adalah kita akan menggunakan tanda petik tunggal **('')**

Solusi yang benar: ✅  
```py
print('Dia berkata: "Ayolah!"')
```

**Contoh Kedua :**

``Aku menimpali: "Apakah kamu ingin diriku 'angkat kaki'?!"``

Karena di dalam string tersebut, baik tanda petik tunggal maupun tanda petik ganda sama-sama ditampilkan?
**Solusinya adalah: escape string dengan backslash!**

```py
# menggunakan petik satu
print('Aku menimpali: "Apakah kamu ingin diriku \'angkat kaki\'?!"')

# menggunakan petik dua
print("Aku menimpali: \"Apakah kamu ingin diriku 'angkat kaki'?!\"")

```

Output :

```
Aku menimpali: "Apakah kamu ingin diriku 'angkat kaki'?!"
```

**Contoh Ketiga :**

``\(^_^ \) (/ -_-/)``

Kita bisa menggunakan double backslash (\\) untuk menampilkan satu backslash

```py
print('\\(^_^ \) (/ -_-/)')
```
Output :

```
\(^_^ \) (/ -_-/)
```

### C. Penggabungan String
Penggabungan string adalah teknik untuk menyusun atau mengkombinasikan beberapa string menjadi satu kesatuan. Hal ini juga biasa disebut sebagai string concatenation.

**- Menggunakan operator** ``+``  

```py

aku = "Andika"
kamu = "Adistia"
kita = aku + " & " + kamu

print(kita)

```

Output :  
```
Andika & Adistia
```

**- String + Non String**  

Anda hanya bisa menambahkan string dengan string juga. Jika anda berusaha menambahkan string dengan integer, double, atau boolean dan sebagainya, maka anda akan mendapatkan error.

```py

bulan    = "Oktober"
tahun    = 2021
lulus    = bulan + tahun

print(lulus)

```

Output :  

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
> Solusinya adalah kita harus mengkonversi data integer menjadi string menggunakan fungsi ``str():``

```py

bulan    = "Oktober"
tahun    = 2021
lulus    = bulan + " " + str(tahun)

print(lulus)

```

Output :  

```
Oktober 2021
```

**- Perkalian String**  

Selain melakukan string concatenation menggunakan operator tambah (+), kita juga bisa menggunakan operator kali ('*').  
Operator perkalian ini akan mengulang-ulang string yang dikalikan.

```py

print('==========') # output: ==========
print('=' * 10)     # output: ==========

```

### D. Memformat String dengan String Interpolation  

Fungsi ini memiliki tujua memasukkan atau menyisipkan variabel atau nilai ke dalam template string yang telah ditentukan. Hanya saja, ia memiliki sintaks yang jauh lebih modern dan lebih sederhana.

Hal ini akan terlihat sangat familiar bagi kalian yang pernah belajar javascript mau pun kotlin, karena secara sintaks penulisannya hampir sama dengan string template literal pada dua bahasa tersebut.

Contoh :

```py

nama = 'Nafatul'
asal = 'Indonesia'

print(f'Perkenalkan saya {nama} dari {asal}')

```

### E. Memecah String Menjadi List

```py

alamat = 'Surabaya, Jawa Timur, Indonesia'

print(alamat.split())
print(alamat.split(','))
print(alamat.split(', '))
print('❤️'.join(['aku', 'suka', 'adistia']))
print('🦖'.join(alamat.split(', ')))

```

Output :

```
['Tegal,', 'Jawa', 'Tengah,', 'Indonesia']
['Tegal', ' Jawa Tengah', ' Indonesia']
['Tegal', 'Jawa Tengah', 'Indonesia']
aku❤️suka❤️adistia
Tegal🦖Jawa Tengah🦖Indonesia
```

> - Fungsi *string.split()* menerima satu parameter optional. Parameter ini akan dijadikan 
  sebagai pembatas atau separator yang kemudian string akan dibagi menjadi list berdasarkan pembatas tersebut.
> - Jika fungsi *string.split()* tidak diberi parameter, maka defaultnya adalah spasi ( ).
> - Fungsi *string.join()* berfungsi untuk menggabungkan item list menjadi string utuh,  dengan string awal sebagai glue atau perekat antar masing-masing item

### F. Mengubah String Menjadi Upper Case  
Memodifikasi string menjadi uppercase alias huruf besar semua.

```py
print('halo selamat sore!'.upper())
print('Halo Selamat Malam!'.upper())
```

Output :  
```
HALO SELAMAT SORE!
HALO SELAMAT MALAM!
```

### G. Mengubah String Menjadi Lower Case  
Memodifikasi string menjadi uppercase alias huruf kecil semua.

```py

print('HALO SELAMAT MALAM!'.lower())
print('Halo Selamat Pagi!'.lower())

```

Output :  
```
halo selamat malam!
halo selamat pagi!
```
### G. Mengubah String Menjadi Title Case  
Memodifikasi string menjadi seperti teks judul.

```py

print('si kancil yang pintar'.title())
print('CORETAN SENJA'.title())

```
Output :

```
Si Kancil Yang Pintar
Coretan Senja
```

### H. Mencari Kata Pada String  
Pada python, mencari sebuah kata atau karakter dalam suatu string caranya sangat mudah. Kita bisa menggunakan fungsi string.find().

Fungsi tersebut akan mengembalikan indeks dari hasil pertama pencarian, dan akan mengembalikan -1 jika karakter yang dicari tidak ditemukan.

```py

nama = "ANDIKA"

print('Huruf D di index ke :', nama.find('D'))
print('Huruf K di index ke :', nama.find('K'))

```

Output :

```py
Huruf D di index ke : 2
Huruf K di index ke : 4
```

### I. Mereplace Kata Pada String

Dengan memanfaatkan fungsi **string.replace()**, kita bisa mencari lalu menimpa sebuah karakter/teks dengan teks baru.

```py

nama = 'Dika'
print(nama.replace('D', 'M'))

```

Output :  

```
Mika
```

### J. Menghapus Karakter Tertentu Pada String

Tentu saja, jika kita memanggil fungsi replace() pada suatu string, lalu kita timpa teks lama dengan string kosong (''), seolah-olah kita telah menghapus karakter tersebut.

```py

nama = 'Dika'
print(nama.replace('k', ''))

```

Output :  

```
Dik
```

### K. Memformat String dengan Format Specifiers  

Format specifiers adalah simbol ``%s`` yang berarti string.  

Contoh :  
```py

template = 'Halo, saya %s dari %s'

print(template % ('Nafatul', 'Indonesia'))
# output: Halo, saya Nafatul dari Indonesia

```

Model cara seperti ini akan terlihat sangat “old-style” jika kita bandingkan dengan fungsi ``string.format()`` pada python 3.

