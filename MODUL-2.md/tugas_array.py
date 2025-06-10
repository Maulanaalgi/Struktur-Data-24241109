# Percobaan 1 : Array
# Praktek 1 : Membuat array
# impor library numpy
import numpy as np

# Cara Membuat Array dengan NumPy
# impor library numpy
import numpy as np

# membuat array dengan numpy
arr1 = np.array([1, 2, 3])           # 1D array
arr2 = np.array([[1, 2], [3, 4]])    # 2D array (matriks)

# Praktek 1 :
# impor library numpy
import numpy as np

# membuat array dengan numpy
nilai_siswa = np.array([85, 55, 40, 90])

# akses data pada array
print(nilai_siswa[3])

# Operasi Dasar Array
# Operasi paling dasar pada array yang wajib dipahami adalah bagaimana cara mengakses array, mengubah nilai pada elemen tertentu, dan mendapatkan informasi ukuran dan dimensi dari array.
# Praktek 2 :
# impor libaray numpy
import numpy as np

# membuat array dengan numpy
nilai_siswa_1 = np.array([75, 65, 45, 80])
nilai_siswa_2 = np.array([[85, 55, 40], [50, 40, 99]])

# cara akses elemen array
print(nilai_siswa_1[0])
print(nilai_siswa_2[1][1])

# mengubah nilai elemen array
nilai_siswa_1[0] = 88
nilai_siswa_2[1][1] = 70

# cek perubahannya dengan akses elemen array
print(nilai_siswa_1[0])
print(nilai_siswa_2[1][1])

# Cek ukuran dan dimensi array
print("Ukuran Array : ", nilai_siswa_1.shape)
print("Ukuran Array : ", nilai_siswa_2.shape)
print("Dimensi Array : ", nilai_siswa_2.ndim)

# Operasi Artimatika
# Sebagaimana tipe data yang lainnya array juga memiliki operasi artimatika, artinya kita dapat melakukan manipulasi terhadap nilai array dengan memanfaatkan operasi aritmatika seperti penjumlahan dan lainnya.
# Praktek 3 :
# impor library numpy
import numpy as np

# membuat array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# menggunakan operasi penjumlahan pada 2 array
print(a + b)       # array([5, 7, 9])

# Indexing dan Slicing pada Array
arr = np.array([10, 20, 30, 40])
print(arr[1:3])    # array([20, 30])


# iterasi pada array
for x in arr:
    print(x)

# Traversal
# Pada array mengunjungi satu per satu elemen array dari elemen pada indeks pertama sampai terakhir, disebut sebagai Traversal.
arr_1 = [10, 20, 30, 40, 50]
print(arr_1)

# Linear Traversal
# Proses mengunjungi setiap elemen array secara berurutan, dimulai dari elemen pertama dan berlanjut ke elemen terakhir.
# Praktek 4
# membuat array
arr = [1, 2, 3, 4, 5]

# Linear Traversal ke tiap elemen arr
print("Linear Traversal: ", end=" ")
for i in arr:
    print(i, end=" ")
print()

# Reverse Traversal
# Proses mengunjungi setiap elemen array mulai dari elemen terakhir dan bergerak menuju elemen pertama.
# Praktek 5
# membuat array
arr = [1, 2, 3, 4, 5]

# Reverse Traversal dari elemen akhir 
print("Reverse Traversal: ", end="")
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
print()

# traversal menggunakan metode perulangan while
# Praktek 7
# membuat array
arr = [1, 2, 3, 4, 5]

# mendeklarasikan nilai awal
n = len(arr)
i = 0

print("Linear Traversal using while loop: ", end=" ")
# Linear Traversal dengan while
while i < n:
    print(arr[i], end=" ")
    i += 1
print()

# Praktek 8
# membuat array
arr = [1, 2, 3, 4, 5]

# mendeklarasikan nilai awal
start = 0
end = len(arr) - 1

print("Reverse Traversal using while loop: ", end=" ")
# Reverse Traversal dengan while
while start < end:
    
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)

# Insertion
# Insertion atau Penyisipan dalam array melibatkan penempatan elemen pada indeks tertentu sambil menggeser elemen yang ada sesuai dengan itu.
# Mari kita implementasikan penyisipan array pada akhir elemen menggunakan .append() atau fungsi yang di gunakan untuk menambahkan satu elemen ke akhir ke sebuah daftar list yang sudah ada melalui code python berikut ini :
# Praktek 9
# membuat array
arr = [12, 16, 20, 40, 50, 70]

# cetak arr sebelum penyisipan
print("Array Sebelum Insertion : ", arr)

# cetak panjang array sebelum penyisipan
print("Panjang Array : ", len(arr))

# menyisipkan array di akhir elemen menggunakan .append()
arr.append(26)

# cetak arr setelah penyisipan
print("Array Setelah Insertion : ", arr)

# cetak panjang array setelah penyisipan
print("Panjang Array : ", len(arr))

# Insertion Pada Tengah Elemen Array
# Operasi penyisipan ke dalam array pada posisi mana pun (ditengah, bukan awal atau akhir elemen) dapat dilakukan dengan menggeser elemen ke kanan, yang berada di sisi kanan posisi yang diperlukan.
# Sekarang coba kita implementasikan pada code python menggunakan .insert(pos, x) atau metode yang di gunakan untuk menyisipkan sebuah elemen ke posisi tertentu, berikut ini
# Praktek 10
# membuat array
arr = [12, 16, 20, 40, 50, 70]

# cetak arr sebelum penyisipan
print("Array Sebelum Insertion : ", arr)

# cetak panjang array sebelum penyisipan
print("Panjang Array : ", len(arr))

# menyisipkan array pada tengah elemen menggunakan .insert(pos, x)
arr.insert(4, 5)

# cetak arr setelah penyisipan
print("Array Setelah Insertion : ", arr)

# cetak panjang array setelah penyisipan
print("Panjang Array : ", len(arr))

# Deletion (Penghapusan)
# Dalam Python elemen dalam array/list tidak hanya bisa disisipkan tetapi juga dapat dihapus. Terdapat tiga cara untuk menghapus elemen dari array/list, yaitu :
# remove(), menghapus elemen array yang pertama kali muncul
# pop(), menghapus elemen array pada indeks yang spesifik atau bisa juga menghapus elemen terakhir dari array jika indeksnya tidak spesifik ditentukan
# del_statement, menghapus elemen array pada indeks yang spesifik
# Praktek 11
# membuat array
a = [10, 20, 30, 40, 50]
print("Array Sebelum Deletion : ", a)

# menghapus elemen array pertama yang nilainya 30
a.remove(30)  
print("Setelah remove(30):", a)

# menghapus elemen array pada index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("Setelah pop(1):", a) 

# Menghapus elemen pertama (10)
del a[0]  
print("Setelah del a[0]:", a)