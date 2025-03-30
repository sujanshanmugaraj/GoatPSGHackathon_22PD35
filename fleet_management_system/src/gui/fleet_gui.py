# src/gui/fleet_gui.py
import tkinter as tk

class FleetManagementApp:
    def __init__(self, root, fleet_manager, traffic_manager):
        self.root = root
        self.root.title("Fleet Management System")

        self.fleet_manager = fleet_manager
        self.traffic_manager = traffic_manager

        # Create canvas for environment visualization
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        # Store robot and vertex data
        self.vertices = {}
        self.robots = {}

        # Initialize the environment
        self.create_vertices()
        self.draw_environment()

    def create_vertices(self):
        # Define the positions of the vertices (locations)
        self.vertices = {
            'A': (100, 100),
            'B': (300, 100),
            'C': (100, 300),
            'D': (300, 300)
        }

    def draw_environment(self):
        # Draw vertices (locations)
        for vertex, (x, y) in self.vertices.items():
            self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue", outline="black")
            self.canvas.create_text(x, y, text=vertex, fill="white", font=('Helvetica', 12))

        # Draw lanes (connections between vertices)
        self.canvas.create_line(self.vertices['A'], self.vertices['B'], fill="black", width=2)
        self.canvas.create_line(self.vertices['A'], self.vertices['C'], fill="black", width=2)
        self.canvas.create_line(self.vertices['B'], self.vertices['D'], fill="black", width=2)
        self.canvas.create_line(self.vertices['C'], self.vertices['D'], fill="black", width=2)

    def spawn_robot(self, vertex):
        # When a vertex is clicked, spawn a robot there
        if vertex not in self.robots:
            robot_id = f"robot_{len(self.robots)+1}"
            x, y = self.vertices[vertex]
            robot = self.canvas.create_oval(x-15, y-15, x+15, y+15, fill="green", outline="black")
            self.robots[robot_id] = robot
            print(f"Robot {robot_id} spawned at {vertex}")

    def assign_task(self, robot_id, destination):
        # Logic for assigning tasks to robots
        robot = self.robots.get(robot_id)
        if robot:
            print(f"Robot {robot_id} assigned to move to {destination}")
            # Change robot color to indicate movement (just for visualization)
            self.canvas.itemconfig(robot, fill="red")
