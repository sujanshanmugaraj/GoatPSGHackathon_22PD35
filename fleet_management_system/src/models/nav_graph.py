import json
import networkx as nx
import matplotlib.pyplot as plt

class NavGraph:
    def __init__(self, file_path):
        """Initialize the graph from a JSON file."""
        self.graph = nx.Graph()
        self.file_path = file_path
        self.load_graph()

    def load_graph(self):
        """Load graph data from the JSON file and construct the graph."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)

            # Add nodes (vertices)
            for node in data.get("nodes", []):
                self.graph.add_node(node["id"], pos=(node["x"], node["y"]))

            # Add edges (connections)
            for edge in data.get("edges", []):
                self.graph.add_edge(edge["from"], edge["to"], weight=edge["cost"])

            print("Graph loaded successfully.")
        except Exception as e:
            print(f"Error loading graph: {e}")

    def find_shortest_path(self, start_node, end_node):
        """Use Dijkstra's algorithm to find the shortest path."""
        try:
            path = nx.dijkstra_path(self.graph, start_node, end_node, weight='weight')
            print(f"Shortest path from {start_node} to {end_node}: {path}")
            return path
        except nx.NetworkXNoPath:
            print(f"No path found between {start_node} and {end_node}.")
            return []

    def draw_graph(self):
        """Visualize the graph using Matplotlib."""
        pos = nx.get_node_attributes(self.graph, 'pos')
        labels = nx.get_edge_attributes(self.graph, 'weight')

        nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_weight='bold')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.title("Graph Visualization")
        plt.show()

# Example Usage
if __name__ == "__main__":
    graph = NavGraph("data/nav_graph.json")
    graph.draw_graph()
