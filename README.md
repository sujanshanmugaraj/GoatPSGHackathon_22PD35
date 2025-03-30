# Fleet Management System with Traffic Negotiation for Multi-Robots

## Overview

The Fleet Management System is a simulation of a fleet of robots that perform tasks based on priority while moving along a network of nodes. The system includes a graphical user interface (GUI) that visualizes the robots' movements and task completions. It also incorporates logging for robot actions, path choices, waiting conditions, and task completions.


## **Features:**
1. **Robot Spawning and Task Assignment**:
   - Users can spawn robots at specific locations (vertices) in the environment via the GUI.
   - Tasks are assigned to robots through the GUI by selecting robots and destination vertices interactively.

2. **Robot Navigation**:
   - Robots navigate through predefined paths (lanes) between vertices based on the tasks assigned to them.
   - Real-time robot movement is visualized on the GUI, showing progress along the path.

3. **Traffic Negotiation & Collision Avoidance**:
   - Robots dynamically negotiate traffic, avoiding lane collisions and managing congestion.
   - Robots can wait or queue at blocked lanes or intersections to ensure smooth movement.
   - Lane occupation is continuously checked to prevent path conflicts.

4. **Real-Time Robot Status Visualization**:
   - Robots' statuses are visually indicated in the GUI, showing whether they are moving, waiting, charging, or have completed tasks.
   - Robot status updates are logged in real-time for user visibility.

5. **Task Management**:
   - Tasks are assigned based on priorities, ensuring high-priority tasks are completed first.
   - Robots can complete tasks and report their status (task complete, waiting, moving).

6. **Dynamic Task Reassignment**:
   - If a task is blocked (due to traffic congestion or a lane being occupied), the system dynamically monitors and reassigns tasks to available robots.
   - Task reassignments are handled based on real-time traffic and robot availability.

7. **Environment Visualization**:
   - The environment, including vertices and lanes, is visually displayed on the GUI.
   - Vertices are interactable (clickable) to spawn robots or assign tasks, providing a clear interface for users.

8. **Real-Time Logging**:
   - All robot actions, movements, task completions, and traffic negotiations are logged to a file (`fleet_logs.txt`).
   - Logs include detailed information such as path choices, robot status updates, and waiting conditions for each robot.

9. **Interactive GUI**:
   - Users can dynamically interact with the GUI to spawn new robots and assign tasks without interrupting ongoing robot activities.
   - The GUI provides real-time feedback on robot movements, task statuses, and traffic conditions.

10. **User Alerts for Occupancy and Conflict**:
    - The system immediately notifies the user when a requested path or vertex is blocked or occupied, preventing the assignment of tasks to already congested paths.

## **Key Highlights:**
- **Dynamic robot task assignments** with real-time updates and status changes.
- **Efficient traffic management** ensuring no robot collides while navigating through the environment.
- **Interactive user interface** that allows for easy robot management and task assignments.
- **Comprehensive logging** of all robot actions and task statuses for monitoring and analysis.


## Technologies used:

Python 3.x

Tkinter (for GUI)

Logging module (for logging robot actions and status)

Custom modules for FleetManager and TrafficManager

## Project Structure

![image](https://github.com/user-attachments/assets/9231a901-bcf7-4c68-b87f-34ed99f45bf1)

Here's a section on how to use the Fleet Management System, which you can add to your README or documentation:

---

## How to Use the Fleet Management System

# 1. **System Setup and Installation**
Before you can start using the Fleet Management System, you need to set it up on your local machine. Follow these steps:

## Install Dependencies:
Make sure you have Python 3.7+ installed. Then, install the required dependencies using `pip`. 

```bash
pip install -r requirements.txt
```

This will install all the necessary libraries, including the graphical interface and the supporting functions for simulation.

## 2. **Running the System**
To start the Fleet Management System, follow these steps:

1. Navigate to the `fleet_management_system/src` directory:

   ```bash
   cd fleet_management_system/src
   ```

2. Run the main application:

   ```bash
   python main.py
   ```

   This will launch the graphical user interface (GUI) where you can interact with the system.

## 3. **Using the Graphical Interface (GUI)**

The GUI will open in a new window, showing a visual representation of the navigation graph (nodes and paths). Below are the steps to interact with the system:

## **Spawning Robots**
1. Click on any vertex (node) to spawn a robot.
2. A new robot will appear at that node, and a unique ID will be assigned to it.

## **Assigning Tasks to Robots**
1. Select a robot by clicking on it in the GUI.
2. After selecting the robot, click on a destination node (another vertex) to assign a task for the robot to move to that location.
3. The robot will start moving toward the assigned destination immediately.

## **Traffic Negotiation**
1. As the robots move, they will negotiate traffic by avoiding collisions with each other.
2. If a robot encounters a blocked path (e.g., another robot is already using the same lane), it will wait until the path becomes clear.
3. The system will visualize the waiting robots and their current statuses in real-time.

## **Monitoring Robot Status**
1. The status of each robot (moving, waiting, charging, task complete) will be updated in the GUI and logged in the system.
2. You can monitor the task progress through the GUI and the log outputs in the terminal.

## 4. **Logs and Monitoring**
Real-time logs are generated during the simulation and stored in a file called `fleet_logs.txt`. The logs provide detailed information about:
- Task assignments
- Path choices
- Robot movements
- Traffic negotiation and collision avoidance

Logs are saved to the `logs/` directory and will be helpful for tracking the progress and diagnosing any issues.

## 5. **Stopping the Simulation**
To stop the simulation, you can simply close the GUI window. The simulation will automatically stop, and the final logs will be saved.

---

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

-**Tkinter**: Used for building the GUI.

-**Dijkstra's Algorithm**: Used for pathfinding.

-**Open-source libraries**: Various libraries for logging and pathfinding.

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


  

