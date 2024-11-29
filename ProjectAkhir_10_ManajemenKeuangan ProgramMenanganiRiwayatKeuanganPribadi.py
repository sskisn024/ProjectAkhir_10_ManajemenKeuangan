import os
os.system("cls")

print("***************************************")
print("Selamat Datang Di Program Kelompok 10")
print("***************************************")

usernames = []
passwords = []
saldo = 0

def register(namauser, password):
    usernames.append(namauser)
    passwords.append(password)
    print("Registrasi berhasil! Anda dapat login.")

def login(namauser, password):
    user_found = False  # Variabel untuk menandai apakah pengguna ditemukan

    for i in range(len(usernames)):
        if usernames[i] == namauser:
            user_found = True  # Pengguna ditemukan
            if passwords[i] == password:
                return True  # Login berhasil
            else:
                print("Password salah!")
                return False  # Password salah

    if not user_found:
        print("Username tidak ditemukan!")
    
    return False  # Pengguna tidak ditemukan

def logout_user(namauser, password):
    user_found = False  # Variabel untuk menandai apakah pengguna ditemukan

    for i in range(len(usernames)):
        if usernames[i] == namauser:
            user_found = True  # Pengguna ditemukan
            if passwords[i] == password:
                print(f"Anda telah berhasil logout, {namauser}.")
                return True  # Logout berhasil
            else:
                print("Password salah! Tidak dapat logout.")
                return False  # Password salah

    if not user_found:
        print("Username tidak ditemukan! Tidak dapat logout.")
    
    return False  # Pengguna tidak ditemukan

cadangan_user = None  # Variabel untuk menyimpan pengguna yang sedang login


