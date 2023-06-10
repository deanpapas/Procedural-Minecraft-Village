from mcpi.minecraft import Minecraft

class TerrainCapture:

    def __init__(self):
        self.mc = Minecraft.create()

    #Returns (x,y,z)
    def captureMap(self, start, end, buffer=0):

        def getBounds(start, end, buffer=0):
            x1, z1 = start
            x2, z2 = end
            left = min(x1, x2) - buffer
            top = min(z1, z2) - buffer
            right = max(x1, x2) + buffer
            bottom = max(z1, z2) + buffer
            return (left, top, right, bottom) 

        def getHeights(start, end, buffer=0):
            x1, z1 = start
            x2, z2 = end
            left = min(x1, x2) - buffer
            top = min(z1, z2) - buffer
            right = max(x1, x2) + buffer
            bottom = max(z1, z2) + buffer
            return self.mc.getHeights(left, top, right-1, bottom-1)
    
        area = getBounds((start.x, start.z), (end.x, end.z), buffer)
        heights = getHeights((start.x, start.z), (end.x, end.z), buffer)

        map = set()
        y = 0
        while y < len(heights)-1:
            for x in range(int(area[0]), int(area[2])):
                for z in range(int(area[1]), int(area[3])):
                    pos = (x, heights[y], z)
                    map.add(pos)
                    y += 1
        return map

    #Returns (x,y,z,block)
    def captureMesh(self, start, end):
        
        mesh = list()

        x1, x2 = min(start.x, end.x), max(start.x, end.x)
        y1, y2 = min(start.y, end.y), max(start.y, end.y)
        z1, z2 = min(start.z, end.z), max(start.z, end.z)

        blocks = self.mc.getBlocksWithData(x1-1, y1-1, z1-1, x2+1, y2+1, z2+1)

        block_counter = 0
        for y in range(y1-1, y2+2):
            for x in range(x1-1, x2+2):
                for z in range(z1-1, z2+2):
                    mesh.append((x,y,z,blocks[block_counter]))
                    block_counter += 1


        return mesh
    
    def cleanArea(self, start, end):

        x1, x2 = min(start.x, end.x), max(start.x, end.x)
        y1, y2 = 0, 200
        z1, z2 = min(start.z, end.z), max(start.z, end.z)

        blocks = self.mc.getBlocksWithData(x1-1, y1-1, z1-1, x2+1, y2+1, z2+1)

        mesh = list()
        block_counter = 0
        for y in range(-1, 201):
            for x in range(x1-1, x2+2):
                for z in range(z1-1, z2+2):
                    mesh.append((x,y,z,blocks[block_counter]))
                    block_counter += 1

        for block in mesh:
            if block[3].id == 18 or block[3].id == 17:
                self.mc.setBlock(block[0], block[1], block[2], 0)
