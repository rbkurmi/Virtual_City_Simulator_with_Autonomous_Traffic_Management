import heapq
import random

# Step 1: Define City Layout using Graph (Adjacency List)
class City:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.graph = {}
        self.traffic_lights = {}  # Store traffic light status (True for green, False for red)
        self.initialize_city()

    def initialize_city(self):
        # Create grid and define intersections as nodes
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.graph[(i, j)] = {}
                self.traffic_lights[(i, j)] = True if random.choice([True, False]) else False

    def add_road(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # Bidirectional road

    def display_city(self):
        for node in self.graph:
            print(f"Intersection {node}: Roads {self.graph[node]}")


# Step 2: Vehicle Class (Autonomous Vehicles)
class Vehicle:
    def __init__(self, vehicle_id, start, destination, city):
        self.vehicle_id = vehicle_id
        self.start = start
        self.destination = destination
        self.city = city
        self.path = []

    def find_shortest_path(self):
        self.path = self.dijkstra(self.city.graph, self.start, self.destination)
        print(f"Vehicle {self.vehicle_id} Route: {self.path}")

    def dijkstra(self, graph, start, end):
        heap = [(0, start)]  # (cost, node)
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        parents = {node: None for node in graph}

        while heap:
            current_dist, current_node = heapq.heappop(heap)

            if current_node == end:
                return self.reconstruct_path(parents, start, end)

            for neighbor, weight in graph[current_node].items():
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parents[neighbor] = current_node
                    heapq.heappush(heap, (distance, neighbor))

        return []  # No path found

    def reconstruct_path(self, parents, start, end):
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = parents[node]
        return path[::-1]


# Step 3: Traffic Management (Dynamic Traffic Light Control)
class TrafficManager:
    def __init__(self, city):
        self.city = city

    def update_traffic_lights(self):
        for intersection in self.city.traffic_lights:
            # Dynamically toggle traffic lights based on congestion (random for simulation)
            self.city.traffic_lights[intersection] = random.choice([True, False])

    def control_traffic(self):
        for light, status in self.city.traffic_lights.items():
            state = "Green" if status else "Red"
            print(f"Traffic light at {light} is {state}.")


# Step 4: Simulation
def run_simulation(city_size, num_vehicles):
    # Create city
    city = City(city_size)

    # Add some roads to the city grid
    for i in range(city_size):
        for j in range(city_size):
            if i + 1 < city_size:
                city.add_road((i, j), (i + 1, j), random.randint(1, 10))  # Vertical road
            if j + 1 < city_size:
                city.add_road((i, j), (i, j + 1), random.randint(1, 10))  # Horizontal road

    city.display_city()

    # Create traffic manager
    traffic_manager = TrafficManager(city)

    # Create vehicles and assign random routes
    vehicles = []
    for i in range(num_vehicles):
        start = (random.randint(0, city_size - 1), random.randint(0, city_size - 1))
        end = (random.randint(0, city_size - 1), random.randint(0, city_size - 1))
        vehicle = Vehicle(f"V{i + 1}", start, end, city)
        vehicles.append(vehicle)

    # Run simulation
    for vehicle in vehicles:
        vehicle.find_shortest_path()

    # Update traffic lights
    traffic_manager.update_traffic_lights()
    traffic_manager.control_traffic()


# Run the simulation with a city of size 5x5 and 3 vehicles
run_simulation(5, 3)
