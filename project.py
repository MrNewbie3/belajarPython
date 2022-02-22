#project python, ide dari agisna
print("Hello, wellcome to our calculator")
print("Silahkan piliih opsi dibawah ini ")
print("1. Sign in")
print("2. Log in")
print("3. Later ")
while True:
    signin = input("")
    if signin == "1.":
        email = input("Masukkan email : ")
        passw = input("Masukkan Password: ")
        while True:
            pasww2 = input("Repeat Password: ")
            if pasww2 == passw:
                a = "..."
                for i in range(0, 4):
                    print(a)
                         
                    break
            print("Wrong Password")
        
    break




             
