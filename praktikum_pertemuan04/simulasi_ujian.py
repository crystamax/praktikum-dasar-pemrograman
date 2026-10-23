soal = [
    "Ibu kota Indonesia adalah?",
    "2 + 2 * 3 hasilnya adalah?",
    "Tipe data untuk teks pada Python disebut?",
    "Siapa penemu bahasa pemrograman Python?", 
    "Apa kepanjangan dari HTML?" 
]

kunci = ["Jakarta", "8", "string", "Guido van Rossum", "Hypertext Markup Language"]
skor = 0

print("=== SIMULASI UJIAN ===")

for nomor in range(len(soal)):
    print(f"\nSoal {nomor + 1}: {soal[nomor]}")
    jawaban = input("Jawaban Anda: ")
    
   
    if jawaban.strip().lower() == kunci[nomor].lower():
        print("Benar!")
        skor += 1
    else:
        print(f"Salah. Jawaban benar: {kunci[nomor]}")

print(f"\nSkor akhir: {skor}/{len(soal)}")


nilai = (skor / len(soal)) * 100
print(f"Nilai akhir: {nilai:.0f}")