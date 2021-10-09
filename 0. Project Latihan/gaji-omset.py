# Aplikasi Penggajian Karyawan, dengan Omset belum diketahui.

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

# Deklarasi Variable
gajiPokok   = 5000000
jmlProduk   = int(input("Masukan jumlah Produk  : "))
hargaSatuan = int(input("Harga Satuan Produk    : "))
omset       = jmlProduk * hargaSatuan

# Percabangan
if( jmlProduk > 100  ):
    bonus = 0.2 * omset
elif( jmlProduk < 100 ):
    bonus = 0.1 * omset
else:
    bonus = 0

# Deklarasi dan Cetak Total Gaji
totalGaji = gajiPokok + omset + bonus

print("-----------------------------")
print("Gaji Pokok      : ", gajiPokok)
print("Omset Penjualan : ", omset)
print("Total Gaji      : ", formatrupiah(str(totalGaji).rstrip('0').rstrip('.')))
print("")
