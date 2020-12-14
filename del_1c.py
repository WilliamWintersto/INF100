import csv

lats_s = []
lons_s = []
lats_f = []
lons_f = []

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            if str(row[20]) == 'SALTVANN':
                lat_s = float(row[-2]) # latitude is second last
                lon_s = float(row[-1]) # longitude is last
                lats_s.append(lat_s)
                lons_s.append(lon_s)
            
            elif str(row[20]) == 'FERSKVANN':
                lat_f = float(row[-2]) # latitude is second last
                lon_f = float(row[-1]) # longitude is last
                lats_f.append(lat_f)
                lons_f.append(lon_f)

        except ValueError:
            continue

try:
    import matplotlib.pyplot as plt
    plt.plot(lons_s,lats_s,'+r', label = 'Saltvann')
    plt.plot(lons_f,lats_f,'+b', label = 'Ferskvann')
    plt.legend()
    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats_s)} latitudes and {len(lons_s)} longitudes for salt water')
    print(f'We have {len(lats_f)} latitudes and {len(lons_f)} longitudes for fresh water')
