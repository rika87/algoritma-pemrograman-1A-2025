contact_book = {}


def tambah_kontak(teks):
    return teks.isdigit()

def tambah_kontak():
    nama = input("Masukkan nama: ")
    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")
    
    contact_book[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan!")

def tampilkan_kontak():
    if not contact_book:
        print("Tidak ada kontak.")
        return
    for nama, data in contact_book.items():
        print(f"Nama: {nama}, Telepon: {data[0]}, Email: {data[1]}")

def cari_kontak():
    nama = input("Masukkan nama kontak: ")
    if nama in contact_book:
        print(f"Telepon: {contact_book[nama][0]}, Email: {contact_book[nama][1]}")
    else:
        print("Kontak tidak ditemukan.")

def update_email():
    nama = input("Masukkan nama kontak yang akan diperbarui: ")
    
    if nama in contact_book:
        email_baru = input("Masukkan email baru: ")
        contact_book[nama][1] = email_baru
        print("Email berhasil diperbarui!")
    else:
        print("Kontak tidak ditemukan.")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang akan dihapus: ")
    
    if nama in contact_book:
        del contact_book[nama]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan.")

while True:
    print("------------------")
    print(" MENU CONTACT BOOK ")
    print("------------------")
    print("1. Tampilkan semua kontak ")
    print("2. Cari kontak ")
    print("3. Tambah kontak ")
    print("4. Update email kontak ")
    print("5. Hapus kontak ")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_kontak()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        update_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")