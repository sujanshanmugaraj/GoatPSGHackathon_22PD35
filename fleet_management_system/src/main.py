import logging
import time
from tkinter import Tk
from src.controllers.fleet_manager import FleetManager
from src.controllers.traffic_manager import TrafficManager
from src.gui.fleet_gui import FleetManagementApp  # Assuming you have this GUI file

class FleetSimulation:
    def __init__(self):
        """Initialize the FleetSimulation with the FleetManager, TrafficManager, and GUI components."""
        # Initialize traffic manager and fleet manager
        self.traffic_manager = TrafficManager()
        self.fleet_manager = FleetManager()

        # Initialize the Tkinter window for GUI
        self.root = Tk()
        self.root.title("Fleet Management Simulation")
        
        # Initialize the fleet management app GUI
        self.app = FleetManagementApp(self.root, self.fleet_manager, self.traffic_manager)
        
        # Set up logging
        self.setup_logging()

    def setup_logging(self):
        """Set up logging to both file and console."""
        # Create a logger
        self.logger = logging.getLogger('FleetSimulationLogger')
        self.logger.setLevel(logging.DEBUG)

        # Log to a file
        file_handler = logging.FileHandler(r'C:\Users\Sujan.S\OneDrive\Documents\GitHub\GoatPSGHackathon_-22PD35-\fleet_management_system\logs\fleet_logs.txt', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)
        self.logger.addHandler(file_handler)

        # Log to console as well (optional, for immediate feedback)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Info level to keep console clean
        console_handler.setFormatter(file_format)
        self.logger.addHandler(console_handler)

    def run_simulation(self):
        """Runs the simulation, handling robot movements, task assignments, and GUI updates."""
        self.logger.info("Starting simulation...")  # Removed emoji for console compatibility
        
        # Spawn robots at initial positions with unique robot IDs
        self.fleet_manager.spawn_robot("A", "Robot-1")  # Robot-1 at node A
        self.fleet_manager.spawn_robot("B", "Robot-2")  # Robot-2 at node B

        # Add tasks with priorities
        self.fleet_manager.add_task("A", "C", priority=1)
        self.fleet_manager.add_task("B", "D", priority=1)
        self.fleet_manager.add_task("C", "E", priority=2)
        self.fleet_manager.add_task("D", "F", priority=3)

        # Assign initial tasks
        self.fleet_manager.assign_tasks(self.traffic_manager)

        # Simulation loop with a step limit to avoid infinite loops
        max_steps = 100
        step_count = 0

        while any(robot.status in ["moving", "idle"] for robot in self.fleet_manager.robots):
            if step_count >= max_steps:
                self.logger.info("Simulation stopped: Exceeded maximum steps.")
                break

            for robot in self.fleet_manager.robots:
                if robot.status == "moving":
                    robot.update_position()  # Update robot's position based on its movement
                    self.logger.debug(f"Robot {robot.id} moved to {robot.position}")  # Use robot.id instead of robot.name
                elif robot.status == "task complete":
                    robot.status = "done"  # Mark robot as done after completing the task
                    self.logger.info(f"Robot {robot.id} has completed its task at {robot.position}")  # Use robot.id instead of robot.name

            # Monitor and reassign tasks if necessary (can handle task priority logic here)
            self.fleet_manager.monitor_and_reassign_tasks(self.traffic_manager)

            # Update GUI visualization
            self.app.update_visualization()

            step_count += 1
            time.sleep(0.5)  # Adjust for visualization speed (slower = more visible movements)

        # Print final status of robots
        for robot in self.fleet_manager.robots:
            self.logger.info(robot.get_status())

        self.logger.info("Simulation completed.")

        # Start GUI main loop
        self.root.mainloop()

# Main function to start the simulation
def main():
    simulation = FleetSimulation()
    simulation.run_simulation()

if __name__ == "__main__":
    main()
#successfully committed!
