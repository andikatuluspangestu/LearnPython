namaPembeli = str(input("nama pembeli:    "))
nomorHP     = int(input("nomor handphone: "))
kodeJurusan = str(input("Kode Jurusan:  "))
jumlahTiket = int(input("Jumlah Tiket:  "))

if(kodeJurusan == "SBY" or kodeJurusan == "sby"):   
    harga_tiket     = "300000"
    total_harga     = harga_tiket * jumlahTiket
    if(jumlahTiket >= 3):
        diskon = 0.1 * total_harga
else:
    total_harga = 0

total_bayar = total_harga - diskon

print("Nama : " , namaPembeli)
print("Nomor HP : " , nomorHP)
print("Kode jurusan : " , kodeJurusan)
print("Harga : " , total_bayar)
print("Potongan : ", diskon)
print("Total : " , total_harga)