import random
from shlex import join

kata_sambutan = ("halo selamat datang sukses")
posisi_kucing = random.randint(1,4)

nama_pemain = input("Masukan nama kamu: ")
bentuk_kamar = "|_|"
kamar_kosong = [bentuk_kamar] * 4
kamar_kosong =" ".join(kamar_kosong)

kamar = kamar_kosong .split()
kamar[posisi_kucing - 1] = "|0_0|"
kamar = " ".join(kamar)

print(f"halo {nama_pemain} coba pilih kamar "
      f"{kamar_kosong}")

pilihan_pemain = int(input("pilih kamar[ 1 / 2 / 3 / 4 ] :"))

if pilihan_pemain in (1,2,3,4):
    if pilihan_pemain == posisi_kucing :
                print(f"{kamar}\n kamu benar")
    else :
                print(f"{kamar}\n kamu salah kucing ada di {posisi_kucing}")
else :
    print ("ulangin lagi")
    exit()
