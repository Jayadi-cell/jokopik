import random

print("SELAMAT DATANG DI TEBAK KAMAR KUCING")
print("PAK JOKOWI BILANG SELAMAT BERJUANG SUKSES")
posisi_kucing = random.randint(1,5)

nama_pemain = input("masukan nama anda:")
bentuk_kamar = "|_|"
bentuk_terpilih = [bentuk_kamar] * 5
bentuk_terpilih = " ".join(bentuk_terpilih)

kamar = bentuk_terpilih .split()
kamar[posisi_kucing - 1] = "|0_0|"
kamar =" ".join(kamar)

print(f"Halo {nama_pemain}! Pilih kamar di mana kucing berada : ")
print(f"coba pilih{bentuk_terpilih}")

while True:
    pilihan = int(input("masukan pilihan anda (1-5): "))
    if pilihan in [1,2,3,4,5]:
        if pilihan == posisi_kucing:
            print(f"{kamar}\n Selamat! Anda menemukan kucing ")
            break
        else:
            print("kamu salah! coba lagi")
    else:
        print("Pilihan tidak valid! Masukkan angka antara 1-5.")

