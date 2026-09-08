def mulaibentuk():
    BENTUK = input(" MASUKAN BENTUK = (PERSEGI,PERSEGI PANJANG,SEGITIGA,TABUNG) = ").upper()
    if BENTUK == "PERSEGI":
            print("LUAS PERSEGI")
            S = float(input("TULISKAN SISI = "))
            LUAS = S * S
            print("LUAS PERSEGI = ", LUAS)

    elif BENTUK == "PERSEGI PANJANG":
            print("LUAS PERSEGI PANJANG")
            PANJANG = float(input("TULISKAN PANJANG = "))
            LEBAR = float(input("TULISKAN LEBAR = "))
            LUAS_PERSEGI_PANJANG = LEBAR * PANJANG
            print("LUAS PERSEGI PANJANG = ", LUAS_PERSEGI_PANJANG)

    elif BENTUK == "SEGITIGA":
            ALAS =float(input("TULISKAN ALAS = "))
            TINGGI = float(input("TULISKAN TINGGI = "))
            LUAS_SEGITIGA = 1/2* ALAS * TINGGI
            print("LUAS SEGITIGA", LUAS_SEGITIGA)


    elif BENTUK == "TABUNG":
            print("LUAS TABUNG")
            JARI_JARI =float(input("TULISKAN JARI JARI = "))
            TINGGI = float(input("TULISKAN TINGGI ="))
            LUAS_TABUNG = 2*22/7*JARI_JARI*(JARI_JARI +TINGGI)
            print(f"LUAS_TABUNG = {LUAS_TABUNG:.2f}")

    else :
            print ("ngga di program itu")