from mcpi import minecraft, block
from mcpi.minecraft import Block
import random
class Well(object):
    def __init__(self):
        self.mc = minecraft.Minecraft.create()

    def build(self, x, y, z):
        # logs
        self.mc.setBlock(x,y,z,Block(17,1))
        self.mc.setBlock(x,y,z+3,Block(17,1))
        self.mc.setBlock(x+3,y,z,Block(17,1))
        self.mc.setBlock(x+3,y,z+3,Block(17,1))
        # base stairs
        self.mc.setBlocks(x,y,z+1,x,y,z+2,Block(109,0))
        self.mc.setBlocks(x+1,y,z+3,x+2,y,z+3,Block(109,3))
        self.mc.setBlocks(x+3,y,z+1,x+3,y,z+2,Block(109,1))
        self.mc.setBlocks(x+1,y,z,x+2,y,z,Block(109,2))
        # fences
        self.mc.setBlocks(x,y+1,z,x,y+2,z,Block(85))
        self.mc.setBlocks(x,y+1,z+3,x,y+2,z+3,Block(85))
        self.mc.setBlocks(x+3,y+1,z,x+3,y+2,z,Block(85))
        self.mc.setBlocks(x+3,y+1,z+3,x+3,y+2,z+3,Block(85))
        # corner slabs
        self.mc.setBlock(x,y+3,z,Block(44,3))
        self.mc.setBlock(x,y+3,z+3,Block(44,3))
        self.mc.setBlock(x+3,y+3,z,Block(44,3))
        self.mc.setBlock(x+3,y+3,z+3,Block(44,3))
        # border slabs
        self.mc.setBlocks(x,y+3,z+1,x,y+3,z+2,Block(44,13))
        self.mc.setBlocks(x+1,y+3,z+3,x+2,y+3,z+3,Block(44,13))
        self.mc.setBlocks(x+3,y+3,z+1,x+3,y+3,z+2,Block(44,13))
        self.mc.setBlocks(x+1,y+3,z,x+2,y+3,z,Block(44,13))
        # roof slab
        self.mc.setBlocks(x+1,y+4,z+1,x+2,y+4,z+2,Block(44,3))
        # water
        self.mc.setBlocks(x,y-3,z,x+3,y-1,z+3,Block(4))
        self.mc.setBlocks(x+1,y-2,z+1,x+2,y-1,z+2,Block(9))

class Bench(object):
    def build(self, x, y, z):
        east = 0
        west = 1
        south = 2
        north = 3
        stone = 109
        oak = 53
        cobble = 67
        bench = [stone, oak, cobble]
        dir = [east, west, south, north]
        chosen_bench = random.choice(bench)
        chosen_dir = random.choice(dir)
        chosen_rest = random.randint(0, 1) # 0 = trapdoor, 1 = sign

        mc = minecraft.Minecraft.create()
        chosen_bench = Block(chosen_bench, chosen_dir)
        if chosen_dir == east or chosen_dir == west:
            mc.setBlocks(x, y, z, x, y, z+1, chosen_bench)
            if chosen_rest == 0:
                mc.setBlock(x, y, z-1, Block(96,4))
                mc.setBlock(x, y, z+2, Block(96,5))
            elif chosen_rest == 1:
                mc.setBlock(x, y, z-1, Block(68,2))
                mc.setBlock(x, y, z+2, Block(68,3))
    
        elif chosen_dir == north or chosen_dir == south:
            mc.setBlocks(x, y, z, x+1, y, z, chosen_bench)
            if chosen_rest == 0:
                mc.setBlock(x-1, y, z, Block(96,6))
                mc.setBlock(x+2, y, z, Block(96,7))
            elif chosen_rest == 1:
                mc.setBlock(x-1, y, z, Block(68,4))
                mc.setBlock(x+2, y, z, Block(68,5))

class Lamp(object):
    def __init__(self):
        self.mc = minecraft.Minecraft.create()
    
    def lamp_choices(self):
        self.choices = [Lamp_1, Lamp_2]
        chosen_design = random.choice(self.choices)
        return chosen_design
    
    def build_lamps(self, x, y, z):
        choices = [Lamp_1, Lamp_2]
        chosen_design = random.choice(choices)
        chosen_design.build(x,y,z)
    
