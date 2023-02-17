# import Towers_Han_Solver.py
import copy
import sys
from time import sleep

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()



TOTAL_DISKS = int(input('How many disks would you like for this game? \n> ')) # More disks means a more difficult puzzle.
OPT = False

# Start with all disks on tower A:
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))





def main(OPT):
##    runSolver()
    print("""The Tower of Hanoi, by Al Sweigart al@inventwithpython.com

Move the tower of disks, one disk at a time, to another tower. Larger
disks cannot rest on top of a smaller disk.

More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""
    )

    # Set up the towers. The end of the list is the top of the tower.
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}

    def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
        TOTAL_MOVES = 0
        sleep(0.3)
        if n == 0:
            return

        ### Recursive step, starting with max number of rings
        ### and decreases until no more rings
        TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
        sleep(0.3)

    ##    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)

        displayTowers(towers)
        TOTAL_MOVES += 1
        # Move the top disk from fromTower to toTower:
        disk = towers[from_rod].pop()
        towers[to_rod].append(disk)
        
        ### Recursive step, starting with max number of rings
        ### and decreases until no more rings
        TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
        

    if OPT:
        def solution():
            while True: # Run the total solution
                TowerOfHanoi(TOTAL_DISKS, 'A', 'C', 'B') 
                
                # Check if the user has solved the puzzle:
                if COMPLETE_TOWER in (towers['B'], towers['C']):
                    displayTowers(towers) # Display the towers one last time.
                    print(f'You have solved the puzzle! Well done!\nYou used the automatic solution.\nThe fastest solution is accomplished in {((2 ** TOTAL_DISKS) - 1)} moves.')
                    sys.exit()
        solution()
    else:
        def manual():
            TOTAL_MOVES = 0
            while True: # Run a single turn.
                # Display the towers and disks:
                displayTowers(towers)

                # Ask the user for a move:
                fromTower, toTower = askForPlayerMove(towers)

                # Move the top disk from fromTower to toTower:
                disk = towers[fromTower].pop()
                towers[toTower].append(disk)

                # Check if the user has solved the puzzle:
                if COMPLETE_TOWER in (towers['B'], towers['C']):
                    displayTowers(towers) # Display the towers one last time.
                    print(f'You have solved the puzzle! Well done!\nYou used {TOTAL_MOVES} moves.\nThe fastest solution is accomplished in {((2 ** TOTAL_DISKS) - 1)} moves')
                    sys.exit()
                TOTAL_MOVES += 1
        manual()

    


def askForPlayerMove(towers):
    """Asks the player for a move. Returns (fromTower, toTower)."""

    while True: # Keep asking player until they enter a valid move.
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print('(e.g. AB to moves a disk from tower A to tower B.)')
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Make sure the user entered valid tower letters
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of AB, AC, BA, BC, CA, or CB.')
            continue # Ask player again for their move.

        # Syntactic sugar - Use more descriptive variable names:
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # The "from" tower cannot be an empty tower:
            print('You selected a tower with no disks.')
            continue # Ask player again for their move.
        elif len(towers[toTower]) == 0:
            # Any disk can be moved onto an empty "to" tower:
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print('Can\'t put larger disks on top of smaller ones.')
            continue # Ask player again for their move.
        else:
            # This is a valid move, so return the selected towers:
            return fromTower, toTower


def displayTowers(towers):
    index = 0
    """Display the current state."""

    color = ['red', 'yellow', 'green', 'blue', 'cyan', 'purple']

    # Display the three towers:
    for level in range(TOTAL_DISKS, -1, -1):
        bext.fg(f'{color[index]}')
        index += 1
        if index == len(color):
            index = 0
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                displayDisk(0) # Display the bare pole with no disks
            else:
                displayDisk(tower[level]) # Display the disk.
        print()

    bext.fg('white')

    # Display the tower labels A, B, and C.
    emptySpace = ' ' * (TOTAL_DISKS)
    print('{0} A{0}{0} B{0}{0} C\n'.format(emptySpace))


def displayDisk(width):
    """Display a disk of the given width. A width of 0 means no disk."""
    emptySpace = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk:
        print(emptySpace + '||' + emptySpace, end='')
    else:
        # Display the disk:
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(emptySpace + disk + numLabel + disk + emptySpace, end='')


def runSolver():
    # Needs basic germX for this code
    getSolution = str(input('Do you want to run the automated solution to this level?\n> '))
    if(getSolution[0].lower().strip() == 'y'):
##        import Towers_Han_Solver.py
##        Towers_Han_Solver.TowerOfHanoi()
        OPT = True
    else:
        OPT = False
    return OPT

        


# If the progrom is run (instead of imported), run the game:
if __name__ == '__main__':
    main(runSolver())
