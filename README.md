Here's a sample `README.md` file for the code provided:

---

# Autonomous City Traffic Simulation

This project simulates a city grid where autonomous vehicles navigate between randomly assigned start and destination points, dynamically adjusting routes based on traffic light states and congestion. The simulation implements basic graph traversal (using Dijkstra's algorithm) to find optimal routes and a traffic management system to control traffic lights.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Future Improvements](#future-improvements)

## Features

- **City Grid Layout**: The city is represented as a grid, with intersections as nodes and roads as edges with randomly assigned travel times.
- **Autonomous Vehicle Navigation**: Vehicles find the shortest route between start and destination points using Dijkstra's algorithm.
- **Traffic Light Management**: Traffic lights at intersections dynamically change states (green/red) to simulate congestion control.
- **Simulation Control**: Easily modify the city size, the number of vehicles, and road weights for a customized simulation.

## Requirements

- Python 3.x
- No external libraries are required beyond Python’s standard library (`random`, `heapq`).

## How It Works

### 1. City Layout
The city is defined as a grid of intersections (nodes) with bidirectional roads (edges) connecting them. Each road has a weight (travel time), randomly assigned for this simulation. Traffic lights at intersections can be green or red, impacting vehicle routes.

### 2. Vehicle Navigation
Vehicles are assigned random start and destination points in the grid. Using Dijkstra’s algorithm, each vehicle calculates the shortest path based on current traffic conditions. The path is recalculated if the traffic light state changes, simulating real-world congestion scenarios.

### 3. Traffic Management
Traffic lights toggle between green and red based on random choices in this simulation. The `TrafficManager` class can be adapted to change traffic light statuses based on actual congestion data or other metrics.


### Sample Code
To run a sample simulation directly, you can call the `run_simulation()` function, which initializes a 5x5 grid city with 3 vehicles:

```python
run_simulation(city_size=5, num_vehicles=3)
```

## Code Structure

- **City**: Represents the city grid, initializes intersections, roads, and traffic lights.
- **Vehicle**: Defines each autonomous vehicle, with methods for finding the shortest path from start to destination.
- **TrafficManager**: Manages the status of traffic lights, dynamically updating them based on traffic conditions.
- **Simulation Runner**: Ties all components together, initializing the city, creating vehicles, and controlling traffic.

## Future Improvements

- **Adaptive Traffic Lights**: Replace random toggling with adaptive control based on vehicle density or queue lengths.
- **Dynamic Rerouting**: Allow vehicles to reroute if a traffic light is red for an extended period.
- **Advanced Pathfinding**: Explore alternative pathfinding algorithms that account for live traffic conditions more effectively.
- **UI Visualization**: Add a graphical interface to visualize the city, vehicle paths, and traffic light statuses in real-time.

---

