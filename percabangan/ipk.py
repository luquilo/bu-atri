nama = str(input('masukkan nama anda :'))
ipk = int(input('masukkan ipk anda (0 - 4):'))

if int(ipk)>=3:
    keterangan = "berhak mendapatkan beasiswa"
else :
    keterangan = "tidak mendapatkan beasiswa"

print('mahasiswa atas nama', nama, ', dinyatakan ', keterangan)