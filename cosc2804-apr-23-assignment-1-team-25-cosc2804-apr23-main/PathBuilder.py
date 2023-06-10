import random
from mcpi.minecraft import Minecraft
from mcpi.minecraft import Block
from Node import Node
import heapq
import math


class PathBuilder:

    PATH_PALLET = [Block(98, 1), Block(98, 2), Block(98, 3), Block(98, 4), Block(98, 5),
                Block(98, 6), Block(98, 7), Block(
                    98, 8), Block(98, 9), Block(98, 10),
                Block(98, 11), Block(98, 12), Block(98, 13), Block(98, 14), Block(98, 15)]

    def __init__(self):
        self.mc = Minecraft.create()

    def buildPaths(self, destinations, map):

        paths = []
        destinations[0].network_status = 0  # Assign initial network status

        number_of_paths = len(destinations)
        path_counter = 0
        
        # Connects destinations
        for destination in destinations:
            if destination.network_status is None:
                closest_location = self.findClosestDestinations(
                    destination, destinations)
                if destination.network_status is None:
                    destination.network_status = closest_location.network_status
                elif closest_location.network_status is None:
                    closest_location.network_status = destination.network_status

                path_counter += 1
                self.mc.postToChat("Path " + str(path_counter) + " of " + str(number_of_paths) + " found.")
                paths.append(self.aStar(destination, closest_location, map))

        # Place blocks
        placed_blocks = []
        for path in paths:
            for coordinate in path:
                for x in range(-1, 1):  # Place blocks in a 3x3 area
                    for z in range(-1, 1):  # Place blocks in a 3x3 area
                        if (coordinate[0]+x, coordinate[1], coordinate[2]+z) not in placed_blocks:
                            placed_blocks.append(
                                (coordinate[0]+x, coordinate[1], coordinate[2]+z))
                            choice = random.randint(0, 10)
                            if choice % 2 == 0:
                                self.mc.doCommand("setblock " + str(coordinate[0]+x) + " " + str(
                                    coordinate[1]) + " " + str(coordinate[2]+z) + " minecraft:dirt_path")
                            else:
                                self.mc.setBlock(
                                    coordinate[0]+x, coordinate[1], coordinate[2]+z, random.choice(self.PATH_PALLET))

                            self.mc.setBlock(
                                coordinate[0]+x, coordinate[1]+1, coordinate[2]+z, 0)  # Clear the block above the pathe

        return placed_blocks

    def heuristic(self, node, goal):
        # Euclidean distance heuristic
        dx = abs(node.x - goal.x)
        dy = abs(node.y - goal.y)
        dz = abs(node.z - goal.z)
        return math.sqrt(dx*dx + dy*dy + dz*dz)

    def get_neighbors(self, current_node, map):
        neighbors = []
        # Check all 26 neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    # Skip current node
                    if i == 0 and j == 0 and k == 0:
                        continue
                    neighbor_pos = (current_node.x + i,
                                    current_node.y + j, current_node.z + k)

                    # Check if neighbor is in map
                    if neighbor_pos in map:
                        new_node = Node(
                            neighbor_pos[0], neighbor_pos[1], neighbor_pos[2])
                        neighbors.append(new_node)
                        continue
                    

        return neighbors

    def aStar(self, start, goal, map):
        open_list = []
        closed_set = set()
        heapq.heappush(open_list, start) # Push start node to open list

        # Loop until open list is empty
        while len(open_list) > 0:
            current_node = heapq.heappop(open_list)
            closed_set.add(current_node)

            # Check if goal is reached
            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(
                        (current_node.x, current_node.y, current_node.z))
                    current_node = current_node.parent
                path.reverse()
                return path
            
            # Get neighbors of current node
            neighbors = self.get_neighbors(current_node, map)
            for neighbor in neighbors:
                if neighbor in closed_set:
                    continue
                # Calculate cost of neighbor
                neighbor.g = current_node.g + 1
                neighbor.h = self.heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h + neighbor.weight
                neighbor.parent = current_node
                
                # Check if neighbor is in open list
                if neighbor not in open_list:
                    heapq.heappush(open_list, neighbor)

        return None

    def findClosestDestinations(self, start, destinations):
        distances = list()
        # Find closest destination
        for destination in destinations:
            if start.network_status != destination.network_status:
                 distances.append((self.heuristic(start, destination), destination))
        return sorted(distances)[0][1] # Return closest destination