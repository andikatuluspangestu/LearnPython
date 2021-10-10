# Python Dasar - Tipe Data

Tipe data adalah jenis dari suatu data. Setiap data memiliki nilai, dan setiap nilai memiliki jenis. Ada data-data yang bertipe angka, ada pula yang bertipe huruf/karakter, ada juga yang bertipe benar/salah dan sebagainya.

Sebagai ibarat, kalau variabel adalah keranjang, maka tipe data adalah jenis barang atau jenis benda yang akan kita masukkan ke dalam keranjang tersebut.

![Source : Jagongoding](https://ik.imagekit.io/jagongoding/storage/2020/09/python-dasar-variabel-dan-tipe-data/pasar-buah.webp)

Kita bisa lihat bahwa di dalam gambar di atas, terdapat banyak kotak dan banyak buah. Setiap kotak tertentu digunakan untuk menyimpan jenis buah tertentu.

Sehingga bisa kita tarik kesimpulan bahwa:  
- Kotak keranjang merepresentasikan variabel.
- Buah merepresentasikan data.
- Dan jenis-jenis buah tersebut merepresentasikan tipe data.

--------------------------------------------

### Memeriksa Tipe Data Pada Python

Untuk memerikas tipe sebuah data, kita bisa menggunakan function ```type()``` bawaan Python.

Contoh Cek Tipe Data :  

```py
nama = "Andika"
umur = 17

print(type(nama))
print(type(umur))
```

Output :  

```
<class 'str'>
<class 'int'>
```

--------------------------------------------

### Jenis-Jenis Tipe Data pada Python
Jika kita lihat kembali kode di atas, maka kita akan mendapati bahwa data dari masing-masing 2 variabel memiliki tipe data yang berbeda-beda.  

```py
nama = "Andika"
umur = 17
```

> Variable *nama* memiliki tipe data **String** atau Teks
  Variable *usia* memiliki tipe data **Integer** atau Numerik


Terdapat 8 Tipe Data pada Bahasa Pemrograman Python, yaitu sebagai berikut.

| Jenis Tipe Data     | Sintaks atau Simbol           |
|---------------------|-------------------------------|
| Tipe Data Teks      | String (str)                  |
| Tipe Data Numerik   | Integer (int), Float, Complex |
| Tipe Data Urutan    | List, Tuple, Range            |
| Tipe Data Pemetaan  | Dictionary (dict)             |
| Tipe Data Set       | Set, Frozenset                |
| Tipe Data Boolean   | bool                          |
| Tipe Data Biner     | bytes, bytearray, memoryview  |

#### A. Tipe Data String ( str )  
Tipe data yang digunakan untuk menyimpan sebuah teks.  
Data yang bertipe string harus diapit oleh tanda petik, baik tanda petik satu *('')* mau pun tanda petik dua *("")*.

```py
namaSaya = "Andika"
namaDia  = "Nafatul"
print(type(namaSaya))
print(type(namaDia))

# Output
<class 'str'>
<class 'str'>
```

**Menggabungkan Dua atau lebih kata, menjadi satu kalimat.**

```py

namaSaya = "Andika"
namaDia  = "Nafatul"
tahunKetemu = "2016"

print("Saya bernama", namaSaya, "dan", namaDia, " selalu menjadi penyemangat saya. Kami bertemu pertama kali pada tahun", tahunKetemu)

```
Output  

```
Saya bernama Andika dan Nafatul selalu menjadi penyemangat saya. Kami bertemu pertama kali pada tahun 2016.
```

**Catatan :**  
> Coba perhatikan variabel *tahunKetemu*, meskipun isinya adalah sebuah angka,  
  tetap saja di situ dia bertipe data string.
  Kenapa? karena ia diapit oleh tanda petik.



#### B. Tipe Data Integer ( int )
Tipe data integer adalah tipe data bilangan bulat. Sehingga setiap variabel yang memiliki nilai bilangan bulat, maka ia akan dikategorikan sebagai integer.

```py
umur = 20
print(type(umur))

# Output
<class 'int'>
```


#### C. Tipe Data Pecahan ( float )
Tipe data float dipergunakan untuk variabel-variabel yang memiliki nilai pecahan / desimal.

```py
nilai_tugas = 89.5
print(type(nilai_tugas))

# Output
<class 'float'>
```


#### D. Tipe Data Complex ( complex )
Tipe data complex adalah tipe data yang sangat kompleks. Tipe Data ini merepresentasikan nilai imajiner suatu bilangan.

```py
kodeTiket = 10j
print(type(kodeTiket))

# Output
<class 'complex'>
```

#### E. Tipe Data Boolean ( True / False)

Tipe data boolean adalah tipe data yang paling simpel dan mudah. Akan tetapi dia sangat penting sekali bahkan untuk membangun program/aplikasi skala besar sekalipun.
*Nilai True* untuk pernyataan bernilai benar, dan *Nilai False* untuk merepresentasikan pernyataan yang bernilai salah.

Contoh :

```py

saya_mahasiswa = True
saya_dokter = False

print("Apakah saya adalah mahasiswa?", saya_mahasiswa )
print("Apakah saya adalah dokter?", saya_dokter )

# Cek Tipe Data
print(type(saya_mahasiswa))
print(type(saya_dokter))

```

Output :

```
Apakah saya adalah mahasiswa? True
Apakah saya adalah dokter? False

<class 'bool'>
<class 'bool'>
```


### Lalu, apa perbedaan antara tipe data angka dan tipe data teks (string)?

> Perbedaannya terletak pada fungsi dan cara mengoperasikannya.
  Misalkan kita ingin menambahkan dua buah variabel bertipe data numerik, yang kita dapatkan adalah hasil penjumlahannya.  
  Berbeda jika kita menambahkan dua buah variabel bertipe data string (teks), yang kita dapatkan adalah hasil penggabungan keduanya.

Contoh :

```py

# penjumlahan dua data numerik
print(8 + 8) # output 16

# penjumlahan dua data string
print('8' + '8') # output 88

```
Oleh karena itu: pemilihan tipe data yang tepat sangatlah penting agar tidak terjadi pada kesalahan operasi.  

#### G. Tipe Data List

List adalah struktur data pada python yang mampu menyimpan lebih dari satu data, seperti array. dan tipe data ini merupakan tipe data koleksi yang bersifat ordered (terurut) dan juga bersifat changable (bisa diubah).  
Tipe data ini bisa kita definisikan dengan tanda kurung siku [] di dalam Python.  

- List dapat kita buat seperti membuat variabel biasa, namun nilai variabelnya diisi dengan tanda kurung siku ([]).  

Contoh :  

```py

# Membuat List kosong
warna = []

# Membuat list dengan isi 1 item
hobi = ["membaca"]

# Membuat list dengan isi lebih satu item
buah = ["jeruk", "apel", "mangga", "duren"]

# Membuat list dengan isi tipe data campuran
laci = ["buku", 21, True, 34.12]

```

**Jenis data apa saja yang boleh diisi ke dalam List?**  

list dapat diisi dengan tipe data apa saja, string, integer, float, double, boolean, object, dan sebagainya.
Kita juga bisa mencampur isinya.

**Menampilkan List**

Kita bisa menggunakan perintah print() untuk melihat isi dari sebuah list, baik secara menyeluruh maupun sebagian dan kita bisa menampilkan isi tertentu dari list dengan menggunakan indeks.  
Setiap data pada list memiliki indeks sebagai alamat. Dan indeks adalah sebuah nilai integer dimulai dari 0 yang menjadi acuan di mana sebuah data disimpan di dalam list.  

![](https://www.petanikode.com/img/python/list/contoh-list.svg)

Nomer indeks list selalu dimulai dari nol (0).  
Nomer indeks ini yang kita butuhkan untuk mengambil isi (item) dari list.  

Contoh :  

```py

# Kita punya list nama-nama buah
buah = ["apel", "anggur", "mangga", "jeruk"]

# Misanya kita ingin mengambil mangga
# Maka indeknya adalah 2
print buah[2]

```

Output :  
```
"mangga"
```

**Mengubah data di dalam list**

Caranya mudah, seperti mengubah nilai variabel pada umumnya.  
Perhatikan contoh berikut:  

```py

list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']

print(list_buah)

# ubah data pertama
list_buah[0] = 'Jeruk'

print(list_buah)

# ubah data terakhir
list_buah[-1] = 'Mangga'

print(list_buah)

```

Output :  

```
['Pisang', 'Nanas', 'Melon', 'Durian']
['Jeruk', 'Nanas', 'Melon', 'Durian']
['Jeruk', 'Nanas', 'Melon', 'Mangga']
```

**Mengubah data list dalam range**

kita juga bisa mengubah data dalam range tertentu secara sekaligus. Caranya tidak jauh berbeda dengan apa yang telah kita pelajari pada poin slicing data list.  

Contoh :  

```py

# ubah data dalam range
list_buah[1:3] = ['Naga', 'Pepaya']

print(list_buah)

```

Output :  

Maka kita akan mendapati bahwa nilai Nanas dan Melon akan berubah menjadi Naga dan Pepaya.

```
['Jeruk', 'Naga', 'Pepaya', 'Mangga']
```

**Menambah item ke dalam list**

- Menambah data di belakang

Kita bisa menggunakan fungsi ``append()``. Fungsi ini menerima satu parameter, yang mana parameter tersebut akan dimasukkan sebagai nilai baru pada list, dan nilai baru tersebut berada pada akhir item.

```py
list_buah = ['Jeruk', 'Naga', 'Pepaya', 'Mangga']
print(list_buah)

# tambah data di belakang list
list_buah.append('Sirsak')
print(list_buah)
```

- Menambah data di depan

Kita juga bisa menambahkan item ke dalam list dengan menggunakan fungsi ``insert()``.  
Fungsi insert ini menerima dua buah parameter:

- Parameter pertama untuk mendefinisikan posisi indeks dari data yang akan dimasukkan.  
- Parameter kedua untuk mendefinisikan nilai yang akan dimasukkan ke dalam list

Berikut ini contoh untuk memasukkan nilai Jambu ke dalam list_buah pada indeks 0.  

```py

# tambah data di awal list
list_buah.insert(0, 'Jambu')
print(list_buah)

```

- Menambah data di mana pun

Tidak hanya terbatas indeks 0, kita juga bisa memasukkan nilai pada indeks berapa pun pada list.  

```py

# tambah data di index mana pun dalam list
list_buah.insert(2, 'Manggis')
print(list_buah)

```

**Menghapus item dari list**

Fungsi ``pop()`` akan mengambil item terakhir dari sebuah list, lalu menghapusnya. Karena ia juga “mengambil”, maka kita bisa menyimpan hasil kembalian dari fungsi ``pop()`` ke dalam sebuah variabel.  

Contoh :  

```py

list_angka = [1, 2, 3, 4, 5]
print(list_angka)

# hapus satu angka di belakang
angka_yang_terhapus = list_angka.pop()

print('angka yang terhapus:', angka_yang_terhapus)
print(list_angka)

```

Output :  

```
[1, 2, 3, 4, 5]
angka yang terhapus: 5
[1, 2, 3, 4]
```

**Menggabungkan dua buah list atau lebih**

Berikutnya hal umum yang biasa kita lakukan dengan list adalah: menggabungkan dua buah list (atau lebih) menjadi satu kesatuan.  

Bisa jadi kita memiliki 3 list berikut:  

```py
a = [1, 2, 3]
b = ['a']
c = [True, 'b', False]

listBaru = a + b + c

print(listBaru)
```

Output :  
```
[1, 2, 3, 'a', True, 'b', False]
```

Kita bisa dengan mudah menggabungkan ketiganya menggunakan operator +.  

**Mengurutkan data list**

kita bisa mengurutkan data list pada python dengan memanggil fungsi ``<list>.sort()``

Contoh :  
```py

list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
print(list_buah)

# urutkan secara ascending
list_buah.sort()
print(list_buah)

# membalikkan posisi item list (tidak harus berurut)
list_buah.reverse()
print(list_buah)

```

Output :  

```
['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
['Apel', 'Durian', 'Jeruk', 'Mangga', 'Zaitun']
['Zaitun', 'Mangga', 'Jeruk', 'Durian', 'Apel']
```

