import csv

art_name = []
art_count = {}

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            art = str(row[12])
        except ValueError:
            continue
        art_name.append(art)
        art_count.setdefault(art,0)
        art_count[art] += 1

print(art_count)
