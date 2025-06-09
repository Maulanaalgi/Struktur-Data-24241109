# Variabel global untuk menyimpan data mahasiswa
mahasiswa = []# Ini adalah tempat untuk menyimpan nama-nama mahasiswa. Kita mulai dengan daftar kosong.



# Fungsi Create
def tambah_mahasiswa(): #Ini adalah fungsi untuk menambahkan mahasiswa baru ke dalam daftar.


    nama = input("Masukkan nama mahasiswa: ") #Program meminta pengguna untuk memasukkan nama mahasiswa yang ingin ditambahkan.


    mahasiswa.append(nama) #Nama yang dimasukkan akan ditambahkan ke dalam daftar mahasiswa.


    print(f"Mahasiswa '{nama}' berhasil ditambahkan.") #Program memberi tahu bahwa mahasiswa baru sudah berhasil ditambahkan.



# Fungsi Read
def tampilkan_mahasiswa(): #Ini adalah awal dari fungsi yang bernama 'tampilkan_mahasiswa'. Fungsi ini digunakan untuk menampilkan daftar mahasiswa.


    if not mahasiswa: #Di sini, kita memeriksa apakah daftar mahasiswa kosong. Jika kosong, maka kita akan menampilkan pesan bahwa belum ada data mahasiswa.

        print("Belum ada data mahasiswa.") #Jika daftar mahasiswa kosong, program akan mencetak pesan ini.

    else:
        print("Daftar Mahasiswa:") #Jika ada mahasiswa, program akan mencetak "Daftar Mahasiswa:".
        for i, nama in enumerate(mahasiswa): #Di sini, kita menggunakan perulangan untuk menampilkan setiap nama mahasiswa. 'enumerate' membantu kita mendapatkan nomor urut (indeks) dan nama mahasiswa.
            print(f"[{i}] {nama}") #Ini mencetak nama mahasiswa dengan nomor urut di depannya.

# Fungsi Update
def ubah_mahasiswa(): #Ini adalah fungsi untuk mengubah nama mahasiswa yang sudah ada.
    tampilkan_mahasiswa() #Pertama, kita tampilkan daftar mahasiswa agar pengguna tahu siapa yang bisa diubah.

    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin diubah: ")) #Kita meminta pengguna untuk memasukkan nomor urut mahasiswa yang ingin diubah. Kita juga menggunakan 'try' untuk menangkap kesalahan jika input bukan angka.

        if 0 <= indeks < len(mahasiswa): #Kita meminta pengguna untuk memasukkan nomor urut mahasiswa yang ingin diubah. Kita juga menggunakan try untuk menangkap kesalahan jika input bukan angka.

            nama_baru = input("Masukkan nama baru: ") #Jika indeks valid, kita meminta pengguna untuk memasukkan nama baru.

            mahasiswa[indeks] = nama_baru #Nama mahasiswa diubah menjadi nama baru yang dimasukkan.

            print("Data mahasiswa berhasil diperbarui.") #Program memberi tahu bahwa data mahasiswa berhasil diperbarui.
        else:
            print("Indeks tidak valid.") #Jika indeks tidak valid, program akan memberi tahu pengguna.

    except ValueError:
        print("Input harus berupa angka.") #Jika indeks tidak valid, program akan memberi tahu pengguna.


# Fungsi Delete
def hapus_mahasiswa(): #Jika indeks tidak valid, program akan memberi tahu pengguna.

    tampilkan_mahasiswa() #Kita tampilkan daftar mahasiswa terlebih dahulu.
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin dihapus: ")) #Kita meminta pengguna untuk memasukkan indeks mahasiswa yang ingin dihapus.

        if 0 <= indeks < len(mahasiswa): #Kita memeriksa apakah indeks yang dimasukkan valid.
            nama = mahasiswa.pop(indeks) #Jika valid, mahasiswa dihapus dari daftar menggunakan 'pop()'.
            print(f"Mahasiswa '{nama}' berhasil dihapus.") #Program memberi tahu bahwa mahasiswa berhasil dihapus.
        else:
            print("Indeks tidak valid.") #Jika indeks tidak valid, program akan memberi tahu pengguna.

    except ValueError:
        print("Input harus berupa angka.") #Jika input bukan angka, program akan memberi tahu bahwa input harus berupa angka.

# Fungsi Menu
def tampilkan_menu(): #Di sini kita membuat sebuah fungsi yang bernama 'tampilkan_menu'. Fungsi adalah sekumpulan perintah yang bisa kita panggil untuk melakukan tugas tertentu.
    print("\n--- MENU MANAJEMEN MAHASISWA ---") #Baris ini akan mencetak (menampilkan) judul menu di layar. Tanda '\n' di depan membuat ada jarak baru sebelum judul muncul.

    print("[1] Tampilkan Mahasiswa") #Di sini, kita menampilkan beberapa pilihan yang bisa dipilih oleh pengguna. Setiap pilihan memiliki nomor dan deskripsi.

    print("[2] Tambah Mahasiswa")
    print("[3] Ubah Mahasiswa")
    print("[4] Hapus Mahasiswa")
    print("[5] Keluar") #Di sini, kita menampilkan beberapa pilihan yang bisa dipilih oleh pengguna. Setiap pilihan memiliki nomor dan deskripsi.


# Main Loop
def main(): #Kita membuat fungsi lain yang bernama 'main'. Ini adalah fungsi utama yang akan menjalankan program.

    while True: #'while' True: berarti kita akan terus menjalankan perintah di dalamnya tanpa henti sampai kita menghentikannya secara manual.
 
        tampilkan_menu() #Di sini, kita memanggil fungsi 'tampilkan_menu()' untuk menampilkan menu pilihan kepada pengguna.

        try:
            pilihan = int(input("Pilih menu: ")) #Kita meminta pengguna untuk memilih menu dengan mengetikkan angka. 'int()' digunakan untuk mengubah input menjadi angka bulat.

            if pilihan == 1: #Di sini, kita memeriksa pilihan yang dimasukkan oleh pengguna:                                 
                tampilkan_mahasiswa() #Jika pengguna memilih 1, maka fungsi 'tampilkan_mahasiswa()' akan dipanggil untuk menampilkan daftar mahasiswa.
            elif pilihan == 2:
                tambah_mahasiswa() #Jika memilih 2, maka 'tambah_mahasiswa()' akan dipanggil untuk menambah mahasiswa baru.
            elif pilihan == 3:
                ubah_mahasiswa() #Jika memilih 3, maka 'ubah_mahasiswa()' akan dipanggil untuk mengubah data mahasiswa.
            elif pilihan == 4:
                hapus_mahasiswa() #Jika memilih 4, maka 'hapus_mahasiswa()' akan dipanggil untuk menghapus mahasiswa.
            elif pilihan == 5:
                print("Terima kasih, program selesai.") #Jika memilih 5, program akan menampilkan pesan terima kasih dan keluar.
                exit()
            else:
                print("Pilihan tidak valid.") #Jika pilihan tidak valid (tidak ada dalam daftar), program akan memberi tahu bahwa pilihan tidak valid.
        except ValueError:  
            print("Masukkan angka saja!") #Jika pengguna tidak memasukkan angka (misalnya, huruf), program akan menangkap kesalahan ini dan menampilkan pesan bahwa hanya angka yang boleh dimasukkan.

# Jalankan program
main() #Terakhir, kita memanggil fungsi 'main()' untuk menjalankan seluruh program.
