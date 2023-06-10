from mcpi.minecraft import Minecraft
from mcpi import block
import math
import random
from Staircase import StairCaseDesigns
from Furniture import Furniture

class House:
    
    doorCoordinates = []
    houseCoordinates = []
    roomCoordinates = []
    frontDoorlocation = 0
    def __init__(self):
        self.mc = Minecraft.create()

    def createHouse(self,x, y, z, x2, y2, z2):
        

        width = abs(x-x2) -1
        depth = abs(z-z2) -1
        
        #Randomize height, stories and roof type
        height = random.randint(3,4)
        stories = random.randint(1,2)
        roofNum = random.randint(0,4)

        #Save room Coordinates and front door Coordinates for furniture
        self.roomCoordinates= []
        door = random.randrange(2,width-1)
        House.frontDoorlocation = door 
        self.houseCoordinates.append(((x,y,z),(x2,y2,z2)))
    
        c = StairCaseDesigns()
        
        #Choose Block Types for house
        floorBlock = block.WOOD_PLANKS.id #CANNOT UPDATE TO USE FILL 
        roof_stair_block = 'spruce_stairs'
        roof_block = 'spruce_planks'
        roof_beam_block = 'spruce_planks'
        roof_slab_block = 'spruce_slab'
        beam_block = 'calcite'
        window_stair_block = 'spruce_stairs'
        window_slab = 'spruce_slab'
        window_fence = 'spruce_fence'
        window_bottom_block = 'barrel'
        window_ground_block = 'moss_block'

        #Randomly pick template for house
        template_list = ['stone','wood','dark_blocks','light_blocks'] 
        chosen_Template = random.choice(template_list)   
        if chosen_Template == 'stone':
            blockList1 = ['cobblestone','stone_bricks','cracked_stone_bricks','polished_andesite']
            blockList2 = ['cobblestone','stone_bricks','cracked_stone_bricks','polished_andesite']
            roof_stair_block = 'nether_brick_stairs'
            roof_block = 'nether_bricks'
            roof_beam_block = 'nether_bricks'
            roof_slab_block = 'nether_brick_slab'
            beam_block = 'stone_bricks'
            window_stair_block = 'polished_andesite_stairs'
            window_slab = 'polished_andesite_slab'
            window_fence = 'andesite_wall'
            window_bottom_block = 'polished_andesite'
            window_ground_block = 'moss_block'

        elif chosen_Template == 'wood':
            blockList1 = ['smooth_quartz','calcite']
            blockList2 = ['smooth_quartz','calcite']
            roof_stair_block = 'birch_stairs'
            roof_block = 'birch_planks'
            roof_beam_block = 'birch_planks'
            roof_slab_block = 'birch_slab'
            beam_block = 'spruce_log'
            window_stair_block = 'spruce_stairs'
            window_slab = 'spruce_slab'
            window_fence = 'spruce_fence'
            window_bottom_block = 'barrel[facing=down]'
            window_ground_block = 'moss_block'

        elif chosen_Template == 'dark_blocks':
            blockList1 = ['cobbled_deepslate','cobblestone','mossy_cobblestone']
            blockList2 = ['chiseled_quartz_block','smooth_quartz']
            roof_stair_block = 'deepslate_brick_stairs'
            roof_block = 'deepslate_bricks'
            roof_beam_block = 'deepslate_bricks'
            roof_slab_block = 'deepslate_brick_slab'
            beam_block = 'deepslate_bricks'
            window_stair_block = 'polished_diorite_stairs'
            window_slab = 'polished_diorite_slab'
            window_fence = 'diorite_wall'
            window_bottom_block = 'gray_shulker_box'
            window_ground_block = 'moss_block'

        elif chosen_Template == 'light_blocks':
            blockList1 = ['sandstone','chiseled_sandstone','smooth_sandstone']
            blockList2 = ['diorite','polished_diorite']
            roof_stair_block = 'mangrove_stairs'
            roof_block = 'mangrove_planks'
            roof_beam_block = 'mangrove_planks'
            roof_slab_block = 'mangrove_slab'
            beam_block = 'oak_wood'
            window_stair_block = 'birch_stairs'
            window_slab = 'birch_slab'
            window_fence = 'birch_fence'
            window_bottom_block = 'birch_planks'
            window_ground_block = 'moss_block'

        for i in range(width+2):
                for j in range(height+2):
                    for k in range(depth+2):
                            self.mc.doCommand("setblock " + str(x+i) + " " + str(y+j) + " " + str(z+k) +" minecraft:" + random.choice(blockList1))
                            if stories > 1:
                                self.mc.doCommand("setblock " + str(x+i) + " " + str(y+(j+height)) + " " + str(z+k) +" minecraft:" + random.choice(blockList2))
        self.mc.doCommand("fill " + str(x+1) + " " + str(y) + " " + str(z+1) + " " + str(x+width) + " " + str(y+(height*stories)+1) + " " + str(z+depth) + " minecraft:air")


        #Create Corner and Top Beams
        #Create Closest Corners
        self.mc.doCommand("fill " + str(x) + " " + str(y) + " " + str(z) + " " + str(x) + " " + str(y+(height*stories)) + " " + str(z) + " minecraft:" + str(beam_block))
        self.mc.doCommand("fill " + str(x+width+1) + " " + str(y) + " " + str(z) + " " + str(x+width+1) + " " + str(y+(height*stories)) + " " + str(z) + " minecraft:" + str(beam_block))
        #Create Furthest Corners
        self.mc.doCommand("fill " + str(x) + " " + str(y) + " " + str(z+depth+1) + " " + str(x) + " " + str(y+(height*stories)) + " " + str(z+depth+1) + " minecraft:" + str(beam_block))
        self.mc.doCommand("fill " + str(x+width+1) + " " + str(y) + " " + str(z+depth+1) + " " + str(x+width+1) + " " + str(y+(height*stories)) + " " + str(z+depth+1) + " minecraft:" + str(beam_block))
        #Top Beams
        heightAdjustment = 1
        if height == 3:
            heightAdjustment = 1
        self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+heightAdjustment) + " " + str(z) + " " + str(x+width+1) + " " + str(y+(height*stories)+heightAdjustment) + " " + str(z) + " minecraft:" + str(beam_block))
        self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+heightAdjustment) + " " + str(z+depth+1) + " " + str(x+width+1) + " " + str(y+(height*stories)+heightAdjustment) + " " + str(z+depth+1) + " minecraft:" + str(beam_block))
        self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+heightAdjustment) + " " + str(z+1) + " " + str(x) + " " + str(y+(height*stories)+heightAdjustment) + " " + str(z+depth+1) + " minecraft:" + str(beam_block))
        self.mc.doCommand("fill " + str(x+width+1) + " " + str(y+(height*stories)+heightAdjustment) + " " + str(z) + " " + str(x+width+1) + " " + str(y+(height*stories)+heightAdjustment) + " " + str(z+depth+1) + " minecraft:" + str(beam_block))
        #Middle beams if 2 Story House
        if stories > 1:
            self.mc.doCommand("fill " + str(x) + " " + str(y+(height+heightAdjustment)) + " " + str(z) + " " + str(x+width+1) + " " + str(y+(height+heightAdjustment)) + " " + str(z) + " minecraft:" + str(beam_block))
            self.mc.doCommand("fill " + str(x) + " " + str(y+(height+heightAdjustment)) + " " + str(z+depth+1) + " " + str(x+width+1) + " " + str(y+(height+heightAdjustment)) + " " + str(z+depth+1) + " minecraft:" + str(beam_block))
            self.mc.doCommand("fill " + str(x) + " " + str(y+(height+heightAdjustment)) + " " + str(z+1) + " " + str(x) + " " + str(y+(height+heightAdjustment)) + " " + str(z+depth+1) + " minecraft:" + str(beam_block))
            self.mc.doCommand("fill " + str(x+width+1) + " " + str(y+(height+heightAdjustment)) + " " + str(z) + " " + str(x+width+1) + " " + str(y+(height+heightAdjustment)) + " " + str(z+depth+1) + " minecraft:" + str(beam_block))

        #Create Roof type based on RoofNum
        y = y + 1
        if roofNum == 0: #Slope roof up/down along x-axis
            for i in range(-1, int(width/2)+1):
                self.mc.doCommand("fill " + str(x+i) + " " + str(y+(height*stories)+i+stories) + " " + str(z-1) + " " + str(x+i) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth+2) + " minecraft:" + str(roof_stair_block) + "[facing=east]")
                self.mc.doCommand("fill " + str(x+width-i+1) + " " + str(y+(height*stories)+i+stories) + " " + str(z-1) + " " + str(x+width-i+1) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth+2) + " minecraft:" + str(roof_stair_block) + "[facing=west]")
                # Gable ends.
                if (int(width/2) - i > 0):
                    self.mc.doCommand("fill " + str(x+1+i) + " " + str(y+(height*stories)+i+stories) + " " + str(z) + " " + str(x+width-i) + " " + str(y+(height*stories)+i+stories) + " " + str(z) + " minecraft:" + str(roof_block))
                    self.mc.doCommand("fill " + str(x+1+i) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth-1) + " " + str(x+width-i) + " " + str(y+(height*stories)+i+stories) + " " + str(z+1+depth) + " minecraft:" + str(roof_block))
            if (width % 2) != 0:
                i = int(width/2)
                self.mc.doCommand("fill " + str(x+(width//2)+1) + " " + str(y+(height*stories)+i+stories) + " " + str(z-1) + " " + str(x+(width//2)+1) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth+2) + " minecraft:" + str(roof_beam_block))
                
        elif roofNum == 1: #Slope roof up/down along z-axis
            if stories == 1 and height == 4:
                y = y + 1
            
            for i in range(0,int(depth/2)+1):
                self.mc.doCommand("fill " + str(x-1) + " " + str(y+(height*stories)+i+stories-1) + " " + str(z+i) + " " + str(x+width+2) + " " + str(y+(height*stories)+i+stories-1) + " " + str(z+i) + " minecraft:" + str(roof_stair_block) + "[facing=south]")
                self.mc.doCommand("fill " + str(x-1) + " " + str(y+(height*stories)+i+stories-1) + " " + str(z+depth-i+1) + " " + str(x+width+2) + " " + str(y+(height*stories)+i+stories-1) + " " + str(z+depth-i+1) + " minecraft:" + str(roof_stair_block) + "[facing=north]")
                # Gable ends.
                if (int(depth/2) - i > 0):
                    self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+i+stories-1) + " " + str(z+1+i) + " " + str(x) + " " + str(y+(height*stories)+i+stories-1) + " " + str(z+depth-i) + " minecraft:" + str(roof_block))
                    self.mc.doCommand("fill " + str(x+width+1) + " " + str(y+(height*stories)+i+stories-1) + " " + str(z+1+i) + " " + str(x+width+1) + " " + str(y+(height*stories)+i+stories-1) + " " + str(z+depth-i) + " minecraft:" + str(roof_block))
            if (depth % 2) != 0:
                i = int(depth/2)
                self.mc.doCommand("fill " + str(x-1) + " " + str(y+(height*stories)+i+stories-1) + " " + str(z+(depth//2)+1) + " " + str(x+width+2) + " " + str(y+(height*stories)+i+stories-1) + " " + str(z+(depth//2)+1) + " minecraft:" + str(roof_beam_block))
            if stories == 1 and height == 4:
                y = y -1
        elif roofNum == 2:  #Flat Roof
            self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+2) + " " + str(z) + " " + str(x+width+1) + " " + str(y+(height*stories)+2) + " " + str(z+depth+1) + " minecraft:" + str(roof_slab_block))
            self.mc.doCommand("fill " + str(x+1) + " " + str(y+(height*stories)+2) + " " + str(z+1) + " " + str(x+width) + " " + str(y+(height*stories)+2) + " " + str(z+depth) + " minecraft:air")
            self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+1) + " " + str(z) + " " + str(x+width+1) + " " + str(y+(height*stories)+1) + " " + str(z+depth+1) + " minecraft:" + str(roof_block))

        elif roofNum == 3:  #Pyramidal Roof
            p = -1
            
            if width >= 14 and depth>=14:
                for i in range(-1,5):
                    self.mc.doCommand("fill " + str(x+i) + " " + str(y+(height*stories)+i+stories) + " " + str(z+p) + " " + str(x+i) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth+1-p) + " minecraft:" + str(roof_stair_block) + "[facing=east]")
                    self.mc.doCommand("fill " + str(x+p) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth-i+1) + " " + str(x+width+1-p) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth-i+1) + " minecraft:" + str(roof_stair_block) + "[facing=north]")
                    self.mc.doCommand("fill " + str(x+p) + " " + str(y+(height*stories)+i+stories) + " " + str(z+i) + " " + str(x+width+1-p) + " " + str(y+(height*stories)+i+stories) + " " + str(z+i) + " minecraft:" + str(roof_stair_block) + "[facing=south]")
                    self.mc.doCommand("fill " + str(x+width-i+1) + " " + str(y+(height*stories)+i+stories) + " " + str(z+p) + " " + str(x+width-i+1) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth-p) + " minecraft:" + str(roof_stair_block) + "[facing=west]")
                    p = p+1
                
                self.mc.doCommand("fill " + str(x+p) + " " + str(y+(height*stories)+4+stories) + " " + str(z+p) + " " + str(x+width+1-p) + " " + str(y+(height*stories)+4+stories) + " " + str(z+depth+1-p) + " minecraft:" + str(roof_block))
            else:
                for i in range(-1,3):
                    self.mc.doCommand("fill " + str(x+i) + " " + str(y+(height*stories)+i+stories) + " " + str(z+p) + " " + str(x+i) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth+1-p) + " minecraft:" + str(roof_stair_block) + "[facing=east]")
                    self.mc.doCommand("fill " + str(x+p) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth-i+1) + " " + str(x+width+1-p) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth-i+1) + " minecraft:" + str(roof_stair_block) + "[facing=north]")
                    self.mc.doCommand("fill " + str(x+p) + " " + str(y+(height*stories)+i+stories) + " " + str(z+i) + " " + str(x+width+1-p) + " " + str(y+(height*stories)+i+stories) + " " + str(z+i) + " minecraft:" + str(roof_stair_block) + "[facing=south]")
                    self.mc.doCommand("fill " + str(x+width-i+1) + " " + str(y+(height*stories)+i+stories) + " " + str(z+p) + " " + str(x+width-i+1) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth-p) + " minecraft:" + str(roof_stair_block) + "[facing=west]")
                    p = p+1
                self.mc.doCommand("fill " + str(x+p) + " " + str(y+(height*stories)+2+stories) + " " + str(z+p) + " " + str(x+width+1-p) + " " + str(y+(height*stories)+2+stories) + " " + str(z+depth+1-p) + " minecraft:" + str(roof_block))
            
        elif roofNum == 4: #clerestory roof (Only facing one direction)
            self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+1) + " " + str(z+depth+1) + " " + str(x+width+1) + " " + str(y+(height*stories)+4) + " " + str(z+depth+1) + " minecraft:" + str(roof_block))
            for i in range(-1,int(depth/2)+1):
                self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+i+stories+4) + " " + str(z+depth//2+1) + " " + str(x+width+1) + " " + str(y+(height*stories)+i+stories+3) + " " + str(z+depth//2+1) + " minecraft:" + str(roof_block))
                self.mc.doCommand("fill " + str(x-1) + " " + str(y+(height*stories)+i+stories+4) + " " + str(z+depth-i+1) + " " + str(x+width+2) + " " + str(y+(height*stories)+i+stories+4) + " " + str(z+depth-i+1) + " minecraft:" + str(roof_stair_block) + "[facing=north]")
                self.mc.doCommand("fill " + str(x-1) + " " + str(y+(height*stories)+i+stories) + " " + str(z+i) + " " + str(x+width+2) + " " + str(y+(height*stories)+i+stories) + " " + str(z+i) + " minecraft:" + str(roof_stair_block) + "[facing=south]")
                if (int(depth/2) - i > 0):
                    self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+i+stories) + " " + str(z+1+i) + " " + str(x) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth//2) + " minecraft:" + str(roof_block))
                    self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+stories-1) + " " + str(z+depth//2) + " " + str(x) + " " + str(y+(height*stories)+stories+height) + " " + str(z+depth+1) + " minecraft:" + str(roof_block))
                    self.mc.doCommand("fill " + str(x+width+1) + " " + str(y+(height*stories)+i+stories) + " " + str(z+1+i) + " " + str(x+width+1) + " " + str(y+(height*stories)+i+stories) + " " + str(z+depth//2) + " minecraft:" + str(roof_block))
                    self.mc.doCommand("fill " + str(x+width+1) + " " + str(y+(height*stories)+stories-1) + " " + str(z+depth//2) + " " + str(x+width+1) + " " + str(y+(height*stories)+stories+height) + " " + str(z+depth+1) + " minecraft:" + str(roof_block))
                    self.mc.doCommand("fill " + str(x) + " " + str(y+(height*stories)+i+stories+4) + " " + str(z+depth//2+1) + " " + str(x) + " " + str(y+(height*stories)+i+stories+4) + " " + str(z+depth-i) + " minecraft:" + str(roof_block))
                    self.mc.doCommand("fill " + str(x+width+1) + " " + str(y+(height*stories)+i+stories+4) + " " + str(z+depth//2+1) + " " + str(x+width+1) + " " + str(y+(height*stories)+i+stories+4) + " " + str(z+depth-i) + " minecraft:" + str(roof_block))
                self.mc.doCommand("fill " + str(x+4) + " " + str(int(y+(height*stories)+stories+(depth/2)+1)) + " " + str(z+depth//2+1) + " " + str(x+width-4) + " " + str(int(y+(height*stories)+stories+(depth/2)+3)) + " " + str(z+depth//2+1) + " minecraft:glass")
            if (depth % 2) != 0:
                i = int(depth/2) 
                self.mc.doCommand("fill " + str(x-1) + " " + str(int(y+(height*stories)+(depth/2)+1+stories+4)) + " " + str(z+depth//2+1) + " " + str(x+width+2) + " " + str(int(y+(height*stories)+(depth/2)+1+stories+4)) + " " + str(z+depth//2+1) + " minecraft:" + str(roof_stair_block) + "[facing=north]")
        y = y-1

        #Add Floor for each Story        
        a = 0
        b = stories
        while b >= 0:
            self.mc.setBlocks(x+1, y - 1+a, z+1, x+width, y - 1+a, z+depth, floorBlock,2)
            #self.self.mc.doCommand("fill " + str(x+1) + " " + str(y-1+a) + " " + str(z+1) + " " + str(x+width) + " " + str(y-1+a) + " " + str(z+depth) + " minecraft:calcite")
            b = b - 1
            a = a + height + 1

        #Add Front Door    
        if chosen_Template == 'stone' or chosen_Template == 'dark_blocks' :
            self.mc.doCommand("setblock " + str(x+door) + " " + str(y+1) + " " + str(z) +" minecraft:spruce_door[half=upper]")
            self.mc.doCommand("setblock " + str(x+door) + " " + str(y) + " " + str(z) +" minecraft:spruce_door[half=lower]")
            #self.mc.doCommand("setblock " + str(x+door) + " " + str(y) + " " + str(z) +" minecraft:air")
            #self.mc.doCommand("setblock " + str(x+door) + " " + str(y+1) + " " + str(z) +" minecraft:air")
        else:
            self.mc.setBlock(x+door, y+1, z, block.DOOR_WOOD.id, 9) # Order is important, number at end specifies direction of door
            self.mc.setBlock(x+door, y, z, block.DOOR_WOOD.id, 1)
        
        self.mc.setBlock(x+door, y-1, z, floorBlock,2)
        self.doorCoordinates.append((x+door,y-1,z - 1))   #Block in front of door
        
        #Create Rooms (Recursive Function)
        j =  random.randint(0,1)      #Alternates which axis wall is placed (0 is x-axis first, 1 is z-axis first)
        k = 2                         #Limits recursions to two
        self.frontDoorLocation = door #Retains front door location
        self.createRooms(x,y,z,x+width+1,y,z+depth+1,height,j,door,stories,k)
        
        #Add Furniture
        d = Furniture()
        roomMeasurementlist = []
        for i in self.roomCoordinates:
            roomMeasurementlist.append((math.fabs(i[0][0]-i[1][0])-1, math.fabs(i[0][2]-i[1][2])-1, i[0][1]))
        d.addFurniture(self.roomCoordinates,roomMeasurementlist,height)
        
        #Add Staircase if possible, if not add Ladder
        c.addStaircase(x,y,z,width,height,depth,stories)
        if c.addStaircase == False:
            self.createHouse(self,x, y, z, x2, y2, z2)

        #Create Windows for all stories
        b = 1
        for j in range(1,stories+1):
            for i in range(2,depth-2,5):
                InsideID = self.mc.getBlock(x+1,y+b,z+i)
                InsideID2 = self.mc.getBlock(x+1,y+b,z+i+1)
                if InsideID == 0 and InsideID2 == 0:
                    self.mc.setBlock(x,y+b,z+i,block.GLASS.id)
                    self.mc.setBlock(x,y+b+1,z+i,block.GLASS.id)
                    self.mc.setBlock(x,y+b,z+i+1,block.GLASS.id)
                    self.mc.setBlock(x,y+b+1,z+i+1,block.GLASS.id)
                    if j > 1:
                        #Top of Window
                        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+b+2) + " " + str(z+i) +" minecraft:" + str(window_stair_block) + "[facing=east]")
                        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+b+2) + " " + str(z+i+1) +" minecraft:" + str(window_stair_block) + "[facing=east]")
                        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+b+2) + " " + str(z+i+2) +" minecraft:" + str(window_slab) + "[type=bottom]")
                        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+b+2) + " " + str(z+i-1) +" minecraft:" + str(window_slab) + "[type=bottom]")
                        #Bottom of Window
                        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+b-1) + " " + str(z+i-1) +" minecraft:" + str(window_slab) + "[type=top]")
                        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+b-1) + " " + str(z+i+2) +" minecraft:" + str(window_slab) + "[type=top]")
                        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+b-1) + " " + str(z+i) +" minecraft:" + str(window_bottom_block))
                        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+b-1) + " " + str(z+i+1) +" minecraft:" + str(window_bottom_block))
                        #Sides of Window
                        self.mc.doCommand("fill " + str(x-1) + " " + str(y+b) + " " + str(z+i-1) + " " + str(x-1) + " " + str(y+b+1) + " " + str(z+i-1) +" minecraft:" + str(window_fence))
                        self.mc.doCommand("fill " + str(x-1) + " " + str(y+b) + " " + str(z+i+2) + " " + str(x-1) + " " + str(y+b+1) + " " + str(z+i+2) +" minecraft:" + str(window_fence))
                    else:
                        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+b-1) + " " + str(z+i) +" minecraft:" + str(window_ground_block))
                        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+b-1) + " " + str(z+i+1) +" minecraft:" + str(window_ground_block))
            for i in range(2,width-2,5):
                InsideID = self.mc.getBlock(x+i,y+b,z+1)
                InsideID2 = self.mc.getBlock(x+i+1,y+b,z+1)
                if InsideID == 0 and InsideID2 == 0 and i != self.frontDoorLocation and i+1 != self.frontDoorLocation:
                    self.mc.setBlock(x+i,y+b,z,block.GLASS.id)
                    self.mc.setBlock(x+i,y+b+1,z,block.GLASS.id)
                    self.mc.setBlock(x+i+1,y+b,z,block.GLASS.id)
                    self.mc.setBlock(x+i+1,y+b+1,z,block.GLASS.id)
                    if j > 1:
                        #Top of Window
                        self.mc.doCommand("setblock " + str(x+i) + " " + str(y+b+2) + " " + str(z-1) +" minecraft:" + str(window_stair_block) + "[facing=south]")
                        self.mc.doCommand("setblock " + str(x+i+1) + " " + str(y+b+2) + " " + str(z-1) +" minecraft:" + str(window_stair_block) + "[facing=south]")
                        self.mc.doCommand("setblock " + str(x+i-1) + " " + str(y+b+2) + " " + str(z-1) +" minecraft:" + str(window_slab) + "[type=bottom]")
                        self.mc.doCommand("setblock " + str(x+i+2) + " " + str(y+b+2) + " " + str(z-1) +" minecraft:" + str(window_slab) + "[type=bottom]")

                        #Bottom of Window
                        self.mc.doCommand("setblock " + str(x+i-1) + " " + str(y+b-1) + " " + str(z-1) +" minecraft:" + str(window_slab)+ "[type=top]")
                        self.mc.doCommand("setblock " + str(x+i+2) + " " + str(y+b-1) + " " + str(z-1) +" minecraft:" + str(window_slab)+ "[type=top]")
                        self.mc.doCommand("setblock " + str(x+i) + " " + str(y+b-1) + " " + str(z-1) +" minecraft:" + str(window_bottom_block))
                        self.mc.doCommand("setblock " + str(x+i+1) + " " + str(y+b-1) + " " + str(z-1) +" minecraft:" + str(window_bottom_block))
                        #Sides of Window
                        self.mc.doCommand("fill " + str(x+i-1) + " " + str(y+b) + " " + str(z-1) + " " + str(x+i-1) + " " + str(y+b+1) + " " + str(z-1) +" minecraft:" + str(window_fence))
                        self.mc.doCommand("fill " + str(x+i+2) + " " + str(y+b) + " " + str(z-1) + " " + str(x+i+2) + " " + str(y+b+1) + " " + str(z-1) +" minecraft:" + str(window_fence))
                    else:
                        self.mc.doCommand("setblock " + str(x+i) + " " + str(y+b-1) + " " + str(z-1) +" minecraft:" + str(window_ground_block))
                        self.mc.doCommand("setblock " + str(x+i+1) + " " + str(y+b-1) + " " + str(z-1) +" minecraft:" + str(window_ground_block))

            for i in range(2,depth-2,5):
                InsideID = self.mc.getBlock(x+width,y+b,z+i)
                InsideID2 = self.mc.getBlock(x+width,y+b,z+i+1)
                if InsideID == 0 and InsideID2 == 0:
                    self.mc.setBlock(x+width+1,y+b,z+i,block.GLASS.id)
                    self.mc.setBlock(x+width+1,y+b+1,z+i,block.GLASS.id)
                    self.mc.setBlock(x+width+1,y+b,z+i+1,block.GLASS.id)
                    self.mc.setBlock(x+width+1,y+b+1,z+i+1,block.GLASS.id)
                    if j > 1:
                        #Top of Window
                        self.mc.doCommand("setblock " + str(x+width+2) + " " + str(y+b+2) + " " + str(z+i) +" minecraft:" + str(window_stair_block) + "[facing=west]")
                        self.mc.doCommand("setblock " + str(x+width+2) + " " + str(y+b+2) + " " + str(z+i+1) +" minecraft:" + str(window_stair_block) + "[facing=west]")
                        self.mc.doCommand("setblock " + str(x+width+2) + " " + str(y+b+2) + " " + str(z+i-1) +" minecraft:" + str(window_slab)+ "[type=bottom]")
                        self.mc.doCommand("setblock " + str(x+width+2) + " " + str(y+b+2) + " " + str(z+i+2) +" minecraft:" + str(window_slab)+ "[type=bottom]")
                        #Bottom of Window
                        self.mc.doCommand("setblock " + str(x+width+2) + " " + str(y+b-1) + " " + str(z+i-1) +" minecraft:" + str(window_slab)+ "[type=top]")
                        self.mc.doCommand("setblock " + str(x+width+2) + " " + str(y+b-1) + " " + str(z+i+2) +" minecraft:" + str(window_slab)+ "[type=top]")
                        self.mc.doCommand("setblock " + str(x+width+2) + " " + str(y+b-1) + " " + str(z+i) +" minecraft:" + str(window_bottom_block))
                        self.mc.doCommand("setblock " + str(x+width+2) + " " + str(y+b-1) + " " + str(z+i+1) +" minecraft:" + str(window_bottom_block))
                        #Sides of Window
                        self.mc.doCommand("fill " + str(x+width+2) + " " + str(y+b) + " " + str(z+i-1) + " " + str(x+width+2) + " " + str(y+b+1) + " " + str(z+i-1)+" minecraft:" + str(window_fence))
                        self.mc.doCommand("fill " + str(x+width+2) + " " + str(y+b) + " " + str(z+i+2) + " " + str(x+width+2) + " " + str(y+b+1) + " " + str(z+i+2)+" minecraft:" + str(window_fence))
                    else:
                        self.mc.doCommand("setblock " + str(x+width+2) + " " + str(y+b-1) + " " + str(z+i) +" minecraft:" + str(window_ground_block))
                        self.mc.doCommand("setblock " + str(x+width+2) + " " + str(y+b-1) + " " + str(z+i+1) +" minecraft:" + str(window_ground_block))
            for i in range(2,width-2,5):
                InsideID = self.mc.getBlock(x+i,y+b,z+depth)
                InsideID2 = self.mc.getBlock(x+i+1,y+b,z+depth)
                if InsideID == 0 and InsideID2 == 0:
                    self.mc.setBlock(x+i,y+b,z+depth+1,block.GLASS.id)
                    self.mc.setBlock(x+i,y+b+1,z+depth+1,block.GLASS.id)
                    self.mc.setBlock(x+i+1,y+b,z+depth+1,block.GLASS.id)
                    self.mc.setBlock(x+i+1,y+b+1,z+depth+1,block.GLASS.id)
                    if j > 1:
                        #Top of Window
                        self.mc.doCommand("setblock " + str(x+i+1) + " " + str(y+b+2) + " " + str(z+depth+2) +" minecraft:" + str(window_stair_block) + "[facing=north]")
                        self.mc.doCommand("setblock " + str(x+i) + " " + str(y+b+2) + " " + str(z+depth+2) +" minecraft:" + str(window_stair_block) + "[facing=north]") 
                        self.mc.doCommand("setblock " + str(x+i-1) + " " + str(y+b+2) + " " + str(z+depth+2) +" minecraft:" + str(window_slab)+ "[type=bottom]") 
                        self.mc.doCommand("setblock " + str(x+i+2) + " " + str(y+b+2) + " " + str(z+depth+2) +" minecraft:" + str(window_slab)+ "[type=bottom]") 
                        #Bottom of Window
                        self.mc.doCommand("setblock " + str(x+i-1) + " " + str(y+b-1) + " " + str(z+depth+2) +" minecraft:" + str(window_slab)+ "[type=top]") 
                        self.mc.doCommand("setblock " + str(x+i+2) + " " + str(y+b-1) + " " + str(z+depth+2) +" minecraft:" + str(window_slab)+ "[type=top]") 
                        self.mc.doCommand("setblock " + str(x+i) + " " + str(y+b-1) + " " + str(z+depth+2) +" minecraft:" + str(window_bottom_block))
                        self.mc.doCommand("setblock " + str(x+i+1) + " " + str(y+b-1) + " " + str(z+depth+2) +" minecraft:" + str(window_bottom_block)) 
                        #Sides of Window
                        self.mc.doCommand("fill " + str(x+i-1) + " " + str(y+b) + " " + str(z+depth+2) + " " + str(x+i-1) + " " + str(y+b+1) + " " + str(z+depth+2) + " minecraft:" + str(window_fence)) 
                        self.mc.doCommand("fill " + str(x+i+2) + " " + str(y+b) + " " + str(z+depth+2) + " " + str(x+i+2) + " " + str(y+b+1) + " " + str(z+depth+2) + " minecraft:" + str(window_fence)) 
                    else:
                        self.mc.doCommand("setblock " + str(x+i) + " " + str(y+b-1) + " " + str(z+depth+2) +" minecraft:" + str(window_ground_block))
                        self.mc.doCommand("setblock " + str(x+i+1) + " " + str(y+b-1) + " " + str(z+depth+2) +" minecraft:" + str(window_ground_block)) 
                    
            b = b + height + 1

        return self.doorCoordinates

    def createRooms(self, x1, y1, z1, x2, y2, z2, h, j, doorLocation, stories, k):
        
        #If stories == 2, generate second story
        if stories == 2:
            stories = stories - 1
            j = random.randint(0,1)
            self.createRooms(x1, y1+(h)+1, z1, x2, y2+(h)+1, z2, h,j,doorLocation,stories, k)

        #Get x distance of target room
        xdistance = math.fabs(x1-x2) -1
        #Get z distance of target room
        zdistance = math.fabs(z1-z2) -1         

        if j == 0 and zdistance >=5 and xdistance >=3 and k >0:
            if stories >= 2:
                i = random.randrange(math.ceil(zdistance/2) -1,math.ceil(zdistance/2)+2)
            else:
                i = random.randrange(3, zdistance-2)
            #Make sure inner wall is not placed on door
            if i == doorLocation:
                if random.random() < 0.5:
                    i = i + 1
                else:
                    i = i -1

            #Place inner dividing wall
            self.mc.setBlocks(x1+1, y1, z1+(i), x1+xdistance,y1+h-1,z1+(i),block.WOOD_PLANKS.id)
            #Randomize and place door on inner wall
            doorLocation = random.randrange(1,xdistance)
            self.mc.setBlock(x1+doorLocation, y1+1,z1+(i), block.DOOR_WOOD.id,9)
            self.mc.setBlock(x1+doorLocation, y1,z1+(i), block.DOOR_WOOD.id,1)

            #Place Torch on wall
            self.mc.setBlock(x1+doorLocation+1, y1+1,z1+(i)-1, block.TORCH.id,4)

            #Subdivide room 1 if a >= 1:
            j = 1
            a = random.randint(0,3)
            if a >=1:
                x2 = x1 + xdistance + 1
                y2 = y1
                z2 = z1 + i
                if k == 1:
                    self.roomCoordinates.append(((x1,y1,z1),(x2,y2,z2)))
                self.createRooms(x1, y1, z1, x2, y2, z2, h,j, doorLocation, stories, k-1)
            else:
                if k >0:
                    x2 = x1 + xdistance + 1
                    y2 = y1
                    z2 = z1 + i
                    self.roomCoordinates.append(((x1,y1,z1),(x2,y2,z2)))
        
            #Subdivide room 2 if a >= 1:
            a = random.randint(0,3)
            if a >=1:
                z1v1 = z1 + i
                x2 = x1 + xdistance + 1
                y2 = y1
                z2 = z1v1 + (zdistance - i) + 1
                if k == 1:
                    self.roomCoordinates.append(((x1,y1,z1v1),(x2,y2,z2)))
                self.createRooms(x1, y1, z1v1, x2, y2, z2, h,j,doorLocation, stories, k-1)
            else:
                if k >0:
                    z1v1 = z1 + i
                    x2 = x1 + xdistance + 1
                    y2 = y1
                    z2 = z1v1 + (zdistance - i) + 1
                    self.roomCoordinates.append(((x1,y1,z1v1),(x2,y2,z2)))
            

        elif j ==1 and xdistance >=5 and zdistance >=3 and k >0:
            if stories >=2:
                i = random.randrange(math.ceil(xdistance/2) -1,math.ceil(xdistance/2)+2)
            else:
                i = random.randrange(3, xdistance-2)
            if i == doorLocation:
                if random.random() < 0.5:
                    i = i + 1
                else:
                    i = i -1
            #Check if wall is placed on front door, if it is add or minus 1 block
            elif stories == 1 and i == self.frontDoorlocation:
                if random.random() < 0.5:
                    i = i + 1
                else:
                    i = i -1
                if i == doorLocation:
                    if random.random() < 0.5:
                        i = i + 1
                    else:
                        i = i -1
            #Place Inner wall
            self.mc.setBlocks(x1+i, y1, z1+1, x1+i,y1+h-1,z1+zdistance,block.WOOD_PLANKS.id)
            #Randomize and place inner door
            doorLocation = random.randrange(1,zdistance)
            self.mc.setBlock(x1+i, y1+1,z1+doorLocation, block.DOOR_WOOD.id,10)
            self.mc.setBlock(x1+i, y1,z1+doorLocation, block.DOOR_WOOD.id,2)

            #Place Torch on wall next to door
            self.mc.setBlock(x1+i+1, y1+1,z1+doorLocation+1, block.TORCH.id,1)

            j = 0
            #Subdivide Room 1 if a >=1
            a = random.randint(0,3)
            if a >=1:
                x2 = x1 + i
                y2 = y1
                z2 = z1 +zdistance + 1
                if k == 1:
                    self.roomCoordinates.append(((x1,y1,z1),(x2,y2,z2)))
                self.createRooms(x1, y1, z1, x2, y2, z2, h,j ,doorLocation, stories, k-1)
            else:
                if k >0:
                    x2 = x1 + i
                    y2 = y1
                    z2 = z1 +zdistance + 1
                    self.roomCoordinates.append(((x1,y1,z1),(x2,y2,z2)))
            
            #Subdivide Room 2 if a >=1
            a = random.randint(0,3)
            if a >=1:
                x2 = x1 + xdistance + 1
                z2 = z1 + zdistance + 1
                y2 = y1
                x1v1 = x1 + i
                if k == 1:
                    self.roomCoordinates.append(((x1v1,y1,z1),(x2,y2,z2)))
                self.createRooms(x1v1, y1, z1, x2, y2, z2, h,j,doorLocation,stories, k-1)
            else:
                if k >0:
                    x2 = x1 + xdistance + 1
                    z2 = z1 + zdistance + 1
                    y2 = y1
                    x1v1 = x1 + i
                    self.roomCoordinates.append(((x1v1,y1,z1),(x2,y2,z2)))

    def getDoorCoordinates(self):
        return self.doorCoordinates
            

    def getHouseCoordinates(self):
        return self.houseCoordinates


        
        

        

            
                
    