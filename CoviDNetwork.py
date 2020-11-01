import random
import networkx as nx
import matplotlib.pyplot as plt
import pylab
pylab.ion()

# random_pos = nx.random_layout(G, seed=1)
# pos = nx.spring_layout(G, pos=random_pos)

def add_cluster(network, size, deg, status):
    h = nx.Graph()
    node_list = list(range(len(network.nodes()), len(network.nodes()) + size))
    h.add_nodes_from(node_list, state = status)
    for u in h.nodes():
        for v in h.nodes():
            randno = random.uniform(0, 1)
            p = deg/len(h.nodes())
            if randno <= p and u < v:
                h.add_edge(u, v, weight = round(random.uniform(0.5, 1), 2))
    return nx.disjoint_union(network, h)

def add_edges(h, index1, index2, index3, index4, p):
    for u in h.nodes():
        if index1 <= u and index2 >= u:
            for v in h.nodes():
                if index3 <= v and index4 >= v:
                    randno = random.uniform(0, 1)
                    if randno <= p:
                        h.add_edge(u, v, weight = round(random.uniform(0, 0.7), 2))
    return h

def infect(G):
    for edge in G.edges():
        if G[edge[0]][edge[1]]['weight'] < 0.5:
            continue
        if G.nodes[edge[0]]['state'] == 'I' and G.nodes[edge[1]]['state'] == 'S':
            G.nodes[edge[1]]['state'] = 'I'    
        elif G.nodes[edge[0]]['state'] == 'S' and G.nodes[edge[1]]['state'] == 'I':
            G.nodes[edge[0]]['state'] = 'I'

def spread(G):
    infect(G)
    color = []
    for node in G.nodes():
        if G.nodes[node]['state'] == 'I':
            color.append('r')
        else:
            color.append('b')
    # print(G.nodes.data('state'))
    fig = pylab.figure()
    nx.draw(G, node_color = color, with_labels = True)
    return fig

def run(G):
    n = 5
    pylab.show()
    for i in range(n):
        fig = spread(G)
        fig.canvas.draw()
        pylab.draw()
        plt.pause(2)
        pylab.close(fig)

H = nx.Graph()

H = add_cluster(H, 5, 3, 'S')
H = add_cluster(H, 4, 3, 'S')
H = add_cluster(H, 2, 2, 'I')

H = add_edges(H, 0, 4, 5, 8, 0.25)
H = add_edges(H, 9, 10, 5, 8, 0.25)
H = add_edges(H, 0, 4, 9, 10, 0.25)

print((H.nodes(data = True)))
print("\n")
print((H.edges(data = True)))

# nx.draw(H)
# plt.show(20)

run(H)