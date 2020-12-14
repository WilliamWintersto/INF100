# du kan definere flere hjelpefunksjoner om du trenger dem


def print_diamond(N): # ikke endre den linjen
    print('Tall:', N)
    
    ######## din kode her ####
   
    # Bredden til diamanten
    bredde = 2*N - 1

    # Printer ut til og med halvveis
    for num_of_X_opp in range(1,bredde,2):
        mellomrom_halvdel = int((bredde - num_of_X_opp) / 2)
        print(' ' * mellomrom_halvdel  +  'X' * num_of_X_opp  +  ' ' * mellomrom_halvdel)
    
    # Printer ut resten bortsett fra den aller siste X-en
    for num_of_X_ned in range(bredde,1,-2):
        mellomrom_halvdel = int((bredde - num_of_X_ned) / 2)
        print(' ' * mellomrom_halvdel  +  'X' * num_of_X_ned  +  ' ' * mellomrom_halvdel)

    # Printer ut den siste X-en så lenge N ikkje er 0
    if N != 0:
        mellomrom_halvdel = int((bredde - 1) / 2)
        print(' ' * mellomrom_halvdel  +  'X'  +  ' ' * mellomrom_halvdel)
    ##########################
    
    
    
# ikke endre noe nedenfor
if __name__ == "__main__":
    print_diamond(1)
    print()
    
    print_diamond(2)
    print()
    
    print_diamond(3)
    print()
    
    print_diamond(4)
    print()
    
    print_diamond(10)
