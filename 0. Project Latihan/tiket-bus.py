namaPembeli = str(input("nama pembeli:    "))
nomorHP     = int(input("nomor handphone: "))

print(" -SBY : Surabaya ")
print(" -BL  : Bali     ")
print(" -LMP : Lampung  ")

kodeJurusan = str(input("Kode Jurusan:  "))
jumlahTiket = int(input("Jumlah Tiket:  "))

if(kodeJurusan == "SBY" or kodeJurusan == "sby"):   
    harga_tiket     = "300000"
    kota_jurusan    = "Surabaya"
    total_harga     = harga_tiket * jumlahTiket
elif(kodeJurusan == "BL" or kodeJurusan == "bl"):
    harga_tiket     = "350000"
    kota_jurusan    = "Bali"
    total_harga     = harga_tiket * jumlahTiket
elif(kodeJurusan == "LMP" or kodeJurusan == "lmp"):
    harga_tiket     = "500000"
    kota_jurusan    = "Lampung"
    total_harga     = harga_tiket * jumlahTiket
else:
    total_harga = 0


if(jumlahTiket >= 3):
    diskon = 0.1 * total_harga
else:
    diskon = 0

total_bayar = total_harga - diskon

print("Nama Pembeli : " , namaPembeli)
print("Nomor Handphone : " , nomorHP)
print("Kode jurusan yang dipilih : " , kodeJurusan)
print("Nama kota tujuan :" , kota_jurusan)
print("Harga : " , total_bayar)
print("Jumlah Beli :" , jumlahTiket)
print("potongan yang didapat : ", diskon)
print("Total Bayar : " , total_harga)
uang_bayar = int(input("masukan uang bayar: " ))
uang_kembali = uang_bayar - total_bayar

print("uang kembali: " , uang_kembali)