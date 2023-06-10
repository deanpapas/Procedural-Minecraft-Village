class Node:
    def __init__(self, x, y, z, weight=0):
        self.x = x
        self.y = y
        self.z = z
        self.g = 0
        self.h = 0
        self.f = 0
        self.weight = weight
        self.parent = None
        self.network_status = None
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))