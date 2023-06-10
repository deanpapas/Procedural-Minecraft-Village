from mcpi.minecraft import Minecraft
from CreateHouse import House
from Staircase import StairCaseDesigns
from TerrainCapture import TerrainCapture
from PathBuilder import PathBuilder
from VillageWall import VillageWall
from Chunk import Chunk, Sites
from Node import Node
from Decorations import decorateArea
from Decorations import Backyard

mc = Minecraft.create()

quit = False
while not quit:

    chatEvents = mc.events.pollChatPosts()
    for chatEvent in chatEvents:

        if chatEvent.message.upper() == "./QUIT":
            quit = True
        elif chatEvent.message.upper() == "./BUILD":

            # Get Player Position
            x, y, z = mc.player.getTilePos()

            # Define Areas
            village_area = ((x-80, mc.getHeight(x-80, z-80), z-80),
                     (x+80, mc.getHeight(x+80, z+80), z+80))
            village_area_node_0 = Node(village_area[0][0], village_area[0][1], village_area[0][2])
            village_area_node_1 = Node(village_area[1][0], village_area[1][1], village_area[1][2])
            build_area_node_0 = Node(village_area_node_0.x + 25, village_area_node_0.y, village_area_node_0.z + 25)
            build_area_node_1 = Node(village_area_node_1.x - 25, village_area_node_1.y, village_area_node_1.z - 25)
            
            # Clear Area
            tc = TerrainCapture()
            tc.cleanArea(village_area_node_0, village_area_node_1)

            # Capture Terrain for Wall
            wall_map = TerrainCapture.captureMap(tc, village_area_node_0, village_area_node_1)
            
            # Build Wall
            vw = VillageWall()
            gate_locations = vw.buildWall(village_area_node_0, village_area_node_1, wall_map)

            # Capture Terrain for Village
            map = TerrainCapture.captureMap(tc, build_area_node_0, build_area_node_1)

            # Terraforming Area
            ch = Chunk()
            site_dict = Chunk.get_chunks(ch, map) 
            Sites.levelSites(site_dict)

            # Build Houses                
            GenerateHouse = House()
            c = StairCaseDesigns()
            b = Backyard()

            for key in site_dict:
                surface = (site_dict[key]['house_start'][1]) + 1
                x = site_dict[key]['house_start'][0]
                y = site_dict[key]['house_start'][1]+1
                z = site_dict[key]['house_start'][2]
                x2 = site_dict[key]['house_end'][0]
                y2 = site_dict[key]['house_end'][1]+1
                z2 = site_dict[key]['house_end'][2]
                GenerateHouse.createHouse(x,y,z,x2,y2,z2)

                site_z = site_dict[key]['site_end'][1]
                # Check there's enough room in site for backyard to be built
                if (site_z - z2) >= 8:
                    b.decorateBackyard(x, y2, z2+1, x2, y2, site_z)
                
            # Recapture Terrain
            new_map = TerrainCapture.captureMap(tc, village_area_node_0, village_area_node_1)

            # Remove Houses from New Map
            overlap = set()
            for key in site_dict:
                start = site_dict[key]['site_start']
                end = site_dict[key]['site_end']
            
                x1, x2 = min(start[0], end[0]), max(start[0], end[0])
                z1, z2 = min(start[1], end[1]), max(start[1], end[1])

                for x in range(x1, x2):
                    for z in range(z1, z2):
                        for pos in new_map:
                            if pos[0] == x and pos[2] == z: 
                                overlap.add((x, pos[1], z))

            path_map = [pos for pos in new_map if pos not in overlap]

            # Add Doors to New Map
            for door in House.doorCoordinates:
                path_map.append(door)
                path_map.append((door[0], door[1], door[2]-1))
                path_map.append((door[0], door[1], door[2]-2))
                path_map.append((door[0], door[1], door[2]-3))

            # Build Roads
            destinations = []
            for door in House.doorCoordinates:
                destinations.append(Node(door[0], door[1], door[2]))
            destinations.append(gate_locations[0])
            destinations.append(gate_locations[1])
            pb  = PathBuilder()
            mc.postToChat("Pathfinding...")
            try:
                paths = pb.buildPaths(destinations, path_map)
            except:
                print("Pathfinding Failed.")
            mc.postToChat("Paths Built.")

            # Build Decorations
            decorateArea(paths, set(path_map))

            # Flowers in Front of Houses
            by = Backyard()
            by.frontFlowers(site_dict)
                
            print("Build Complete.")
            mc.postToChat("Build Complete.")

mc.postToChat("Exiting Python script.")