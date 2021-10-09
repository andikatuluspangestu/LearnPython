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

print('=========') # output: =========
print('=' * 10)    # output: ========

```