while True:
    print("Menu: ")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == "1":
        namauser_input = input("Masukkan username: ")
        password_input = input("Masukkan password: ")

        if not namauser_input or not password_input:
            print("Username dan password tidak boleh kosong!")
            continue

        if namauser_input in usernames:
            print("Username sudah terdaftar, silakan gunakan username lain.")
            continue

        register(namauser_input, password_input)

    elif pilihan == "2":
        print("Anda memilih login")
        namauser = input("Nama: ")
        password = input("Password: ")

        # Memastikan username dan password tidak boleh kosong
        if not namauser or not password:
            print("Username dan password tidak boleh kosong!")
            continue  # Kembali ke awal loop

        if login(namauser, password):
            print("***************************")
            print(f"Selamat Datang {namauser}!")
            print("***************************")
            user_login = namauser  # Simpan username yang sedang login
            
            # Menu setelah login
            while True:
                print("Pilihan: ")
                print("1. Riwayat Keuangan")
                print("2. Kalkulator Anggaran")
                print("3. Tabungan")
                print("4. next")
                pilihan = input("Masukkan pilihan: ")

                if pilihan == "1":
                    catatan_transaksi = []

                    def cek_saldo():
                        print(f"Saldo saat ini: {saldo}")

                    def tambah_transaksi(jenis, jumlah):
                        global saldo
                        if jenis == "pemasukan":
                            saldo += jumlah
                            cttn = f"Pemasukan: {jumlah}"
                            catatan_transaksi.append(cttn)
                            print(f"Catatan pemasukan berhasil ditambahkan: {cttn}")
                        elif jenis == "pengeluaran":
                            if saldo >= jumlah:
                                saldo -= jumlah
                                cttn = f"Pengeluaran: {jumlah}"
                                catatan_transaksi.append(cttn)
                                print(f"Catatan pengeluaran berhasil ditambahkan: {cttn}")
                            else:
                                print("Saldo tidak cukup untuk melakukan pengeluaran!")

                    def lihat_catatan_transaksi():
                        print("Catatan Transaksi:")
                        for cttn in catatan_transaksi:
                            print(cttn)

                    while True:
                        print("Pilihan: ")
                        print("1. Cek Saldo")
                        print("2. Transaksi (Pemasukan/Pengeluaran)")
                        print("3. Catatan Transaksi")
                        print("4. Back")
                        pilihan = input("Masukkan pilihan: ")

                        if pilihan == "1":
                            cek_saldo()
                        elif pilihan == "2":
                            jenis = input(" Masukkan jenis transaksi (pemasukan/pengeluaran): ")
                            if jenis not in ["pemasukan", "pengeluaran"]:
                                print("Jenis transaksi tidak valid! Harap masukkan 'pemasukan' atau 'pengeluaran'.")
                                continue
                            jumlah = float(input("Masukkan jumlah: "))
                            if jumlah < 0:
                                print("Jumlah tidak boleh negatif!")
                            else:
                                tambah_transaksi(jenis, jumlah)
                        elif pilihan == "3":
                            lihat_catatan_transaksi()
                        elif pilihan == "4":
                            print("Kembali ke menu utama.")
                            break
                        else:
                            print("Pilihan tidak valid.")
                
                elif pilihan == "2":
                    catatan_pembagian = []

                    def cek_saldo():
                        print(f"Saldo saat ini: {saldo}")

                    def tambah_saldo(jumlah):
                        global saldo
                        saldo += jumlah
                        print(f"Saldo berhasil ditambah: {jumlah}")

                    def kurang_saldo(jumlah):
                        global saldo
                        if saldo >= jumlah:
                            saldo -= jumlah
                            print(f"Saldo berhasil dikurangi: {jumlah}")
                        else:
                            print("Saldo tidak cukup!")

                    def catatan():
                        print("Catatan Pembagian:")
                        for cttn in catatan_pembagian:
                            print(cttn)

                    def tambah_catatan_pembagian(makan, transportasi, dana_darurat, kebutuhan_lainnya):
                        total = makan + transportasi + dana_darurat + kebutuhan_lainnya
                        cttn = f"Makan: {makan}, Transportasi: {transportasi}, Dana Darurat: {dana_darurat}, Kebutuhan Lainnya: {kebutuhan_lainnya}, Total: {total}"
                        catatan_pembagian.append(cttn)
                        print(f"Catatan pembagian berhasil ditambahkan: {cttn}")

                    while True:
                        print("Pilihan: ")
                        print("1. Cek Saldo")
                        print("2. Tambah Saldo")
                        print("3. Kurang Saldo")
                        print("4. Catatan")
                        print("5. Pembagian")
                        print("6. Back")
                        pilihan = input("Masukkan pilihan: ")

                        if pilihan == "1":
                            cek_saldo()
                        elif pilihan == "2":
                            jumlah = float(input("Masukkan jumlah untuk ditambahkan: "))
                            if jumlah < 0:
                                print("Jumlah tidak boleh negatif!")
                            else:
                                tambah_saldo(jumlah)
                        elif pilihan == "3":
                            jumlah = float(input("Masukkan jumlah untuk dikurangi: "))
                            if jumlah < 0:
                                print("Jumlah tidak boleh negatif!")
                            else:
                                kurang_saldo(jumlah)
                        elif pilihan == "4":
                            catatan()
                        elif pilihan == "5":
                            makan = float(input("Masukkan nominal untuk makan: "))
                            transportasi = float(input("Masukkan nominal untuk transportasi: "))
                            dana_darurat = float(input("Masukkan nominal untuk dana darurat: "))
                            kebutuhan_lainnya = float(input("Masukkan nominal untuk kebutuhan lainnya: "))
                            
                            if makan < 0 or transportasi < 0 or dana_darurat < 0 or kebutuhan_lainnya < 0:
                                print("Nominal tidak boleh negatif!")
                            else:
                                tambah_catatan_pembagian(makan, transportasi, dana_darurat, kebutuhan_lainnya)
                        elif pilihan == "6":
                            print("Kembali ke menu utama.")
                            break
                        else:
                            print("Pilihan tidak valid.")
                
                elif pilihan == "3":
                    data_tabungan = []
                    # Fungsi untuk menambahkan tabungan
                    def tambah_tabungan(tanggal, jumlah):
                        global data_tabungan
                        data_tabungan.append({'tanggal': tanggal, 'jumlah': jumlah})
                        print(f"Tabungan sebesar Rp{jumlah:,} pada {tanggal} berhasil ditambahkan.")

                    # Fungsi untuk melihat semua tabungan
                    def lihat_tabungan():
                        global data_tabungan
                        if not data_tabungan:
                            print("Belum ada data tabungan.")
                            return
                        print("Data Tabungan:")
                        for i, tabungan in enumerate(data_tabungan, 1):
                            print(f"{i}. Tanggal: {tabungan['tanggal']}, Jumlah: Rp{tabungan['jumlah']:,}")
                        print(f"Total Tabungan Saat Ini: Rp{hitung_total_tabungan():,}\n")

                    # Fungsi untuk memperbarui tabungan
                    def perbarui_tabungan(i, tanggal_baru, jumlah_baru):
                        global data_tabungan
                        if 0 <= i < len(data_tabungan):
                            data_tabungan[i] = {'tanggal': tanggal_baru, 'jumlah': jumlah_baru}
                            print(f"Data tabungan pada {i + 1} berhasil diperbarui.")
                        else:
                            print("tidak valid.")

                    # Fungsi untuk menghapus tabungan
                    def hapus_tabungan(i):
                        global data_tabungan
                        if 0 <= i < len(data_tabungan):
                            tabungan = data_tabungan.pop(i)
                            print(f"Data tabungan pada {tabungan['tanggal']} sebesar Rp{tabungan['jumlah']:,} berhasil dihapus.")
                        else:
                            print("tidak valid.")

                    # Fungsi untuk menghitung total tabungan ```python
                    def hitung_total_tabungan():
                        global data_tabungan
                        return sum(tabungan['jumlah'] for tabungan in data_tabungan)

                    # Fungsi untuk menghitung waktu yang dibutuhkan untuk mencapai target
                    def hitung_waktu_mencapai_target(target_tabungan, tabungan_harian, total_tabungan):
                        if tabungan_harian <= 0:
                            print("Tabungan harian harus lebih dari 0 untuk menghitung waktu.")
                            return None
                        hari_dibutuhkan = (target_tabungan - total_tabungan) // tabungan_harian
                        if (target_tabungan - total_tabungan) % tabungan_harian != 0:
                            hari_dibutuhkan += 1
                        print(f"Waktu yang dibutuhkan untuk mencapai target: {hari_dibutuhkan} hari.")
                        return hari_dibutuhkan

                    # Fungsi untuk menabung harian
                    def tabung_harian(tabungan_harian, total_tabungan):
                        total_tabungan += tabungan_harian
                        print(f"Anda menabung Rp{tabungan_harian:,} hari ini.")
                        print(f"Total tabungan saat ini: Rp{total_tabungan:,}")
                        return total_tabungan

                    # Fungsi untuk memberikan pengingat harian
                    def pengingat_harian(hari, target_tabungan, tabungan_harian, total_tabungan):
                        print(f"--- Hari ke-{hari} ---")
                        print(f"Target tabungan: Rp{target_tabungan:,}")
                        print(f"Tabungan harian: Rp{tabungan_harian:,}")
                        print(f"Total tabungan saat ini: Rp{total_tabungan:,}")
                        print("Jangan lupa menabung hari ini!")

                    # Fungsi untuk menjalankan tabungan harian
                    def jalankan_simulasi():
                        target_tabungan = int(input("Masukkan target tabungan (Rp): "))
                        tabungan_harian = int(input("Masukkan jumlah tabungan harian (Rp): "))
                        total_tabungan = 0
                        print(f"Target tabungan telah diset sebesar Rp{target_tabungan:,}.")
                        print(f"Tabungan harian telah diset sebesar Rp{tabungan_harian:,}.")

                        while True:
                            print("=== Catatan Tabungan Harian ===")
                            print("1. Hitung Waktu Mencapai Target")
                            print("2. Mulai Simulasi Harian")
                            print("3. Kembali ke Menu Utama")
                            pilihan = input("Pilih menu (1-3): ")

                            if pilihan == '1':
                                hitung_waktu_mencapai_target(target_tabungan, tabungan_harian, total_tabungan)
                            elif pilihan == '2':
                                hari = 1
                                while total_tabungan < target_tabungan:
                                    pengingat_harian(hari, target_tabungan, tabungan_harian, total_tabungan)
                                    lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
                                    if lanjut == 'n':
                                        print("Simulasi dihentikan. Anda kembali ke menu utama.")
                                        break
                                    total_tabungan = tabung_harian(tabungan_harian, total_tabungan)
                                    hari += 1

                                # Cek apakah target tercapai setelah keluar dari loop
                                if total_tabungan >= target_tabungan:
                                    print("Selesai. Anda telah mencapai target tabungan!")
                            elif pilihan == '3':
                                print("Kembali ke menu utama.")
                                break
                            else:
                                print("Pilihan tidak valid, silakan coba lagi.")

                    # Langsung menggunakan loop while True
                    while True:
                        print("=== Riwayat Menabung ===")
                        print("1. Tambah Tabungan")
                        print("2. Saldo Tabungan")
                        print("3. Perbarui Tabungan")
                        print("4. Hapus Tabungan")
                        print("5. Tracker Tabungan")
                        print("6. Back")
                        pilihan = input("Pilih menu (1-6): ")

                        if pilihan == '1':
                            tanggal = input("Masukkan tanggal: ")
                            jumlah = int(input("Masukkan jumlah tabungan: "))
                            tambah_tabungan(tanggal, jumlah)
                        elif pilihan == '2':
                            lihat_tabungan()
                        elif pilihan == '3':
                            lihat_tabungan()
                            i = int(input("Pilih tabungan yang ingin diperbarui: ")) - 1
                            tanggal_baru = input("Masukkan tanggal baru: ")
                            jumlah_baru = int(input("Masukkan jumlah tabungan baru: "))
                            perbarui_tabungan(i, tanggal_baru, jumlah_baru)
                        elif pilihan == '4':
                            lihat_tabungan()
                            i = int(input("Pilih tabungan yang ingin dihapus: ")) - 1
                            hapus_tabungan(i)
                        elif pilihan == '5':
                            jalankan_simulasi()
                        elif pilihan == '6':
                            print("Kembali ke menu utama.")
                            break
                        else:
                            print("Pilihan tidak valid, silakan coba lagi.")
                elif pilihan == "4":
                    while True:
                        print("Ingin Logout atau kembali ke menu utama: ")
                        print("1. Logout")
                        print("2. back")
                        pilihan_next = input("Masukkan pilihan: ")
                        if pilihan_next == "1":
                            if logout_user(namauser, input("Masukkan password untuk logout: ")):
                                print("Terima kasih telah memakai program kami")
                                exit()  # Keluar dari program setelah logout
                        elif pilihan_next == "2":
                            break  # Kembali ke menu utama
                        else:
                            print("Pilihan tidak valid.")
                else:
                    print("Pilihan tidak valid.")
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini!")
        break  # Keluar dari loop utama
    else:
        print("Pilihan tidak valid.")