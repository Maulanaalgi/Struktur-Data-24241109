batas = int(input("Masukkan batas deret: "))#Program minta kamu memasukkan angka terakhir dari deret yang ingin dibuat.



for i in range(1, batas + 1, 2):#Program mulai menghitung dari angka 1, lalu lompat 2 angka setiap kali sampai mencapai angka batas.


    print(i, end=', ' if i + 2 <= batas else '\n')#Program menampilkan angka-angka deret yang sudah dihitung, dipisah dengan koma, kecuali angka terakhir yang langsung ganti baris baru.


print(f"berikut hasil dari deret: {batas}")#Setelah selesai, program menampilkan pesan bahwa deret sampai angka yang kamu masukkan sudah selesai dibuat.

