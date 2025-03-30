import tkinter as tk
from tkinter import ttk
from src.controllers.fleet_manager import FleetManager
from src.controllers.traffic_manager import TrafficManager

class Dashboard:
    def __init__(self, root, fleet_manager, traffic_manager):
        self.root = root
        self.root.title("Fleet Management - Real-Time Dashboard")
        self.root.geometry("800x600")

        self.fleet_manager = fleet_manager
        self.traffic_manager = traffic_manager

        # Frames for organization
        self.robot_frame = ttk.LabelFrame(root, text="Robot Status", padding=10)
        self.robot_frame.pack(fill="both", padx=10, pady=10, expand=True)

        self.task_frame = ttk.LabelFrame(root, text="Task Progress", padding=10)
        self.task_frame.pack(fill="both", padx=10, pady=10, expand=True)

        self.traffic_frame = ttk.LabelFrame(root, text="Traffic Status", padding=10)
        self.traffic_frame.pack(fill="both", padx=10, pady=10, expand=True)

        self.robot_tree = self.create_treeview(self.robot_frame, ["ID", "Position", "Status", "Destination"])
        self.task_tree = self.create_treeview(self.task_frame, ["Start", "End", "Priority", "Status"])
        self.traffic_tree = self.create_treeview(self.traffic_frame, ["Lane", "Status"])

        # Start auto-update
        self.update_dashboard()

    def create_treeview(self, parent, columns):
        """
        Create a table-like Treeview with the given column names.
        """
        tree = ttk.Treeview(parent, columns=columns, show="headings", height=5)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")
        tree.pack(fill=tk.BOTH, expand=True)
        return tree

    def update_dashboard(self):
        """
        Refresh the data for robots, tasks, and traffic.
        """
        self.update_robot_status()
        self.update_task_progress()
        self.update_traffic_status()

        # Refresh every 1 second
        self.root.after(1000, self.update_dashboard)

    def update_robot_status(self):
        """
        Update the robot status in the UI.
        """
        for row in self.robot_tree.get_children():
            self.robot_tree.delete(row)

        for robot in self.fleet_manager.robots:
            status = robot.status
            destination = robot.destination if robot.destination else "N/A"
            self.robot_tree.insert("", "end", values=(robot.id, robot.position, status, destination))

    def update_task_progress(self):
        """
        Update the task progress in the UI.
        """
        for row in self.task_tree.get_children():
            self.task_tree.delete(row)

        tasks = self.fleet_manager.task_queue.queue
        for priority, _, start_node, end_node in tasks:
            self.task_tree.insert("", "end", values=(start_node, end_node, priority, "Pending"))

        for robot in self.fleet_manager.robots:
            if robot.status == "moving":
                self.task_tree.insert("", "end", values=(robot.start_node, robot.destination, "N/A", "In Progress"))

    def update_traffic_status(self):
        """
        Update the traffic status in the UI.
        """
        for row in self.traffic_tree.get_children():
            self.traffic_tree.delete(row)

        traffic_data = self.traffic_manager.get_traffic_data()
        for lane, status in traffic_data.items():
            self.traffic_tree.insert("", "end", values=(lane, status))


def main():
    # Initialize FleetManager and TrafficManager
    fleet_manager = FleetManager()
    traffic_manager = TrafficManager()

    # Create the root Tkinter window
    root = tk.Tk()

    # Create the dashboard
    dashboard = Dashboard(root, fleet_manager, traffic_manager)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
