# Fleet Management System with Traffic Negotiation for Multi-Robots

## Overview

The Fleet Management System is a simulation of a fleet of robots that perform tasks based on priority while moving along a network of nodes. The system includes a graphical user interface (GUI) that visualizes the robots' movements and task completions. It also incorporates logging for robot actions, path choices, waiting conditions, and task completions.
 
## Features:

### Robot Spawning and Task Assignment:

Users can spawn robots at specific locations (vertices) in the environment via the GUI.

Tasks are assigned to robots through the GUI by selecting robots and destination vertices interactively.

### Robot Navigation:

Robots navigate through predefined paths (lanes) between vertices based on the tasks assigned to them.

Real-time robot movement is visualized on the GUI, showing progress along the path.

### Traffic Negotiation & Collision Avoidance:

Robots dynamically negotiate traffic, avoiding lane collisions and managing congestion.

Robots can wait or queue at blocked lanes or intersections to ensure smooth movement.

Lane occupation is continuously checked to prevent path conflicts.

### Real-Time Robot Status Visualization:

Robots' statuses are visually indicated in the GUI, showing whether they are moving, waiting, charging, or have completed tasks.

Robot status updates are logged in real-time for user visibility.

### Task Management:

Tasks are assigned based on priorities, ensuring high-priority tasks are completed first.

Robots can complete tasks and report their status (task complete, waiting, moving).

### Dynamic Task Reassignment:

If a task is blocked (due to traffic congestion or a lane being occupied), the system dynamically monitors and reassigns tasks to available robots.

Task reassignments are handled based on real-time traffic and robot availability.

### Environment Visualization:

The environment, including vertices and lanes, is visually displayed on the GUI.

Vertices are interactable (clickable) to spawn robots or assign tasks, providing a clear interface for users.

### Real-Time Logging:

All robot actions, movements, task completions, and traffic negotiations are logged to a file (fleet_logs.txt).

Logs include detailed information such as path choices, robot status updates, and waiting conditions for each robot.

### Interactive GUI:

Users can dynamically interact with the GUI to spawn new robots and assign tasks without interrupting ongoing robot activities.

The GUI provides real-time feedback on robot movements, task statuses, and traffic conditions.

### User Alerts for Occupancy and Conflict:

The system immediately notifies the user when a requested path or vertex is blocked or occupied, preventing the assignment of tasks to already congested paths.


## Technologies used:

Python 3.x

Tkinter (for GUI)

Logging module (for logging robot actions and status)

Custom modules for FleetManager and TrafficManager

## Project Structure

![image](https://github.com/user-attachments/assets/9231a901-bcf7-4c68-b87f-34ed99f45bf1)

## How to Use the System

Spawning Robots: Click on any vertex (location) to spawn a robot. Each robot will have a unique identifier displayed.

Assigning Tasks: After spawning a robot, click on the robot and then click on the destination vertex to assign a task. The robot will begin navigating immediately.

Traffic Management: Robots will avoid collisions by negotiating traffic. If a robot encounters an occupied lane, it will wait until the lane is free.

Monitoring Robot Status: The robot's current status (moving, waiting, charging, or task complete) will be visually indicated on the GUI.

Real-Time Logs: All robot actions, path choices, and task completions are logged in fleet_logs.txt and can be optionally viewed in the GUI.

## Key GUI Interactions

Spawn Robot: Click on a vertex to spawn a robot at that location.

Assign Task: Click on a robot, then click on a destination vertex to assign a navigation task.

View Robot Status: The robot’s status (such as moving, waiting, charging, or task complete) is displayed in real-time on the GUI.

Traffic Management: Robots dynamically adjust their movement to avoid lane collisions and intersections where traffic is blocked.

## Navigation Graph (nav_graph.json)


{

    "coordinates": {
    
      "A": [0, 0],
      
      "B": [1, 0],
      
      "C": [2, 0],
      
      "D": [1, 1],
      
      "E": [2, 1],
   
      "F": [3, 1]
    },
    
    
    "graph": {
    
      "A": {
      
        "B": 1,
        
        "C": 2
      },
      
      
      "B": {
      
        "D": 1
      },
      
      
      "C": {
      
        "E": 2
      },
      
      
      "D": {
      
        "F": 3
      },
     
      
      "E": {},
      
      "F": {}
    }
    
  }
  
## Logs and Monitoring

The simulation will continuously log robot actions, path choices, waiting conditions, and task completions into the fleet_logs.txt file. This file is located in the logs/ directory.

# Sample Log Output:

![image](https://github.com/user-attachments/assets/54958695-3cd0-477b-a312-1e420e9e1538)

## Acknowledgments

Tkinter: Used for building the GUI.

Dijkstra's Algorithm: Used for pathfinding.

Open-source libraries: Various libraries for logging and pathfinding.

## Screenshots and Visuals

![image](https://github.com/user-attachments/assets/ef9c7c6a-50f7-43af-8ceb-33626ca24a55)


**Simulation Progress and Log Output:**

In the image, we can see a successful run of the Fleet Management System simulation:

1. **Robot Spawning & Task Assignment**:  
   Robots are spawned at vertices A and B, with tasks assigned to navigate to destinations C and D, respectively. The system dynamically assigns paths and manages the traffic negotiation process between robots.

2. **Path Selection & Movement**:  
   Robot-1 and Robot-2 move through the network, avoiding collisions and following their assigned paths. The log displays their progress as they move from one node to another, with real-time updates on their position and task completion status.

3. **Task Completion & Status Updates**:  
   Upon completing their tasks, each robot’s status is updated to "task complete," and their positions are logged. The simulation ends with both robots having successfully completed their tasks.

4. **Real-Time Logging**:  
   The simulation log includes critical information, such as granted lane access, path choices, and robot movements, which ensures full traceability and monitoring of each robot's progress throughout the simulation.


  

