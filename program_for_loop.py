print("Silahkan masukkan jumlah data yang akan diinput ")
data = int(input("Masukkan jumlah data : "))
nama = []
usia = []

for i in range(0, data):
    print("Data ke 1")
    nama_masuk= input("Masukkan nama: ")
    usia_masuk= int(input("Masukkan usia: "))

    nama.append(nama_masuk)
    usia.append(usia_masuk)

for a in range(0, len(nama)):
    inptp = nama[a]
    inpt = usia[a]
    print(f"Hallo {inptp} usia anda sekarang {inpt}")