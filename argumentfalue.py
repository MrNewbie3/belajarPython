#argument default value


#Value kedua tidak boleh kosong supaya tidak error
def nama_orang(firstname= "Anda", lastname="" ):
   print(f"Hello {firstname}: {lastname}")


nama_orang("Alka")
#ini supaya tidak terjadi error dengan code def tsb..
nama_orang(lastname="Adriano") 