class Lamp_1(Lamp):
    def __init__(self):
        super().__init__(self)

    def build(x, y, z):
        mc = minecraft.Minecraft.create()
        mc.setBlocks(x,y+1,z,x,y+2,z,block.FENCE)
        mc.setBlock(x+1, y+3, z, block.FENCE_BIRCH)
        mc.setBlock(x-1, y+3, z, block.FENCE_BIRCH)
        mc.setBlock(x, y+3, z-1, block.FENCE_BIRCH)
        mc.setBlock(x, y+3, z+1, block.FENCE_BIRCH)
        mc.setBlock(x,y,z, block.COBBLESTONE)
        mc.setBlock(x,y+3,z,block.GLOWSTONE_BLOCK)
        mc.setBlock(x,y+4,z, block.STONE_SLAB)
        mc.setBlock(x+1, y+4, z, block.Block(96,3))
        mc.setBlock(x-1, y+4, z, block.Block(96,3))
        mc.setBlock(x, y+4, z-1, block.Block(96,3))
        mc.setBlock(x, y+4, z+1, block.Block(96,3))

class Lamp_2(Lamp):
    def __init__(self):
        super().__init__(self)

    def build(x, y, z):
        mc = minecraft.Minecraft.create()
        mc.setBlocks(x,y,z,x,y+2,z,block.Block(17))
        mc.setBlock(x-1,y+2,z,block.Block(67,4))
        mc.setBlock(x+1,y+2,z,block.Block(67,5))
        mc.setBlock(x,y+2,z-1,block.Block(67,6))
        mc.setBlock(x,y+2,z+1,block.Block(67,7))
        mc.setBlock(x-1,y+3,z,block.FENCE)
        mc.setBlock(x+1,y+3,z,block.FENCE)
        mc.setBlock(x,y+3,z-1,block.FENCE)
        mc.setBlock(x,y+3,z+1,block.FENCE)
        mc.setBlock(x,y+3,z,block.GLOWSTONE_BLOCK)
        mc.setBlock(x-1,y+4,z,block.Block(53,0))
        mc.setBlock(x+1,y+4,z,block.Block(53,1))
        mc.setBlock(x,y+4,z-1,block.Block(53,2))
        mc.setBlock(x,y+4,z+1,block.Block(53,3))
        mc.setBlock(x,y+5,z,block.Block(126))

class Trees(object):
    def __init__(self):
        self.mc = minecraft.Minecraft.create()

    def build(self,x,y,z):
        oak = 0
        birch = 2
        tree_type = [oak, birch]
        tree_type = random.choice(tree_type)

        # Trunk placed at x,y,z
        # Layers of leaves
        self.mc.setBlocks(x-2,y+3,z-2,x+2,y+4,z+2,Block(18,tree_type))
        self.mc.setBlocks(x-1,y+5,z-1,x+1,y+6,z+1,Block(18,tree_type))

        # Trunk
        self.mc.setBlocks(x,y,z,x,y+5,z,Block(17, tree_type))

        # Clean
        self.mc.setBlock(x-1,y+6,z-1, block.AIR)
        self.mc.setBlock(x-1,y+6,z+1, block.AIR)
        self.mc.setBlock(x+1,y+6,z-1, block.AIR)
        self.mc.setBlock(x+1,y+6,z+1, block.AIR)
        self.mc.setBlock(x-2,y+4,z-2, block.AIR)
        self.mc.setBlock(x+2,y+4,z+2, block.AIR)
        self.mc.setBlock(x+2,y+4,z-2, block.AIR)
        self.mc.setBlock(x-2,y+3,z+2, block.AIR)

def addLamps(footpath, available):
        mc = minecraft.Minecraft.create()
        lamp = Lamp()
        placed = set()
        for co_ord in footpath[::30]:
            x = co_ord[0] - 3
            z = co_ord[2] - 3

            for pos in available:
                if pos[0] == x and pos[2] == z:
                    y = pos[1]

                    lamp_placement = (x,y,z)
                    if lamp_placement in available:
                        block_below = mc.getBlockWithData(x,y,z).id
                        if block_below != 208 and block_below  != 0:
                            lamp.build_lamps(x, y+1, z)
                            off_limits = offLimits(x, y+1, z)
                            placed.update(off_limits)
            

        return placed

# available = area remaining in map to build (- houses & footpaths)
def decorateArea(footpath, available):
    available = available.difference(set(footpath))
    lamps = addLamps(footpath, available)
    available = available.difference(lamps)

    decorations = []
  
    for i in range(0, 45):
        random_area = random.choice(list(available))
        decorations.append(random_area)
        off_limits = offLimits(random_area[0], random_area[1], random_area[2])
        available = available.difference(off_limits)
    
    options = [Well(), Trees(), Bench()]

    for spot in decorations:
        chosen = random.choices(options, weights=(10, 70, 20), k=1)
        chosen[0].build(spot[0], spot[1] + 1, spot[2])

