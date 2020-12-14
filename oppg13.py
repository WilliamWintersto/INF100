import random

def simulate(rounds):

    pre_board = [100000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    new_board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if rounds == 0:
        print(f'100   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0')
        return None

    for current_round in range(1,rounds+1):
                    
        tile_nr = 0
        for players_on_tile in pre_board:
            
            if players_on_tile == 0:
                tile_nr += 1
                continue
            
            for dice_throw in range(0,players_on_tile):            
                
                dice = random.randint(1,6)
                move_to = tile_nr + dice
                
                if (tile_nr + dice) > 15:
                    move_to -= 16
                
                if move_to == 3:
                    move_to = 8
                
                if move_to == 9:
                    move_to = 13
                
                if move_to == 10:
                    move_to = 2
                
                if move_to == 15:
                    move_to = 6
                
                new_board[move_to] += 1
            
            tile_nr += 1

        percent_board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   
        
        for idx in range(0,16):
            percent_board[idx] = round(new_board[idx]/1000)
        
        pre_board = new_board
        new_board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    print(f'{percent_board[0]} {percent_board[1]} {percent_board[2]} {percent_board[3]} {percent_board[4]} {percent_board[5]} {percent_board[6]} {percent_board[7]} {percent_board[8]} {percent_board[9]} {percent_board[10]} {percent_board[11]} {percent_board[12]} {percent_board[13]} {percent_board[14]} {percent_board[15]}')

simulate(20)
