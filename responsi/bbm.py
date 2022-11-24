print('\n','\tdaftar harga bbm')
print('---------------------------------------------------')

pertalite = int(input('masukkan harga pertalite (perliter) :'))
pertamax = int(input('masukkan harga pertamax (perliter) :'))

print('\n')
print('---------------------------------------------------')
print('pertalite        harga(Rp)      pertamax      harga(Rp)')
print('---------------------------------------------------')

liter = 1
while liter<6:
    rp_pertalite = int(pertalite)  * liter
    rp_pertamax = int(pertamax)  * liter
    print(liter,"liter          ",rp_pertalite,"\t",liter, "liter     ", rp_pertamax)
    liter += 1