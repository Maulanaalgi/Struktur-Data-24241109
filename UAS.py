# Program Rekapitulasi Data Customer dan Belanja
# Dictionary untuk menyimpan data
data_customer = {}

# Input jumlah customer
jumlah_customer = int(input("Masukkan jumlah customer: "))

for i in range(jumlah_customer):
    print(f"\nCustomer ke-{i+1}")
    
    # Input nama customer
    nama_customer = input("Masukkan Nama Customer: ")
    
    # Input ID customer (validasi angka)
    while True:
        id_customer = input("Masukkan ID Customer: ")
        if id_customer.isdigit():
            break
        else:
            print(" ❌ ID customer harus berupa angka!")
    
    # Input tanggal belanja
    tanggal_belanja = input("Masukkan tanggal belanja (YYYY-MM-DD): ")
    
    # Input daftar belanja
    jumlah_belanja = int(input("Masukkan jumlah item belanja: "))
    daftar_belanja = []
    
    for j in range(jumlah_belanja):
        nama_barang = input(f"Nama Barang ke-{j+1}: ")
        
        # Validasi harga barang harus float
        while True:
            try:
                harga = float(input(f"Harga Barang '{nama_barang}': "))
                break
            except ValueError:
                print(" ❌ Harga harus berupa angka (misal: 10000 atau 7500.5)!")
        
        # Validasi jumlah barang harus integer
        while True:
            try:
                jumlah = int(input(f"Jumlah Barang '{nama_barang}': "))
                break
            except ValueError:
                print(" ❌ Jumlah harus berupa angka!")
        
        daftar_belanja.append((nama_barang, harga, jumlah))
    
    # Hitung total bayar
    total_bayar = sum(harga * jumlah for nama_barang, harga, jumlah in daftar_belanja)
    
    # Simpan ke dictionary sesuai struktur
    data_customer[id_customer] = {
        'nama': nama_customer,
        'tanggal_belanja': tanggal_belanja,
        'belanja': daftar_belanja,
        'total_bayar': total_bayar
    }

# Menampilkan semua data
print("\n=== Rekap Data Customer dan Belanja ===")
for id_customer, info in data_customer.items():
    print(f"\nID Customer : {id_customer}")
    print(f"Nama Customer : {info['nama']}")
    print(f"Tanggal Belanja : {info['tanggal_belanja']}")
    print("Daftar Belanja:")
    for barang, harga, jumlah in info['belanja']:
        print(f" - {barang}: {jumlah} x Rp{harga:.2f} = Rp{harga * jumlah:.2f}")
    print(f"Total Bayar: Rp{info['total_bayar']:.2f}")