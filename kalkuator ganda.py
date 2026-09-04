nomor1 = float(input("masukan nomor = "))
operator = input("masukan operator ( + - * )").strip()
nomor2 = float(input("masukan nomor = "))
operator2 = input("masukan operator (+ - * )").strip()
nomor3 = float(input("masukan nomor = "))
#--------------------------------
if operator == "+":
    hasil = nomor1 + nomor2

elif operator == "-":
    hasil = nomor1 - nomor2

elif operator == "*":
    hasil = nomor1 * nomor2
#--------------------------------
if operator2 == "+":
    hasil2 = hasil + nomor3
    print("hasil2 = ", hasil2)
elif operator2 == "-":
    hasil2 = hasil - nomor3
    print("hasil2 = ", hasil2)
elif operator2 == "*":
    hasil2 = hasil * nomor3
    print("hasil2 = ", hasil2)
else :
    print ("GAK NGOTAK ANDA, GAK BISA DIJUMBLAH ITU!!!!!")
