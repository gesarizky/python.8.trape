# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# math module
import math 
# Menginput alas , sisi miring , dan tinggi
alas = float(input('Tulis Alas Trapesium: '))
tinggi = float(input('Tulis Tinggi Trapesium: '))
sisi = float(input('Tulis Sisi Atas Trapesium: '))

# Hitung Luas dan Keliling Trapesium
luas = (alas + sisi) / 2 * tinggi
alassimir = (alas - sisi) / 2
simir = math.sqrt(alassimir ** 2 + tinggi ** 2)
keliling = sisi + alas + simir + simir

#Menampilkan Hasil Perhitungan
print('Luas Trapesium  adalah %0.2f' %luas)
print('Sisi Miring Trapesium  adalah %0.2f' %simir)
print('keliling Trapesium adalah %0.2f' %keliling)
