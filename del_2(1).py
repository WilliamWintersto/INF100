def find_item(garden,item):
    # din kode her
    for row in garden:
        if item in row:
            return (garden.index(row), row.index(item))

def swap_items(garden1,garden2,pos1,pos2):
    # din kode her
    a, b = pos1
    c, d = pos2
    garden1[a][b], garden2[c][d] = garden2[c][d], garden1[a][b]

def clean_garden(my_garden, neighbors_garden):
    """
    Bytt ut all "rock" med "strawberry", og "moss" med "raspberry" fra naboen sin hage
    så lenge det finnes muligheter for bytte.

        Args:
            my_garden - din hage
            neighbors_garden - naboen sin hage
    """
    # din kode her
    for row in my_garden:
        while 'rock' in row:
            try:
                rock_pos = find_item(my_garden, 'rock')
                strawberry_pos = find_item(neighbors_garden, 'strawberry')
                swap_items(my_garden, neighbors_garden, rock_pos, strawberry_pos)
            except:
                break
    
    for row in my_garden:
        while 'moss' in row:
            try:
                moss_pos = find_item(my_garden, 'moss')
                raspberry_pos = find_item(neighbors_garden, 'raspberry')
                swap_items(my_garden, neighbors_garden, moss_pos, raspberry_pos)
            except:
                break

if __name__ == "__main__":

    my_garden = [
        ["grass", "moss"],
        ["moss", "strawberry"],
        ["moss","rock"]
    ]

    other_garden = [
        ["grass", "raspberry"],
        ["grass", "strawberry"],
        ["strawberry","rock"]
    ]

    clean_garden(my_garden, other_garden)

    my_after = [
        ['grass', 'raspberry'],
        ['moss', 'strawberry'],
        ['moss', 'strawberry']
    ]

    other_after = [
        ['grass', 'moss'],
        ['grass', 'rock'],
        ['strawberry', 'rock']
    ]

    if my_after == my_garden and other_after == other_garden:
        print('OK!')
