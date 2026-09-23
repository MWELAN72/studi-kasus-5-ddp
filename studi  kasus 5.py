def hitung_biaya(jenis_kendaraan, durasi):
    if jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "motor":
        tarif = 3000
    else:
        tarif = 0

    total_biaya = tarif * durasi
    return total_biaya


jenis_kendaraan = input("Masukkan jenis kendaraan (mobil/motor): ")
jam_masuk = int(input("Masukkan jam masuk: "))
jam_keluar = int(input("Masukkan jam keluar: "))

if jam_keluar >= jam_masuk:
    lama_parkir = jam_keluar - jam_masuk
else:
    lama_parkir = (24 - jam_masuk) + jam_keluar

total_biaya = hitung_biaya(jenis_kendaraan, lama_parkir)

print("\n=== HASIL PERHITUNGAN PARKIR ===")
print("Jenis kendaraan :", jenis_kendaraan)
print("Jam masuk       :", jam_masuk)
print("Jam keluar      :", jam_keluar)
print("Lama parkir     :", lama_parkir, "jam")
print("Total biaya     : Rp", total_biaya)