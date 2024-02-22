# Input:    Block number, Rods coordinates (can block coordinates merge with rod coordinates? need third coordinates?)
# Output:   Motion to move block

#import robomaster
#from robomaster import robot

height = [ 0, 1, 2, 3 ]
Block_1, Block_2, Block_3, Block_4 = ['1x','1y','1z'], ['2x','2y','2z'], ['3x','3y','3z'], ['4x','4y','4z']
# Block coordinates (import block coordinates and map into block1,2,3?)
block = [Block_1, Block_2, Block_3, Block_4] # Block List to contain all block coordinates
num = int(3-1) # The 1 is to change the index to base-0
source, destination, intermediate = ['Ax','Ay',height[3]], ['Cx','Cy',height[1]], ['Bx','By',height[1]]   # A,B,C should be changed to rod coordinates

# Operation function to contain all actions of moving the block from source to destination/ intermediate pos (By Wong Alex Yu Hin)
def operation(blockname, source, destination, intermediate):
    if (source != destination) and (source != intermediate) and (destination != intermediate):
        print("Move the robot from current position to", source)
        # move(current, source) #move from current place to source

        print("Grab", blockname, "at", source[0:1], "with height", source[2])
        # grab(block) #identify block and grab block

        print("Move the robot from", source, 'to', destination)
        # move(source, destination) #move from source to destination

        print("Release", blockname, "at", destination[0:1], "with height", destination[2])
        # release(block) #release block on top (above other existing blocks)

        #print('.')
        #source[2], destination[2] = height[], height[]
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