import networkx as nx
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import warnings
from tkinter import ttk

def draw_graph(G, canvas, pos):
    plt.clf()
    nx.draw(G, pos=pos, with_labels=True)
    canvas.draw()



# First graph (with risky attributes)
G = nx.Graph()

# Define the people, safe centers, and hospitals
people = ['p1', 'p2', 'p3', 'p4', 'p5']
centers = ['s1', 's2', 's3', 's4', 's5', 's6']
hospitals = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
disaster = ['fire', 'flood', 'earthquake']

# Add the nodes to the graph
G.add_nodes_from(people + centers)

# Define road conditions (weights) and attributes
road_conditions = {'good': 1, 'average': 5, 'poor': 10}
road_attributes = ['forest', 'bridge', 'tunnel']

# Define specific edges between all persons and all centers
# (same as in the original code)
# Define specific edges between all persons and all centers
edges = [
    # Edges from person p1 to centers
    ('p1', 's1', {'weight': 7, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('p1', 's2', {'weight': 5, 'forest': False, 'bridge': True, 'tunnel': False}),
    ('p1', 's3', {'weight': 3, 'forest': False, 'bridge': True, 'tunnel': False}),
    ('p1', 's4', {'weight': 4, 'forest': False, 'bridge': False, 'tunnel': True}),
    ('p1', 's5', {'weight': 8, 'forest': True, 'bridge': False, 'tunnel': True}),
    ('p1', 's6', {'weight': 6, 'forest': True, 'bridge': True, 'tunnel': False}),

    # Edges from person p2 to centers
    ('p2', 's1', {'weight': 4, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('p2', 's2', {'weight': 6, 'forest': False, 'bridge': True, 'tunnel': False}),
    ('p2', 's3', {'weight': 5, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('p2', 's4', {'weight': 3, 'forest': True, 'bridge': False, 'tunnel': False}),
    ('p2', 's5', {'weight': 9, 'forest': True, 'bridge': True, 'tunnel': True}),
    ('p2', 's6', {'weight': 7, 'forest': True, 'bridge': False, 'tunnel': True}),

    # Edges from person p3 to centers
    ('p3', 's1', {'weight': 6, 'forest': True, 'bridge': False, 'tunnel': False}),
    ('p3', 's2', {'weight': 8, 'forest': True, 'bridge': True, 'tunnel': False}),
    ('p3', 's3', {'weight': 4, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('p3', 's4', {'weight': 5, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('p3', 's5', {'weight': 7, 'forest': True, 'bridge': False, 'tunnel': False}),
    ('p3', 's6', {'weight': 3, 'forest': False, 'bridge': False, 'tunnel': True}),

    # Edges from person p4 to centers
    ('p4', 's1', {'weight': 9, 'forest': True, 'bridge': False, 'tunnel': False}),
    ('p4', 's2', {'weight': 7, 'forest': True, 'bridge': True, 'tunnel': False}),
    ('p4', 's3', {'weight': 6, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('p4', 's4', {'weight': 4, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('p4', 's5', {'weight': 5, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('p4', 's6', {'weight': 8, 'forest': True, 'bridge': False, 'tunnel': False}),

    # Edges from person p5 to centers
    ('p5', 's1', {'weight': 5, 'forest': False, 'bridge': False, 'tunnel': True}),
    ('p5', 's2', {'weight': 3, 'forest': True, 'bridge': False, 'tunnel': True}),
    ('p5', 's3', {'weight': 7, 'forest': True, 'bridge': True, 'tunnel': False}),
    ('p5', 's4', {'weight': 9, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('p5', 's5', {'weight': 6, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('p5', 's6', {'weight': 4, 'forest': False, 'bridge': True, 'tunnel': False}),
]
# Add the edges to the graph
G.add_edges_from(edges)

# Second graph (with hospitals)
G_hospitals = nx.Graph()

# Add the nodes to the second graph
G_hospitals.add_nodes_from(people + hospitals + centers)

# Define the road condition for edges between people and hospitals
hospital_road_condition = 'average'  # You can change this to 'good' or 'poor' if needed

# Define specific edges between all persons and all hospitals
edges_hospitals = [
    # Edges from person p1 to hospitals
    ('p1', 'h1', {'weight': road_conditions[hospital_road_condition]}),
    ('p1', 'h2', {'weight': road_conditions[hospital_road_condition]}),
    ('p1', 'h3', {'weight': road_conditions[hospital_road_condition]}),
    ('p1', 'h4', {'weight': road_conditions[hospital_road_condition]}),
    ('p1', 'h5', {'weight': road_conditions[hospital_road_condition]}),
    ('p1', 'h6', {'weight': road_conditions[hospital_road_condition]}),
    ('p1', 'h7', {'weight': road_conditions[hospital_road_condition]}),
    ('p1', 'h8', {'weight': road_conditions[hospital_road_condition]}),

    # Edges from person p2 to hospitals
    ('p2', 'h1', {'weight': road_conditions[hospital_road_condition]}),
    ('p2', 'h2', {'weight': road_conditions[hospital_road_condition]}),
    ('p2', 'h3', {'weight': road_conditions[hospital_road_condition]}),
    ('p2', 'h4', {'weight': road_conditions[hospital_road_condition]}),
    ('p2', 'h5', {'weight': road_conditions[hospital_road_condition]}),
    ('p2', 'h6', {'weight': road_conditions[hospital_road_condition]}),
    ('p2', 'h7', {'weight': road_conditions[hospital_road_condition]}),
    ('p2', 'h8', {'weight': road_conditions[hospital_road_condition]}),

    # Edges from person p3 to hospitals
    ('p3', 'h1', {'weight': road_conditions[hospital_road_condition]}),
    ('p3', 'h2', {'weight': road_conditions[hospital_road_condition]}),
    ('p3', 'h3', {'weight': road_conditions[hospital_road_condition]}),
    ('p3', 'h4', {'weight': road_conditions[hospital_road_condition]}),
    ('p3', 'h5', {'weight': road_conditions[hospital_road_condition]}),
    ('p3', 'h6', {'weight': road_conditions[hospital_road_condition]}),
    ('p3', 'h7', {'weight': road_conditions[hospital_road_condition]}),
    ('p3', 'h8', {'weight': road_conditions[hospital_road_condition]}),

    # Edges from person p4 to hospitals
    ('p4', 'h1', {'weight': road_conditions[hospital_road_condition]}),
    ('p4', 'h2', {'weight': road_conditions[hospital_road_condition]}),
    ('p4', 'h3', {'weight': road_conditions[hospital_road_condition]}),
    ('p4', 'h4', {'weight': road_conditions[hospital_road_condition]}),
    ('p4', 'h5', {'weight': road_conditions[hospital_road_condition]}),
    ('p4', 'h6', {'weight': road_conditions[hospital_road_condition]}),
    ('p4', 'h7', {'weight': road_conditions[hospital_road_condition]}),
    ('p4', 'h8', {'weight': road_conditions[hospital_road_condition]}),

    # Edges from person p5 to hospitals
    ('p5', 'h1', {'weight': road_conditions[hospital_road_condition]}),
    ('p5', 'h2', {'weight': road_conditions[hospital_road_condition]}),
    ('p5', 'h3', {'weight': road_conditions[hospital_road_condition]}),
    ('p5', 'h4', {'weight': road_conditions[hospital_road_condition]}),
    ('p5', 'h5', {'weight': road_conditions[hospital_road_condition]}),
    ('p5', 'h6', {'weight': road_conditions[hospital_road_condition]}),
    ('p5', 'h7', {'weight': road_conditions[hospital_road_condition]}),
    ('p5', 'h8', {'weight': road_conditions[hospital_road_condition]}),
]

# Add the edges between hospitals and safe centers with the same attributes as in the first graph
edges_hospitals.extend([
    # Edges from hospital h1 to safe centers
    ('h1', 's1', {'weight': 7, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('h1', 's2', {'weight': 5, 'forest': False, 'bridge': True, 'tunnel': False}),
    ('h1', 's3', {'weight': 3, 'forest': False, 'bridge': True, 'tunnel': False}),
    ('h1', 's4', {'weight': 4, 'forest': False, 'bridge': False, 'tunnel': True}),
    ('h1', 's5', {'weight': 8, 'forest': True, 'bridge': False, 'tunnel': True}),
    ('h1', 's6', {'weight': 6, 'forest': True, 'bridge': True, 'tunnel': False}),

    # Edges from hospital h2 to safe centers
    ('h2', 's1', {'weight': 4, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('h2', 's2', {'weight': 6, 'forest': False, 'bridge': True, 'tunnel': False}),
    ('h2', 's3', {'weight': 5, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('h2', 's4', {'weight': 3, 'forest': True, 'bridge': False, 'tunnel': False}),
    ('h2', 's5', {'weight': 9, 'forest': True, 'bridge': True, 'tunnel': True}),
    ('h2', 's6', {'weight': 7, 'forest': True, 'bridge': False, 'tunnel': True}),

    # Edges from hospital h3 to safe centers
    ('h3', 's1', {'weight': 6, 'forest': True, 'bridge': False, 'tunnel': False}),
    ('h3', 's2', {'weight': 8, 'forest': True, 'bridge': True, 'tunnel': False}),
    ('h3', 's3', {'weight': 4, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('h3', 's4', {'weight': 5, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('h3', 's5', {'weight': 7, 'forest': True, 'bridge': False, 'tunnel': False}),
    ('h3', 's6', {'weight': 3, 'forest': False, 'bridge': False, 'tunnel': True}),

    # Edges from hospital h4 to safe centers
    ('h4', 's1', {'weight': 9, 'forest': True, 'bridge': False, 'tunnel': False}),
    ('h4', 's2', {'weight': 7, 'forest': True, 'bridge': True, 'tunnel': False}),
    ('h4', 's3', {'weight': 6, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('h4', 's4', {'weight': 4, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('h4', 's5', {'weight': 5, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('h4', 's6', {'weight': 8, 'forest': True, 'bridge': False, 'tunnel': False}),

    # Edges from hospital h5 to safe centers
    ('h5', 's1', {'weight': 5, 'forest': False, 'bridge': False, 'tunnel': True}),
    ('h5', 's2', {'weight': 3, 'forest': True, 'bridge': False, 'tunnel': True}),
    ('h5', 's3', {'weight': 7, 'forest': True, 'bridge': True, 'tunnel': False}),
    ('h5', 's4', {'weight': 9, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('h5', 's5', {'weight': 6, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('h5', 's6', {'weight': 4, 'forest': False, 'bridge': True, 'tunnel': False}),

    # Edges from hospital h6 to safe centers
    ('h6', 's1', {'weight': 8, 'forest': True, 'bridge': False, 'tunnel': False}),
    ('h6', 's2', {'weight': 6, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('h6', 's3', {'weight': 4, 'forest': True, 'bridge': True, 'tunnel': True}),
    ('h6', 's4', {'weight': 5, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('h6', 's5', {'weight': 7, 'forest': True, 'bridge': True, 'tunnel': True}),
    ('h6', 's6', {'weight': 3, 'forest': False, 'bridge': False, 'tunnel': True}),

    # Edges from hospital h7 to safe centers
    ('h7', 's1', {'weight': 7, 'forest': True, 'bridge': False, 'tunnel': False}),
    ('h7', 's2', {'weight': 5, 'forest': False, 'bridge': True, 'tunnel': False}),
    ('h7', 's3', {'weight': 3, 'forest': False, 'bridge': True, 'tunnel': True}),
    ('h7', 's4', {'weight': 4, 'forest': True, 'bridge': True, 'tunnel': True}),
    ('h7', 's5', {'weight': 6, 'forest': False, 'bridge': False, 'tunnel': False}),
    ('h7', 's6', {'weight': 2, 'forest': True, 'bridge': False, 'tunnel': True}),

    # Edges from hospital h8 to safe centers
    ('h8', 's1', {'weight': 5, 'forest': False, 'bridge': False, 'tunnel': True}),
    ('h8', 's2', {'weight': 3, 'forest': True, 'bridge': False, 'tunnel': True}),
    ('h8', 's3', {'weight': 6, 'forest': True, 'bridge': True, 'tunnel': False}),
    ('h8', 's4', {'weight': 8, 'forest': False, 'bridge': True, 'tunnel': False}),
    ('h8', 's5', {'weight': 5, 'forest': True, 'bridge': True, 'tunnel': True}),
    ('h8', 's6', {'weight': 4, 'forest': False, 'bridge': False, 'tunnel': True}),
])

# Add the edges to the second graph
G_hospitals.add_edges_from(edges_hospitals)

root = tk.Tk()

pos = nx.spring_layout(G)
fig = plt.figure(figsize=(5,5))



source_var = tk.StringVar()
disaster_var = tk.StringVar()

node_frame = tk.Frame(root)
node_frame.pack()

# Label
label = tk.Label(node_frame, text="")
label.pack(padx=10, pady=10)  # padding on x and y axes

source_label = tk.Label(node_frame, font=("Arial", 20), text="Current Location Node")
source_label.pack()


source_entry = tk.Entry(node_frame, font=("Arial", 20), textvariable=source_var)
source_entry.pack()

# Label
label = tk.Label(node_frame, text="")
label.pack(padx=10, pady=10)  # padding on x and y axes

def show_dialog():
    response = messagebox.askyesno("Question", "Do you want to go to hospital?")
    if response == 1:
        return True
    else:
        return False

def draw_graph_with_path(G, canvas, pos, path):
    # Clear the current figure
    plt.clf()

    # Draw the graph
    nx.draw(G, pos, with_labels=True)

    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Draw the path with a different color and width
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    # Redraw the canvas
    canvas.draw()


def shortest_path_correct(source_var, disaster_var, text_var, root):
    source_var = source_var.get()
    disaster_var = disaster_var.get()
    # Define risky attributes based on the disaster type
    risky_attributes = {
        'fire': 'forest',
        'flood': 'bridge',
        'earthquake': ['bridge', 'tunnel'],
    }[disaster_var]
    #
    for u, v, data in G.edges(data=True):
        if v in centers:
            if isinstance(risky_attributes, list):
                if any(data.get(attr) for attr in risky_attributes):
                    data['weight'] += 50  # Adding penalty for risky routes
            else:
                if data.get(risky_attributes):
                    data['weight'] += 50

    # Now let the user decide whether to go to the hospital first
    go_to_hospital_first = show_dialog()

    if go_to_hospital_first:
        # User wants to go to the hospital first
        nearest_hospital = min(hospitals, key=lambda hospital: nx.shortest_path_length(G_hospitals, source=source_var,
                                                                                       target=hospital,
                                                                                       weight='weight'))
        path_to_hospital = nx.shortest_path(G_hospitals, source=source_var, target=nearest_hospital, weight='weight')

        nearest_center = min(centers, key=lambda center: nx.shortest_path_length(G_hospitals, source=nearest_hospital,
                                                                                 target=center, weight='weight'))
        path_to_center = nx.shortest_path(G_hospitals, source=nearest_hospital, target=nearest_center, weight='weight')

        # Output the result
        text_var.set(f'For {source_var}, the nearest hospital is {nearest_hospital} via path {path_to_hospital} and From {nearest_hospital}, the nearest safe center during a {disaster_var} is {nearest_center} via path {path_to_center}.')
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")

        total_path = path_to_hospital[:-1] + path_to_center[:]
        # total_path = list(set(total_path))
        pos = nx.spring_layout(G_hospitals)
        draw_graph_with_path(G_hospitals, canvas, pos, total_path)

        root.update()

    else:
        # User wants to go to the safe center directly
        nearest_center = min(centers, key=lambda center: nx.shortest_path_length(G, source=source_var, target=center,
                                                                                 weight='weight'))
        path_to_center = nx.shortest_path(G, source=source_var, target=nearest_center, weight='weight')

        # Output the result
        text_var.set(f'For {source_var}, the nearest safe center during a {disaster_var} is {nearest_center} via path {path_to_center}.')
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")

        total_path = path_to_center
        total_path = list(set(total_path))
        pos = nx.spring_layout(G)
        draw_graph_with_path(G, canvas, pos, total_path)


        root.update()
def draw_graph_all_paths(G, canvas, pos, path, color):

    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Draw the path with a different color and width
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color=color, width=2)

    # Redraw the canvas
    canvas.draw()


def all_path_correct(source_var, disaster_var, text_var, root):
    source_var = source_var.get()
    disaster_var = disaster_var.get()

    # Define risky attributes based on the disaster type
    risky_attributes = {
        'fire': 'forest',
        'flood': 'bridge',
        'earthquake': ['bridge', 'tunnel'],
    }[disaster_var]
    #
    for u, v, data in G.edges(data=True):
        if v in centers:
            if isinstance(risky_attributes, list):
                if any(data.get(attr) for attr in risky_attributes):
                    data['weight'] += 50  # Adding penalty for risky routes
            else:
                if data.get(risky_attributes):
                    data['weight'] += 50

    import networkx as nx

    paths_to_hospitals = {hospital: nx.shortest_path(G_hospitals, source=source_var, target=hospital, weight='weight') for
                          hospital in hospitals}

    # Then for each hospital, we find the shortest path to each safe center.
    paths_to_centers = {
        hospital: {center: nx.shortest_path(G_hospitals, source=hospital, target=center, weight='weight') for center in centers}
        for hospital in paths_to_hospitals.keys()}

    # Now, for each hospital, we combine the path to that hospital with the path from that hospital to each center.
    all_paths = {
        hospital: {center: paths_to_hospitals[hospital] + paths_to_centers[hospital][center][1:] for center in centers}
        for hospital in hospitals}

    # For each center, we keep only the shortest path.
    shortest_paths = {}
    for center in centers:
        paths_to_center = [(hospital, path) for hospital, paths in all_paths.items() for center_, path in paths.items()
                           if center_ == center]
        shortest_paths[center] = min(paths_to_center, key=lambda x: len(x[1]))[1]

    # all_paths now contains every path from the source to each center via each hospital.
    pos = nx.spring_layout(G_hospitals)
    # draw_graph_with_path(G_hospitals, canvas, pos, all_paths)

    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']  # Add more colors if necessary

    plt.clf()
    nx.draw(G_hospitals, pos, with_labels=True)

    # Draw paths with different colors
    for i, path in enumerate(shortest_paths.values()):
        draw_graph_all_paths(G_hospitals, canvas, pos, path, colors[i % len(colors)])
        if i == 3:
            break

    root.update()

def all_path(source_var, disaster_var,text_var,root):
    source = source_var.get()
    target = disaster_var.get()

    text_var.set("Your shortest path is loading")
    root.update()

    if source not in people:
        text_var.set("Invalid location. Please enter a location from p1 to p5: ")
        root.update()
    elif target not in disaster:
        text_var.set("Invalid disaster type. Please enter 'fire', 'flood', or 'earthquake': ")
        root.update()
    else:
        all_path_correct(source_var, disaster_var, text_var, root)

def shortest_path(source_var, disaster_var, text_var, root):
    source = source_var.get()
    target = disaster_var.get()

    text_var.set("Your shortest path is loading")
    root.update()

    if source not in people:
        text_var.set("Invalid location. Please enter a location from p1 to p5: ")
        root.update()
    elif target not in disaster:
        text_var.set("Invalid disaster type. Please enter 'fire', 'flood', or 'earthquake': ")
        root.update()
    else:
        shortest_path_correct(source_var, disaster_var, text_var, root)



target_label = tk.Label(node_frame, font=("Arial", 20) , text="Disaster (fire, flood, earthquake)")
target_label.pack()
# target_entry = tk.Entry(node_frame, font=("Arial", 20) , textvariable=disaster_var)
# target_entry.pack()

options = ['fire', 'flood', 'earthquake']
#
# Create a Combobox
target_entry = ttk.Combobox(node_frame,font=("Arial", 20), values=options, textvariable=disaster_var)
target_entry.set('fire')
target_entry.pack()

text_var = tk.StringVar()
text_var.set("Hello, you can give the relevant input!!")


# Label
label = tk.Label(node_frame, text="")
label.pack(padx=10, pady=10)  # padding on x and y axes

shortest_button = tk.Button(root, text="Shortest Path", font=("Arial", 20), command=lambda: shortest_path(source_var, disaster_var,text_var,root))
shortest_button.pack(padx=200)



all_paths_button = tk.Button(root, text="Show all paths", font=("Arial", 20), command=lambda: all_path(source_var, disaster_var,text_var,root))
all_paths_button.pack(padx=200)




canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

draw_graph(G, canvas, pos)

# Label
label = tk.Label(node_frame, text="")
label.pack(padx=10, pady=10)  # padding on x and y axes

label = tk.Label(root, textvariable=text_var, font=("Arial", 30), foreground="white", bg="black")
label.pack()

root.mainloop()





