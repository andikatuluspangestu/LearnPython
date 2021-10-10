# Struktur Percabangan if else

Blok if else ini biasa dinamakan percabangan, percabangan If/Else digunakan saat terdapat dua pilihan keputusan.  
Karena memiliki setidaknya 2 cabang:

- Cabang ``if``
- Cabang ``else``

--------------------------------------------------------------------------------------

**Contoh Pertama :**

```py3

nilai = 60

print('Nilai anda adalah:', nilai )

if nilai >= 80:
  keputusan = "Selamat, anda lulus!"
else:
  keputusan = "Maaf, anda tidak lulus."

print(keputusan)

```

Output :

```
Nilai anda adalah: 60 
Maaf, anda tidak lulus.
```

--------------------------------------------------------------------------------------

**Contoh Kedua :**

> jika umur diatas atau sama dengan 18 tahun boleh membuat SIM.
> Sedangkan dibawah itu belum boleh.

![](https://www.petanikode.com/img/python/percabangan/struktur-ifelse.png)

```py3

# Deklarasi Variable Umur
umur = 20

if umur >= 18:
    keputusan = "Kamu boleh membuat SIM"
else:
    keputusan = "Kamu belum boleh membuat SIM"

print(keputusan)

```

Output :

```
Kamu boleh membuat SIM
```

> Selain blok ``if``, terdapat juga blok ``else`` yang akan dieksekusi apabila ``kondisi umur >= 18 salah (False)``.

