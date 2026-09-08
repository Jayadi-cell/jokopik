from time import sleep

def selamat_datang():
    style = "*" *(len("Semangat") + 6)


    print(style)
    print(f"** Semangat **")
    print(style)

def programmasuk():
    print("Selamat")
    sleep(1)
    print("Berjuang.")
    sleep(1)
    print("Sukses.")
    sleep(1)
 
if __name__ == "__main__":    
     selamat_datang()