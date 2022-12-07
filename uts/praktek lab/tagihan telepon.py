print('\nPROGRAM MENGHITUNG TAGIHAN TELEPON')
print('------------------------------------------\n')


print('DATA PELANGGAN')
nama276 = input('Nama Pelanggan\t\t: ')
percakapan = int(input('percakapan (menit)\t: '))
sms = int(input('SMS berapa kali\t\t: '))

abonemen = 28000
biaya_percakapan = 2000 * percakapan
biaya_sms = 350 * sms
total_tagihan = abonemen + biaya_percakapan + biaya_sms


print('\nTAGIHAN')
print('Abonemen \t\t: Rp',abonemen)
print('Biaya percakapan \t: Rp',biaya_percakapan)
print('Biaya SMS \t\t: Rp', biaya_sms)
print('Total tagihan \t\t: Rp', total_tagihan)
