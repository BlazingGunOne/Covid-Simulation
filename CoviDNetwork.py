import networkx as nx
import matplotlib.pyplot as plt
import pylab
pylab.ion()

G = nx.Graph()
random_pos = nx.random_layout(G, seed=1)
pos = nx.spring_layout(G, pos=random_pos)

def initialize():
    G.add_node("a", state = "S")
    G.add_node("b", state = "S")
    G.add_node("c", state = "S")
    G.add_node("d", state = "S")
    G.add_node("e", state = "I")
    G.add_node("f", state = "S")
    G.add_edge("a", "b", weight=0.6)
    G.add_edge("a", "c", weight=0.2)
    G.add_edge("c", "d", weight=0.1)
    G.add_edge("c", "e", weight=0.7)
    G.add_edge("c", "f", weight=0.9)
    G.add_edge("a", "d", weight=0.3)
    G.add_edge("a", "f", weight=0.5)

def infect():
    for edge in G.edges():
        if G[edge[0]][edge[1]]['weight'] < 0.5:
            continue
        if G.nodes[edge[0]]['state'] == 'I' and G.nodes[edge[1]]['state'] == 'S':
            G.nodes[edge[1]]['state'] = 'I'    
        elif G.nodes[edge[0]]['state'] == 'S' and G.nodes[edge[1]]['state'] == 'I':
            G.nodes[edge[0]]['state'] = 'I'
initialize()
def spread():
    infect()
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
n = 5
pylab.show()
for i in range(n):
    fig = spread()
    fig.canvas.draw()
    pylab.draw()
    plt.pause(2)
    pylab.close(fig)