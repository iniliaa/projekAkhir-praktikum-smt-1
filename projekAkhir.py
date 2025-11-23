# LOGIN
USERNAME = "admin"
PASSWORD = "12345"

# DATA PENYIMPANAN
ruangan = {}
reservasi = {}

HARGA_TIPE = {
    "STANDART": 100000,
    "PREMIUM": 200000,
    "EXECUTIVE": 350000,
    "VIP": 500000
}

# VALIDASI
def validasi_tipe(tipe):
    return tipe in HARGA_TIPE


# LOGIN
def login():
    while True:
        user = input("Username: ")
        pw = input("Password: ")
        if user == USERNAME and pw == PASSWORD:
            print("Login berhasil.\n")
            return
        print("Username atau password salah.\n")


# FUNGSI RUANGAN
def tambah_ruangan():
    tipe = input("Tipe ruangan (STANDART/PREMIUM/EXECUTIVE/VIP): ").upper()
    
    if not validasi_tipe(tipe):
        print("Tipe tidak valid.")
        return
    
    id_ruangan = f"R{len(ruangan)+1:03d}"
    ruangan[id_ruangan] = {
        "tipe": tipe,
        "harga": HARGA_TIPE[tipe]
    }
    print(f"Ruangan ditambahkan: ID {id_ruangan}")

def tampilkan_ruangan():
    if not ruangan:
        print("Belum ada ruangan.")
        return
    
    print("\nDaftar Ruangan:")
    for i, (id_r, d) in enumerate(ruangan.items(), start=1):
        print(f"{i}. {id_r} | {d['tipe']} | Rp{d['harga']}")
    print()

def hapus_ruangan():
    tampilkan_ruangan()
    id_del = input("ID yang ingin dihapus: ").upper()
    
    if id_del in ruangan:
        del ruangan[id_del]
        print("Ruangan dihapus.")
    else:
        print("ID tidak ditemukan.")

# FUNGSI RESERVASI
def tambah_reservasi():
    if not ruangan:
        print("Belum ada ruangan. Tambahkan ruangan dulu.")
        return
    
    nama = input("Nama pemesan: ")
    tanggal = input("Tanggal (YYYY-MM-DD): ")

    tampilkan_ruangan()
    id_r = input("ID ruangan yang ingin dipesan: ").upper()

    if id_r not in ruangan:
        print("ID ruangan tidak ada.")
        return

    # CEK BENTROK
    for r in reservasi.values():
        if r["ruangan"] == id_r and r["tanggal"] == tanggal:
            print("\n Gagal: Ruangan sudah dipesan pada tanggal tersebut!")
            return

    id_res = f"RS{len(reservasi)+1:03d}"
    reservasi[id_res] = {
        "nama": nama,
        "tanggal": tanggal,
        "ruangan": id_r,
        "total": ruangan[id_r]["harga"]
    }

    print(f"Reservasi berhasil! ID: {id_res}")

def tampilkan_reservasi():
    if not reservasi:
        print("Belum ada reservasi.")
        return
    
    print("\nDaftar Reservasi:")
    for i, (id_r, d) in enumerate(reservasi.items(), start=1):
        print(f"{i}. {id_r} | {d['nama']} | {d['tanggal']} | {d['ruangan']} | Rp{d['total']}")
    print()

def hapus_reservasi():
    tampilkan_reservasi()
    
    if not reservasi:
        return
    
    id_del = input("ID reservasi yang ingin dihapus: ").upper()

    if id_del in reservasi:
        del reservasi[id_del]
        print("Reservasi dihapus.")
    else:
        print("ID tidak ditemukan.")

def edit_reservasi():
    tampilkan_reservasi()
    if not reservasi:
        return

    id_edit = input("ID reservasi yang ingin diedit: ").upper()

    if id_edit not in reservasi:
        print("ID reservasi tidak ditemukan.")
        return

    data = reservasi[id_edit]

    print("""
=== EDIT RESERVASI ===
1. Edit Nama Pemesan
2. Edit Tanggal
3. Edit Ruangan
0. Batal
""")

    pilih = input("Pilih: ")

    # ----- Edit Nama -----
    if pilih == "1":
        baru = input("Nama baru: ")
        data["nama"] = baru
        print("Nama berhasil diperbarui.")

    # ----- Edit Tanggal -----
    elif pilih == "2":
        baru = input("Tanggal baru (YYYY-MM-DD): ")

        # Cek bentrok
        for r_id, r in reservasi.items():
            if r_id != id_edit and r["ruangan"] == data["ruangan"] and r["tanggal"] == baru:
                print("Gagal: Ruangan sudah dipesan di tanggal itu!")
                return

        data["tanggal"] = baru
        print("Tanggal berhasil diperbarui.")

    # ----- Edit Ruangan -----
    elif pilih == "3":
        tampilkan_ruangan()
        baru = input("ID ruangan baru: ").upper()

        if baru not in ruangan:
            print("Ruangan tidak ditemukan!")
            return

        # Cek bentrok
        for r_id, r in reservasi.items():
            if r_id != id_edit and r["ruangan"] == baru and r["tanggal"] == data["tanggal"]:
                print("Gagal: Ruangan sudah dipakai pada tanggal ini!")
                return

        data["ruangan"] = baru
        data["total"] = ruangan[baru]["harga"]
        print("Ruangan berhasil diperbarui.")

    elif pilih == "0":
        return
    else:
        print("Pilihan tidak valid.")


# MENU

def menu_ruangan():
    while True:
        print("""
=== MENU RUANGAN ===
1. Tambah Ruangan
2. Tampilkan Ruangan
3. Hapus Ruangan
0. Kembali
""")
        pilih = input("Pilih: ")
        if pilih == "1":
            tambah_ruangan()
        elif pilih == "2":
            tampilkan_ruangan()
        elif pilih == "3":
            hapus_ruangan()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")

def menu_reservasi():
    while True:
        print("""
=== MENU RESERVASI ===
1. Tambah Reservasi
2. Tampilkan Reservasi
3. Hapus Reservasi
4. Edit Reservasi
0. Kembali
""")
        pilih = input("Pilih: ")
        if pilih == "1":
            tambah_reservasi()
        elif pilih == "2":
            tampilkan_reservasi()
        elif pilih == "3":
            hapus_reservasi()
        elif pilih == "4":
            edit_reservasi()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")

def menu_utama():
    while True:
        print("""
=== MENU UTAMA ===
1. Kelola Ruangan
2. Kelola Reservasi
0. Keluar
""")
        pilih = input("Pilih: ")
        
        if pilih == "1":
            menu_ruangan()
        elif pilih == "2":
            menu_reservasi()
        elif pilih == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


login()
menu_utama()
