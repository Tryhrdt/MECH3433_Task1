# Input:    Block number, Rods coordinates
# (can block coordinates merge with rod coordinates? need third coordinates?)
# Output:   Motion to move block

# Using recursive function to solve Hanoi Tower (By Wong Alex Yu Hin)
def HanoiTower(block, source, destination, intermediate):
    if (source != destination) and (source != intermediate) and (destination != intermediate):
        if block == 1:
            print("Move the robot from current position to", source)
            #move(current, source) #move from current place to source

            print("Grab Block 1 at", source)
            #grab(block1) #identify block1 and grab block1

            print("Move the robot from", source, 'to', destination)
            #move(source, destination) #move from source to destination

            print("Release Block 1 at", destination)
            #release(block1) #release block1 above other existing blocks
            return

        HanoiTower(block - 1, source, intermediate, destination)     # Move block from source to intermediate to start the recursive sub-system

        print("Move the robot from current position to", source)
        # move(current, source) #move from current place to source

        print("Grab Block", block, "at", source)
        # grab(block) #identify block1 and grab block1

        print("Move the robot from", source, 'to', destination)
        # move(source, destination) #move from source to destination

        print("Release Block", block, "at", destination)
        # release(block) #release block1 above other existing blocks

        HanoiTower(block - 1, intermediate, destination, source)     # Move block from intermediate to destination to complete the recursive sub-system

# Driver code   (by Wong Alex Yu Hin)
def sequence(block, source, destination, intermediate):
    if block > 0: HanoiTower(block, source, destination, intermediate)    # A, B, C are the name of rods
    return

#import block coordinates and map into block1,2,3
#block = [block1, block2, block3]
block = int(4)
source, destination, intermediate = ['A','a'], ['C','c'], ['B','b']   #A,B,C should be changed to rod coordinates
sequence(block, source, destination, intermediate)