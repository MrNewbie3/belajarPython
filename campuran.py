#ntahlah bikin apaan ini kaga paham gua
print("Hello, back to the my ribetz calculator")
data = int(input("Masukkan jumlah data yang akan diinput: "))
nama = []
usiaa =  []

for i in range(0, data):
    print(f"Data {i}")
    masuk = input("Masukkan nama anda terlebih dahulu: ")
    usia = int(input("Masukkan usia anda terlebih dahulu: "))
    if masuk != "Anjas" or "anjas":
        print(f"Hello Mr. / Mrs. {masuk}")
        if usia > 30:
            print("Our senior executive's here")
        elif usia < 30:
            print("Our young executive's here") 
    nama.append(masuk)
    usiaa.append(usia)

for a in range(0, len(nama)):
    datam = nama[a]
    hwwm = usiaa[a]
    print(f"Your verification is complete, your known as Mr. {datam} and {hwwm} years as old")


print("Okey, langsung saja masuk ke kalkulator")
print("Sebelum ke kalkulator masukkan username dan password yang telah diberikan developer")
use = input("Masukkan Username: ")
passwo = input("Masukkan password: ")
if use == "Atharafi":
    passwo = input("Masukkan Password: ")
    if passwo == "Atharafi26":
        print("Password dan username benar")


        print("So this the calculator")
        numf = int(input("Input first number: "))
        typ = input("Masukkan jenis operasi(*,-,+,:) : ")
        nums = int(input("Input second number"))
        if typ == "*":
            print(numf * nums)
        elif typ == "-":
            print(numf - nums)
        elif typ == "+":
            print(numf + nums)
        elif typ == ":":
            print(numf / nums)
        else:
            print("You type wrong symbol")

elif use != "Atharafi":
    print("Username salah")
    sec = input("Masukkan username lagi: ")
    if sec != "Atharafi":
        print("Username salah, silahkan anda lihat pesan dari kami dan masukkan username dan password secara benar.")

elif passwo != "Atharafi26 ":
    print("Wrong password, try to login again. ")

else:
    print("Something wen't wrong")