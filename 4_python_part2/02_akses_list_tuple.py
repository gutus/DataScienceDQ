bulan_pembelian = ("Januari", "Februari", "Maret", "April", "Mei", "Juni",
                   "Juli", "Agustus", "September", "Oktober", "November", "Desember")
# akses dari bulan ke 5 hingga bulan 7
pertengahan_tahun = bulan_pembelian[4:8]
print(pertengahan_tahun)
awal_tahun = bulan_pembelian[:5]  # dari awal tahun hingga bulan ke 6
print(awal_tahun)
akhir_tahun = bulan_pembelian[8:]  # dari bulan ke 8 hingga akhir
print(akhir_tahun)
# dari bulan ke 4 dari akhir hingga 1 bulan sebelum terakhir
print(bulan_pembelian[-4:-1])
