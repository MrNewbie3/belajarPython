print("Hello, welcome to our calculator")
while True:
    pas= input("Password: ")
    if pas == "1234":
        print('Pilih jenis kalkulasi: ')
        print("1. Aritmatika")
        print("2. Konversi suhu")
        print("0. Exit")
        while True:
            jen= input("Pilih jenis: ")
            if jen == "0":
                print("Goodbye!")    
                break
        
            elif jen == "1":
                angka = float(input("Masukkan angka pertama: "))    
                angka2 = float(input("Masukkan angka kedua: "))
                
                while True:
                    operasi = input("Masukkan jenis operasi sederhana (+,-,:,x): ")
                    if operasi == "+":
                        penjumlahan = angka + angka2
                        print(f"{angka} + {angka2} = {penjumlahan}")
                        break
            
                    elif operasi =="-":
                        pengurangan = angka - angka2
                        print(f"{angka} - {angka2} = {pengurangan}")
                        break
                    
                    elif operasi ==":":
                        pembagian = angka / angka2
                        print(f"{angka} : {angka2} = {pembagian}")
                        break
            
                    elif operasi == "x":
                        perkalian = angka * angka2
                        print(f"{angka} x {angka2} = {perkalian}")
                        break
                    print("Wrong option")               
                    print("Input option again")
                break
            elif jen == "2":
                print("Pilih suhu awal (C, R, K, F): ")
                while True:
                    pilihan = input("Input here: ")
                    if pilihan == "C":
                        masuk = float(input("Masukkan suhu celcius: "))
                        print("Pilih konversi suhu")
                        print("1. C to R")
                        print("2. C to F")
                        print("3. C to K")  
                        while True:
                            konversi = input("Masukkan disini: ")
                            if konversi == "1" :
                                Reamur = masuk / 5 * 4
                                print(f"{masuk} C = {Reamur} R")
                                break
                            elif konversi == "2":
                                Fahrenheit = masuk / 5 * 9 + 32
                                print(f"{masuk} C = {Fahrenheit} F")
                                break
                            elif konversi == "3":
                                Kelvin = masuk / 5 * 5 + 273
                                print(f"{masuk} C = {Kelvin} K")
                                break
                            print("Wrong option")
                        break

                    elif pilihan == "R":
                        suhu = int(input("Masukkan suhu reamur: "))
                        print("Pilih konversi suhu")
                        print("1. R to C ")
                        print("2. R to F ")
                        print("3. R to K ")
                        while True:
                            Convertion = input("Masukkan disini: ")
                            if Convertion ==  "1":
                                celcius = suhu / 4 * 5
                                print(f"{suhu} R = {celcius} C")
                                break
                            elif Convertion == "2":
                                fahrenheit = suhu / 4 * 9 + 32 
                                print(f"{suhu} R = {fahrenheit} F")
                                break
                            elif Convertion == '3':
                                kelvin = suhu / 4 * 5 + 273 
                                print(f'{suhu} R = {kelvin} K')
                                break
                            print("Wrong option")
                        break

                    elif pilihan == "F":
                        temp = int(input("Masukkan suhu Fahrenheit: "))
                        print("Pilih konversi suhu")
                        print("1. F to C ")
                        print("2. F to R ")
                        print("3. F to K ")
                        while True:
                            ConvertioN = input("Masukkan disini: ")
                            if ConvertioN == "1":
                                celciuS = (temp - 32)/ 9 * 5
                                print(f"{temp} F = {celciuS} C")
                                break
                            elif ConvertioN == "2":
                                reamuR = (temp - 32)/ 9 * 4 
                                print(f"{temp} F = {reamuR} R")
                                break
                            elif ConvertioN == '3':
                                kelviN = (temp - 32) / 9 * 5 + 273 
                                print(f'{temp} F = {kelviN} K')
                                break
                            print("Wrong option")
                        break

                    elif pilihan == "K":
                        Temp = int(input("Masukkan suhu Kelvin: "))
                        print("Pilih konversi suhu")
                        print("1. K to C ")
                        print("2. K to R ")
                        print("3. K to F ")
                        while True:
                            ConVertioN = input("Masukkan disini: ")
                            if ConVertioN ==  "1":
                                CelciuS = (Temp - 273)/ 5 * 5
                                print(f"{Temp} K = {CelciuS} C")
                                break
                            elif ConVertioN == "2":
                                ReamuR = (Temp - 273)/ 5 * 4 
                                print(f"{Temp} K = {ReamuR} F")
                                break
                            elif ConVertioN == '3':
                                FaHrenheit = (Temp - 273) / 5 * 9 + 32 
                                print(f'{Temp} K = {FaHrenheit} R')
                                break
                            print("Wrong option")
                        break
                    print("Wrong option")
                    print("Input option again")
                break
            print("Option doesn't exist")
            
            
        break
    print("Wrong password")
    print("Input password again")