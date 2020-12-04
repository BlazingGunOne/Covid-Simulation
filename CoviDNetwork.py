import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import pylab
pylab.ion()


def add_cluster(network, size, deg, status):
    h = nx.Graph()
    node_list = []
    for n in range(len(network.nodes()), len(network.nodes()) + size):
        viral_load = 0
        if(status == 'I'):
            viral_load = round(random.uniform(0, 1), 2)
        attr = {
            'state' : status,
            'immunity' : round(random.choice([-1, 1])*random.uniform(0.1, 1), 2),
            'load' : viral_load
        }
        node_list.append((n, attr))
    # print(node_list)
    h.add_nodes_from(node_list)
    for u in h.nodes():
        for v in h.nodes():
            randno = random.uniform(0, 1)
            p = deg/len(h.nodes())
            if randno <= p and u < v:
                h.add_edge(u, v, weight = round(random.uniform(0.5, 1), 2))
    return nx.disjoint_union(network, h)


def add_edges(G, index1, index2, index3, index4, p):
    for u in G.nodes():
        if index1 <= u and index2 >= u:
            for v in G.nodes():
                if index3 <= v and index4 >= v:
                    randno = random.uniform(0, 1)
                    if randno <= p:
                        G.add_edge(u, v, weight = round(random.uniform(0, 0.7), 2))


def infect(G):
    for edge in G.edges():
        if G.nodes[edge[0]]['state'] == 'I' and G.nodes[edge[1]]['state'] == 'S':
            virus = G.nodes[edge[0]]['load']*(G[edge[0]][edge[1]]['weight']*2)*(2**(-1-G.nodes[edge[1]]['immunity']))
            if virus > 0.35:
                G.nodes[edge[1]]['state'] = 'I'
                G.nodes[edge[1]]['load'] = min(virus, 1)    
        elif G.nodes[edge[0]]['state'] == 'S' and G.nodes[edge[1]]['state'] == 'I':
            virus = G.nodes[edge[1]]['load']*(G[edge[0]][edge[1]]['weight']*2)*(2**(-1-G.nodes[edge[0]]['immunity']))
            if virus > 0.25:
                G.nodes[edge[0]]['state'] = 'I'
                G.nodes[edge[0]]['load'] = min(virus, 1)    


def remove(G):
    for node in G.nodes():
        if G.nodes[node]['state'] == 'I':
            G.nodes[node]['load'] -= 0.1*G.nodes[node]['immunity']
            if G.nodes[node]['load'] >= 1 or G.nodes[node]['load'] <= 0.2:
                G.nodes[node]['state'] = 'R'


################################################################################################################

def spread(G, layout):
    color = []
    for node in G.nodes():
        if G.nodes[node]['state'] == 'I':
            color.append('r')
        elif G.nodes[node]['state'] == 'S':
            color.append('b')
        elif G.nodes[node]['state'] == 'R':
            color.append('g') 
    # print(G.nodes.data('state'))
    fig = pylab.figure()
    nx.draw(G, pos = layout, node_color = color, with_labels = True)
    remove(G)
    infect(G)
    return fig

def run(G, n):
    layout = nx.spring_layout(G)
    pylab.show()
    for i in range(n):
        fig = spread(G, layout)
        fig.canvas.draw()
        pylab.draw()
        plt.pause(2)
        pylab.close(fig)

# nx.draw(H)
# plt.show(20)

# run(H, 5)