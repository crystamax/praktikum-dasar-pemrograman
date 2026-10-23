harga_satuan = float(input("harga satuan:"))
jumlah_barang = float(input("jumlah barang:"))
diskon = float(input("diskon:"))
subtotal = harga_satuan*jumlah_barang
nominal_diskon = subtotal*diskon/100
total = subtotal-nominal_diskon
print("subtotal:", subtotal)
print("nominal dikon", nominal_diskon)
print("total bayar", total)