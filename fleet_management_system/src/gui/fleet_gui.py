import tkinter as tk
from tkinter import messagebox
import time

class FleetManagementApp:
    def __init__(self, root, fleet_manager, traffic_manager):
        self.root = root
        self.fleet_manager = fleet_manager
        self.traffic_manager = traffic_manager
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.node_positions = {
            "A": (50, 200),
            "B": (50, 300),
            "C": (200, 150),
            "D": (200, 350),
            "E": (400, 150),
            "F": (400, 350)
        }
        self.robot_positions = {}
        self.robot_colors = {}

        self.create_graph_visualization()

        # Buttons for control
        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_simulation)
        self.reset_button.pack(side=tk.RIGHT)

        self.selected_robot = None

        # Add click listeners
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # Log box at the bottom of the window
        self.log_box = tk.Text(root, height=10, width=50)
        self.log_box.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def log_to_gui(self, message):
        """
        Append logs to the GUI log box.
        """
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.yview(tk.END)  # Auto-scroll to the bottom

    def create_graph_visualization(self):
        """
        Draws the nodes and edges on the canvas.
        """
        # Draw nodes
        for node, (x, y) in self.node_positions.items():
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue", outline="black")
            self.canvas.create_text(x, y, text=node, font=("Arial", 14))

        # Draw edges (lanes)
        lanes = [("A", "C"), ("B", "D"), ("C", "E"), ("D", "F")]
        for lane in lanes:
            x1, y1 = self.node_positions[lane[0]]
            x2, y2 = self.node_positions[lane[1]]
            self.canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)

    def start_simulation(self):
        """
        Start the fleet management simulation and visualize the movement.
        """
        self.fleet_manager.assign_tasks(self.traffic_manager)
        self.update_visualization()
        self.log_to_gui("🚀 Simulation started.")

    def reset_simulation(self):
        """
        Reset the simulation for a fresh start.
        """
        self.canvas.delete("robot")
        self.robot_positions.clear()
        self.robot_colors.clear()
        print("🔄 Simulation Reset.")
        self.log_to_gui("🔄 Simulation Reset.")

    def update_visualization(self):
        """
        Update the visualization to reflect robot movements.
        """
        for robot in self.fleet_manager.robots:
            if robot.id not in self.robot_positions:
                self.robot_positions[robot.id] = self.node_positions[robot.position]
                self.robot_colors[robot.id] = f"#{hash(robot.id) % 0xFFFFFF:06x}"

            if robot.status == "moving":
                robot.update_position()
                self.log_to_gui(f"🚗 Robot {robot.id} is moving to {robot.position}")

            # Update robot position on canvas
            x, y = self.node_positions[robot.position]
            self.robot_positions[robot.id] = (x, y)

            # Color based on status
            if robot.status == "moving":
                self.robot_colors[robot.id] = "green"  # Moving robots are green
            elif robot.status == "waiting":
                self.robot_colors[robot.id] = "yellow"  # Waiting robots are yellow
            elif robot.status == "charging":
                self.robot_colors[robot.id] = "blue"  # Charging robots are blue
            elif robot.status == "task complete":
                self.robot_colors[robot.id] = "gray"  # Task complete robots are gray

            self.canvas.create_oval(
                x-10, y-10, x+10, y+10,
                fill=self.robot_colors[robot.id],
                outline="black",
                tags="robot"
            )
            self.canvas.create_text(x, y-20, text=f"🤖 {robot.id[:5]}", tags="robot", font=("Arial", 8))

            if robot.status == "task complete":
                print(f"✅ Robot {robot.id} has completed its task at {robot.position}")
                self.log_to_gui(f"✅ Robot {robot.id} has completed its task at {robot.position}")

        self.root.after(500, self.update_visualization)  # Update every 500ms

    def on_canvas_click(self, event):
        """
        Handle click events on the canvas.
        """
        # Check if a robot is selected
        if self.selected_robot:
            self.assign_task_to_robot(event.x, event.y)
        else:
            self.spawn_robot(event.x, event.y)

    def spawn_robot(self, x, y):
        """
        Spawn a robot at the clicked location.
        """
        # Find closest node based on click location
        closest_node = None
        min_distance = float('inf')
        for node, (node_x, node_y) in self.node_positions.items():
            distance = ((x - node_x)**2 + (y - node_y)**2)**0.5
            if distance < min_distance:
                min_distance = distance
                closest_node = node

        if closest_node:
            robot_id = f"Robot-{len(self.robot_positions) + 1}"
            self.fleet_manager.spawn_robot(closest_node, robot_id)  # Spawn robot at the closest node
            self.robot_positions[robot_id] = self.node_positions[closest_node]
            self.robot_colors[robot_id] = f"#{hash(robot_id) % 0xFFFFFF:06x}"
            print(f"✅ Robot {robot_id} spawned at {closest_node}")
            self.log_to_gui(f"✅ Robot {robot_id} spawned at {closest_node}")

            # Update visualization
            self.update_visualization()

    def assign_task_to_robot(self, x, y):
        """
        Assign a task to the selected robot to move to the clicked location.
        """
        # Find closest node based on click location
        closest_node = None
        min_distance = float('inf')
        for node, (node_x, node_y) in self.node_positions.items():
            distance = ((x - node_x)**2 + (y - node_y)**2)**0.5
            if distance < min_distance:
                min_distance = distance
                closest_node = node

        if closest_node:
            self.fleet_manager.assign_task(self.selected_robot, closest_node)
            print(f"✅ Task assigned to {self.selected_robot} to go to {closest_node}")
            self.log_to_gui(f"✅ Task assigned to {self.selected_robot} to go to {closest_node}")
            self.selected_robot = None  # Reset robot selection

    def select_robot_for_task(self, robot_id):
        """
        Select a robot for task assignment.
        """
        self.selected_robot = robot_id
        print(f"✅ Robot {robot_id} selected for task assignment.")
        self.log_to_gui(f"✅ Robot {robot_id} selected for task assignment.")
