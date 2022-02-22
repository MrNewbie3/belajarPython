#Module adalah program untuk menyatukan beberapa file, module bisa digunakan di file lain.

import hello_world

hasil = hello_world.angk(1,2,3,4,5,6)
print(hasil)
halo = hello_world.halo("My work")
print(halo)

#itu jika ingin mengimport semua program

#ini jika ingin mengimport salah satu program saja
from hello_world import angk

total = angk(12,12,12,12,12)        #jika sudah memakai from .... import .... pada saat memakai variable tidak perlu menambah nama file.
print(total)