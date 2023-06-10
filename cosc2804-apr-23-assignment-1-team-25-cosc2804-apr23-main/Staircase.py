from mcpi import minecraft, block
import random
from Furniture import Furniture
mc = minecraft.Minecraft.create()

# 1 facing right
# 2 facing front
# 3 facing back
# 8 facing left

class StairCaseDesigns:
    mc = minecraft.Minecraft.create()

    def addStaircase(self,x,y,z,w,h,d,stories):
        mc = self.mc
        #1 = back right, 2 = back left, 3 = front left, 4 = front right
        o = Furniture()
        Check = True
        if stories == 1:
            stairs = 1
        else:
            stairs = 0
        list = [1,2,3,4]
        r = random.choice(list)
        list.remove(r)
        
        while stairs != 1 and bool(list):
            if stories > 1:
                if r == 1:
                    Check = True
                    level1 = mc.getBlocks(x+1,y,z+d,x+3,y+h-1,z+d-2)
                    level2 = mc.getBlocks(x+1,y+h+1,z+d,x+3,y+(h*2)-2,z+d-2)
                    #mc.doCommand("fill " + str(x+1) + " " + str(y) + " " + str(z+d) + " " + str(x+3) + " " + str(y+h-1) + " " + str(z+d-2) + " minecraft:grass_block")
                    #mc.doCommand("fill " + str(x+1) + " " + str(y+h+1) + " " + str(z+d) + " " + str(x+3) + " " + str(y+(h*2)-2) + " " + str(z+d-2) + " minecraft:grass_block")
                    
                    for cube in level1:
                        if cube != 0:
                            Check = False
                            break
                    for cube in level2:
                        if cube != 0:
                            Check = False
                            break
                    if Check == True:
                        if h == 3:
                            self.createSpiralStaircaseFront(x+1,y,z+d-1,h)
                        elif h == 4:
                            self.createSpiralStaircaseLeft(x+1,y,z+d-1,h)
                        stairs = 1
                    else:
                        r = random.choice(list)
                        list.remove(r)
                    
                elif r == 2:
                    Check = True
                    level1 = mc.getBlocks(x+w-2,y,z+d-2,x+w,y+h-1,z+d)
                    level2 = mc.getBlocks(x+w-2,y+h+1,z+d-2,x+w,y+(h*2),z+d)
                    #mc.doCommand("fill " + str(x+w-2) + " " + str(y) + " " + str(z+d-2) + " " + str(x+w) + " " + str(y+h-1) + " " + str(z+d) + " minecraft:grass_block")
                    #mc.doCommand("fill " + str(x+w-2) + " " + str(y+h+1) + " " + str(z+d-2) + " " + str(x+w) + " " + str(y+(h*2)) + " " + str(z+d) + " minecraft:grass_block")
                    
                    for cube in level1:
                        if cube != 0:
                            Check = False
                            break
                    for cube in level2:
                        if cube != 0:
                            Check = False
                            break
                    if Check == True:
                        if h == 3:
                            self.createSpiralStaircaseFront(x+w-2,y,z+d-1,h)
                        elif h == 4:
                            self.createSpiralStaircaseFront(x+w-2,y,z+d-1,h)
                        stairs = 1
                    else:
                        r = random.choice(list)
                        list.remove(r)
                    
                elif r == 3:
                    Check = True
                    level1 = mc.getBlocks(x+w-2,y,z+1,x+w,y+h-1,z+3)
                    level2 = mc.getBlocks(x+w-2,y+h+1,z+1,x+w,y+(h*2)-2,z+3)
                    
                    for cube in level1:
                        if cube != 0:
                            Check = False
                            break
                    for cube in level2:
                        if cube != 0:
                            Check = False
                            break
                    if Check == True:
                        if h == 3:
                            self.createSpiralStaircaseRight(x+w-2,y,z+2,h)
                        elif h == 4:
                            self.createSpiralStaircaseRight(x+w-2,y,z+2,h)
                        stairs = 1
                    else:
                        r = random.choice(list)
                        list.remove(r)
                    
                elif r == 4:
                    Check = True
                    level1 = mc.getBlocks(x+1,y,z+1,x+3,y+h-1,z+3)
                    level2 = mc.getBlocks(x+1,y+h+1,z+1,x+3,y+(h*2)-2,z+3)
                    
                    for cube in level1:
                        if cube != 0:
                            Check = False
                            break
                    for cube in level2:
                        if cube != 0:
                            Check = False
                            break
                    if Check == True:
                        if h == 3:
                            self.createSpiralStaircaseLeft(x+1,y,z+2,h)
                        elif h == 4:
                            self.createSpiralStaircaseRight(x+1,y,z+2,h)
                        stairs = 1
                    else:
                        r = random.choice(list)
                        list.remove(r)
            else:
                break       
        if stairs != 1:

            o.createLadder(x,y,z+d)

                   
    def createSpiralStaircaseFront(self,x,y,z,h):
        mc = self.mc
        mc.setBlocks(x,y,z-1,x+2,y+(h),z+1,block.AIR.id)
        
        mc.setBlocks(x+1,y,z,x+1,y+h,z,block.WOOD_PLANKS.id)
        mc.setBlock(x,y,z,(block.STAIRS_WOOD.id),2)
        mc.setBlock(x,y,z+1,block.WOOD_PLANKS.id)
        mc.setBlock(x+1,y+1,z+1,(block.STAIRS_WOOD.id),8)
        mc.setBlock(x+2,y+1,z+1,block.WOOD_PLANKS.id)
        mc.setBlock(x+2,y+2,z,(block.STAIRS_WOOD.id),3)
        mc.setBlock(x+2,y+2,z-1,block.WOOD_PLANKS.id)
        mc.setBlock(x+1,y+3,z-1,(block.STAIRS_WOOD.id),1)
        mc.setBlock(x,y+3,z-1,block.WOOD_PLANKS.id)
        if h == 4:
            mc.setBlock(x,y+4,z,(block.STAIRS_WOOD.id),2)
            mc.setBlock(x,y+4,z+1,block.WOOD_PLANKS.id)             

    def createSpiralStaircaseLeft(self,x,y,z,h):   
        mc = self.mc
        mc.setBlocks(x,y,z-1,x+2,y+(h),z+1,block.AIR.id)
        
        #Standing pole for staircase
        mc.setBlocks(x+1,y,z,x+1,y+h,z,block.WOOD_PLANKS.id)
        #First step
        mc.setBlock(x+1,y,z-1,(block.STAIRS_WOOD.id),1)
        mc.setBlock(x,y,z-1,block.WOOD_PLANKS.id)
        #Second step
        mc.setBlock(x,y+1,z,(block.STAIRS_WOOD.id),2)
        mc.setBlock(x,y+1,z+1,block.WOOD_PLANKS.id)
        #Third step
        mc.setBlock(x+1,y+2,z+1,(block.STAIRS_WOOD.id),8)
        mc.setBlock(x+2,y+2,z+1,block.WOOD_PLANKS.id)
        #Fourth step
        mc.setBlock(x+2,y+3,z,(block.STAIRS_WOOD.id),3)
        mc.setBlock(x+2,y+3,z-1,block.WOOD_PLANKS.id)
        if h == 4:
            mc.setBlock(x+1,y+4,z-1,(block.STAIRS_WOOD.id),1)
            mc.setBlock(x,y+4,z-1,block.WOOD_PLANKS.id)
            
    def createSpiralStaircaseRight(self,x,y,z,h):
        mc = self.mc
        mc.setBlocks(x,y,z-1,x+2,y+(h),z+1,block.AIR.id)
        
        mc.setBlocks(x+1,y,z,x+1,y+h,z,block.WOOD_PLANKS.id)
        mc.setBlock(x+1,y,z+1,(block.STAIRS_WOOD.id),8)
        mc.setBlock(x+2,y,z+1,block.WOOD_PLANKS.id)
        mc.setBlock(x+2,y+1,z,(block.STAIRS_WOOD.id),3)
        mc.setBlock(x+2,y+1,z-1,block.WOOD_PLANKS.id)
        mc.setBlock(x+1,y+2,z-1,(block.STAIRS_WOOD.id),1)
        mc.setBlock(x,y+2,z-1,block.WOOD_PLANKS.id)
        mc.setBlock(x,y+3,z,(block.STAIRS_WOOD.id),2)
        mc.setBlock(x,y+3,z+1,block.WOOD_PLANKS.id)
        if h ==4:
            mc.setBlock(x+1,y+4,z+1,(block.STAIRS_WOOD.id),8)
            mc.setBlock(x+2,y+4,z+1,block.WOOD_PLANKS.id)

    def createSpiralStaircaseBack(self,x,y,z,h):
        mc = self.mc
        mc.setBlocks(x,y,z-1,x+2,y+h,z+1,block.AIR.id)
        
        mc.setBlocks(x+1,y,z,x+1,y+h,z,block.WOOD_PLANKS.id)
        mc.setBlock(x+2,y,z,(block.STAIRS_WOOD.id),3)
        mc.setBlock(x+2,y,z-1,block.WOOD_PLANKS.id)
        mc.setBlock(x+1,y+1,z-1,(block.STAIRS_WOOD.id),1)
        mc.setBlock(x,y+1,z-1,block.WOOD_PLANKS.id)
        mc.setBlock(x,y+2,z,(block.STAIRS_WOOD.id),2)
        mc.setBlock(x,y+2,z+1,block.WOOD_PLANKS.id)
        mc.setBlock(x+1,y+3,z+1,(block.STAIRS_WOOD.id),8)
        mc.setBlock(x+2,y+3,z+1,block.WOOD_PLANKS.id)
        if h == 4:
            mc.setBlock(x+2,y+4,z,(block.STAIRS_WOOD.id),3)
            mc.setBlock(x+2,y+4,z-1,block.WOOD_PLANKS.id)
    
        
            
         

