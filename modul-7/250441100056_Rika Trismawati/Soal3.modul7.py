kupon = {
    "HEMAT10": 10,
    "DISKON20": 20,
    "MURAH50": 50
}

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon yang tersedia.")
        return

    print("\n===== DAFTAR KUPON TERSEDIA =====")
    for kode, diskon in kupon.items():
        print(f"Kode: {kode}, Diskon: {diskon}%")
    print("=================================\n")

def proses_transaksi():
    try:
        total_belanja = float(input("Masukkan total belanja: "))
    except ValueError:
        print("Input total harus angka!")
        return
    kode = input("Masukkan kode kupon: ")
    if kode not in kupon:
        print("Kupon tidak valid")
        return
    
    diskon = kupon[kode]
    potongan = total_belanja * diskon / 100
    total_bayar = total_belanja - potongan

    del kupon[kode]

    print(f"Kupon valid! Diskon {diskon}%")
    print(f"Total potongan : Rp{potongan:.0f}")
    print(f"Total pembayaran setelah diskon : Rp{total_bayar:.0f}")


def menu():
    while True:
        print("""
===== SISTEM KASIR - KUPON DISKON =====
1. Tampilkan Semua Kupon
2. Proses Transaksi
3. Keluar
""")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            tampilkan_kupon()
        elif pilihan == "2":
            proses_transaksi()
        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
menu()