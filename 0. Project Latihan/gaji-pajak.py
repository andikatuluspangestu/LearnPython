# Aplikasi Penggajian dengan Pajak

# Format Rupiah
def transform_to_rupiah_format(value):
    str_value = str(value)
    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]
    reverse = after_decimal[::-1]
    temp_reverse_value = ""
    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val
    temp_result = temp_reverse_value[::-1]
    return "Rp " + temp_result + "," + before_decimal


# Deklarasi Variable
gajiPokok          = int(input("Gaji Pokok         : "))
jamKerja           = int(input("Total Jam Kerja    : ")) 
tunjangan          = 0.2 * gajiPokok
uangBonuslembur    = 20000
tarifPajak         = 0.1

# Percabangan JamLembur
if( jamKerja > 200 ):
    jamKerjaLebih     = jamKerja - 200
    totalBonusLembur  = jamKerjaLebih * uangBonuslembur
else:
    totalBonusLembur  = 0

# Deklarasi dan Assignment totalGaji
totalGaji = (gajiPokok + tunjangan + totalBonusLembur) - tarifPajak
totalGaj  = int(totalGaji)

# Cetak Rincian Total Gaji
print("Tunjangan          :", transform_to_rupiah_format(tunjangan))
print("---------------------------")
print("Total Gaji ", transform_to_rupiah_format(totalGaji))
print("")
