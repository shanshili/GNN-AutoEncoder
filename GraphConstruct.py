import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import numpy as np
import networkx as nx


def location_graph(location):
    test = NearestNeighbors(radius = 0.05)
    test.fit(location)  #??????
    """
    dis,ind = test.radius_neighbors(radius = 0.05)
    print("dis:",dis)
    print("ind:",ind)
    """

    # Epsilon neighbor
    #A = test.radius_neighbors_graph(radius = 0.08)
    # K neighbor
    A = test.kneighbors_graph(n_neighbors= 4)
    A = A + A.T.multiply(A.T > A) - A.multiply(A.T > A)  # Undirected graphs, but it doesn't affect here
    #print("A:",A)
    location_g = nx.from_numpy_array(A)
    nx.draw(location_g,pos = location, alpha = 0.4, node_size=10)
    #plt.show()
    plt.title('Knn_4_graph')
    plt.savefig('Knn_4_graph'+'.svg', format='svg')
    return location_g,A


def data_color_graph(data,locationgraph,location,epoch_range):
    #locationgraph = location_graph(location)
    plt.figure()
    plt.title('epoch:'+str(epoch_range))
    nx.draw(locationgraph, pos=location, with_labels=True,  alpha = 0.8, node_size=5,node_color= data, cmap = 'rainbow',font_size = 3)
    plt.savefig('node_quality_epoch'+str(epoch_range)+'.svg', format='svg')


def topological_features_construct(G):
    topological_features = pd.DataFrame((nx.degree_centrality(G), nx.harmonic_centrality(G), nx.closeness_centrality(G),
                                         nx.betweenness_centrality(G), nx.subgraph_centrality(G), nx.clustering(G)))
    return topological_features
