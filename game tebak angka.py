import random
angka_rahasia = random.randint(1, 100)

print("SELAMAT DATANG DI GAME TEBAK ANGKA")
print("PAK JOKOWI BILANG SELAMAT BERJUANG SUKSES")
nama_pemain = input("Masukkan nama anda: ")

print(f"Halo, {nama_pemain} Silakan tebak angka antara 1 dan 100.")

while True:
        pilihan_pemain = input("Masukkan tebakan anda: ")
        tebakan = int(pilihan_pemain)
        if tebakan < 1 or tebakan > 100:
            print("Masukkan angka antara 1-100.")
        elif tebakan < angka_rahasia:
            print("Tebakan anda terlalu rendah.")
        elif tebakan > angka_rahasia:
            print("Tebakan anda terlalu tinggi.")
        else:
            print(f"Mantap, {nama_pemain} Anda berhasil menebak angka rahasia {angka_rahasia}.")
            break