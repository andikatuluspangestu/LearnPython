# Python Dasar - Struktur Percabangan If

Percabangan If digunakan saat terdapat satu pilihan keputusan.  

Blok kode if pada python, strukturnya seperti ini:

```py3
if kondisi:
  statements()
```

> Bagian **kondisi** adalah sebuah variabel / atau **nilai yang bertipe data boolean.**
> Baik **berupa nilai True/False secara langsung, atau pun sebuah ekspresi logika.**
> Jika kondisi bernilai True, maka statements() akan dieksekusi oleh sistem.

**Misalkan :**  
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
 
