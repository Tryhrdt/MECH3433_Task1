# Sequencing Codes  (By Wong Alex Yu Hin)
# Input:    Number of blocks, Rods/Block coordinates
# Output:   Motion to move blocks between 'rods'

height = [ 0, 1, 2, 3 ]  # Should be modified to actual height of stacked blocks, the '0' is to mitigate base-0 counting
block = ['Block_1', 'Block_2', 'Block_3'] # Block List to contain all blocks (name)
num = int(3) # Total number of blocks
source, destination, intermediate = ['0°', height[3]], ['180°',height[1]], ['90°',height[1]]   # Cyclindrical coordinates of three 'rods'

# Operation function to contain all actions of moving the block from source to destination/intermediate 'rod' (By Wong Alex Yu Hin)
def operation(blockname, source, destination, intermediate):
    if (source != destination) and (source != intermediate) and (destination != intermediate):
        #print("Move the robot from current position to", source)
        moveto(source) #move the robot to source position

        #print("Grab", blockname, "at", source[0], "with height", source[1])
        grab(block) #identify and grab the top block in block stack at source 'rod'

        #print("Move the robot from", source, 'to', destination)
        moveto(destination) #move the robot with grabbed block from source to destination

        #print("Release", blockname, "at", destination[0], "with height", destination[1])
        release(block) #release block on top of block stack at destination 'rod'

        return

# Using recursive function to solve Hanoi Tower with divide and conquer strategy (By Wong Alex Yu Hin)
def HanoiTower(num, source, destination, intermediate):
    if num == 1:
        operation(block[0], source, destination, intermediate)
        return
    HanoiTower(num - 1, source, intermediate, destination)     # Move block from source to intermediate to start the recursive sub-system
    operation(block[num - 1], source, destination, intermediate)
    HanoiTower(num - 1, intermediate, destination, source)     # Move block from intermediate to destination to complete the recursive sub-system

# Driver code   (by Wong Alex Yu Hin)
HanoiTower(num, source, destination, intermediate)
