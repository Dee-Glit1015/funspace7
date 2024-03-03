#Hitung Luas Segitiga Sederhana

def luas_segitiga():
    a = int(input("Masukkan alas segitiga :"))
    t = int (input("Masukkan tinggi segtiga :"))
    luas = a * t / 2
    print("Luas Segitiga adalah : ", luas)
    
luas_segitiga()

#Hitung Luas Persegi Panjang
def luas_persegi_panjang():
    p = int(input("Masukakn Panjan Persegi : "))
    l = int(input("Masukan Lebar Persegi : "))
    luas = p * l
    print ("Luas Persegi adalah : ", luas)

luas_persegi_panjang()

#Hitung Luas Lingkaran
def luas_lingkaran () :
    r = int (input ("Masukkan Jari- Jari lingkaran : "))
    luas = 3.14 * r *r
    print ("Luas Lingkaran adalah : " , luas )

luas_lingkaran()