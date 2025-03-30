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

