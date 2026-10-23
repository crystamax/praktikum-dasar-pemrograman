kode_token = ""

while kode_token != "GWSIGMA1945":
    kode_token = input("Masukkan kode token akses ujian: ")
    if kode_token != "GWSIGMA1945":
        print("Kode token salah, silakan coba lagi.")

print("Token valid. Anda dapat memulai ujian.")