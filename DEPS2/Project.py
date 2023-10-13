import heapq

# Function to get user's choice for going to the hospital first
def get_user_choice():
    choice = input("Do you want to go to the hospital first? (yes/no): ").lower()
    while choice not in ['yes', 'no']:
        choice = input("Invalid choice. Please enter 'yes' or 'no': ").lower()
    return choice == 'yes'

# Define the people, safe centers, and hospitals
people = ['p1', 'p2', 'p3', 'p4', 'p5']
centers = ['s1', 's2', 's3', 's4', 's5', 's6']
hospitals = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

# Define road conditions (weights) and attributes
road_conditions = {'good': 1, 'average': 5, 'poor': 10}
road_attributes = ['forest', 'bridge', 'tunnel']

# Define specific edges between all persons and all centers
edges = [
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
hospital_road_condition = 'average'
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

# Convert edges to a dictionary format for easy access
graph = {}
for u, v, data in edges:
    if u not in graph:
        graph[u] = {}
    graph[u][v] = data

for u, v, data in edges_hospitals:
    if u not in graph:
        graph[u] = {}
    graph[u][v] = data

# Dijkstra's Algorithm using Priority Queue
def dijkstra(graph, start, end):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            return cost

        for neighbor, data in graph.get(current_node, {}).items():
            neighbor_cost = cost + data['weight']
            heapq.heappush(pq, (neighbor_cost, neighbor))

    return float('inf')

# Get the user's location and the disaster type
location = input("Enter your location (p1 to p5): ")
while location not in people:
    location = input("Invalid location. Please enter a location from p1 to p5: ")

disaster_type = input("Enter the disaster type (fire, flood, or earthquake): ")
while disaster_type not in ['fire', 'flood', 'earthquake']:
    disaster_type = input("Invalid disaster type. Please enter 'fire', 'flood', or 'earthquake': ")

# Define risky attributes based on the disaster type
risky_attributes = {
    'fire': 'forest',
    'flood': 'bridge',
    'earthquake': ['bridge', 'tunnel'],
}[disaster_type]

# Modify edge weights based on risky attributes
for u, neighbors in graph.items():
    if u in centers or u in hospitals:
        for v, data in neighbors.items():
            if isinstance(risky_attributes, list):
                if any(data.get(attr) for attr in risky_attributes):
                    data['weight'] += 50  # Adding penalty for risky routes
            else:
                if data.get(risky_attributes):
                    data['weight'] += 50

# Now let the user decide whether to go to the hospital first
go_to_hospital_first = get_user_choice()

if go_to_hospital_first:
    # User wants to go to the hospital first
    nearest_hospital = min(hospitals, key=lambda hospital: dijkstra(graph, location, hospital))
    path_to_hospital = dijkstra(graph, location, nearest_hospital)

    nearest_center = min(centers, key=lambda center: dijkstra(graph, nearest_hospital, center))
    path_to_center = dijkstra(graph, nearest_hospital, nearest_center)

    # Output the result
    print(f'For {location}, the nearest hospital is {nearest_hospital} via path ["{location}","{nearest_hospital}"].')
    print(f'From {nearest_hospital}, the nearest safe center during a {disaster_type} is {nearest_center} via path["{nearest_hospital}","{nearest_center}"].')
else:
    # User wants to go to the safe center directly
    nearest_center = min(centers, key=lambda center: dijkstra(graph, location, center))
    path_to_center = dijkstra(graph, location, nearest_center)

    # Output the result
    print(f'For {location}, the nearest safe center during a {disaster_type} is {nearest_center} via path ["{location}","{nearest_center}"].')
