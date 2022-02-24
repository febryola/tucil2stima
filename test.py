# Database 1 load_iris
# ini file untuk melakukan pengetesan dengan file ekstensi python bukan jupyter (ipynb)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from MyConvexHull import MyConvexHull

data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()
plt.figure(figsize = (10, 6))
colors = ['m','c','b']
plt.title('Library MyConvexHull')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = MyConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    print(hull)
    for simplex in hull:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.show()