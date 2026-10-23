nama_mahasiswa = ["Ayu", "Bima", "Citra", "Doni"]
cari = input("Nama yang dicari: ").strip()

if cari in nama_mahasiswa:
    print("Nama ditemukan")
else:
    print("Nama tidak ditemukan")