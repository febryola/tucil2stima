'''
Nama : Febryola Kurnia Putri
NIM  : 13520140
Kelas: K02
'''

# Fungsi-Fungsi Dasar Pembentuk Fungsi ConvexHull

# import library untuk mengkomputasikan array 2 dimensi pada program
import numpy as np

'''
Fungsi ini akan mereturn determinan dari kumpulan titik
yang dimasukkan yaitu ada 3 titik dan berada dalam array buc
'''
def determinan(p1, pn, cek, bucket):
    # Menginisialisasikan semua elemen dari titik-titiknya
    x1 = bucket[p1][0]
    y1 = bucket[p1][1]
    x2 = bucket[pn][0]
    y2 = bucket[pn][1]
    x3 = bucket[cek][0]
    y3 = bucket[cek][1]
    #Mengembalikan determinan dari kumpulan titik p1,pn,dan cek
    return x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3

'''
Fungsi untuk mengecek apakah sebuah titik berada pada bagian 
kiri(atas) atau kanan(bawah) dari garis. Garis ini merupakan
perpanjangan dari titik terluar pada kumpulan titik, yaitu titik p1 dan pn.
Cara menentukannya adalah untuk titik yang berada di sebelah kiri (atas)
maka akan dihasilkan determinan yang positif, titik yang akan diperiksa
adalah titik cek dengan koordinat (x3,y3)

Fungsi ini akan mengembalikan determinan dari kumpulan titik-titik
p1,pn,dan cek
'''
def CheckPointPosition(p1, pn, cek, bucket):
    #posisi dicari dengan menggunakan determinan
    #jika dia > 0 atau positif maka berada di sebelah kiri
    #jika dia <= 0 maka berada di sebelah kanan
    #akan mereturn hasil dari determinan dari kumpulan titik yang ada
    return determinan(p1, pn, cek, bucket)

'''
Fungsi ini berfungsi untuk mencari indeks dari titik koordinat pada bucket(array)
yang memiliki nilai x yang minimal atau pun maksimal. Langkah-langkah:
dijelaskan dalam setiap line berikut
'''
def statusIndexOfX(bucket):
    valueOfX = []                     #pertama nilai x diinisialisasi sebagai suatu array kosong
    for i in range(len(bucket)):      #mengecek untuk setiap titik pada bucket
        valueOfX.append(bucket[i][0]) #menambahkan nilai x ke bucket sebanyak elemen yang terdapat pada bucket
    maxOfX = max(valueOfX)            #nilai maksimum x dengan rumus max(valueOfX)
    minOfX = min(valueOfX)            #nilai minimum x dengan rumus min(valueOfX)

    # Masuk ke pengecekan
    found = True                     #pertama boolean found diinisialisasi dengan true
    indexMaxOfBucket = 0              #indek maksimum dari bucket diinisialisasi dengan 0
    #melakukan pengecekan untuk semua bucket
    #jika bucket pada indeks ke 0 sama dengan nilai maksimum, maka found=False
    #lanjutkan pencarian sampai indeks terakhir dari bucket
    while (indexMaxOfBucket < len(bucket) and found):
        if bucket[indexMaxOfBucket][0] == maxOfX:
            found = False
        else:
            indexMaxOfBucket += 1

    # Masuk ke pengecekan
    found = True                      #pertama boolean found diinisialisasi dengan true
    indexMinOfBucket = 0               #indek minimum dari bucket diinisialisasi dengan 0
    #melakukan pengecekan untuk semua bucket
    #jika bucket pada indeks ke 0 sama dengan nilai minimum, maka found=False
    #lanjutkan pencarian sampai indeks terakhir dari bucket
    while (indexMinOfBucket < len(bucket) and found):
        if bucket[indexMinOfBucket][0] == minOfX:
            found = False
        else:
             indexMinOfBucket += 1

    #mengembalikan indeks minimum dan indeks maksimum dari bucket
    return (indexMinOfBucket, indexMaxOfBucket)

