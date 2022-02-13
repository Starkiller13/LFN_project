import itertools
import sys
import threading
from graph_tool.all import Graph, motifs, random_rewire, isomorphism, graph_draw
import pandas as pd
from tqdm import tqdm
import time
#read the csv file
df = pd.read_csv("../data/soc-sign-bitcoinotc.csv")
#print(df.head())
file = open("../mc_sim3.txt","a")

def subRoutine(r_g,it):
    temp = []
    for i in range(0,it):
        random_rewire(r_g, model='erdos',n_iter=100*r_g.num_edges(), edge_sweep=False, parallel_edges=False, self_loops=False)
        temp.append(motifs(r_g, k=3))
    pos = temp[0][0]
    res = [0]*len(pos)
    cnt = [0]*len(pos)
    for item in temp:
        subg, count = item
        for k,el in enumerate(subg):
            flag = 0
            for j,s in enumerate(pos):
                if(isomorphism(s,el)):
                    flag = 1
                    res[j] += count[k]
                    cnt[j] += 1
            if(flag==0):
                pos.append(el)
                res.append(count[k])
                cnt.append(1)
    return pos,[i/cnt[j] for j,i in enumerate(res)]

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading Graph from file ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


done = False
t = threading.Thread(target=animate)
t.start()
#create graph
g = Graph(directed=True)
g.vp['name'] = g.new_vp('string')
#g.ep['weight'] = g.new_ep('int')
#g.ep['timestamp'] = g.new_ep('float')
nodes = set()

for i,row in df.iterrows():
    a,b,c,d = row
    nodes.add(a)
    nodes.add(b)
for n in nodes:
    v = g.add_vertex()
    g.vp['name'][v] = n
nodes = list(nodes)
for i,row in df.iterrows():
    a,b,c,d = row
    s = nodes.index(a)
    t = nodes.index(b)
    vs = g.vertex(s)
    vt = g.vertex(t)
    e = g.add_edge(vs, vt)
    #g.ep['weight'][e] = c
    #g.ep['timestamp'][e] = d
#print("Vertex count:",g.num_vertices())
#print("Edge count:",g.num_edges())
done = True

r_g = Graph(g)
random_rewire(r_g, model='erdos',n_iter=100*r_g.num_edges(), edge_sweep=False, parallel_edges=False, self_loops=False)
res = motifs(r_g, k=3)
for i,item in enumerate(res[0][:7]):
    graph_draw(item,output_size=(100,100), adjust_aspect=False, bg_color='white', output="drawings/motif_"+str(i)+".png")


'''
results = []
with tqdm(total=1000) as pbar:
    for v in range(1000):
        x = results.append(subRoutine(Graph(g),10))
        file.write(str(results[v][1][:7])+"\n")
        file.flush()
        pbar.update(1)
    file.close()
pbar.close()
'''