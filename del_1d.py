import csv

lats_mat = []
lons_mat = []
lats_sette = []
lons_sette = []

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:

            if str(row[11]) == 'MATFISK':
                lat = float(row[-2]) # latitude is second last
                lon = float(row[-1]) # longitude is last
                lats_mat.append(lat)
                lons_mat.append(lon)

            elif str(row[11]) == 'SETTEFISK':
                lat = float(row[-2]) # latitude is second last
                lon = float(row[-1]) # longitude is last
                lats_sette.append(lat)
                lons_sette.append(lon)
        
        except ValueError:
            continue

try:
    import matplotlib.pyplot as plt
    plt.plot(lons_mat,lats_mat,'+', label = 'Matfisk')
    plt.plot(lons_sette,lats_sette,'+', label = 'Settefisk')
    plt.legend()
    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats_mat)} latitudes and {len(lons_mat)} longitudes for matfisk')
    print(f'We have {len(lats_sette)} latitudes and {len(lons_sette)} longitudes for settefisk')


# Koden viser ein oversikt over dei to vanligste produksjonsformene: Matfisk og Settefisk 
