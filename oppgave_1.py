# Uke 4 - oppgave 1

# ikke endre def-linjen
def poly_string(a, b, c):
    """
    Read coefficients of ax^2 + bx + c and return a string of the polynomial.
    We can assume that a,b,c are 0 or positive int
    """
    # Din kode her...
    
    if a != 0 and b != 0 and c != 0:
        return f'{a}x^2 + {b}x + {c}'

    elif a != 0 and b != 0 and c == 0:
        return f'{a}x^2 + {b}x'

    elif a != 0 and b == 0 and c != 0:
        return f'{a}x^2 + {c}'

    elif a != 0 and b == 0 and c == 0:
        return f'{a}x^2'

    elif a == 0 and b != 0 and c != 0:
        return f'{b}x + {c}'

    elif a == 0 and b != 0 and c == 0:
        return f'{b}x'
    
    elif a == 0 and b == 0 and c != 0:
        return f'{c}'
    
    elif a == 0 and b == 0 and c == 0:
        return f'0'

    else:
        return 'ERROR'


# ikke endre koden nedenfor

if __name__ == "__main__":
    a = int(input("Angi koeffisient foran x^2: "))
    b = int(input("Angi koeffisient foran x: "))
    c = int(input("Angi konstantterm: "))

    print(f"Ditt polynom er {poly_string(a, b, c)}.")
