# Program Antrian Nama Pelanggan
# Struktur Data: Queue (FIFO)

from collections import deque

# Membuat antrian kosong
antrian = deque()

# Input jumlah pelanggan
jumlah = int(input("Masukkan jumlah pelanggan: "))

# Input nama pelanggan
for i in range(jumlah):
    nama = input("Masukkan nama pelanggan: ")
    antrian.append(nama)

# Menampilkan daftar antrian awal
print("\n=== Cetak Antrian ===")
for i, nama in enumerate(antrian, start=1):
    print(f"{i}. {nama}")
print("=====================\n")

# Melayani pelanggan satu per satu
while antrian:
    pelanggan = antrian.popleft()
    print(f"Sedang disiapkan : {pelanggan}")
    print("---------------------------")

    # Menampilkan sisa antrian
    if antrian:
        print("=== Cetak Antrian ===")
        for i, nama in enumerate(antrian, start=1):
            print(f"{i}. {nama}")
        print("=====================\n")
    else:
        print("=== Cetak Antrian ===")
        print("(Tidak ada antrian tersisa)")
        print("=====================\n")