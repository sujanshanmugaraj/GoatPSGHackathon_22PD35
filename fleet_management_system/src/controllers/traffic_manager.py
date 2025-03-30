
# src/controllers/traffic_manager.py

class TrafficManager:
    def __init__(self):
        """
        Initialize the Traffic Manager with an empty lane management system.
        """
        self.lane_occupancy = {}  # Tracks which lanes are occupied

    def request_lane_access(self, start_node, end_node, robot_id):
        """
        Request access to a lane from start_node to end_node.
        Returns True if access is granted, otherwise False.
        """
        lane_key = (start_node, end_node)
        reverse_lane_key = (end_node, start_node)

        # Check if the lane is available (or if the reverse lane is already occupied)
        if lane_key not in self.lane_occupancy and reverse_lane_key not in self.lane_occupancy:
            self.lane_occupancy[lane_key] = robot_id
            print(f"✅ Robot {robot_id} granted access to lane from {start_node} to {end_node}.")
            return True
        else:
            print(f"🚧 Robot {robot_id} waiting. Lane from {start_node} to {end_node} is occupied.")
            return False

    def release_lane(self, start_node, end_node, robot_id):
        """
        Release the lane after the robot completes its movement.
        """
        lane_key = (start_node, end_node)

        # Ensure the robot is the owner of the lane before releasing it
        if lane_key in self.lane_occupancy and self.lane_occupancy[lane_key] == robot_id:
            # Release the lane by removing it from the lane_occupancy dictionary
            del self.lane_occupancy[lane_key]
            print(f"🔓 Robot {robot_id} released lane from {start_node} to {end_node}.")
        else:
            # This error happens when the robot either tries to release a lane that it doesn't own,
            # or the lane has already been cleared.
            print(f"⚠️ Error: Robot {robot_id} tried to release a lane it doesn't own or the lane is no longer assigned.")

    def get_lane_status(self):
        """
        Display the current lane occupancy status.
        """
        if not self.lane_occupancy:
            print("🌿 All lanes are free.")
        else:
            print("🚦 Current Lane Occupancy:")
            for lane, robot in self.lane_occupancy.items():
                print(f"  {lane[0]} → {lane[1]}: Occupied by Robot {robot}")
