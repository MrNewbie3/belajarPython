#belajar dictionary

customer = {"Nama":"Atharafi", "Alamat":"Malang", "Usia":12}
name = customer["Nama"]
addres = customer["Alamat"]
age = customer["Usia"]

for key, value in customer.items():
    print(f'{key}:{value}')
