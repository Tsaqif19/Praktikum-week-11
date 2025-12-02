data_mahasiswa = {}

# Fungsi untuk menampilkan data
def tampilkan():
    print("Program Input Nilai")
    print("=" * 65)
    print(f"{('| No').ljust(5)}| {('Nama').ljust(20)}| {('NIM').ljust(10)}| {('TUGAS').ljust(6)}| {('UTS').ljust(6)}| {('UAS').ljust(6)}| {('AKHIR').ljust(6)}|")
    print("=" * 65)

    if not data_mahasiswa:
        print("|                         TIDAK ADA DATA                        |")
        print("="*65)
        return


    no = 1
    for nama, i in data_mahasiswa.items():
        print(f"{('| %d'%no).ljust(5)}| {str(nama).ljust(20)}| {(i['nim']).ljust(10)}| {str(i['tugas']).ljust(6)}| {str(i['uts']).ljust(6)}| {str(i['uas']).ljust(6)}| {str('%d'%i['akhir']).ljust(6)}|",end="\n")
        no += 1
    print("="*65)

# Fungsi untuk menambah data
def tambah():
    print("\nTambah Data Mahasiswa")
    nim = input("NIM           : ")
    nama = input("Nama          : ") 
    tugas = float(input("Nilai Tugas   : "))
    uts = float(input("Nilai UTS     : "))
    uas = float(input("Nilai UAS     : "))
    akhir = (tugas*0.3) + (uts*0.35) + (uas*0.35)

    data_mahasiswa[nama] = {
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }
    print("Data berhasil ditambah!")

# Fungsi untuk mengubah data
def ubah(nama):
    if nama not in data_mahasiswa:
        print("Data tidak ditemukan!")
        return

    print("Data ditemukan. Masukkan data baru:")
    nim = input("masukkan Nim    : ") 
    tugas = float(input("Tugas baru   : "))
    uts = float(input("UTS baru     : "))
    uas = float(input("UAS baru     : "))
    akhir = (tugas*0.3)+(uts*0.35)+(uas*0.35)

    data_mahasiswa[nama] = {
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }
    print("Data berhasil diubah!")
# Fungsi untuk menambah data 
def hapus(nama):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan!")

while True:
    print("\nProgram Input Nilai")
    print("====================")
    pilihan = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]: ").lower()

    if pilihan == "l":
        tampilkan()
    elif pilihan == "t":
        tambah()
    elif pilihan == "u":
        nama = input("\nMasukkan nama yang akan diubah: ")
        ubah(nama)
    elif pilihan == "h":
        nama = input("\nMasukkan nama yang akan hapus: ")
        hapus(nama)
    elif pilihan == "k":
        print("Terimakasih sudah menggunakan program ini")
        break
    else:
        print("Pilihan tidak sesuai")