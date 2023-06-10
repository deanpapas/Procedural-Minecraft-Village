import random
from mcpi.minecraft import Minecraft
from mcpi import block


mc = Minecraft.create()

class Chunk:
    # This takes the block coordinates provided by the tcMap and 
    # calculates the 16 x 16 chunk coordinates that are already utilised by minecraft
    # As each chunk is made up of multiple blocks, each chunk has multiple block coordinates within the one chunk.
    def get_chunks(self, tcMap):
        
        # Chunks are added to a nested dictionary which has multiple keys for the chunk characteristics/info
        chunkDict = {}

        for coord_set in tcMap:
            # divide each coordinate within each set of the returned tcMap coordinates by 16 to get chunk coords            
            for t in range(len(coord_set)):
                cx = coord_set[0]
                cy = coord_set[1]
                cz = coord_set[2]
                cx //= 16
                cy //= 16
                cz //= 16
                chunk = (cx, cz)
            
            # as multiple block coords within one chunk, if chunk already exists in the dictionary, 
            # just add the block coordinates to that chunk
            if chunk in chunkDict:
                chunkDict[chunk]['CoordList'].append(list(coord_set))             

            # if the chunk isn't in the dictionary, calculate the start, 
            # end, neighbours, and add to the dictionary
            else:     
                start = Chunk.getChunkStart(cx, cz)
                end = Chunk.getChunkEnd(cx, cz)
                cn = Chunk.getNeighbours(cx, cy, cz)
                chunkDict[chunk] = {'Start': start, 'End': end, 'NeighbourChunks': cn, 'CoordList':[list(coord_set)]}
        
        # get the common heights for the chunk from the tuples in dictionary
        # get if there are less than 4 heights in chunk
        # get the common block for the chunk 
        for chunk in chunkDict:
            chunkHeights = []
            chunkCoords = chunkDict[chunk]['CoordList']
            for coords in chunkCoords:
                for h in coords:
                    ccHeights = coords[1]
                    chunkHeights.append(ccHeights)
            less3 = 'no'
            if len(set(chunkHeights)) <= 5:
                less3 = 'yes'
            mf = max(set(chunkHeights), key = chunkHeights.count)
            bt = Chunk.findBlockType(chunk, start, mf, end)
            chunkDict[chunk]['FewHeights'] = less3
            chunkDict[chunk]['FreqHeight'] = mf
            chunkDict[chunk]['ComBlockType'] = bt


        sixSites = Sites.possibleSites(chunkDict)
        site_dict = Sites.makeSites(chunkDict, sixSites)
        return site_dict
    
    
    
    # chunk start coordinates are at chunkx = 0, chunkz = 0
    def getChunkStart(cx, cz):
        x1 = cx * 16
        z1 = cz * 16
        start = (x1, z1)
        return start

    # chunk end coordinates are at chunkx = 15, chunkz = 15
    def getChunkEnd(cx, cz):
        x2 = (cx * 16) + 15
        z2 = (cz * 16) + 15
        end = (x2, z2)
        return end

    # neighbour chunks are +/- the x OR z coordinate of a chunk, not both
    def getNeighbours(cx, cy, cz):
        cneighbours = []
        cneighbours.append([cx+1, cy, cz])
        cneighbours.append([cx-1, cy, cz])
        cneighbours.append([cx, cy, cz+1])
        cneighbours.append([cx, cy, cz-1])
        return cneighbours

    # get the most common block type for the chunk
    def findBlockType(self, start, cy, end):
        x1 = 0
        z1 = 0
        for c in start:
            x1 = start[0]
            z1 = start[1]
        x2 = 0
        z2 = 0
        for c in end:
            x2 = end[0]
            z2 = end[1]
        bt = mc.getBlocks(x1, cy, z1, x2, cy, z2)
        bt = (list(bt))
            
        mb = max(set(bt), key = bt.count)
        # if the most common block type is air, change it to be grass.
        if mb == 0 or mb == 3 or mb == 1:
            mb = 2
        return mb



