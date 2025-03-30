from src.gui.fleet_gui import FleetManagementApp
from src.controllers.fleet_manager import FleetManager
from src.controllers.traffic_manager import TrafficManager
from src.models.robot import Robot
import tkinter as tk

class FleetSimulation:
    def __init__(self):
        # Initialize the traffic manager and fleet manager
        self.traffic_manager = TrafficManager()
        self.fleet_manager = FleetManager()

        # Initialize the Tkinter window for GUI
        self.root = tk.Tk()
        # Initialize the FleetManagementApp with the root Tk window and the traffic and fleet managers
        self.app = FleetManagementApp(self.root, self.fleet_manager, self.traffic_manager)

    def run_simulation(self):
        # Create robots and assign them tasks
        robot1 = Robot(start_node="A", traffic_manager=self.traffic_manager)
        robot2 = Robot(start_node="B", traffic_manager=self.traffic_manager)

        # Simulate robots' movements
        lane1_assigned = self.traffic_manager.request_lane_access("A", "C", robot1.id)  # Request lane for robot1
        lane2_assigned = self.traffic_manager.request_lane_access("B", "D", robot2.id)  # Request lane for robot2

        if lane1_assigned and lane2_assigned:
            # Assign tasks to the robots
            robot1.assign_task("C")  # Robot1 moving from A to C
            robot2.assign_task("D")  # Robot2 moving from B to D

            # Simulate robots' movements
            robot1.update_position("B")  # Robot1 moves from A to B (doesn't reach destination yet)
            robot1.update_position("C")  # Robot1 reaches its destination (C), task complete

            robot2.update_position("C")  # Robot2 moves from B to C (doesn't reach destination yet)
            robot2.update_position("D")  # Robot2 reaches its destination (D), task complete

            # Check status of robots
            print(robot1.get_status())  # Robot1 status
            print(robot2.get_status())  # Robot2 status

            # Release lanes once robots complete their tasks (ensure task is complete before release)
            self.traffic_manager.release_lane("A", "C", robot1.id)  # Robot1 releases the lane from A to C
            self.traffic_manager.release_lane("B", "D", robot2.id)  # Robot2 releases the lane from B to D

        # Run the GUI loop
        self.root.mainloop()


# Main function to initialize and run the simulation
def main():
    # Create and run the simulation
    simulation = FleetSimulation()
    simulation.run_simulation()

if __name__ == "__main__":
    main()
