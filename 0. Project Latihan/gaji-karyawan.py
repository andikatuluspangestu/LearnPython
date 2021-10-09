
# PROGRAM HITUNG GAJI KARYAWAN

# Judul Aplikasi
print("----------------------------------")
print("-- PROGRAM HITUNG GAJI KARYAWAN --")

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
print("----------------------------------")
namaKaryawan       = str(input("Nama Karyawan       : "))
golJabatan         = int(input("Golongan Jabatan    : "))
pendidikan         = str(input("Pendidikan          : "))
jamKerja           = int(input("Jumlah Jam Kerja    : "))
gajiPokok          = 300000
print("----------------------------------") 

# Proses Percabangan Tunjangan Jabatan
if( golJabatan == 1 ):
    tunjanganJabatan = 0.05 * gajiPokok
elif( golJabatan == 2 ):
    tunjanganJabatan = 0.10 * gajiPokok
elif( golJabatan == 3 ):
    tunjanganJabatan = 0.15 * gajiPokok
else:
    tunjanganJabatan = 0 

# Proses Percabangan Tingkat Pendidikan
if( pendidikan == "SMA" or pendidikan == "sma" ):
    tunjanganPendidikan = 0.025 * gajiPokok
elif( pendidikan == "D1" or pendidikan == "d1" ):
    tunjanganPendidikan = 0.05 * gajiPokok
elif( pendidikan == "D3" or pendidikan == "d3" ):
    tunjanganPendidikan = 0.2 * gajiPokok
elif( pendidikan == "S1" or pendidikan == "s1" ):
    tunjanganPendidikan = 0.3 * gajiPokok
else:
    tunjanganPendidikan = 0

# Proses Percabangan Honor Lembur
jamNormal = 8

if ( jamKerja > 8 ):
    prosesHonorLembur = jamKerja -  jamNormal
    jumlahHonorLembur = prosesHonorLembur * 3500
else:
    jumlahHonorLembur = 0

# Total Gaji
tunjangan = tunjanganJabatan + tunjanganPendidikan
totalGaji = gajiPokok + tunjangan + jumlahHonorLembur

# Cetak 

print("Honor yang diterima : ")
print("")
print("Gaji Pokok            ", formatrupiah(gajiPokok))
print("Tunjangan Jabatan     ", formatrupiah(str(tunjanganJabatan).rstrip('0').rstrip('.')))
print("Tunjangan Pendidikan  ", formatrupiah(str(tunjanganPendidikan).rstrip('0').rstrip('.')))
print("Honor Lembur          ", formatrupiah(jumlahHonorLembur))
print("----------------------------------")
print("Total Gaji            ", formatrupiah(str(totalGaji).rstrip('0').rstrip('.')))
print("----------------------------------")
