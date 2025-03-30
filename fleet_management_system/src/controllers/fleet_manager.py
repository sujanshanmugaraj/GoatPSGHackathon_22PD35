from src.models.robot import Robot
from src.controllers.traffic_manager import TrafficManager

class FleetManager:
    def __init__(self):
        self.robots = []
        self.traffic_manager = TrafficManager()

    def spawn_robot(self, start_node):
        """
        Spawn a new robot at a given starting position.
        """
        new_robot = Robot(start_node)
        self.robots.append(new_robot)
        print(f"🤖 Spawned Robot {new_robot.id} at {start_node}")

    def assign_task(self, robot_id, destination):
        """
        Assign a task to a robot, with traffic management.
        """
        for robot in self.robots:
            if robot.id == robot_id:
                print(f"🚧 Robot {robot_id} assigned to move from {robot.position} to {destination}")

                # Request lane access using TrafficManager
                if self.traffic_manager.request_lane_access(robot.position, destination, robot_id):
                    robot.update_position(destination)
                    self.traffic_manager.release_lane(robot.position, destination, robot_id)
                else:
                    print(f"⏳ Robot {robot_id} is waiting for the lane to clear.")
                    # You could add the robot to a waiting queue or handle re-assignment logic here.
                return
        print(f"❗ Robot {robot_id} not found.")

    def print_fleet_status(self):
        """
        Display the current status of all robots and lane occupancy.
        """
        print("\n--- 🚀 Fleet Status ---")
        for robot in self.robots:
            print(robot.get_status())
        self.traffic_manager.get_lane_status()
        print("----------------------")

# Example Usage
if __name__ == "__main__":
    manager = FleetManager()

    # Spawn robots
    manager.spawn_robot("A")
    manager.spawn_robot("B")

    manager.print_fleet_status()

    # Assign tasks
    robot1_id = manager.robots[0].id
    robot2_id = manager.robots[1].id

    manager.assign_task(robot1_id, "C")
    manager.assign_task(robot2_id, "C")  # Intentional conflict for testing

    manager.print_fleet_status()
