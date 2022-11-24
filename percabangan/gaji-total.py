print('PROGRAM MENGHITUNG GAJI KARYAWAN')

masaKerja = str(input('Masukkan masa kerja (tahun) :'))
gapok = int(input('masukkan gaji pokok :'))

if int(masaKerja)>3:
    tunjangan = 0.25*int(gapok)
else :
    tunjangan = 0.1*int(gapok)

totalGaji = int(gapok)+tunjangan

print("gaji total anda : Rp ", totalGaji)