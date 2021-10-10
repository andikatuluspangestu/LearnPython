# Perulangan Bersarang/Bertingkat

Perulangan bersarang atau perulangan bertingkat adalah sebuah perulangan yang berada atau terletak di dalam perulangan yang lain.  

Contoh yang simpel adalah: hubungan antara bumi, bulan, dan matahari.  

![](https://ik.imagekit.io/jagongoding/storage/2021/01/python-perulangan-bersarang/rotasi.png)

- Bulan mengelilingi bumi  
- Bumi mengelilingi matahari  
- Akhirnya bulan juga ikutan mengelilingi matahari karena bumi pun mengelilinginya. 

----------------------------------------------------------------------------------

## Perulangan Bersarang dengan while

**Contoh Pertama : Putaran jarum jam**

Ada tiga jarum:  
- jarum detik  
- jarum panjang / menit  
- jarum pendek / jam  

Alurnya:
- Dalam sehari, jarum jam akan berputar 360 derajat sebanyak 1 kali.  
- Setiap jam, jarum menit akan berputar 360 derajat sebanyak 1 kali. Sehingga jarum panjang akan berputar sebanyak 60 kali dalam sehari.  
- dan setiap menit, jarum detik akan berputar 360 derajat sebanyak 1 kali, sehingga dalam satu jam, ia akan berputar sebanyak 60 kali.  

> Intinya di dalam setiap satu putaran, di dalamnya masih ada putaran yang lainnya, dan ada putaran yang lainnya lagi.
> Inilah yang dinamakan perulangan bersarang

Oke, biar tidak makin bingung, mari kita seduh kopi dulu kemudian kita mulai contoh pengaplikasiannya dalam kode program python.

☕☕☕☕

### Alur Dasar

```py

for i in range(3):
  print('Perulangan luar [i] = ', i)

  for j in range(5):
    print('   Perulangan dalam [i, j] = ', str(i) + ', ' + str(j))

```

Output :  

```
Perulangan luar [i] =  0
   Perulangan dalam [i, j] =  0, 0
   Perulangan dalam [i, j] =  0, 1
   Perulangan dalam [i, j] =  0, 2
   Perulangan dalam [i, j] =  0, 3
   Perulangan dalam [i, j] =  0, 4
Perulangan luar [i] =  1
   Perulangan dalam [i, j] =  1, 0
   Perulangan dalam [i, j] =  1, 1
   Perulangan dalam [i, j] =  1, 2
   Perulangan dalam [i, j] =  1, 3
   Perulangan dalam [i, j] =  1, 4
Perulangan luar [i] =  2
   Perulangan dalam [i, j] =  2, 0
   Perulangan dalam [i, j] =  2, 1
   Perulangan dalam [i, j] =  2, 2
   Perulangan dalam [i, j] =  2, 3
   Perulangan dalam [i, j] =  2, 4
```

Di dalam kode program kita di atas, kita telah membuat 2 buah perulangan:  

- Perulangan pertama sebanyak 3 kali.  
- Dan perulangan kedua sebanyak 5 kali setiap satu kali perulangan pertama.  

Sehingga, total iterasi seluruhnya adalah 3x5 yaitu 15.

----------------------------------------------------------------------------------

**Contoh Kedua ( Membuat Pattern ) :**  

```py

for baris in range(5):
  for kolom in range(7):
    print('o', end = ' ')
  else:
    print('')

```

Output :

```
o o o o o o o 
o o o o o o o 
o o o o o o o 
o o o o o o o 
o o o o o o o
```

----------------------------------------------------------------------------------

## Perulangan Bersarang dengan while

Kita juga bisa menggunakan while untuk membangun sebuah perulangan bersarang, perhatikan contoh berikut:  

```py3

listKota = [
  'Jakarta', 'Surabaya', 'Makassar'
]

for kota in listKota:
  print(kota)
  
  listTempat = [
    'Taman', 'Lapangan', 'Mall'
  ]

  while listTempat:
    print('-->', listTempat.pop(0))

```

Output :  

```
Jakarta
--> Taman
--> Lapangan
--> Mall
Surabaya
--> Taman
--> Lapangan
--> Mall
Makassar
--> Taman
--> Lapangan
--> Mall
```


