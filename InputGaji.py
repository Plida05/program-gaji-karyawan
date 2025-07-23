# Array Gaji berdasarkan golongan
gaji = [5000000, 6500000, 9500000]

# Array persen lembur (dalam persen)
lembur_persen = [30, 32, 34, 36, 38]

# Input dari user
golongan = input("Masukkan Golongan (A/B/C): ").upper()
jam_lembur = int(input("Masukkan Jam Lembur: "))

# Inisialisasi variabel
index_gaji = -1

# Tentukan index gaji berdasarkan golongan
if golongan == 'A':
    index_gaji = 0
elif golongan == 'B':
    index_gaji = 1
elif golongan == 'C':
    index_gaji = 2
else:
    print("Golongan tidak valid.")
    exit()

# Ambil gaji pokok
gaji_pokok = gaji[index_gaji]

# Hitung persen lembur berdasarkan jam lembur
if jam_lembur == 1:
    persen = lembur_persen[0]
elif jam_lembur == 2:
    persen = lembur_persen[1]
elif jam_lembur == 3:
    persen = lembur_persen[2]
elif jam_lembur == 4:
    persen = lembur_persen[3]
elif jam_lembur >= 5:
    persen = lembur_persen[4]
else:
    persen = 0

# Hitung gaji lembur
gaji_lembur = (persen / 100) * gaji_pokok

# Hitung total penghasilan
total_penghasilan = gaji_pokok + gaji_lembur

# Tampilkan hasil
print("==================================")
print(f"Golongan        : {golongan}")
print(f"Gaji Pokok      : Rp{gaji_pokok:,.0f}")
print(f"Gaji Lembur     : Rp{gaji_lembur:,.0f}")
print(f"Total Gaji      : Rp{total_penghasilan:,.0f}")
print("==================================")