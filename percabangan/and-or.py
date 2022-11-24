print('\n')
print('\n')

print('Program Yudisium')
print('-----------------\n')

ipk = float((input('Masukkan IPK :')))
lamaKuliah = float(input('Masukkan lama kuliah :'))
print('\n')

if float(ipk) >= 3.5 and float(lamaKuliah) <= 4:
    keterangan = 'cumlaude'
else :
    keterangan = 'tidak cumlaude'

print(keterangan)
print('\n')