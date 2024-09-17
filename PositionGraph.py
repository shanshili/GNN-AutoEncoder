import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import numpy as np
import networkx as nx


"""
Position Graph Generation
"""

BJ_position = pd.read_csv('./dataset/北京-天津气象数据集2022/北京-天津气象数据集2022/BJ_position.csv')
TJ_position = pd.read_csv('./dataset/北京-天津气象数据集2022/北京-天津气象数据集2022/TJ_position.csv')

dataset_location = pd.concat([BJ_position, TJ_position])
# print(dataset_location)
lat = dataset_location['lat'].values
lon = dataset_location['lon'].values
x = np.transpose(np.vstack((lat, lon)))
#print(x)
print("x.shape:",x.shape)

plt.scatter(lon, lat, 5)  # cmap_name_r, 加_r反转映射关系
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.colorbar()
# plt.savefig('map1.svg', format='svg')
plt.show()

test = NearestNeighbors(radius = 0.05)
test.fit(x)  #?/?????

# Epsilon neighbor
#A = test.radius_neighbors_graph(radius = 0.08)
# K neighbor
A = test.kneighbors_graph(n_neighbors= 4)
print("A:",A)
G = nx.from_numpy_array(A)
nx.draw(G,pos = x, node_size=10)
plt.show()