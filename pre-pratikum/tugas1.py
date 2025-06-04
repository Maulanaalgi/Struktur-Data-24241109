baris = int(input("Masukkan jumlah baris bintang: ")) #Ini adalah sebuah perulangan (loop) yang akan berjalan sebanyak jumlah yang dimasukkan oleh pengguna. Jika pengguna memasukkan 5, maka perulangan ini akan berjalan 5 kali, dengan 'i' mulai dari 0 hingga 4.


for i in range(baris): # Ini adalah sebuah perulangan (loop) yang akan berjalan sebanyak jumlah yang dimasukkan oleh pengguna. Jika pengguna memasukkan 5, maka perulangan ini akan berjalan 5 kali, dengan i mulai dari 0 hingga 4.

    spasi = ' ' * (baris - i - 1) # Di sini, kita menghitung berapa banyak spasi yang perlu ditambahkan di depan bintang. Semakin banyak baris yang kita buat, semakin sedikit spasi yang dibutuhkan. Misalnya, pada baris pertama (i=0), kita butuh 4 spasi, pada baris kedua (i=1) kita butuh 3 spasi, dan seterusnya.
    bintang = '*' * (2 * i + 1) #Di sini, kita menghitung berapa banyak bintang yang akan ditampilkan di setiap baris. Pada baris pertama (i=0), kita akan menampilkan 1 bintang, pada baris kedua (i=1) kita akan menampilkan 3 bintang, dan seterusnya. Rumusnya adalah  2 x i + 1.

    print(spasi + bintang)#Di sini, kita mencetak (menampilkan) spasi dan bintang yang sudah kita hitung sebelumnya. Jadi, setiap baris akan terlihat seperti segitiga yang terbalik, dengan bintang di tengah dan spasi di sebelah kiri.

print(f"berikut hasil dari jumlah bintang : {baris}")#Setelah semua baris bintang ditampilkan, kita mencetak pesan yang memberitahukan berapa banyak baris bintang yang telah dibuat. Misalnya, jika pengguna memasukkan 5, maka akan muncul pesan "berikut hasil dari jumlah bintang : 5".