def offLimits(x, y, z):
            bottom_left = (x-6, y, z+6)
            top_right = (x+8, y, z-8)
            x1 = bottom_left[0]
            x2 = top_right[0]
            z1 = bottom_left[2]
            z2 = top_right[2]
            co_ords = set()
            
            for x in range(int(x1), int(x2+1)):
                for z in range(int(z2), int(z1-1)):
                    pos = (x, y, z)
                    co_ords.add(pos)
                    

            return (co_ords) 

class Backyard(object):
    def __init__(self):
        self.mc = minecraft.Minecraft.create()

    def createGarden(self,x, y, z, x2, y2, z2):
        # Farm area
        self.mc.setBlocks(x+2,y-1,z+2, x2-2,y-1,z+2,Block(60))
        self.mc.setBlocks(x+2,y-1,z+3, x2-2,y-1,z+3,Block(9))
        self.mc.setBlocks(x+2,y-1,z+4, x2-2,y-1,z+4,Block(60))

        self.mc.setBlocks(x+2,y,z+2, x2-2,y,z+2,Block(141))
        self.mc.setBlocks(x+2,y,z+4, x2-2,y,z+4,Block(141))

        # Random bench
        Bench.build(self, x+4,y,z2-3)

        length = abs(x2 - x)
        mid = length // 2
        flower_choices = [Block(175, 1), Block(175,3), Block(175,4), Block(175,5), Block(38), Block(38,1), Block(38,2), Block(38,3), Block(38,8)]
        for x in range(int(x2-mid), int(x2-1)):
            for z in range(int(z2-3), int(z2-1)):
                flower = random.choice(flower_choices)
                self.mc.setBlock(x,y,z,flower)


    def decorateBackyard(self,x, y, z, x2, y2, z2):
        # Build fence
        self.mc.setBlocks(x2,y,z+1,x2,y,z2-1,block.FENCE)
        self.mc.setBlocks(x,y,z+1,x,y,z2-1,block.FENCE)
        self.mc.setBlock(x,y,z,block.WOOD)
        self.mc.setBlock(x2,y,z,block.WOOD)
        self.mc.setBlocks(x+1,y,z2,x2-1,y,z2,block.FENCE)
        self.mc.setBlock(x,y,z2,block.WOOD)
        self.mc.setBlock(x2,y,z2,block.WOOD)

        area_options = [self.createGarden]
        decorate = random.choice(area_options)
        decorate(x, y, z, x2, y2, z2)

    
    def frontFlowers(self, site_dict):
        # JUST SOME IDEAS FOR PLANTS ON THE FRONT CORNERS OF THE HOUSES. 
            # It just randomises the plants and is in the same spot for each house so idk if you want to use it or not.
            plants = ('crimson_fungus', 'warped_fungus', 'poppy', 'dandelion', 'red_tulip', 'orange_tulip', 'white_tulip', 
                'pink_tulip', 'blue_orchid', 'allium', 'lily_of_the_valley', 'cornflower', 'oxeye_daisy', 'wither_rose', 
                'peony', 'sunflower', 'rose_bush', 'lilac', 'flowering_azalea', 'azure_bluet')
            for key in site_dict:
                bx = site_dict[key]['house_start'][0]
                bz = site_dict[key]['house_start'][2]
                cx = site_dict[key]['house_end'][0] 
                cz = site_dict[key]['house_end'][2]
                y = site_dict[key]['house_end'][1] + 1 
                
                plantA = (random.choice(plants))

                #font corners
                self.mc.doCommand("setblock " + str(bx-1) + " " + str(y) + " " + str(bz+1) + " minecraft:" + str(plantA))
                self.mc.doCommand("setblock " + str(bx-1) + " " + str(y) + " " + str(bz) + " minecraft:" + str(plantA))
                self.mc.doCommand("setblock " + str(bx-1) + " " + str(y) + " " + str(bz-1) + " minecraft:" + str(plantA))
                self.mc.doCommand("setblock " + str(bx) + " " + str(y) + " " + str(bz-1) + " minecraft:" + str(plantA))
                self.mc.doCommand("setblock " + str(bx+1) + " " + str(y) + " " + str(bz-1) + " minecraft:" + str(plantA))
                
                self.mc.doCommand("setblock " + str(cx-1) + " " + str(y) + " " + str(bz-1) + " minecraft:" + str(plantA))
                self.mc.doCommand("setblock " + str(cx) + " " + str(y) + " " + str(bz-1) + " minecraft:" + str(plantA))
                self.mc.doCommand("setblock " + str(cx+1) + " " + str(y) + " " + str(bz-1) + " minecraft:" + str(plantA))
                self.mc.doCommand("setblock " + str(cx+1) + " " + str(y) + " " + str(bz) + " minecraft:" + str(plantA))
                self.mc.doCommand("setblock " + str(cx+1) + " " + str(y) + " " + str(bz+1) + " minecraft:" + str(plantA))