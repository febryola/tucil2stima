import pandas as pd
import matplotlib.pyplot as plt
import random
from scipy.spatial import ConvexHull
from MyConvexHull import MyConvexHull

def header():
    print("""\033[33m
 ██████  ██████  ███    ██ ██    ██ ███████ ██   ██     ██   ██ ██    ██ ██      ██      
██      ██    ██ ████   ██ ██    ██ ██       ██ ██      ██   ██ ██    ██ ██      ██      
██      ██    ██ ██ ██  ██ ██    ██ █████     ███       ███████ ██    ██ ██      ██      
██      ██    ██ ██  ██ ██  ██  ██  ██       ██ ██      ██   ██ ██    ██ ██      ██      
 ██████  ██████  ██   ████   ████   ███████ ██   ██     ██   ██  ██████  ███████ ███████ \033[0m""")

def logo():
    print("""\033[36m\n\n
    ________________________________█████_____█████
______________________________███____██_██_____███
_____________________________██________██__________██
____________________________██__________█____________██
________██████____________██________________________██
_____███████████________██________________________██
____█████████████_______██_______________________██
___███████████████______██______________________██
___████████████████______██___________________██
___████████████████_______██_________________██
____███████████████_______███_______________██
_______███████████_______██__██_____________██
___________███████______████___██__________██
____██████__██████████████_____██_____██
__██████████████████████________██__██
_████████████████████_____________████
██_█████_████████████_______________█
█__█_██__████████████
_____█__████████████
_______█████████████
_______██████████████
_______███████████████
________███████████████
_______███████__████████
______███████_____███████
____█████████________██████\n\n\033[0m""")

def selamatDatang():
    print("""\033[31m \nSelamat Datang Di Program Convex Hull YOLSSSSSS \033[0m""")
    print("""\033[32m Ini adalah program yang dibuat oleh \033[0m""")
    print("""\033[34m FEBRYOLA KURNIA PUTRI - 13520140 DARI K02 \033[0m""")
    print("""\033[34m Untuk memenuhi tugas kecil 2 IF2211 Strategi Algoritma \033[0m""")
    print("""\033[33m Berikut Beberapa menu yang tersedia pada program ini: \n\033[0m""")

def semangat():
    print("""\033[33mBiar kamu semangat terus, ini aku kasiiiii emot yang lucu-lucu\033[0m""")
    print("""\033[37m(👍 ͡❛ ͜ʖ ͡❛)👍\033[0m""")
    print("""\033[31m"KAMUUUU KERENNNNNNN\033[0m""")
    print("""\033[37m💪 ( ͡❛ ͜ʖ ͡❛) 👊\033[0m""")
    print("""\033[37m( ͡❛ ͜ʖ ͡❛)👌\033[0m""")
    print("""\033[36mSEMANGAT TERUS YAKKKKKKkkkkkKKKKKKK\033[0m""")

def menu():
    print("""\033[37m
    1. Lihat dan testing dataset yang tersedia pada program ini
    2. Exit Program\n\033[0m""")
    pilih = int(input("""\033[36mMasukkan menu yang ingin dilakukan:\033[0m """))
    if pilih == 1:
        print("Berikut Dataset yang tersedia pada program ini:")
        print("""\033[37m
        1. Dataset iris
        2. Dataset digits
        3. Dataset wine
        4. Dataset breast_cancer\n\033[0m""")
        pilihlagi=int(input("""\033[36mMasukkan dataset yang ingin dicoba:\033[0m """))
        if pilihlagi==1:
            iris()
        elif pilihlagi==2:
            digits()
        elif pilihlagi==3:
            wine()
        elif pilihlagi==4:
            breast_cancer()
    elif pilih==2:
        exit()

def terimakasih():
    print("""\033[36m
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄    ▄▄▄   ▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ ▄▄   ▄▄ 
█       █       █   ▄  █ █   █  █▄█  █      █  █   █ █ █      █       █   █  █ █  █
█▄     ▄█    ▄▄▄█  █ █ █ █   █       █  ▄   █  █   █▄█ █  ▄   █  ▄▄▄▄▄█   █  █▄█  █
  █   █ █   █▄▄▄█   █▄▄█▄█   █       █ █▄█  █  █      ▄█ █▄█  █ █▄▄▄▄▄█   █       █
  █   █ █    ▄▄▄█    ▄▄  █   █       █      █  █     █▄█      █▄▄▄▄▄  █   █   ▄   █
  █   █ █   █▄▄▄█   █  █ █   █ ██▄██ █  ▄   █  █    ▄  █  ▄   █▄▄▄▄▄█ █   █  █ █  █
  █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄█▄█   █▄█▄█ █▄▄█  █▄▄▄█ █▄█▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█▄▄█ █▄▄█

    \033[0m""")

