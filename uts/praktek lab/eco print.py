print('\t\t Eco Print Boutiq')
print('\t Jl. Mahameru 18 Surakarta')
print('-----------------------------------------------\n')

ukuran_s = 50000
ukuran_m = 75000
ukkuran_l = 90000


ukuran_baju = str(input('Masukkan Ukuran Baju (s-l) \t:'))
jumlah_beli = int(input('Masukkan Jumlah Beli \t\t:'))



if(ukuran_baju)=='s':
    harga_satuan = ukuran_s
elif(ukuran_baju)=='m':
    harga_satuan = ukuran_m
elif(ukuran_baju)=='l':
    harga_satuan = ukkuran_l
else:
    print('mohon maaf! ukuran yang anda masukkan tidak terdaftar!')
    
print('Harga Satuan\t\t\t:Rp', harga_satuan)
print('------------------------------------------------\n')


harga_total = harga_satuan * jumlah_beli

if(harga_total)>1000000:
    harga_diskon = harga_total * 0.1
    total_harga = harga_total * 0.9
else:
    harga_diskon = 0
    total_harga = harga_total


print('Harga Total\t\t\t:Rp', harga_total)
print('Mendapat Diskon 10%\t\t:Rp',harga_diskon)
print('Total Harga\t\t\t:Rp', total_harga)

print('--------------------------------------------------')


jumlah_uang_pembeli = int(input('Jumlah Uang dibayar\t\t:Rp '))
uang_kembalian = jumlah_uang_pembeli - total_harga
print('Uang Kembalian\t\t\t:Rp', uang_kembalian)

