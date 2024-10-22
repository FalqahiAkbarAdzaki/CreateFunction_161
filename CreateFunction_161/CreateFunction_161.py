import math #library untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r #lambda = berfungsi untuk membuat fungsi anonim

#contoh penggunaannya
jari_jari =7# untuk menentukan nilai jari-jari sebuah lingkaran
area = luas_lingkaran(jari_jari) #area=variabel yang menyimpan hitungan luas lingkaran
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")#mencetak hasil akhir dari hitungan
