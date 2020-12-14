# du kan definere flere hjelpefunksjoner om du trenger dem


def print_prime_factors(N): # ikke endre den linjen
    print('Input:', N)
    
    ######## din kode her ####  
    for devider in range(2,N):
        
        while (N % devider) == 0:
            N /= devider    
            print(devider)

    # Etter me har skrive ut den siste faktoren har me 1 igjen og den skal ikkje printes
    if N != 1:
        print(N)
    ##########################
    
    
    
# ikke endre noe nedenfor
if __name__ == "__main__":
    print_prime_factors(10)
    print()
    
    print_prime_factors(27)
    print()
    
    print_prime_factors(28)
    print()
    
    print_prime_factors(53)
    print()
    
    print_prime_factors(14092020)
