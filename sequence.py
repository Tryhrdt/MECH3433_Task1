# Input:    Block number, Rods coordinates (can block coordinates merge with rod coordinates? need third coordinates?)
# Output:   Motion to move block

Block_1, Block_2, Block_3 = ['1x','1y','1z'], ['2x','2y','2z'], ['3x','3y','3z']
#Block coordinates (import block coordinates and map into block1,2,3?)
block = [Block_1, Block_2, Block_3] #Block List to contain all block coordinates
num = int(3-1)
source, destination, intermediate = ['A','a'], ['C','c'], ['B','b']   #A,B,C should be changed to rod coordinates

# Operation function to contain all actions of moving the block from source to destination/ intermediate pos (By Wong Alex Yu Hin)
def operation(blockname, source, destination, intermediate):
    if (source != destination) and (source != intermediate) and (destination != intermediate):
        print("Move the robot from current position to", source)
        # move(current, source) #move from current place to source

        print("Grab", blockname, "at", source)
        # grab(block) #identify block and grab block

        print("Move the robot from", source, 'to', destination)
        # move(source, destination) #move from source to destination

        print("Release", blockname, "at", destination)
        # release(block) #release block on top (above other existing blocks)

        #print('.')
        return

# Using recursive function to solve Hanoi Tower (By Wong Alex Yu Hin)
def HanoiTower(num, source, destination, intermediate):
    if num == 0:
        operation(block[0], source, destination, intermediate)
        return
    HanoiTower(num - 1, source, intermediate, destination)     # Move block from source to intermediate to start the recursive sub-system
    operation(block[num], source, destination, intermediate)
    HanoiTower(num - 1, intermediate, destination, source)     # Move block from intermediate to destination to complete the recursive sub-system

# Driver code   (by Wong Alex Yu Hin)
HanoiTower(num, source, destination, intermediate)