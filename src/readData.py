from mainProgram import *

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
