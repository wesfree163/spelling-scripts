def TowerOfHanoi(n , from_rod, to_rod, aux_rod):

    if n == 0:
        return

    ### Recursive step, starting with max number of rings
    ### and decreases until no more rings
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)

    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)

    ### Recursive step, starting with max number of rings
    ### and decreases until no more rings
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

         
# Driver code

n = int(input("Enter tower size (rings)\n>"))

TowerOfHanoi(n, 'A', 'C', 'B') 
# A, C, B are the name of towers
