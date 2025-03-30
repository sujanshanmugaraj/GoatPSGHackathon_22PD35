# import json
# import networkx as nx
# import matplotlib.pyplot as plt

# class NavGraph:
#     def __init__(self, graph_file="data/nav_graph.json"):
#         """Initialize the graph using data from a JSON file."""
#         self.graph_file = graph_file
#         self.graph = nx.Graph()
#         self.coordinates = {}
#         self.load_graph()

#     def load_graph(self):
#         """Load graph data from the JSON file and build the NetworkX graph."""
#         try:
#             with open(self.graph_file, "r") as file:
#                 data = json.load(file)
                
#                 # Load coordinates
#                 self.coordinates = data.get("coordinates", {})
                
#                 # Add nodes with positions
#                 for node, coords in self.coordinates.items():
#                     self.graph.add_node(node, pos=(coords[0], coords[1]))

#                 # Add edges with weights
#                 for start_node, neighbors in data.get("graph", {}).items():
#                     for end_node, weight in neighbors.items():
#                         self.graph.add_edge(start_node, end_node, weight=weight)

#                 print("✅ Graph loaded successfully.")
#         except Exception as e:
#             print(f"❗ Error loading graph: {e}")

#     def get_graph(self):
#         """Returns the graph object."""
#         return self.graph

#     def get_coordinates(self):
#         """Returns the coordinates of the nodes."""
#         return self.coordinates

#     def find_shortest_path(self, start_node, end_node):
#         """Find the shortest path between two nodes using Dijkstra's algorithm."""
#         if start_node not in self.graph.nodes or end_node not in self.graph.nodes:
#             print(f"❗ Invalid nodes: {start_node} or {end_node} do not exist.")
#             return None

#         try:
#             # Use NetworkX built-in Dijkstra's algorithm to find the shortest path
#             path = nx.shortest_path(self.graph, source=start_node, target=end_node, weight="weight")
#             print(f"🛤️ Shortest path from {start_node} to {end_node}: {path}")
#             return path
#         except nx.NetworkXNoPath:
#             print(f"❗ No valid path found from {start_node} to {end_node}.")
#             return None

#     def draw_graph(self):
#         """Visualize the graph using Matplotlib."""
#         try:
#             pos = nx.get_node_attributes(self.graph, 'pos')
#             labels = nx.get_edge_attributes(self.graph, 'weight')

#             # Draw the graph with node labels, edge weights, and custom styling
#             nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_weight='bold')
#             nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
#             plt.title("Graph Visualization")
#             plt.show()
#         except Exception as e:
#             print(f"❗ Error visualizing graph: {e}")

# # Example Usage
# if __name__ == "__main__":
#     graph = NavGraph("data/nav_graph.json")
#     graph.draw_graph()
#     graph.find_shortest_path("A", "D")



# import json
# import networkx as nx
# import matplotlib.pyplot as plt

# class NavGraph:
#     def __init__(self, graph_file="data/nav_graph.json"):
#         self.graph = nx.Graph()
#         self.vertices = []
#         self.lanes = []
#         self.load_graph(graph_file)
#         self.coordinates = {}

#     def load_graph(self, json_file):
#         try:
#             with open(json_file, 'r') as file:
#                 data = json.load(file)
#                 self.vertices = data.get('vertices', [])
#                 self.lanes = data.get('lanes', [])

#                 # Add vertices to graph
#                 for index, (x, y, attr) in enumerate(self.vertices):
#                     attr['pos'] = (x, y)
#                     self.graph.add_node(index, **attr)

#                 # Add lanes to graph
#                 for lane in self.lanes:
#                     if len(lane) == 2 and lane[0] < len(self.vertices) and lane[1] < len(self.vertices):
#                         self.graph.add_edge(lane[0], lane[1])
#                     else:
#                         print(f"⚠️ Invalid lane definition: {lane}")
#             print("✅ Graph loaded successfully.")
#         except Exception as e:
#             print(f"❗ Error loading graph: {e}")

#     def visualize_graph(self):
#         pos = nx.get_node_attributes(self.graph, 'pos')
#         labels = nx.get_node_attributes(self.graph, 'name')
        
#         plt.figure(figsize=(10, 8))
        
#         # Draw nodes
#         nx.draw(self.graph, pos, with_labels=False, node_size=500, node_color='skyblue')
        
