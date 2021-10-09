# Aplikasi Penjualan Tiket

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

# Deklarasi Variable Data Pembeli
print("===================================")
print("     Input Data Penumpang Bus      ")
print("===================================")
namaPembeli = str(input("Nama Penumpang : ")) 
noTelepon   = int(input("No Telepon     : "))

# Deklarasi Variable Data Tiket
print("===================================")
print("         Daftar Jurusan Bus        ")
print("===================================")
print("- SBY : Surabaya")
print("- BL  : Bali")
print("- LMP : Lampung")
print("-----------------------------------")
kodeJurusan = str(input("Masukan Kode Jurusan : "))
jumlahTiket = int(input("Masukan Jumlah Tiket : "))
print("===================================")


# Percabangan Harga Tiket
if(kodeJurusan == "SBY" or kodeJurusan == "sby"):
    harga_Tiket      = 300000
    kota_Jurusan     = "Surabaya"
    total_HargaTiket = jumlahTiket * harga_Tiket

elif(kodeJurusan == "BL" or kodeJurusan == "bl"):
    harga_Tiket      = 350000
    kota_Jurusan     = "Bali"
    total_HargaTiket = jumlahTiket * harga_Tiket

elif(kodeJurusan == "LMP" or kodeJurusan == "lmp"):
    harga_Tiket      = 500000
    kota_Jurusan     = "Lampung"
    total_HargaTiket = jumlahTiket * harga_Tiket

else:
    total_HargaTiket = 0
    print("Jurusan yang anda masukan tidak tersedia")

# Menghitung Diskon Tiket 10%
if( jumlahTiket >= 3):
    diskon = 0.1 * total_HargaTiket
else:
    diskon = 0

# Deklarasi Variable Total Harga Tiket_ yang harus dibayar
total_bayar = total_HargaTiket - diskon

# Loading Cetak Tiket
print("")
print("Sedang Mencetak Tiket..")
print("Sedang Mencetak Tiket...")
print("Sedang Mencetak Tiket.....")

# Cetak Data Tiket
print("")
print("---------------------------------------------------")
print("                Penjualan Tiket Bus                ")
print("                        XYZ                        ")
print("---------------------------------------------------")
print("Nama Pembeli         : ", namaPembeli)
print("No. Handphone        : ", noTelepon)
print("Kode Jurusan         : ", kodeJurusan)
print("Nama Kota Tujuan     : ", kota_Jurusan)
print("Harga per-Tiket      : ", formatrupiah(harga_Tiket))
print("Jumlah Pembelian     : ", jumlahTiket)
print("---------------------------------------------------")
print("Potongan Harga       : ", formatrupiah(str(diskon).rstrip('0').rstrip('.')))
print("Total Pembayaran     : ", formatrupiah(str(total_bayar).rstrip('0').rstrip('.')))
uangBayar   = int(input("Masukkan Uang Bayar  :  Rp ")) 
uangKembali = uangBayar - total_bayar
print("Uang Kembali         : ", formatrupiah(str(uangKembali).rstrip('0').rstrip('.')))
print("---------------------------------------------------")
print("")
