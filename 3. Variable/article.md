# Python Dasar - Variable

**Variable adalah** adalah sebuah wadah atau kita anggap aja keranjang, tempat di mana kita bisa memasukkan sesuatu di dalamnya, yaitu data.

Penulisan variabel Python sendiri juga memiliki aturan tertentu, yaitu :

- Karakter pertama harus berupa huruf atau garis bawah/underscore _
- Karakter selanjutnya dapat berupa huruf, garis bawah/underscore _ atau angka
- Karakter pada nama variabel bersifat sensitif (case-sensitif). Artinya huruf kecil dan huruf besar dibedakan.   
  Sebagai contoh, variabel ``namaDepan`` dan ``namadepan`` adalah variabel yang berbeda.
  
 Sebagai contoh, berikut ini adalah variabel-variabel yang benar xdan variabel-variabel yang salah:

```py
_nama ✅
1nama ❌
nama depan ❌
namaDepan ✅
nama_belakang ✅
nama%lengkap ❌
```

  
 ### Cara Membuat Variable
 Secara singkat, membuat variabel di Python sangat mudah sekali. Kita hanya perlu menuliskan nama variabel lalu diikuti oleh nilai yang kita inginkan.

Perhatikan contoh kode berikut ini:

```py
nama = 'Andika'
usia = 18
kekasih = True

print('Nama :', nama)
print('Usia :', usia)
print('Punya kekasih :', kekasih)
```

Jika kita eksekusi, program di atas akan menghasilkan output seperti berikut:

```
Nama : Andika
Usia : 18
Punya kekasih : True
```
> **Penjelasan**  
> 
> Pada skrip di atas, kita membuat 3 buah variabel:  
> 
>  nama  
>  usia  
>  kekasih 
>
> Masing-masing variabel kita berikan sebuah nilai.  
> 
>  Variabel nama memiliki nilai "Andika"  
>  Variabel usia memiliki nilai 18  
>  Variabel kekasih memiliki nilai True  
>  
>  Lalu di baris selanjutnya, kita menampilkan isi dari masing-masing variabel menggunakan perintah ```print()```.  



--------------------
#### Membuat Program Biodata

```py
nama         = "Andika Tulus Pangestu"
alamat       = "Slawi"
umur         = 18
jenisKelamin = "Laki-Laki"
menikah      = false

print("=========================")
print("Nama          :", nama)
print("Alamat        :", alamat)
print("Umur          :", umur)
print("Jenis Kelamin :", jenisKelamin)
print("Status        :", menikah)
print("=========================")
```

--------------------
