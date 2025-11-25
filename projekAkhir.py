from datetime import datetime

#login
USERNAME = "admin"
PASSWORD = "12345"

#data
ruangan = {}
reservasi = {}

HARGA_TIPE = {
    "STANDART": 100000,
    "PREMIUM": 200000,
    "EXECUTIVE": 350000,
    "VIP": 500000
}

#validasi
def validasi_tipe(tipe):
    return tipe in HARGA_TIPE

def validasi_nama(nama):
    return nama.replace(" ", "").isalpha()

def validasi_tanggal(tgl):
    try:
        datetime.strptime(tgl, "%d-%m-%Y")
        return True
    except:
        return False


#loginnn
def login():
    while True:
        if input("Username: ") == USERNAME and input("Password: ") == PASSWORD:
            print("Login berhasil.\n")
            return
        print("Username atau password salah.\n")


#ruangan
def tambah_ruangan():
    tipe = input("Tipe (STANDART/PREMIUM/EXECUTIVE/VIP): ").upper()
    if not validasi_tipe(tipe):
        print("Tipe tidak valid!")
        return
    
    id_r = f"R{len(ruangan)+1:03d}"
    ruangan[id_r] = {
        "tipe": tipe,
        "harga": HARGA_TIPE[tipe]
    }
    print(f"Ruangan ditambahkan: {id_r}")

def tampilkan_ruangan():
    if not ruangan:
        print("Belum ada ruangan.")
        return
    print("\nDaftar Ruangan:")
    for i, (id_r, d) in enumerate(ruangan.items(), start=1):
        print(f"{i}. {id_r} | {d['tipe']} | Rp{d['harga']}")

def edit_ruangan():
    tampilkan_ruangan()
    if not ruangan:
        return
    
    id_r = input("ID ruangan yang diedit: ").upper()
    if id_r not in ruangan:
        print("ID tidak ada!")
        return

    tipe_baru = input("Tipe baru (STANDART/PREMIUM/EXECUTIVE/VIP): ").upper()
    if not validasi_tipe(tipe_baru):
        print("Tipe tidak valid!")
        return

    # Update ruangan
    ruangan[id_r]["tipe"] = tipe_baru
    ruangan[id_r]["harga"] = HARGA_TIPE[tipe_baru]

    # Update harga di reservasi
    for r in reservasi.values():
        if r["ruangan"] == id_r:
            r["total"] = HARGA_TIPE[tipe_baru]

    print("Ruangan berhasil diupdate!")

def hapus_ruangan():
    tampilkan_ruangan()
    id_r = input("ID yang ingin dihapus: ").upper()
    if id_r in ruangan:
        del ruangan[id_r]
        print("Ruangan dihapus.")
    else:
        print("ID tidak ditemukan.")


#reservasi
def tambah_reservasi():
    if not ruangan:
        print("Tambahkan ruangan terlebih dahulu!")
        return

    nama = input("Nama pemesan: ")
    if not validasi_nama(nama):
        print("Nama tidak valid!")
        return

    tanggal = input("Tanggal (DD-MM-YYYY): ")
    if not validasi_tanggal(tanggal):
        print("Tanggal tidak valid!")
        return

    tampilkan_ruangan()
    id_r = input("ID ruangan: ").upper()
    if id_r not in ruangan:
        print("ID ruangan tidak ada!")
        return

    # Cek bentrok
    for d in reservasi.values():
        if d["ruangan"] == id_r and d["tanggal"] == tanggal:
            print("Ruangan sudah dipesan pada tanggal itu!")
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

def edit_reservasi():
    tampilkan_reservasi()
    if not reservasi:
        return

    id_r = input("ID reservasi: ").upper()
    if id_r not in reservasi:
        print("ID tidak ada!")
        return

    data = reservasi[id_r]

    print("""
1. Edit Nama
2. Edit Tanggal
3. Edit Ruangan
0. Batal
""")

    pilih = input("Pilih: ")

    if pilih == "1":
        baru = input("Nama baru: ")
        if validasi_nama(baru):
            data["nama"] = baru
            print("Nama diperbarui.")
        else:
            print("Nama tidak valid!")

    elif pilih == "2":
        baru = input("Tanggal baru (DD-MM-YYYY): ")
        if not validasi_tanggal(baru):
            print("Tanggal tidak valid!")
            return

        # Cek bentrok
        for k, r in reservasi.items():
            if k != id_r and r["ruangan"] == data["ruangan"] and r["tanggal"] == baru:
                print("BENTROK!")
                return

        data["tanggal"] = baru
        print("Tanggal diperbarui.")

    elif pilih == "3":
        tampilkan_ruangan()
        baru = input("ID ruangan baru: ").upper()

        if baru not in ruangan:
            print("Ruangan tidak ada!")
            return

        # Cek bentrok
        for k, r in reservasi.items():
            if k != id_r and r["ruangan"] == baru and r["tanggal"] == data["tanggal"]:
                print("Ruangan sudah dipakai tanggal itu!")
                return

        data["ruangan"] = baru
        data["total"] = ruangan[baru]["harga"]
        print("Ruangan diperbarui.")

def hapus_reservasi():
    tampilkan_reservasi()
    id_r = input("ID reservasi: ").upper()

    if id_r in reservasi:
        del reservasi[id_r]
        print("Reservasi dihapus.")
    else:
        print("ID tidak ditemukan.")


#menu
def menu_ruangan():
    while True:
        print("""
=== MENU RUANGAN ===
1. Tambah Ruangan
2. Tampilkan Ruangan
3. Edit Ruangan
4. Hapus Ruangan
0. Kembali
""")
        p = input("Pilih: ")
        if p == "1": tambah_ruangan()
        elif p == "2": tampilkan_ruangan()
        elif p == "3": edit_ruangan()
        elif p == "4": hapus_ruangan()
        elif p == "0": break
        else: print("Pilihan salah!")

def menu_reservasi():
    while True:
        print("""
=== MENU RESERVASI ===
1. Tambah Reservasi
2. Tampilkan Reservasi
3. Edit Reservasi
4. Hapus Reservasi
0. Kembali
""")
        p = input("Pilih: ")
        if p == "1": tambah_reservasi()
        elif p == "2": tampilkan_reservasi()
        elif p == "3": edit_reservasi()
        elif p == "4": hapus_reservasi()
        elif p == "0": break
        else: print("Pilihan salah!")

def menu_utama():
    while True:
        print("""
=== MENU UTAMA ===
1. Kelola Ruangan
2. Kelola Reservasi
0. Keluar
""")
        p = input("Pilih: ")
        if p == "1": menu_ruangan()
        elif p == "2": menu_reservasi()
        elif p == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan salah!")

# START
login()
menu_utama()
