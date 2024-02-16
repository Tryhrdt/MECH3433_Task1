# Using recursive function to solve Hanoi Tower.
def HanoiTower(disk, source, destination, intermediate):
    if (source != destination) and (source != intermediate) and (destination != intermediate):
        if disk == 1:
            print("Move Disk 1 from source", source, "to destination", destination+'.')
            return
        HanoiTower(disk - 1, source, intermediate, destination)     # Move disk from source to intermediate to start the recursive sub-system
        print("Move Disk", disk, "from source", source, "to destination", destination+'.')
        HanoiTower(disk - 1, intermediate, destination, source)     # Move disk from intermediate to destination to complete the recursive sub-system


# Driver code
disk = int(input("Number of disk: "))
if disk > 0: HanoiTower(disk, 'A', 'C', 'B')    # A, B, C are the name of rods
print('Stopping the program...')

#Reference:
#https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/
#https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
