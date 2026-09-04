def hari_lahir(tanggal, bulan, tahun):
    # Januari dan Februari diperlakukan sebagai bulan 13 dan 14
    if bulan == 1:
        bulan = 13
        tahun -= 1
    elif bulan == 2:
        bulan = 14
        tahun -= 1

    q = tanggal
    K = tahun % 100
    J = tahun // 100

    h = (q + (13 * (bulan + 1)) // 5+ K + K // 4+ J // 4+ 5 * J) % 7

    nama_hari = ["Sabtu", "Minggu", "Senin", "Selasa", "Rabu", "Kamis","Jumat"]

    return nama_hari[h]


# Program utama
print("=== PROGRAM MENGHITUNG HARI LAHIR ===")

tanggal = int(input("Masukkan tanggal lahir : "))
bulan = int(input("Masukkan bulan lahir   : "))
tahun = int(input("Masukkan tahun lahir   : "))

hasil = hari_lahir(tanggal, bulan, tahun)

print(f"\nAnda lahir pada hari: {hasil}")