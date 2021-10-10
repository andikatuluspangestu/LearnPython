# Program untuk mengecek diskon

total_belanja = int(input("Total belanja: Rp "))

# jumlah yang harus dibayar adalah berapa total belanjaannya
# tapi kalau dapat diskon akan berkurang
bayar = total_belanja

# jika dia belanja di atas 20rb maka berikan notif diskon
if(total_belanja > 20000):
    notif = "Kamu mendapatkan bonus diskon 10%"

    # hitung diskonnya
    diskon = total_belanja * 10/100 #10%
    bayar = total_belanja - diskon


# cetak struk
print("-" * 25)
print(notif)
print("Total bayar: Rp", bayar)
print("Terima kasih sudah berbelanja")
print("-" * 25)
