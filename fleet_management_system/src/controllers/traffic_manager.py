
class TrafficManager:
    def __init__(self):
        """
        Initialize the Traffic Manager with an empty lane management system.
        """
        self.lane_status = {}  # Tracks the status of each lane

    def request_lane_access(self, start_node, end_node, robot_id):
        """
        Request access to a lane from start_node to end_node.
        Returns True if access is granted, otherwise False.
        """
        lane_key = (start_node, end_node)
        reverse_lane_key = (end_node, start_node)

        # Check if the lane or its reverse is occupied
        if self.lane_status.get(lane_key, "free") != "free" or self.lane_status.get(reverse_lane_key, "free") != "free":
            print(f"🚫 Lane from {start_node} to {end_node} is occupied. Robot {robot_id} cannot proceed.")
            return False

        # Grant access to the lane
        self.lane_status[lane_key] = f"Occupied by {robot_id}"
        print(f"✅ Robot {robot_id} granted access to lane from {start_node} to {end_node}.")
        return True

    def release_lane(self, start_node, end_node, robot_id, robot_status):
        """
        Release a lane once a robot has completed its task.
        """
        lane_key = (start_node, end_node)

        if lane_key in self.lane_status and self.lane_status[lane_key] == f"Occupied by {robot_id}":
            if robot_status == "task complete" or robot_status == "done":
                self.lane_status[lane_key] = "free"
                print(f"🔓 Robot {robot_id} successfully released lane from {start_node} to {end_node}.")
            else:
                print(f"⚠️ Robot {robot_id} cannot release lane. Status: {robot_status}")
        else:
            print(f"⚠️ Error: Lane from {start_node} to {end_node} is not occupied by Robot {robot_id}.")

    def get_lane_status(self):
        """
        Display the current lane occupancy status.
        """
        if not self.lane_status:
            print("🌿 All lanes are free.")
        else:
            print("🚦 Current Lane Occupancy:")
            for (start, end), status in self.lane_status.items():
                print(f"  {start} → {end}: {status}")

    def get_traffic_data(self):
        """
        Get lane status as a dictionary for external use (e.g., dashboards).
        """
        return self.lane_status
