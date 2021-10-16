# Program Chicken - 12210940 Andika Tulus Pangestu

# Format Rupiah
def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p
    print("Rp", formatrupiah(q), ".", p)

# Judul Aplikasi
print("=" * 52)
print(" " * 14, "Chicken Setulus Hati", " " * 20)
print("=" * 52)
print("Kode  Jenis    Harga")
print("-" * 23)
print("D     Dada     Rp 2500")
print("P     Paha     Rp 2000")
print("S     Sayap    Rp 1500")

# Deklarasi Variable
banyakJenis     = int(input("Berapa Jenis yang akan anda beli :  "))
kodePotong      = []
banyakPotong    = []
jenisPotong     = []
hargaPerPotong  = []
JumlahHarga     = []

# Perulangan menentukan BanyakPotong, jenisPotong, hargaPerPotong, dan JumlahHarga
i = 0
while i < banyakJenis:

    print("-" * 32)

    # Cetak Jenis ke- (Dari Nilai Variable i)
    print("Jenis ke - ", i+1)

    # Tambahkan kodePotong D/P/S ke list kodePotong
    kodePotong.append(str(input("Kode Potong [D/P/S] : ")))

    # Tambahkan banyakPotong D/P/S ke list banyakPotong
    banyakPotong.append(int(input("Banyak Potong   : ")))

    # Percabangan Penentuan Jenis, Harga, JumlahHarga
    # Jika kodePotong bernilai seperti Variable i dan sama dengan kodePotong tersedia maka..

    if(kodePotong[i] == "D" or kodePotong[i] == "d"):
        jenisPotong.append("Dada ")                      # Add jenisPotong ke list jenisPotong
        hargaPerPotong.append(2500)                      # Add hargaPerPotong ke list hargaPerPotong
        JumlahHarga.append(banyakPotong[i] * int(2500))  # Add JumlahHarga ke list JumlahHarga
    elif(kodePotong[i] == "P" or kodePotong[i] == "p"):
        jenisPotong.append("Paha ")
        hargaPerPotong.append(2000)
        JumlahHarga.append(banyakPotong[i] * int(2000))
    elif(kodePotong[i] == "S" or kodePotong[i] == "s"):
        jenisPotong.append("Sayap")
        hargaPerPotong.append(1500)
        JumlahHarga.append(banyakPotong[i] * int(1500))
    else:
        jenisPotong.append("Jenis Potong Tidak Tersedia")
        hargaPerPotong.append(0)
        JumlahHarga.append(banyakPotong[i] * int(0))

    # Kondisi agar variable i selalu ditambahkan satu.
    i += 1


# Notifikasi
print("")
print("Sedang Mencetak Struk .....")
print("")

# Bagian Struk Pembelian

# Header Struk
print("=" * 52)
print(" " * 14, "Chicken Setulus Hati", " " * 20)
print("=" * 52)

# Template Tabel List
print(" No    Jenis      Harga        Jumlah    Jumlah")
print("       Potong     PerPotong    Beli      Harga ")
print("-" * 52)
template = ' {c}     {jenis_potong}      {harga}          {banyak_potong}        {jumlah}'


# Perulangan Daftar Jenis Chicken yang dipesan
a = 0
while a < banyakJenis:
    c = a + 1
    print(template.format(c = c, jenis_potong = jenisPotong[a], harga = hargaPerPotong[a], banyak_potong = banyakPotong[a], jumlah = JumlahHarga[a]))
    a = a + 1

print("=" * 52)
totalPembelian = sum(JumlahHarga) # Jumlah Total Harga Chicken yang di Beli
print("Total Pembelian : ", formatrupiah(totalPembelian))
jumlahBayar = int(input("Jumlah Bayar    :  Rp "))
jumlahPajak = jumlahBayar * 0.1 # Menghitung Pajak
totalBayar  = jumlahBayar + jumlahPajak
print("Pajak 10%       : ", formatrupiah(str(jumlahPajak).rstrip('0').rstrip('.')))
print("Total Bayar     : ", formatrupiah(str(totalBayar).rstrip('0').rstrip('.')))
print("=" * 52)

