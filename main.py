from persegi_panjang import PersegiPanjang
from segitiga import Segitiga

print('Menggunakan OOP')

p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(4, 2)
print(s1.info())
print(s1.luas_segitiga())