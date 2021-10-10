# Struktur Percabangan If

Percabangan If digunakan saat terdapat satu pilihan keputusan.  
Blok kode if pada python, strukturnya seperti ini:

```py3
if kondisi:
  statements()
```

> Bagian **kondisi** adalah sebuah variabel / atau **nilai yang bertipe data boolean.**
> Baik **berupa nilai True/False secara langsung, atau pun sebuah ekspresi logika.**
> Jika kondisi bernilai True, maka statements() akan dieksekusi oleh sistem.

--------------------------------------------------------------------------

**Contoh Pertama :**  
_kalau kita tidak lulus dalam ujian, maka kita ikut remidi._  
_Sedangkan kalau lulus tidak perlu ikut remidi._

**Flowchart :**  
![image](https://user-images.githubusercontent.com/62005221/136678304-8683fc27-d20f-4cea-95bd-ef5381316b75.png)

**Maka kita bisa membuat kode-nya seperti ini :** 

```py3
if(lulus == tidak):
    print("kamu harus ikut remidi")
```

**Keterangan :**  
```
“Jika lulus == "tidak" maka cetak teks "kamu harus ikut remidi"”

Kita menggunakan operator perbandingan sama dengan (==) untuk membandingkan isi variabel lulus.  
Sedangkan tanda titik-dua (:) adalah tanda untuk memulai blok kode If atau bisa dikatakan "Maka"

Penulisan blok If, harus diberikan indentasi tab atau spasi 4x.

```

**❌ Contoh penulisan yang salah:**  

```py3
if lulus == "tidak":
print("Kamu harus ikut remidi")
```

**✔️ Contoh penulisan yang benar:**  

```py3
if lulus == "tidak":
    print("kamu harus ikut remidi")
```
 
-----------------------------------------------------------------------------------
**Contoh Kedua :**

```py
if True:
  print('Kode program ini akan dieksekusi')

if False:
  print('Kode program ini tidak akan dieksekusi')

print('Kode program ini akan selalu dieksekusi karena tidak termasuk pada percabangan')
```

Output :  
```
Kode program ini akan dieksekusi
Kode program ini akan selalu dieksekusi
```
Kenapa?
Karena kondisi ``if`` **yang kedua tidak bernilai** ``True``, sehingga statemen yang ada di dalamnya pun tidak akan pernah dieksekusi oleh sistem.
Dan ``print()`` yang ke-3 akan selalu dieksekusi karena ia **berada di luar blok kode if.**
Ingat bahwa blok kode di dalam python ditentukan oleh indentasi.  

![](https://ik.imagekit.io/jagongoding/storage/2021/01/python-percabangan/indentasi.png)

Selain menggunakan boolean secara langsung, kita juga bisa menggunakan ekspresi logika untuk percabangan.

```py3

if 5 > 10: # ❌
  print('Nilai 5 lebih dari 10')

if 10 > 5: # ✅
  print('Nilai 10 lebih dari 5')

```

Output :
```
Nilai 10 lebih dari 5
```

-------------------------------------------------------------------------------------

**Contoh Ketiga :**

Kita akan membuat program menentukan apakah seorang siswa ikut ujian ulang atau tidak.  

```py

# Deklarasi Variable
lulus = input("Apakah kamu lulus? (ya/tidak): ")

# Percabangan if
if(lulus == "tidak"):
    keputusan = "Kamu harus ikut ujian ulang"

print("Keputusannya adalah ", keputusan)

```

Output :

```
Apakah kamu lulus? [ya/tidak]: tidak
Keputusannya adalah Kamu harus ikut ujian ulang
```

-------------------------------------------------------------------------------------

**Contoh Ke-empat :**

Kita akan membuat sebuah latihan dengan studi kasus "Aplikasi Diskon Belanja".

> Jika Total Belanja lebih besar dari Rp 20.000 maka pembeli akan diberikan diskon  
> sebesar 10%, dan hal itu harus dicetak pada struk.

```py3

# Program untuk mengecek diskon

total_belanja = int(input("Total belanja: Rp "))

# jumlah yang harus dibayar adalah berapa total belanjaannya
# tapi kalau dapat diskon akan berkurang
bayar = total_belanja

# jika dia belanja di atas 20rb maka berikan notif diskon
if(total_belanja > 20000):
    notif = "Kamu mendapatkan bonus diskon 10%"

    # hitung diskonnya
    diskon = total_belanja * 10/100 #10%
    bayar = total_belanja - diskon


# cetak struk
print("-" * 25)
print(notif)
print("Total bayar: Rp", bayar)
print("Terima kasih sudah berbelanja")
print("-" * 25)


```

Output :  
![image](https://user-images.githubusercontent.com/62005221/136682040-dd8ccd40-2f0f-4eb0-a750-7f1e0ee84334.png)

-------------------------------------------------------------------------------------

Setelah ini kita bisa lanjut ke bagian **Percabangan If Else**