#         # Draw labels
#         for index, (x, y) in pos.items():
#             label = labels.get(index, str(index))
#             plt.text(x, y, label, fontsize=12, ha='right')
            
#             # Mark chargers with a red circle
#             if self.graph.nodes[index].get('is_charger', False):
#                 plt.plot(x, y, 'ro', markersize=12)

#         # Draw edges
#         nx.draw_networkx_edges(self.graph, pos)
#         plt.title("Navigation Graph")
#         plt.show()
#     def get_graph(self):
#         return self.graph
#     def get_coordinates(self):
#         """Returns the coordinates of the nodes."""
#         return self.coordinates

#     def find_shortest_path(self, start_name, end_name):
#         name_to_index = {self.graph.nodes[i]['name']: i for i in self.graph.nodes}
#         if start_name not in name_to_index or end_name not in name_to_index:
#             print("❗ Invalid start or end node.")
#             return None
#         start_index = name_to_index[start_name]
#         end_index = name_to_index[end_name]

#         try:
#             path = nx.shortest_path(self.graph, source=start_index, target=end_index)
#             path_names = [self.graph.nodes[i]['name'] for i in path]
#             print(f"🚀 Shortest Path from {start_name} to {end_name}: {path_names}")
#             return path_names
#         except nx.NetworkXNoPath:
#             print("❗ No Path Found.")
#             return None

# # Example Usage
# if __name__ == "__main__":
#     graph = NavGraph('data/nav_graph.json')
#     graph.visualize_graph()
#     graph.find_shortest_path('P1', 'P4')


import json
import networkx as nx
import matplotlib.pyplot as plt

class NavGraph:
    def __init__(self, graph_file="data/nav_graph.json"):
        """Initialize the graph using data from a JSON file."""
        self.graph_file = graph_file
        self.graph = nx.Graph()
        self.coordinates = {}
        self.load_graph()

    def load_graph(self):
        """Load graph data from the JSON file and build the NetworkX graph."""
        try:
            with open(self.graph_file, "r") as file:
                data = json.load(file)
                
                # Load coordinates
                self.coordinates = data.get("coordinates", {})
                
                # Add nodes with positions and assign name attribute
                for node, coords in self.coordinates.items():
                    # Add 'name' attribute to each node along with its position
                    self.graph.add_node(node, pos=(coords[0], coords[1]), name=node)

                # Add edges with weights
                for start_node, neighbors in data.get("graph", {}).items():
                    for end_node, weight in neighbors.items():
                        self.graph.add_edge(start_node, end_node, weight=weight)

                print("✅ Graph loaded successfully.")
        except Exception as e:
            print(f"❗ Error loading graph: {e}")

    def get_graph(self):
        """Returns the graph object."""
        return self.graph

    def get_coordinates(self):
        """Returns the coordinates of the nodes."""
        return self.coordinates

    def find_shortest_path(self, start_node, end_node):
        """Find the shortest path between two nodes using Dijkstra's algorithm."""
        if start_node not in self.graph.nodes or end_node not in self.graph.nodes:
            print(f"❗ Invalid nodes: {start_node} or {end_node} do not exist.")
            return None

        try:
            # Use NetworkX built-in Dijkstra's algorithm to find the shortest path
            path = nx.shortest_path(self.graph, source=start_node, target=end_node, weight="weight")
            print(f"🛤️ Shortest path from {start_node} to {end_node}: {path}")
            return path
        except nx.NetworkXNoPath:
            print(f"❗ No valid path found from {start_node} to {end_node}.")
            return None

    def draw_graph(self):
        """Visualize the graph using Matplotlib."""
        try:
            pos = nx.get_node_attributes(self.graph, 'pos')
            labels = nx.get_edge_attributes(self.graph, 'weight')

            # Draw the graph with node labels, edge weights, and custom styling
            nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_weight='bold')
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
            plt.title("Graph Visualization")
            plt.show()
        except Exception as e:
            print(f"❗ Error visualizing graph: {e}")

# Example Usage
if __name__ == "__main__":
    # Replace the path with the actual path to your nav_graph.json file
    graph = NavGraph("data/nav_graph.json")
    
    # Draw the graph visualization
    graph.draw_graph()

    # Find the shortest path between nodes "A" and "D"
    graph.find_shortest_path("A", "D")