class Sites:

    # Take the chunks from the dictionary, and figure out the most appropriate sites based on heights and block type
    def possibleSites(chunkd):
        possSites = []
        # avoid the mostly water and lava chunks
        #exclblocks = [block.WATER, 8, block.WATER_FLOWING, 9, block.LAVA, 10, block.LAVA_FLOWING, 11]
        exclblocks = [8, 9, 10, 11]

        for key in chunkd.items():
            chunk = key[0]
            if chunkd[chunk]['FewHeights'] == 'yes' and chunkd[chunk]['ComBlockType'] not in exclblocks:
                possSites.append(chunk)

        # sort the sites to help with resizing the chunks for the houses
        ordered_ps = sorted(possSites)

        # remove next door neighbour chunks from the possible sites
        ops_set = Sites.removeNeighbourChunks(ordered_ps)
        
        # take all the sites and randomly select 6
        sixSites = Sites.createSiteList(ops_set)
        
        return sixSites

    
    def removeNeighbourChunks(ordered_ps):
        #remove chunks from list that are neighbours to avoid collision when building
            #enumerate ordered possible sites
        for i, (first, last) in enumerate(ordered_ps):
            #enumerate ordered possible sites in reverse
            for k, (f1, l1) in reversed(list(enumerate(ordered_ps))):
                #if the first elements are the same
                if first == f1:
                    #if last is the same, probably the same chunk, so continue through the list
                    if last == l1:
                        continue
                    #if last element is one above or below the last element in comparison chunk, remove it from the list as is a neighbour
                    if l1 == last+1 or l1 == last-1:
                        ordered_ps.pop(k)
                #if second elements are the same
                if last == l1:
                    #if first elements are different by one, remove as is a neighbour
                    if f1 == first+1 or f1 == first-1:
                        ordered_ps.pop(k)
                #if first elements are different by one
                if f1 == first+1:
                    #and last elements are different by one, remove as is diagonal neighbour, not direct neighbour
                    if l1 == last+1 or l1 == last-1:
                        ordered_ps.pop(k)
            # create a set of distinct site chunks from ordered_ps
        ops_set = set(ordered_ps)
            
        return ops_set



    def createSiteList(ops_set):
        ttlSites = len(ops_set)

        if ttlSites >= 6 and ttlSites <= 10:
            sixSites = sorted(random.sample(list(ops_set), ttlSites))
        elif ttlSites > 10:
            sixSites = sorted(random.sample(list(ops_set),(random.randint(6, 10))))
        else:
            sixSites = sorted(ops_set)
        return sixSites



    # This creates a nested dictionary of sites and their start/end coordinates. 
        # the sites have a house size of -2 from each start and end coordinate
        # Each site coordinates will vary based on their position in the site list
        # and each site can only expand in certain directions pased on potential locations in possible build area
        # each site expansion will change with positive or negative integers between 2-8.
        # starting at 2 as some change is necessary, and ending at 8 as is half of 16 
        # and if each site is only expanded half a chunk in any direction (within area bounds) 
        # this, along with having neighbouring chunks removed from the possible sites list,
        # should (hopefully) prevent other sites from intersecting one another.
    def makeSites(chunkd, sixSites):
        
        site_dict = {}

        for i in range(len(sixSites)):
            site = sixSites[i]

            # the first site in the sorted list
                # worst case scenario it is in the lowest corner of area,
                # therefore should only increase the size of chunk site in positive direction of end coordinates
            if i == 0:
                sx = (chunkd[site]['Start'][0])
                sz = (chunkd[site]['Start'][1])
                ex = (chunkd[site]['End'][0]+(random.randint(2, 8)))
                ez = (chunkd[site]['End'][1]+(random.randint(2, 8)))
            
            
            # the second site in the sorted list
                # Worst case scenario it is on the lowest edge of area,
                # Therefore can increase the size of chunk site by extending start z in negative direction,
                # and in positive direction of end coordinates
            elif i == 1:
                sx = (chunkd[site]['Start'][0])
                sz = (chunkd[site]['Start'][1]-(random.randint(2, 8)))
                ex = (chunkd[site]['End'][0]+(random.randint(2, 8)))
                ez = (chunkd[site]['End'][1]+(random.randint(2, 8)))


            # the last site of the sorted list, 
                # Worst case scenario is in the highest corner of area. 
                # Therefore should only increase the site size by decreasing the starting x and z coordinates, 
                # leaving end coords the same so as to avoid expanding beyond build area
            elif (i == len(sixSites)-1):
                sx = (chunkd[site]['Start'][0]-(random.randint(2, 8)))
                sz = (chunkd[site]['Start'][1]-(random.randint(2, 8)))
                ex = (chunkd[site]['End'][0])
                ez = (chunkd[site]['End'][1])


            # the second last site of the sorted list, 
                # worst case scenario is along the highest limit of area. 
                # Therefore should only increase the site size by decreasing the starting x and ending z coordinates, 
                # leaving start z and end x coords the same so as to avoid expanding beyond build area
            elif (i == len(sixSites)-2):
                sx = (chunkd[site]['Start'][0]-(random.randint(2, 8)))
                sz = (chunkd[site]['Start'][1])
                ex = (chunkd[site]['End'][0])
                ez = (chunkd[site]['End'][1]+(random.randint(2, 8)))

        
            # the middle site/s of the sorted list, 
                # worst case scenario is along the edges of the build area. 
                # Therefore should increase the site size in all directions - 
                # we have cleared a build area 15 blocks beyond build limits, so if site is along edge, it will still be within the cleared area.
            else:
                sx = (chunkd[site]['Start'][0]-(random.randint(2, 8)))
                sz = (chunkd[site]['Start'][1]-(random.randint(2, 8)))
                ex = (chunkd[site]['End'][0]+(random.randint(2, 8)))
                ez = (chunkd[site]['End'][1]+(random.randint(2, 8)))
                

            y = Sites.getSiteHeights(chunkd[site]['Start'], chunkd[site]['End'])
            fbl = (chunkd[site]['ComBlockType'])

            
            # These next conditions check the size of each site plot and reduce the house size based on this
            # if the whole site is enormous, reduce the house size dramatically (mostly from the back)
            if ((ex - sx) >= 22) and ((ez - sz) >= 22):
                site_dict[i+1] = {'site_start': (sx, sz), 'site_end': (ex, ez), 'house_start': ((sx+2), y, (sz+2)), 
                              'house_end': ((ex-(random.randint(6, 9))), y, (ez-(random.randint(6, 9)))), 'block_type': fbl}
            
            # if the width is much larger, reduce along the width
            elif ((ez - sz) >= 24):
                site_dict[i+1] = {'site_start': (sx, sz), 'site_end': (ex, ez), 'house_start': ((sx+(random.randint(5, 8))), y, (sz+2)), 
                              'house_end': ((ex-(random.randint(2, 5))), y, (ez-(random.randint(5, 8)))), 'block_type': fbl}

            # if the length is much larger, reduce long the length
            elif ((ex - sx) >= 24):
                site_dict[i+1] = {'site_start': (sx, sz), 'site_end': (ex, ez), 'house_start': ((sx+(random.randint(5, 9))), y, (sz+2)), 
                              'house_end': ((ex-(random.randint(4, 8))), y, (ez-(random.randint(2, 5)))), 'block_type': fbl}
            
            # if not dramatically large, randomly reduce house
            else:
                site_dict[i+1] = {'site_start': (sx, sz), 'site_end': (ex, ez), 'house_start': ((sx+(random.randint(2, 5))), y, (sz+2)), 
                                'house_end': ((ex-(random.randint(2, 5))), y, (ez-(random.randint(2, 5)))), 'block_type': fbl}        
        
        return site_dict
        


    def getSiteHeights(start, end):
        siteHeights = mc.getHeights(start, end)
        sh = max(set(siteHeights), key = siteHeights.count)
        return sh
        
        

    def levelSites(site_dict):
        for key in site_dict:
            sx = site_dict[key]['site_start'][0]
            sz = site_dict[key]['site_start'][1]
            ex = site_dict[key]['site_end'][0]
            ez = site_dict[key]['site_end'][1]
            sy = site_dict[key]['house_start'][1]
            site_block = site_dict[key]['block_type']

            mc.setBlocks(sx-1, sy+1, sz-1, ex+1, sy+20, ez+1, block.AIR)

            #blend the site in - ground steps down
            mc.setBlocks(sx-1, sy-1, sz-2, ex+1, sy-1, ez+2, site_block)
            mc.setBlocks(sx-3, sy-2, sz-2, ex+3, sy-2, ez+3, site_block)
            mc.setBlocks(sx-4, sy-3, sz-3, ex+4, sy-5, ez+4, site_block)

            #one corner
            mc.setBlocks(sx+6, sy, sz-2, sx-1, sy, sz-2, site_block)
            mc.setBlocks(sx+5, sy-1, sz-3, sx-1, sy-1, sz-3, site_block)
            mc.setBlocks(sx+6, sy-2, sz-4, sx-1, sy-1, sz-4, site_block)

            #shaping the back
            mc.setBlocks(ex-5, sy, ez+1, ex-10, sy, ez+2, site_block)
            mc.setBlocks(ex-4, sy-1, ez+1, ex-6, sy-1, ez+3, site_block)

            # air steps up in layers around site
            mc.setBlocks(sx-2, sy+1, sz-2, ex+3, sy+15, ez+3, block.AIR)
            mc.setBlocks(sx-4, sy+2, sz-4, ex+4, sy+15, ez+4, block.AIR)
            mc.setBlocks(sx-5, sy+3, sz-6, ex+6, sy+15, ez+6, block.AIR)
            mc.setBlocks(sx-7, sy+4, sz-7, ex+8, sy+15, ez+7, block.AIR)
            mc.setBlocks(sx-8, sy+5, sz-9, ex+9, sy+15, ez+8, block.AIR)

            mc.setBlocks(ex-3, sy, ez-2, ex-1, sy+1, ez-3, block.AIR)
            mc.setBlocks(ex-4, sy+1, ez-3, ex-1, sy+3, ez-4, block.AIR)
            mc.setBlocks(ex-4, sy+1, ez+1, ex-6, sy+1, ez+3, block.AIR)

            # actual site block
            mc.setBlocks(sx, sy, sz, ex, sy-2, ez, site_block)

        return None

