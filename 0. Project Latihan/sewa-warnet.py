# Program Hitung Pembayaran Sewa Warnet

# Input Data Pemakaian
jamPemakaian = int(input("Lama Pemakaian : ")) # 7

# Percabangan 
if( jamPemakaian > 3):
    jamPertama     = jamPemakaian -3
    jamKedua       = jamPertama * 5000
    totalbayar     = jamKedua + 6000
elif( jamPemakaian <= 3 and jamPemakaian >= 1):
    totalbayar = jamPemakaian * 6000
else:
    print("Anda Tidak Menyewa Warnet")

# Cetak Total Bayar
print("Anda harus membayar sewa sebesar Rp", totalbayar)
