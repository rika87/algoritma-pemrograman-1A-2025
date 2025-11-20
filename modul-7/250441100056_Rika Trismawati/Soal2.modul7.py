inventaris = {}

def hanya_huruf_angka(teks):
    return teks.isalnum()

def tambah_barang():
    id_barang = input("Masukkan ID Barang: ") 
#bukan
    if not hanya_huruf_angka(id_barang):
        print("ID tidak valid! coba lagi")
        return
#ada
    if id_barang in inventaris:
        print("ID sudah ada! Gunakan ID lain.")
        return

    nama = input("Masukkan Nama Barang : ")
    if not hanya_huruf_angka(nama):
        print("ingat !!harus berupa huruf & angka Silahkan coba lagi!")
        return
    try:
        harga = int(input("Masukkan Harga Barang: "))
        stok = int(input("Masukkan Stok Barang: "))
    except ValueError:
        print("Tidak valid!")
        return

    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil di tambahkan")

def tampilkan_barang():
    if not inventaris:
        print("Belum ada barang di inventaris.")
        return

    print("\n===== DATA INVENTARIS =====")
    for id_brg, data in inventaris.items():
        print(f"ID: {id_brg}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")
    print("============================\n")

def cari_barang():
    id_cari = input("Masukkan ID Barang: ")

    if not hanya_huruf_angka(id_cari):
        print("ID hanya boleh huruf dan angka!")
        return

    if id_cari in inventaris:
        data = inventaris[id_cari]
        print(f"ID: {id_cari}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.")

def update_stok():
    id_update = input("Masukkan ID Barang yang ingin diperbarui: ")

    if not hanya_huruf_angka(id_update):
        print("ID hanya boleh huruf dan angka!")
        return

    if id_update not in inventaris:
        print("Barang tidak ditemukan.")
        return

    try:
        tambahan = int(input("Masukkan perubahan stok (tidak boleh negatif): "))
    except ValueError:
        print("Input harus angka.")
        return

    stok_baru = inventaris[id_update][2] + tambahan

    if stok_baru < 0:
        print("Stok tidak boleh negatif!")
    else:
        inventaris[id_update][2] = stok_baru
        print("Stok berhasil diperbarui!")

def hapus_barang():
    id_hapus = input("Masukkan ID Barang yang ingin dihapus: ")

    if not hanya_huruf_angka(id_hapus):
        print("ID hanya boleh huruf dan angka!")
        return

    if id_hapus in inventaris:
        del inventaris[id_hapus]
        print("Barang berhasil dihapus!")
    else:
        print("Barang tidak ditemukan.")

def menu():
    while True:
        print("""
===== MENU INVENTARIS GUDANG =====
1. Tampilkan Semua Barang
2. Cari Barang Berdasarkan ID
3. Tambah Barang
4. Update Stok Barang
5. Hapus Barang
6. Keluar
""")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            cari_barang()
        elif pilihan == "3":
            tambah_barang()
        elif pilihan == "4":
            update_stok()
        elif pilihan == "5":
            hapus_barang()
        elif pilihan == "6":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
menu()