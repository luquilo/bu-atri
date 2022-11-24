nilai = int(input('masukkan bilangan anda :'))

if int(nilai)%2==0:
    keterangan = 'genap'
else :
    keterangan = 'ganjil'

print('anda memasukkan angka %d, yang merupakan bilangan %s' % (nilai, keterangan))