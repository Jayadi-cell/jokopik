from games import kucing
import hihi
import harilahir
import hitungluas
from perpus import programmasuk, selamat_datang 
def pilihan ():
    pilihan  = int(input("Pilih program :\n1. Game Angka\n2. Game Kucing\n3. Hari Lahir\n4. Hitung luas \nMasukkan pilihan (1/2/3): "))
    return pilihan

def main():
    selamat_datang()

def main():
    
        programmasuk()
        selamat_datang()
        while True:
            pilihan_game = pilihan()
            if pilihan_game == 1:
                kucing.mulai()
            elif pilihan_game == 2 :
                hihi.mulaigame()
            elif pilihan_game == 3 :
                harilahir.harimulai()
            elif pilihan_game == 4 :
                hitungluas.mulaibentuk()
                

if __name__ == "__main__":
    main()