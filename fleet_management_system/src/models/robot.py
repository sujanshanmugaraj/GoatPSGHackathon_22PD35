

import time
from src.utils.helpers import a_star
from src.models.nav_graph import NavGraph

class Robot:
    def __init__(self, robot_id, start_node, nav_graph):
        """
        Initialize the robot with an ID, start node, and a navigation graph.
        """
        self.id = robot_id
        self.position = start_node
        self.start_node = start_node
        self.destination = None
        self.status = "idle"
        self.nav_graph = nav_graph  # Store the navigation graph
        self.path = []
        self.last_position = start_node
        self.last_movement_time = time.time()
        self.task_completed = False

    def assign_task(self, destination):
        """
        Assign a task to the robot by setting its destination and planning a path using A*.
        """
        if self.status == "moving":
            print(f"⚠️ Robot {self.id} is already moving. Cannot assign a new task.")
            return

        print(f"🚀 Robot {self.id} assigned to move from {self.position} to {destination}")

        # Ensure nodes are properly checked for names
        name_to_index = {data['name']: i for i, data in self.nav_graph.graph.nodes(data=True) if 'name' in data}

        # Debugging output to see available nodes
        print("🔎 Available Nodes:", name_to_index)
        print("🔎 Checking if node exists: Start -", self.position, "Destination -", destination)

        if self.position not in name_to_index:
            print(f"❗ Invalid start node: {self.position}")
            return
        
        if destination not in name_to_index:
            print(f"❗ Invalid destination: {destination}")
            return

        start_index = name_to_index[self.position]
        end_index = name_to_index[destination]

        # Plan path using A* algorithm
        path = a_star(self.nav_graph.graph, self.nav_graph.get_coordinates(), start_index, end_index)

        if not path:
            print(f"❗ No path found from {self.position} to {destination}")
            return

        print(f"🛤️ Path for Robot {self.id}: {path}")
        self.status = "moving"
        self.path = path
        self.destination = destination
        self.task_completed = False

    def update_position(self):
        """
        Update the robot's position along its path.
        """
        if self.status != "moving" or not self.path or self.task_completed:
            return

        # Move to the next node
        next_node = self.path.pop(0)
        print(f"📍 Robot {self.id} moved to {next_node}")
        self.position = next_node

        # Check if the robot reached its destination
        if not self.path and self.status != "task complete" and not self.task_completed:
            self.status = "task complete"
            self.destination = None
            print(f"✅ Robot {self.id} has completed its task at {self.position}")
            self.task_completed = True

    def detect_stuck(self):
        """
        Detect if the robot is stuck by checking for lack of movement.
        """
        if self.status == "moving" and self.position == self.last_position:
            if time.time() - self.last_movement_time > 15:
                print(f"⏳ Robot {self.id} is stuck at {self.position}")
                return True
        else:
            self.last_position = self.position
            self.last_movement_time = time.time()
        return False

    def reset_for_new_task(self):
        """
        Reset the robot to an idle state, ready for a new task.
        """
        if self.status == "task complete":
            print(f"🔄 Robot {self.id} is now idle and ready for a new task.")
            self.status = "idle"
            self.task_completed = False
            self.position = self.start_node
            self.path = []

    def get_status(self):
        """
        Return the current status of the robot.
        """
        return f"Robot {self.id}: Status={self.status}, Position={self.position}, Destination={self.destination if self.destination else 'N/A'}"
