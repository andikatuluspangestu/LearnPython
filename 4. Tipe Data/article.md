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

#### Lalu, apa perbedaan antara tipe data angka dan tipe data teks (string)?

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