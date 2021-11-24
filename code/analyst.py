# pylint: disable=unused-import
from graph_tool.centrality import betweenness, closeness
from numpy import NaN
import pandas as pd
from graph_tool.all import *
from graph_tool.clustering import *

df = pd.read_csv("soc-sign-bitcoinotc.csv")
print(df.head())
# create a graph with four nodes and two edges
g = Graph(directed=True)
weight = g.new_edge_property("int")
timestamp = g.new_edge_property("int")

for i,row in df.iterrows():
    a,b,c,d = row
    a = int(a)
    b = int(b)
    e = g.add_edge(a,b)
    weight[e] = c
    timestamp[e] = d

print("Vertex count:",g.num_vertices())
print("Edge count:",g.num_edges())

a = closeness(g).get_array()
c_x = [0,0]
for v,ct in enumerate(a):
    if c_x[0] < ct and ct != NaN:
        c_x[0] = ct
        c_x[1] = v
print("max closeness centrality vertex",c_x[1],"with value: ",c_x[0])

b = betweenness(g)[0].get_array()
b_x = [0,0]
for v,bt in enumerate(b):
    if b_x[0] < bt and bt != NaN:
        b_x[0] = bt
        b_x[1] = v
print("max betweenness centrality vertex",b_x[1],"with value: ",b_x[0])

cc = global_clustering(g)
print("Global clustering coefficient:",cc[0],"with std:",cc[1])

f = motifs(g,k=3)
for i,j in enumerate(f[0]):
    graph_draw(j, vertex_text=j.vertex_index, output="drawings/motif"+str(i)+".pdf")

#graph_draw(g, vertex_text=g.vertex_index, output="trial1.pdf")
