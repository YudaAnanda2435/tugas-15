print("=========SAUNG MAKAN BALAREA==========")
pembeli = input("Nama Pembeli: ")

def makanan():
    global totalmakanan
    global porsi
    global makanan
    print("\n==========MENU MAKANAN===========")
    print("1. Nasi Bakar Ayam - Rp.25000,00")
    print("2. Opor Ayam Kampung - Rp.20000,00")
    print("3. Paket Nasi Liwet Komplit - Rp.40000,00")
    print("4. Gulai Kambing - Rp.45000,00")
    print("5. Sate Kikil - Rp.30000,00")
    fx = int(input("masukkan pilihan 1/2/3/4/5 : "))
    porsi = int(input("masukkan posrsi : "))

    if fx == 1:
        totalmakanan = porsi * 25000
        print(porsi, "Nasi Bakar Ayam - Rp.", totalmakanan)
        makanan = ("Nasi Bakar Ayam")
    elif fx == 2:
        totalmakanan = porsi * 20000
        print(porsi, "Opopr Ayam Kampung - Rp.", totalmakanan)
        makanan = ("Opor Ayam Kampung")
    elif fx == 3:
        totalmakanan = porsi * 40000
        print(porsi, "Paket Nasi Liwet Komplit - Rp.", totalmakanan)
        makanan = ("Paket Nasi Liwet Komplit")
    elif fx == 4:
        totalmakanan = porsi * 45000
        print(porsi, "Gulai kambing - Rp.", totalmakanan)
        makanan = ("Gulai Kambing")
    elif fx == 5:
        totalmakanan = porsi * 30000
        print(porsi, "Sate Kikil - Rp.", totalmakanan)
        makanan = ("Sate Kikil")
    else:
        print("Pilihan anda tidak ada dalam daftar menu\nSilahkan pilih kembali!!")
        makanan()

def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n==========MENU MINUMAN==========")
    print("1. juice Alpukat - Rp.10000,00")
    print("2. Es Teh Manis - Rp.5000,00")
    print("3. Kopi Mocca - Rp.8000,00")
    print("4. Teh Green Tea - Rp.7000,00")
    print("5. Teh Tawar - Rp.2000,00")
    print("6. Es Jeruk Segar - Rp.6000,00")
    print("7. Susu Coklat - Rp.8000,00")
    fx = int(input("masukkan pilihan 1/2/3/4/5/6/7 : "))
    gelas = int(input("berapa gelas : "))

    if fx == 1:
        totalminuman = gelas * 10000
        print(gelas, "Juice Alpukat - Rp.", totalminuman)
        minum = ("Juice Alpukat")
    elif fx == 2:
        totalminuman = gelas * 5000
        print(gelas, "Es Teh Manis - Rp.", totalminuman)
        minum = ("Es Teh Manis")
    elif fx == 3:
        totalminuman = gelas * 8000
        print(gelas, "Kopi Mocca - Rp.", totalminuman)
        minum = ("Kopi Mocca")
    elif fx == 4:
        totalminuman = gelas * 7000
        print(gelas, "Teh Grean Tea - Rp.", totalminuman)
        minum = ("Teh Grean Tea")
    elif fx == 5:
        totalminuman = gelas * 2000
        print(gelas, "Es Teh Tawar - Rp.", totalminuman)
        minum = ("Es Teh Tawar")
    elif fx == 6:
        totalminuman = gelas * 6000
        print(gelas, "Es Jeruk Segar - Rp.", totalminuman)
        minum = ("Es Jeruk Segar")
    elif fx == 7:
        totalminuman = gelas * 8000
        print(gelas, "Susu Coklat - Rp.", totalminuman)
        minum = ("Susu Coklat")
    else:
        print("Pilihan anda tidak ada dalam daftar menu\nSilahkan pilih kembali!!")
        minuman()

makanan()
minuman()
total_semua = totalmakanan + totalminuman

print("\nTotal yang harus anda bayar : Rp.", total_semua)
uang = int(input("masukkan uang anda : RP."))
kembalian = int(uang - total_semua)
print("kembalian : ", kembalian)

f = open("nota.txt","w")
f.write("==========S T R U K  P E M B E L I A N==========" + "\n")
f.write("Nama : " + (pembeli) + "\n")
f.write("Beli : " + str(porsi) + str(makanan) + "(Rp." + str(totalmakanan) + ")" + "\n")
f.write("Beli : " + str(gelas) + str(minum) + "(Rp." + str(totalminuman) + ")" + "\n")
f.write("Tagihan : Rp." + str(total_semua) + "\n")
f.write("Dibayar : Rp." + str(uang) + "\n")
f.write("Kembalian : Rp." + str(kembalian) + "\n")
f.write("===============================================" + "\n")
f.close()

print("nota telah disimpan")