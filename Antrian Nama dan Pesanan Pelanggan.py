from collections import deque

# Membuat antrian kosong
antrian = deque()

# Input jumlah pelanggan
jumlah = int(input("Masukkan jumlah pelanggan: "))

# Input nama dan pesanan tiap pelanggan
for i in range(jumlah):
    print(f"\nPelanggan ke-{i+1}")
    nama = input("Nama pelanggan: ")
    pesanan = input("Pesanan: ")
    antrian.append((nama, pesanan))   # menyimpan tuple (nama, pesanan)

# Menampilkan daftar antrian awal (nomor. nama - pesanan)
print("\n=== Cetak Antrian ===")
for i, (nama, pesanan) in enumerate(antrian, start=1):
    print(f"{i}. {nama} - {pesanan}")
print("=====================\n")

# Proses melayani pelanggan satu per satu
while antrian:
    nama, pesanan = antrian.popleft()
    print(f"Sedang disiapkan : {nama}")
    print(f"Pesanannya       : {pesanan}")
    print("---------------------------")

    # Menampilkan sisa antrian
    if antrian:
        print("=== Cetak Antrian ===")
        for i, (n, p) in enumerate(antrian, start=1):
            print(f"{i}. {n} - {p}")
        print("=====================\n")
    else:
        print("=== Cetak Antrian ===")
        print("(Tidak ada antrian tersisa)")
        print("=====================\n")