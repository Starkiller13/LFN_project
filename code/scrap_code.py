'''
graphlets_c = [[0]*g.num_vertices() for i in range(len(motif_res[0]))]
for i,subg in enumerate(motif_res[2]):
    for item in subg:
        for node in item.get_array():
            graphlets_c[i][int(node)]+=1

bad = [0]*len(motif_res[0])
total = [0]*len(motif_res[0])
for i,k in enumerate(graphlets_c):
    for j,p in enumerate(k):
        if int(g.vp['name'][j]) in badguys:
            bad[i]+=p
        total[i]+=p

'''