'''
Fungsi ini bertujuan untuk melakukan partisi dari segitiga dengan cara menentukan
nilai sudut dari segitiga ABC misalnya yaitu titik tengah yang dibentuk dari segitiga tersebut
(intinya mencari sudut yang terapitnya)
'''
def triangle_partition(bug1, bug2, bug3):
    diffOfBug1dan2 = bug1 - bug2 #beda jarak antara titik bug2 dan bug1
    diffOfBug2dan3 = bug3 - bug2 #beda jarak antara titik bug3 dan bug2
    #mencari dot product antara vektor diffOfBug1dan2 dan diffOfBug2dan3
    product1 = np.dot(diffOfBug1dan2, diffOfBug2dan3)
    #mengkalkulasikan vektor normalnya
    product2 = np.linalg.norm(diffOfBug1dan2)*np.linalg.norm(diffOfBug2dan3)
    #mencari nilai kosinusnya
    cosinusValue = product1/product2
    #mencari sudut dari bug2
    degreeOfBucket = np.degrees(np.arccos(cosinusValue))
    #mengembalikan besar sudut terapit dari partisi segitiga tersebut
    return degreeOfBucket

'''
Fungsi yang secara rekursif digunakan pada pemanggilan fungsi
convexhull nantinya. Fungsi ini menerima 4 parameter, yaitu
1. p1 = titik terjauh 1
2. pn = titik terjauh 2
3. bucket_true = titik yang berada pada convexhull
4. bucket = semua titik pada bucket
'''
def funcRecursive(p1, pn, bucket_true, bucket):
    if len(bucket)!=0:
        temp = []       #ditampung dulu titik sementara dengan inisialisasi kosong
        #perulangan untuk mengecek semua titik pada bucket
        for i in range(len(bucket)):
            #Pengecekan apakah p1,pn,dan nilai titik ke i pada bucket berbeda
            if p1 != pn and p1 != bucket[i] and pn != bucket[i]:
                #jika berbeda maka lakukan pengecekan sudut dengan menggunakan fungsi triange_partition
                degreeOfTemp = triangle_partition(bucket_true[pn], bucket_true[p1], bucket_true[bucket[i]])
            else:
                #jika semua posisinya sama maka sudut yang terbentuk dari partisi segitiganya adalah 0
                degreeOfTemp = 0
            #menambahkan sudut temp tadi ke array temp
            temp.append(degreeOfTemp)
        #titik px diinialisasi dengan bucket pada index ke max dari array temp
        px = bucket[temp.index(max(temp))]

        #pengecekan devide and conquernya dengan rekursif
        #array titik pada garis px dan pn diinisialisasi dengan kosong
        pointOfPxPn = []
        #melakukan pengecekan sebanyak titik pada bucket
        for i in range(len(bucket)):
            #mengecek apakah titik berada di kiri dengan determian > 0 dan titik pada bucket tidak
            #sama dengan titik terjauhnya yaitu p1 dan pn
            if CheckPointPosition(px, pn, bucket[i],bucket_true) > 0 and bucket[i] != p1 and bucket[i] != pn:
                pointOfPxPn.append(bucket[i]) #jika ya berada di kiri maka tambahkan pada array antara px dan pn

        #array titik pada garis p1 dan px diinisialisasi dengan kosong
        pointOfP1Px = []
        #melakukan pengecekan sebanyak titik pada bucket
        for i in range(len(bucket)):
            #mengecek apakah titik berada di kiri dengan determian > 0 dan titik pada bucket tidak
            #sama dengan titik terjauhnya yaitu p1 dan pn
            if CheckPointPosition(p1, px, bucket[i], bucket_true) > 0 and bucket[i] != p1 and bucket[i] != pn:
                pointOfP1Px.append(bucket[i]) #jika ya berada di kiri maka tambahkan pada array antara p1 dan px
            #memanggil fungsi rekursif untuk mendapatkan titik-tik yang sesuai pada bucket
        #sesuai dengan partisinya yang sudah dilakukan
        left = funcRecursive(p1, px, bucket_true,pointOfP1Px)
        right = funcRecursive(px, pn, bucket_true,pointOfPxPn)

        #Mengembalikan kombinasi antara partisi yang sudah dilakukan sebelumnya berupa 
        #array dari bucket yang bernilai true
        return left+right
    
    else:                                       #jika banyak titik pada bucket=0
        if p1 != pn:                            #dan p1 tidak sama dengan pn maka didapatkan titik garis terjauh
            return [[p1, pn]]                   #titik yg dibentuk oleh p1 dan pn
        else:
            return []                           #jika nilainya sama maka tidak akan terbentuk garis





