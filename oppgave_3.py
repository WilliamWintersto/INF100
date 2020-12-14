# ikke endre def-linjen
def wavelength_to_color(w):
    """Convert a float wavelength in nm to a colour string"""
    # din kode her
    if 380 <= w <= 450:
        return 'fiolett'
    elif 450 <= w <= 485:
        return 'blå'
    elif 485 <= w <= 500:
        return 'cyan'
    elif 500 <= w <= 565:
        return 'grønn'
    elif 565 <= w <= 590:
        return 'gul'
    elif 590 <= w <= 625:
        return 'oransje'
    elif 625 <= w <= 740:
        return 'rød' # fiks returnverdien her

# ikke endre def-linjen
def frequency_to_color(f):
    """Convert a float frequency in THz to a colour string"""
    # din kode her
    if 680 <= f <= 790:
        return 'fiolett'
    elif 620 <= f <= 680:
        return 'blå'
    elif 600 <= f <= 620:
        return 'cyan'
    elif 530 <= f <= 600:
        return 'grønn'
    elif 510 <= f <= 530:
        return 'gul'
    elif 480 <= f <= 510:
        return 'oransje'
    elif 405 <= f <= 480:
        return 'rød' # fiks returnverdien her



# Fyll inn de to manglende linjene nedenfor, ikke endre resten

if __name__ == "__main__":
    unit = input("Hvilken enhet vil du bruke? Svare med 'nm' eller 'THz': ")

    if unit == "nm":
        value = float(input("Angi en verdi i nm: "))
        color = wavelength_to_color(value) # fiks denne linjen
        print(f"Lys med bølgelengden {value} nm har fargen {color}.")
    elif unit == "THz":
        value = float(input("Angi en verdi i THz: "))
        color = frequency_to_color(value) # fiks denne linjen
        print(f"Lys med frekvensen {value} THz har fargen {color}.")