def iris():
        from sklearn import datasets
        data = datasets.load_iris()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['label'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head)
        kolom1 = int(input("Masukkan pasangan kolom 1: "))
        kolom2 = int(input("Masukkan pasangan kolom 2: "))
        namafile = input("Masukkan nama file yang diinginkan: ")
        buatanPython(df, "Library Python Spicy",data.feature_names[kolom1],data.feature_names[kolom2],kolom1,kolom2,data.target_names,namafile+"python")
        buatanSendiri(df, "Library MyConvexHull",data.feature_names[kolom1],data.feature_names[kolom2],kolom1,kolom2,data.target_names,namafile)

def digits():
        from sklearn import datasets
        data = datasets.load_digits()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['label'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head)
        kolom1 = int(input("Masukkan pasangan kolom 1: "))
        kolom2 = int(input("Masukkan pasangan kolom 2: "))
        namafile = input("Masukkan nama file yang diinginkan: ")
        buatanPython(df, "Library Python Spicy",data.feature_names[kolom1],data.feature_names[kolom2],kolom1,kolom2,data.target_names,namafile+"python")
        buatanSendiri(df, "Library MyConvexHull",data.feature_names[kolom1],data.feature_names[kolom2],kolom1,kolom2,data.target_names,namafile)

def wine():
        from sklearn import datasets
        data = datasets.load_wine()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['label'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head)
        kolom1 = int(input("Masukkan pasangan kolom 1: "))
        kolom2 = int(input("Masukkan pasangan kolom 2: "))
        namafile = input("Masukkan nama file yang diinginkan: ")
        buatanPython(df, "Library Python Spicy",data.feature_names[kolom1],data.feature_names[kolom2],kolom1,kolom2,data.target_names,namafile+"python")
        buatanSendiri(df, "Library MyConvexHull",data.feature_names[kolom1],data.feature_names[kolom2],kolom1,kolom2,data.target_names,namafile)

def breast_cancer():
        from sklearn import datasets
        data = datasets.load_breast_cancer()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['label'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head)
        kolom1 = int(input("Masukkan pasangan kolom 1: "))
        kolom2 = int(input("Masukkan pasangan kolom 2: "))
        namafile = input("Masukkan nama file yang diinginkan: ")
        buatanPython(df, "Library Python Spicy",data.feature_names[kolom1],data.feature_names[kolom2],kolom1,kolom2,data.target_names,namafile+"python")
        buatanSendiri(df, "Library MyConvexHull",data.feature_names[kolom1],data.feature_names[kolom2],kolom1,kolom2,data.target_names,namafile)

def buatanSendiri(df, judul, xlabel, ylabel,xkolom, ykolom, labelnames, namafile):
    plt.figure(figsize = (10, 6))
    labelsize = len(df['label'].unique())
    warna = fungsiWarna2(labelsize)
    plt.title(judul)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for i in range(labelsize):
        bucket = df[df['label'] == i]
        bucket = bucket.iloc[:,[xkolom,ykolom]].values
        hull = MyConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=labelnames[i], color=warna[i])
        for simplex in hull:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], color=warna[i])
    plt.legend()
    plt.savefig('output/' + namafile)
    plt.show()

def buatanPython(df, judul, xlabel, ylabel,xkolom, ykolom, labelnames, namafile):
    plt.figure(figsize = (10, 6))
    labelsize = len(df['label'].unique())
    warna = fungsiWarna1(labelsize)

    plt.title(judul)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    for i in range(labelsize):
        bucket = df[df['label'] == i]
        bucket = bucket.iloc[:,[xkolom,ykolom]].values
        hull = ConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=labelnames[i], color=warna[i])
        for simplex in hull.simplices:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], color=warna[i])
    plt.legend()
    plt.savefig('output/' + namafile)

def fungsiWarna1(n):
    warna = ['b','r','g','c','m','y','k','w']
    if n > len(warna):
        for i in (range(n-len(warna))):
            r = random.random()
            g = random.random()
            b = random.random()
            warna.append((r, g, b))
    return warna

def fungsiWarna2(n):
    warna = ['y','b','m','c','g','y','k','w']
    if n > len(warna):
        for i in (range(n-len(warna))):
            r = random.random()
            g = random.random()
            b = random.random()
            warna.append((r, g, b))
    return warna

if __name__ == "__main__":
    header()
    logo()
    semangat()
    selamatDatang()
    menu()
    terimakasih()

