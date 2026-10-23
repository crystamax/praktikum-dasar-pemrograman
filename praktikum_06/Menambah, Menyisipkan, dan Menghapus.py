daftar_matkul = ["Algoritma", "Tipe Data"]
print("Awal:", daftar_matkul)

daftar_matkul.append("Basis Data")
print("Setelah append:", daftar_matkul)

daftar_matkul.insert(1, "Pemrograman")
print("Setelah insert:", daftar_matkul)

del daftar_matkul[0]
print("Setelah del indeks 0:", daftar_matkul)

terhapus = daftar_matkul.pop()
print("Terhapus dengan pop:", terhapus)
print("List akhir:", daftar_matkul)