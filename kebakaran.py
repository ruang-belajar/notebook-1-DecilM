# PERSIAPAN DATA

import pandas as pd

# download file contoh csv
df = pd.read_csv("data-kebakaran.csv")  # Replace with the actual filename
df.head()

# 1. Filter data laporan kebakaran yang sumber informasinya dari Masyarakat
filtered_data_1 = df[df['sumber_info'] == 'Masyarakat']
print("1. Filter data laporan kebakaran yang sumber informasinya dari Masyarakat:")
print(filtered_data_1)
print()

# 2. Filter data laporan kebakaran yang sumber informasinya dari Masyarakat di bulan Februari
filtered_data_2 = df[(df['sumber_info'] == 'Masyarakat') & (df['bulan'] == 2)]
print("2. Filter data laporan kebakaran yang sumber informasinya dari Masyarakat di bulan Februari:")
print(filtered_data_2)
print()

# 3. Filter data laporan kebakaran dengan nilai kerugian lebih dari 100juta
filtered_data_3 = df[df['kerugian'] > 100000000]
print("3. Filter data laporan kebakaran dengan nilai kerugian lebih dari 100juta:")
print(filtered_data_3)
print()

# 4. Filter data laporan kebakaran selama semester 2 tahun 2022
filtered_data_4 = df[(df['tanggal'] > 6)]
print("4. Filter data laporan kebakaran selama semester 2 tahun 2022:")
print(filtered_data_4)
print()

# 5. Filter data laporan kebakaran selama dari Maret sampai Juli 2022
filtered_data_5 = df[(df['bulan'].between(3, 7))]
print("5. Filter data laporan kebakaran selama dari Maret sampai Juli 2022:")
print(filtered_data_5)
print()

# 6. Filter data laporan kebakaran selama dari Maret sampai Juli 2022
filtered_data_6 = df[(df['bulan'].between(3, 7))]
print("6. Filter data laporan kebakaran selama dari Maret sampai Juli 2022:")
print(filtered_data_6)
print()

# 7. Filter data laporan kebakaran Rumah Tinggal yang disebabkan oleh Listrik
filtered_data_7 = df[(df['objek_awal'] == 'Rumah Tinggal') & (df['penyebab'] == 'Listrik')]
print("7. Filter data laporan kebakaran Rumah Tinggal yang disebabkan oleh Listrik:")
print(filtered_data_7)



