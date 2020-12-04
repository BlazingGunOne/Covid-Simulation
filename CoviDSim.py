from CoviDNetwork import *

H = nx.Graph()

H = add_cluster(H, 10, 8, 'S')
H = add_cluster(H, 10, 7, 'S')
H = add_cluster(H, 5, 3, 'I')

add_edges(H, 0, 9, 9, 19, 0.25)
add_edges(H, 0, 19, 20, 24, 0.4)

print((H.nodes(data = True)))
print("\n")
print((H.edges(data = True)))


def update(num, layout, G, ax):
    ax.clear()
    color = []
    for node in G.nodes():
        if G.nodes[node]['state'] == 'I':
            color.append('r')
        elif G.nodes[node]['state'] == 'S':
            color.append('b')
        elif G.nodes[node]['state'] == 'R':
            color.append('g')

    nx.draw(G, pos = layout, node_color = color, with_labels = True, ax = ax)

    # Set the title
    ax.set_title("Frame {}".format(num))
    remove(G)
    infect(G)


def animate(G):

    # Build plot
    fig, ax = plt.subplots(figsize=(6,4))

    layout = nx.spring_layout(G)

    ani = animation.FuncAnimation(fig, update, interval=750, fargs=(layout, G, ax))

    plt.show(1)

animate(H)