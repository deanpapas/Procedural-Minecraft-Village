import random
from mcpi.minecraft import Minecraft
from mcpi.minecraft import Block
from Node import Node

class VillageWall:

    WALL_PALLET = [Block(98, 1), Block(98, 2), Block(98, 3), Block(98, 4), Block(98, 5), \
                Block(98, 6), Block(98, 7), Block(98, 8), Block(98, 9), Block(98, 10), \
                Block(98, 11), Block(98, 12), Block(98, 13), Block(98, 14), Block(98, 15)]
    
    def __init__(self):
        self.mc = Minecraft.create()

    def buildWall(self, start, end, map):

        def add_to_wall(map,wall,x,z):
            for pos in map:
                if pos[0] == x and pos[2] == z: 
                    wall.append(pos)

        x1, x2 = min(start.x, end.x), max(start.x, end.x)
        z1, z2 = min(start.z, end.z), max(start.z, end.z)

        north_wall = list()
        east_wall = list()
        south_wall = list()
        west_wall = list()
        
        for x in range(x1, x2+1):
                for z in range(z1, z2+1):
                    if x == x1:
                        add_to_wall(map,west_wall,x,z)
                    elif x == x2-1:
                        add_to_wall(map,east_wall,x,z)
                    elif z == z1:
                        add_to_wall(map,north_wall,x,z)
                    elif z == z2-1:
                        add_to_wall(map,south_wall,x,z)

        walls = [north_wall, east_wall, south_wall, west_wall]
        centre = (x1+x2)/2
        gate_postions = list()
        position_counter = -1
        previous_height = walls[0][0][1]
        for wall in walls:
            for pos in wall:
                position_counter += 1
                if not centre-3 < pos[0] < centre+3:
                    for i in range(-20, 4):
                        self.mc.setBlock(pos[0], pos[1]+i, pos[2], random.choice(self.WALL_PALLET))
                    if position_counter % 6 == 1:
                        for i in range(-20, 4):
                            self.mc.doCommand("setblock " + str(pos[0]) + " " + str(pos[1]+i) + " " + str(pos[2]) + " minecraft:stone_brick_wall")
                        self.mc.setBlock(pos[0], pos[1]+5, pos[2], 98,0)
                        self.mc.doCommand("setblock " + str(pos[0]) + " " + str(pos[1]+6) + " " + str(pos[2]) + " minecraft:lantern")
                    elif position_counter % 2 == 0 or previous_height != pos[1]:
                        self.mc.doCommand("setblock " + str(pos[0]) + " " + str(pos[1]+4) + " " + str(pos[2]) + " minecraft:stone_brick_wall")
                        self.mc.setBlock(pos[0], pos[1]+5, pos[2], 44,5)
                    else:
                        self.mc.setBlock(pos[0], pos[1]+5, pos[2], 44,5)
                    
                else:
                    self.mc.setBlock(pos[0], pos[1], pos[2], random.choice(self.WALL_PALLET))
                    gate_postions.append(Node(pos[0], pos[1], pos[2]))
                previous_height = pos[1]

        
        gate_postions[2].z += 1
        return (gate_postions[2], gate_postions[7])