# Uke 4 - oppgave 2

# ikke endre def-linjen
def poly_string(a, b, c):
    """
    Read coefficients of ax^2 + bx + c and return a string of the polynomial.
    We can assume that a,b,c can be any int
    """
    # Din kode her...
    
    output = ''
    list_abc = [a, b, c]
    counter = 0

    for number in list_abc:
        
        if counter == 0:
            if number < 0:
                if number == -1:
                    output += f'-x^2 '
                else:
                    output += f'-{number * -1}x^2 '
                
            elif number > 0:
                if number == 1:
                    output += f'x^2 '
                else:
                    output += f'{number}x^2 '


        elif counter == 1:

            if number < 0:

                if number == -1:
                    output += f'- x '
                
                else:
                    output += f'- {number * -1}x'

            elif number > 0:
                if number == 1:
                    output += f'+ x '
                else:
                    output += f'+ {number}x '


        elif counter == 2:

            if number < 0:
                output += f'- {number * -1}'

            elif number > 0:
                output += f'+ {number}' 
        
        else:
            print('ERROR')
        

        counter += 1
    
    if output == '':
        output = '0'
    
    return output

# ikke endre koden nedenfor

if __name__ == "__main__":
    a = int(input("Angi koeffisient foran x^2: "))
    b = int(input("Angi koeffisient foran x: "))
    c = int(input("Angi konstantterm: "))

    print(f"Ditt polynom er {poly_string(a, b, c)}.")
