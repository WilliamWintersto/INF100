# du kan definere flere hjelpefunksjoner om du trenger dem


def pytag_trippel(sum_abc): # ikke endre den linjen
    ######## din kode her ####

    def pytag_check(a, b, c):
        return (a**2) + (b**2) == (c**2)

    # Sjekker alle verdier for a
    for a in range(1, sum_abc):
        
        # Sjekker alle verdier for b
        for b in range(a+1, sum_abc):
            c = sum_abc - (a + b)
            
            # Viss programmet finner ein pytagoreisk trippel
            if pytag_check(a, b, c):
                
                # Viss det er riktig pytagoreisk trippel
                if a + b + c == sum_abc:
                    break
        
        # Viss programmet finner ein pytagoreisk trippel
        if pytag_check(a, b, c):
            
            # Viss det er riktig pytagoreisk trippel
            if a + b + c == sum_abc:
                break

    return a*b*c
    



# ikke endre noe nedenfor
if __name__ == "__main__":
    solution = pytag_trippel(1000)
    print(solution)
    if solution == 31875000:
        print("That's right!")
