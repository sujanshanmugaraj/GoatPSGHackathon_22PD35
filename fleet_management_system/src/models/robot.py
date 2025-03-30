import uuid

class Robot:
    def __init__(self, start_node, traffic_manager):
        """
        Initialize a robot with a unique ID, starting position, and the traffic manager.
        """
        self.id = str(uuid.uuid4())[:8]  # Short unique ID
        self.position = start_node
        self.start_node = start_node  # Track the start node
        self.destination = None
        self.status = "idle"  # Possible statuses: idle, moving, waiting, charging, task complete
        self.traffic_manager = traffic_manager  # Assigning traffic_manager to robot
        self.assigned_lane = None  # Track the lane assigned to this robot

    def assign_task(self, destination):
        """
        Assign a destination to the robot if it is idle.
        """
        if self.status == "idle":
            self.destination = destination
            self.status = "moving"
            print(f"🚀 Robot {self.id} assigned to move from {self.position} to {self.destination}")
            
            # Request lane access before starting movement
            if not self.traffic_manager.request_lane_access(self.position, self.destination, self.id):
                self.status = "waiting"  # Set the robot to waiting if lane is occupied
            else:
                self.status = "moving"
                self.assigned_lane = (self.position, self.destination)  # Save the assigned lane
        elif self.status == "moving":
            print(f"⚠️ Robot {self.id} is currently moving to {self.destination}. Please wait.")
        else:
            print(f"⚠️ Robot {self.id} is busy. Status: {self.status}")

    def update_position(self, new_position):
        """
        Update the robot's position and check if the task is complete.
        """
        self.position = new_position
        print(f"📍 Robot {self.id} moved to {self.position}")

        if self.position == self.destination:
            self.status = "task complete"
            print(f"✅ Robot {self.id} has completed its task at {self.destination}.")
            self.destination = None  # Clear the destination after completion
            self.release_lane()  # Release the lane after completing the task
        else:
            self.status = "moving"
            print(f"🚙 Robot {self.id} is still moving towards {self.destination}.")

    def release_lane(self):
        """
        Release the lane after the robot completes its task.
        """
        if self.status == "task complete" and self.assigned_lane:
            # Release the lane in the traffic manager
            start_node, end_node = self.assigned_lane
            self.traffic_manager.release_lane(start_node, end_node, self.id)
            print(f"✅ Robot {self.id} has released the lane from {start_node} to {end_node}")
            self.assigned_lane = None  # Clear the assigned lane after releasing it
        else:
            print(f"⚠️ Robot {self.id} is not ready to release lane. Status: {self.status}")

    def get_status(self):
        """
        Get the current status of the robot.
        """
        return f"🤖 Robot {self.id} is at {self.position}, Status: {self.status}"
