import csv

def print_fylke(num):
    
    fylket = ''
    kommuner_i_fylket = []

    with open('NO_ADM12.csv', newline='', encoding='utf8') as csvfile:
        NO_ADM12_reader = csv.reader(csvfile, delimiter=';')

        for line in NO_ADM12_reader:
            print(line[7])
            if line[7] == num:
                kommuner_i_fylket.append(line[1])
    
    print(kommuner_i_fylket)

# Tom for tid            




fylker = []
kommuner = []

with open('NO_ADM12.csv', newline='', encoding='utf8') as csvfile:
    NO_ADM12_reader = csv.reader(csvfile, delimiter=';')
    
    for line in NO_ADM12_reader:

        if line[5] == 'ADM1':
            fylker.append([line[1], line[7], line[9]])

        elif line[5] == 'ADM2':
            kommuner.append([line[1], line[7], line[9]])


population_list = []

for element in kommuner:
    population_list.append(int(element[2]))

population_list.sort()

five_largest_population = population_list[:-6:-1]
five_smallest_population = population_list[:6]


five_largest_kommune = []

for population in five_largest_population:
    for element in kommuner:
        if int(element[2]) == int(population):
            five_largest_kommune.append(element[0])
            

five_smallest_kommune = []

for population in five_smallest_population:
    for element in kommuner:
        if int(element[2]) == int(population):
            five_smallest_kommune.append(element[0])
            
print(f'The 5 biggest kommuner (largest first) is: {five_largest_kommune[0]}, {five_largest_kommune[1]}, {five_largest_kommune[2]}, {five_largest_kommune[3]}, {five_largest_kommune[4]}')
print(f'The 5 smallest kommuner (smallest first) is: {five_smallest_kommune[0]}, {five_smallest_kommune[1]}, {five_smallest_kommune[2]}, {five_smallest_kommune[3]}, {five_smallest_kommune[4]}')
