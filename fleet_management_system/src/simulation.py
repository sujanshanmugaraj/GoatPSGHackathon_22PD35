import time
from src.controllers.fleet_manager import FleetManager
from src.controllers.traffic_manager import TrafficManager


class Simulation:
    def __init__(self, fleet_manager: FleetManager, traffic_manager: TrafficManager):
        """
        Initialize the simulation with the fleet manager and traffic manager.
        """
        self.fleet_manager = fleet_manager
        self.traffic_manager = traffic_manager

    def run_simulation(self):
        """
        Run the simulation, which includes robot task assignment, traffic management, and status monitoring.
        """
        print("🚀 Starting simulation...")

        # Start by spawning robots and adding tasks to the queue
        self.fleet_manager.spawn_robot("A")  # Spawning robot at location "A"
        self.fleet_manager.spawn_robot("B")  # Spawning robot at location "B"

        self.fleet_manager.add_task("A", "C", priority=1)
        self.fleet_manager.add_task("B", "D", priority=1)
        self.fleet_manager.add_task("C", "E", priority=2)
        self.fleet_manager.add_task("D", "F", priority=3)

        # Start assigning tasks to robots
        self.fleet_manager.assign_tasks(self.traffic_manager)

        # Simulate robot movements
        while True:
            self.fleet_manager.monitor_and_reassign_tasks(self.traffic_manager)
            time.sleep(1)  # Simulate a small time step for the robots to perform actions
            self.traffic_manager.get_lane_status()  # Print the current lane status

            # Check if all tasks are completed and break the loop if true
            if all(robot.status == "task complete" for robot in self.fleet_manager.robots):
                print("✅ All tasks are completed!")
                break


# Main entry point to run the simulation
if __name__ == "__main__":
    fleet_manager = FleetManager()
    traffic_manager = TrafficManager()
    simulation = Simulation(fleet_manager, traffic_manager)
    simulation.run_simulation()

