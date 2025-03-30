from queue import PriorityQueue
from src.models.robot import Robot
from src.models.nav_graph import NavGraph

class FleetManager:
    def __init__(self):
        # Assuming you have a navigation graph or some structure that the robots use
        self.nav_graph = NavGraph()  # Assuming NavGraph is an object that holds the navigation data
        self.robots = []
        self.tasks = []
        self.task_queue = PriorityQueue()
        self.task_counter = 0

    def spawn_robot(self, start_node, robot_id):
        """
        Spawns a robot at the given node.
        """
        # Create a new Robot object, passing the nav_graph
        new_robot = Robot(robot_id, start_node, self.nav_graph)  # Pass nav_graph here
        self.robots.append(new_robot)
        print(f"✅ Robot {robot_id} spawned at {start_node}.")
    
    def add_task(self, start_node, end_node, priority=1):
        """
        Add a new task to the priority queue with priority management.
        """
        self.task_counter += 1
        self.task_queue.put((priority, self.task_counter, start_node, end_node))
        print(f"📝 Task added: {start_node} → {end_node} with priority {priority}")

    # def assign_tasks(self, traffic_manager):
    #     """
    #     Assign tasks to available robots using priority-based scheduling.
    #     """
    #     while not self.task_queue.empty():
    #         # Get all idle robots
    #         available_robots = [robot for robot in self.robots if robot.status == "idle"]
            
    #         if not available_robots:
    #             print("⏳ No available robots. Tasks will remain in queue.")
    #             break

    #         # Fetch the highest-priority task
    #         _, _, start_node, end_node = self.task_queue.get()
    #         robot = available_robots[0]

    #         # Request lane access using traffic manager
    #         if traffic_manager.request_lane_access(start_node, end_node, robot.id):
    #             robot.assign_task(end_node)
    #         else:
    #             print(f"❗ Lane from {start_node} to {end_node} is blocked. Task requeued.")
    #             self.add_task(start_node, end_node, priority=2)  # Lower priority on requeue

    def assign_tasks(self, traffic_manager):
        """
    Assign tasks to available robots using priority-based scheduling.
    """
        while not self.task_queue.empty():
            # Get all idle robots
            available_robots = [robot for robot in self.robots if robot.status == "idle"]
        
            if not available_robots:
                print("⏳ No available robots. Tasks will remain in queue.")
                break

        # Fetch the highest-priority task
            _, _, start_node, end_node = self.task_queue.get()
            robot = available_robots[0]

        # Request lane access using traffic manager
            if traffic_manager.request_lane_access(start_node, end_node, robot.id):
                robot.assign_task(end_node)
            else:
                print(f"❗ Lane from {start_node} to {end_node} is blocked. Task requeued.")
                self.add_task(start_node, end_node, priority=2)  # Lower priority on requeue

    def monitor_and_reassign_tasks(self, traffic_manager):
        """
        Monitor and manage tasks by checking robot statuses, releasing lanes, 
        and reassigning tasks when necessary.
        """
        for robot in self.robots:
            # Handle completed tasks
            if robot.status == "task complete":
                # Release the lane
                traffic_manager.release_lane(robot.start_node, robot.position, robot.id, robot.status)
                print(f"✅ Robot {robot.id} completed its task at {robot.position}")

                # Reset robot state
                robot.status = "idle"
                robot.destination = None

                # Assign new tasks if available
                self.assign_tasks(traffic_manager)

            # Handle stuck robots
            elif robot.status == "moving" and robot.detect_stuck():
                print(f"⚠️ Robot {robot.id} is stuck at {robot.position}. Reallocating task.")
                robot.status = "idle"
                self.add_task(robot.position, robot.destination, priority=1)
