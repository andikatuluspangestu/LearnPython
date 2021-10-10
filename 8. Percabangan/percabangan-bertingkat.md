# Percabangan Bertingkat

Percabangan bertingkat adalah sebuah istilah untuk if di dalam if.  
Kalau dalam dunia per-bakso-an, percabangan bertingkat adalah bakso beranak 🤤.  
Alias di dalam pentol ada pentol yang lainnya 🍢🍢  

---------------------------------------------------------------------------------------

**Contoh Pertama :**

```py

# Deklarasi variable
nilai = 78
usia = 18

# Jika nilai lebih dari 75 maka..
if nilai >= 75:
  # Jika usia kurang dari 15 maka cetak 'Selamat adek, kamu lulus!'
  if (usia < 15):
    print('Selamat adek, kamu lulus!')
  # Jika usida lebih dari 15 maka cetak 'Selamat kakak, kamu lulus!'
  else:
    print('Selamat kakak, kamu lulus!')

# Jika nilai tidak lebih dari 75 maka..
else:
  # Jika usia kurang dari 15 maka cetak 'Mohon maaf dek, coba lagi ya!'
  if (usia < 15):
    print('Mohon maaf dek, coba lagi ya!')
  # Jika usia lebih dari 15 maka cetak 'Mohon maaf kak, coba lagi ya!'
  else:
    print('Mohon maaf kak, coba lagi ya!')

```

Output :

```
Selamat kakak, kamu lulus!
```

> Kode program di atas akan memeriksa terlebih dahulu apakah nilai yang dimasukkan  
> adalah lulus atau tidak. Setelah itu, program akan memeriksa usia, apakah dia akan  
> disapa dengan “kakak” atau kah dengan “adek”

---------------------------------------------------------------------------------------
Selanjutnya adalah tentang perulangan pada Python.