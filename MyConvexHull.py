'''
Nama : Febryola Kurnia Putri
NIM  : 13520140
Kelas: K02
'''

import numpy as np
from Function import *

#Fungsi utama convexhull
'''
Fungsi ini berfungsi sebagai fungsi utama yang akan membentuk
titik-titik mana saja yang merupakan titik terluar dari convechull yang ada
Fungsi ini menerima 1 parameter yaitu
berupa bucket yang merupakan kumpulan dari array of titik convexhull yang diuji
'''
def MyConvexHull(bucket):
    #divide kumpulan titik menjadi bagian kanan dan kiri
    left_bucket = []        #bagian kiri
    right_bucket = []       #bagian kanan

    #Mendaftarkan titik-titik pada array bucket
    bucket_true = np.array(bucket).astype(float)

    #mencari titik p1 dan pn yang merupakan titik terluar pada bucket
    p1, pn = statusIndexOfX(bucket_true)

    #perulangan untuk mengecek posisi titik sebanyak array bucket
    for i in range(len(bucket_true)):
        #jika titik di kiri dan titik tersebut bukan pada p1 dan pn maka tambahkan pada array left_bucket
        if CheckPointPosition(p1, pn, i, bucket_true) > 0 and i != p1 and i != pn:
            left_bucket.append(i)
        #jika titik tersebut di kanan dan bukan merupakan titik p1 dan pn maka tambahkan pada right_bucket
        elif CheckPointPosition(p1, pn, i, bucket_true) < 0 and i != p1 and i != pn:
            right_bucket.append(i)

    #memanggil fungsi rekursif untuk mendapatkan titik-tik yang sesuai pada bucket
    #sesuai dengan partisinya yang sudah dilakukan
    left = funcRecursive(p1,pn, bucket_true,left_bucket)
    right = funcRecursive(pn,p1, bucket_true,right_bucket)

    #Mengembalikan kombinasi antara partisi yang sudah dilakukan sebelumnya berupa 
    #array dari bucket yang bernilai true
    return left+right

