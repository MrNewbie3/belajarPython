#Oke kita kali ini akan ke if statement
#Ini dia rumus untuk if


#if harus disertai tab terlebih dahulu supaya komputer bisa membaca command

People = int(input("Input angka: "))


for people in range(1,100000000000001):
    if people % 2 == 0:
        print("Hmmm......")
        if people % 3 == 0:
            print("Yaa bro")
            if people % 5 == 0:
                print("Salah Bro")
                if people % 10 == 0:
                    print("Wrong pass") 