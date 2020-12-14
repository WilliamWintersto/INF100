def is_leap_year(year):
    """Determine if 'year' is a leap year according to Gregorian rules"""
    # din kode her
    if year % 4 == 0:
        
        if year % 100 == 0:
            
            if year % 400 == 0:
                return True
            
            else:
                return False
        
        else:
            return True
    
    else:
        return False # du må returnere en bool-verdi her

if __name__ == "__main__":
    year = int(input("Angi et årtall: "))

    if is_leap_year(year):
        print(f"År {year} er et skuddår.")
    else:
        print(f"År {year} er ikke et skuddår.")
