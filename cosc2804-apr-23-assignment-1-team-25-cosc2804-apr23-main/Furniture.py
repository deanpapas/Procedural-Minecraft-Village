from mcpi.minecraft import Minecraft
import random
class Furniture():
    crafting_table = False
    bed = False
    kitchen = False
    workbench = False
    table = False
    fancyTable = False
    fancyCabinet = False
    sideBench = False
    firePlace = False
    lightPost = False
    wallShelf = False
    indoorTree = False

    def __init__(self):
        self.mc = Minecraft.create()
    def addFurniture(self, roomCoordinates,roomMeasurementList,height):
        j = 0
        
        #Add Furniture based on length and width of each room
        for i in roomCoordinates:
            
            if roomMeasurementList[j][0] >5 and roomMeasurementList[j][1] > 5 and self.bed == False:
                self.createBed(i[0][0]+2,i[0][1],i[0][2]+1)
                self.bed = True
            
            elif roomMeasurementList[j][0] >6 and roomMeasurementList[j][1] > 6 and self.kitchen == False:
                self.createKitchen(int(i[0][0]+(roomMeasurementList[j][0]//2)),i[0][1],i[0][2]+int(roomMeasurementList[j][1]//2)-1)
                self.kitchen = True

            elif roomMeasurementList[j][0] >5 and roomMeasurementList[j][1] > 6 and self.firePlace == False:
                self.createFirePlace(int(i[0][0]+(roomMeasurementList[j][0])-2),i[0][1],int(i[0][2]+roomMeasurementList[j][1]//2))
                self.firePlace = True

            elif roomMeasurementList[j][0] >5 and roomMeasurementList[j][1] >5 and self.fancyTable == False:
                self.createFancytable(int(i[0][0]+(roomMeasurementList[j][0]//2)),i[0][1],int(i[0][2]+(roomMeasurementList[j][1]//2)-1))
                self.fancyTable = True
            
            elif roomMeasurementList[j][0] >5 and roomMeasurementList[j][1] >5 and self.fancyTable == False:
                self.createFancytable(int(i[0][0]+(roomMeasurementList[j][0]//2)),i[0][1],int(i[0][2]+(roomMeasurementList[j][1]//2)-1))
                self.fancyTable = True

            elif roomMeasurementList[j][0] >5 and roomMeasurementList[j][1] >4 and self.fancyCabinet == False:
                self.createFancyCabinet(int(i[0][0]+2),i[0][1],i[0][2]+2)
                self.fancyCabinet = True
            
            elif roomMeasurementList[j][0] >3 and 4< roomMeasurementList[j][1] <6 and self.sideBench == False:
                self.createBench(int(i[0][0]+(int(roomMeasurementList[j][0]//2))),int(i[0][1]),int(i[0][0]+1))
                self.sideBench = True

            j = j +1

        j = 0
        for i in roomCoordinates: #If no room for Proper Bed, add simple bed
            if roomMeasurementList[j][0] >2 and roomMeasurementList[j][1] > 2 and self.bed == False:
                self.createSimpleBed(i[0][0]+2,i[0][1],i[0][2]+1)
                self.bed = True
            j = j +1
        #add middle lamps and corner lamps to each room
        j = 0
        for i in roomCoordinates:
            self.createMiddleLamp(int(i[0][0]+(roomMeasurementList[j][0]/2)),int(i[0][1]+height-1),int(i[0][2]+(roomMeasurementList[j][1]/2)))
            a = random.randint(0,1)
            if a == 1 and roomMeasurementList[j][0] >4 and roomMeasurementList[j][1] > 4 and self.lightPost == False:
                self.createLightPost(int(i[0][0]+roomMeasurementList[j][0])-1,int(i[0][1]),int(i[0][2]+2))
                self.lightPost = True
            elif a == 0 and roomMeasurementList[j][0] >2 and roomMeasurementList[j][1] > 2 and self.wallShelf == False:
                self.createWallShelf(int(i[0][0]+int(roomMeasurementList[j][0]//2)),int(i[0][1]),int(i[0][2]+roomMeasurementList[j][1]))
                self.wallShelf = True
            elif roomMeasurementList[j][0] >2 and roomMeasurementList[j][1] >2 and self.indoorTree == False:
                self.createIndoorTree(int(i[1][0]-2),int(i[0][1]),int(i[0][2]+2))
                self.indoorTree = True
            j = j + 1
        
    def createSimpleBed(self,x,y,z):
        self.mc.setBlock(x, y, z+1, 26,4) 
        self.mc.setBlock(x, y, z+2, 26,8) 

    def createBed(self,x,y,z):

        self.mc.setBlock(x, y, z+1, 126, 1)
        self.mc.setBlock(x, y, z+2, 126, 1) 
        self.mc.setBlock(x, y, z+3, 47)
        self.mc.setBlock(x, y, z+4, 5,1) 
        self.mc.setBlock(x, y+1, z+4, 5,1)   
        self.mc.setBlock(x+1, y, z+1, 126,1) 
        self.mc.setBlock(x+1, y, z+2, 26,1) 
        self.mc.setBlock(x+1, y, z+3, 26,8) 
        self.mc.setBlock(x+1, y, z+4, 5,1) 
        self.mc.setBlock(x+1, y+1, z+4, 53,6)  
        self.mc.setBlock(x+2, y, z+1, 126,1) 
        self.mc.setBlock(x+2, y, z+2, 26,1) 
        self.mc.setBlock(x+2, y, z+3, 26,8) 
        self.mc.setBlock(x+2, y, z+4, 5,1) 
        self.mc.setBlock(x+2, y+1, z+4, 53,6)  
        self.mc.setBlock(x+3, y, z+1, 126,1) 
        self.mc.setBlock(x+3, y, z+2, 126,1) 
        self.mc.setBlock(x+3, y, z+3, 47) 
        self.mc.setBlock(x+3, y, z+4, 5,1) 
        self.mc.setBlock(x+3, y+1, z+4, 5,1)

    def createKitchen(self,x,y,z):

        self.mc.setBlock(x, y, z+1, 42)
        self.mc.setBlock(x, y, z+2, 118)
        self.mc.setBlock(x, y, z+3, 118)
        self.mc.setBlock(x, y, z+4, 42)
        self.mc.setBlock(x+1, y, z+4, 62)
        self.mc.setBlock(x+2, y, z+4, 62)
        self.mc.setBlock(x+3, y, z+4, 42)
        self.mc.setBlock(x+3, y, z+3, 42)
        self.mc.setBlock(x+3, y, z+2, 58)
        self.mc.setBlock(x+3, y, z+1, 42)
        self.mc.doCommand("setblock " + str(x) + " " + str(y+1) + " " + str(z+4) + " minecraft:potted_fern")

    def createWorkbench(self,x,y,z):

        self.mc.setBlock(x, y, z, 98)
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y) + " " + str(z) + " minecraft:anvil")
        self.mc.doCommand("setblock " + str(x+2) + " " + str(y) + " " + str(z) + " minecraft:blast_furnace")
        self.mc.setBlock(x+3, y, z, 54)
        self.mc.setBlock(x+4, y, z, 98)

    def createTable(self,x,y,z):

        self.mc.setBlock(x, y, z+1, 85)
        self.mc.doCommand("setblock " + str(x) + " " + str(y+1) + " " + str(z+1) + " minecraft:oak_pressure_plate")
        self.mc.doCommand("setblock " + str(x-1) + " " + str(y) + " " + str(z+1) + " minecraft:oak_stairs[facing=west]")

    def createFancytable(self,x,y,z): #X=3,Z=3
        #Add table legs
        self.mc.setBlock(x, y, z+1, 85)
        self.mc.setBlock(x+2, y, z+1, 85)
        self.mc.setBlock(x, y, z+3, 85)
        self.mc.setBlock(x+2, y, z+3, 85)

        #Add Barriers
        self.mc.doCommand("setblock " + str(x) + " " + str(y) + " " + str(z+2) + " minecraft:barrier")
        self.mc.doCommand("setblock " + str(x+2) + " " + str(y) + " " + str(z+2) + " minecraft:barrier")
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y) + " " + str(z+3) + " minecraft:barrier")
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y) + " " + str(z+1) + " minecraft:barrier")

        #Add table top
        self.mc.doCommand("setblock " + str(x) + " " + str(y+1) + " " + str(z+1) + " minecraft:white_carpet")
        self.mc.doCommand("setblock " + str(x) + " " + str(y+1) + " " + str(z+2) + " minecraft:white_carpet")
        self.mc.doCommand("setblock " + str(x) + " " + str(y+1) + " " + str(z+3) + " minecraft:white_carpet")
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y+1) + " " + str(z+1) + " minecraft:white_carpet")
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y+1) + " " + str(z+3) + " minecraft:white_carpet")
        self.mc.doCommand("setblock " + str(x+2) + " " + str(y+1) + " " + str(z+1) + " minecraft:white_carpet")
        self.mc.doCommand("setblock " + str(x+2) + " " + str(y+1) + " " + str(z+2) + " minecraft:white_carpet")
        self.mc.doCommand("setblock " + str(x+2) + " " + str(y+1) + " " + str(z+3) + " minecraft:white_carpet")
        #Add Middle of Table with flower pot
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y) + " " + str(z+2) + " minecraft:spruce_trapdoor[half=top]")
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y+1) + " " + str(z+2) + " minecraft:potted_lily_of_the_valley")

    def createBench(self,x,y,z):    #X=1,Z=3
        #Add bench supports
        self.mc.doCommand("setblock " + str(x) + " " + str(y) + " " + str(z) + " minecraft:iron_bars")
        self.mc.doCommand("setblock " + str(x) + " " + str(y) + " " + str(z+2) + " minecraft:iron_bars")
        #Add barrier Block
        self.mc.doCommand("setblock " + str(x) + " " + str(y) + " " + str(z+1) + " minecraft:barrier")
        #Add Bench Top
        self.mc.doCommand("fill " + str(x) + " " + str(y+1) + " " + str(z) + " " + str(x) + " " + str(y+1) + " " + str(z+2) + " minecraft:brown_carpet")
    
    def createFancyCabinet(self,x,y,z): #X=2,Z=3
        #Create Block of Dark Oak Logs
        self.mc.doCommand("fill " + str(x) + " " + str(y) + " " + str(z) + " " + str(x+1) + " " + str(y+2) + " " + str(z+2) + " minecraft:dark_oak_log[axis=x]")
        #Add chest
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y) + " " + str(z+1) + " minecraft:chest[facing=east]")
        #Add lantern
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y+1) + " " + str(z) + " minecraft:lantern")
        #Add top section
        self.mc.doCommand("fill " + str(x+1) + " " + str(y+2) + " " + str(z) + " " + str(x+1) + " " + str(y+2) + " " + str(z+2) + " minecraft:dark_oak_stairs[facing=west]")
        #Add Flower
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y+1) + " " + str(z+2) + " minecraft:potted_fern")
        #Add Bookshelf
        self.mc.doCommand("fill " + str(x) + " " + str(y+1) + " " + str(z) + " " + str(x) + " " + str(y+1) + " " + str(z+2) + " minecraft:bookshelf")
        #Remove inner wood block
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y+1) + " " + str(z+1) + " minecraft:air")

    def createMiddleLamp(self,x,y,z):
        self.mc.doCommand("setblock " + str(x) + " " + str(y) + " " + str(z) + " minecraft:lantern[hanging=true]")

    def createLightPost(self,x,y,z):
        self.mc.doCommand("setblock " + str(x) + " " + str(y) + " " + str(z) + " minecraft:cauldron")
        self.mc.doCommand("setblock " + str(x) + " " + str(y+1) + " " + str(z) + " minecraft:anvil")
        self.mc.doCommand("setblock " + str(x) + " " + str(y+2) + " " + str(z) + " minecraft:glowstone")
        self.mc.doCommand("setblock " + str(x-1) + " " + str(y+2) + " " + str(z) + " minecraft:ladder[facing=west]")
        self.mc.doCommand("setblock " + str(x) + " " + str(y+2) + " " + str(z-1) + " minecraft:ladder[facing=north]")
        self.mc.doCommand("setblock " + str(x+1) + " " + str(y+2) + " " + str(z) + " minecraft:ladder[facing=east]")
        self.mc.doCommand("setblock " + str(x) + " " + str(y+2) + " " + str(z+1) + " minecraft:ladder[facing=south]")
        
    def createWallShelf(self,x,y,z):
        self.mc.doCommand("fill " + str(x) + " " + str(y+2) + " " + str(z) + " " + str(x+1) + " " + str(y+2) + " " + str(z) + " minecraft:spruce_trapdoor")

    def createFirePlace(self,x,y,z):
        self.mc.doCommand("fill " + str(x) + " " + str(y) + " " + str(z) + " " + str(x+1) + " " + str(y+2) + " " + str(z+2) + " minecraft:cobblestone")
        self.mc.doCommand("fill " + str(x) + " " + str(y+2) + " " + str(z) + " " + str(x) + " " + str(y+2) + " " + str(z+2) + " minecraft:cobblestone_stairs[facing=east]")
        self.mc.doCommand("fill " + str(x) + " " + str(y+1) + " " + str(z) + " " + str(x) + " " + str(y+1) + " " + str(z+2) + " minecraft:air")
        self.mc.doCommand("fill " + str(x-1) + " " + str(y) + " " + str(z) + " " + str(x-1) + " " + str(y) + " " + str(z+2) + " minecraft:cobblestone_stairs[facing=east]")
        self.mc.doCommand("setblock " + str(x) + " " + str(y) + " "+ str(z+1) +  " minecraft:campfire")
    def createLadder(self,x,y,z):
        self.mc.doCommand("fill " + str(x+1) + " " + str(y) + " " + str(z) + " " + str(x+1) + " " + str(y+4) + " " + str(z) + " minecraft:ladder[facing=east]")
    def createIndoorTree(self,x,y,z):
        self.mc.doCommand("setblock " + str(x) + " " + str(y) + " " + str(z) + " minecraft:composter[level=8]")
        self.mc.doCommand("setblock " + str(x) + " " + str(y+1) + " " + str(z) + " minecraft:dark_oak_fence")
        self.mc.doCommand("setblock " + str(x) + " " + str(y+2) + " " + str(z) + " minecraft:flowering_azalea_leaves[persistent=true]")
    