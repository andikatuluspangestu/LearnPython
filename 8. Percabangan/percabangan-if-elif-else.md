# Struktur Percabangan If Elif Else

Sebagaimana pohon, cabangnya tidak hanya 2, tapi bisa 3, 4, 5 bahkan lebih.  
Begitu juga pada logika kita. Kita bisa membuat lebih dari 2 cabang logika. Dan pada python, untuk membuat lebih dari 2 cabang, kita bisa menggunakan blok kode ``if..elif..else.``

---------------------------------------------------------------------------------------

**Contoh Pertama :**  

Contoh yang paling umum digunakan untuk kasus percabangan ``if..elif..else`` adalah menentukan predikat nilai suatu siswa.

Jika nilainya sekian, dia dapat predikat A. Sedangkan jika nilainya sekian maka predikatnya adalah B, dan seterusnya.

Berikut ini aturan yang akan kita gunakan:  

- Predikat A untuk nilai >= 90
- Predikat B untuk nilai >= 80 < 90
- Predikat C untuk nilai >= 60 < 80
- Predikat D untuk nilai >= 40 < 60
- Selain itu, maka predikat E.

> Dari 5 aturan di atas, kita akan menggunakan **satu if, 3 elif, dan 1 else**.

```py3

nilai = 70

if nilai >= 90:
  print('Predikat A')
elif nilai >= 80:
  print('Predikat B')
elif nilai >= 60:
  print('Predikat C')
elif nilai >= 40:
  print('Predikat D')
else:
  print('Predikat E')

```

Jalankan program lalu memasukkan angka 70,  
maka kita akan mendapatkan output predikat C:

Output :

```
Predikat C
```

---------------------------------------------------------------------------------------

**Contoh kedua :**

Membuat aplikasi pencarian buah sederhana.

```py3

buah_yang_tersedia = ['jeruk', 'mangga', 'melon']
buah_yang_dicari = 'melon'

if (buah_yang_dicari in buah_yang_tersedia):
  print('Buah yang anda cari tersedia!')
else:
  print('Buah yang anda cari tidak tersedia!')

```

Output :

```
Buah yang anda cari tersedia!
```

---------------------------------------------------------------------------------------

**Contoh Ketiga :**  

Membuat Aplikasi Minta Maaf ke Doi :)

```py3

jawaban = input("Kamu mau maafin aku? ")

if jawaban == "ya" or jawaban == "y":
    print( "Yeyyy, baikan yaa hihi :)" )
elif jawaban == "gamau" or jawaban == "g":
    print( "Yahhh,, kok gitu :(" )
else:
    print( "ishh, ga direwess auuu.. " )
```

Output :  

```

Kamu mau maafin aku? ya
Yeyyy, baikan yaa hihi :)

```