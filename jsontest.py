#! jsontest.py trying examples in ch3 of data viz with python and js
# section 'Passing Data Around'

import json
import csv

nobel_winners = [
{'category': 'Physics',
 'name': 'Albert Einstein',
 'nationality': 'Swiss',
 'sex': 'male',
 'year': 1921},
{'category': 'Physics',
 'name': 'Paul Dirac',
 'nationality': 'British',
 'sex': 'male',
 'year': 1933},
{'category': 'Chemistry',
 'name': 'Marie Curie',
 'nationality': 'Polish',
 'sex': 'female',
 'year': 1911}
]

col_keys = nobel_winners[0].keys()
cols = sorted(col_keys)

with open('data/nobelwinners.csv', 'w') as f:
    ''' turn nobel_winners into a csv file with column labels '''
    f.write(','.join(cols) + '\n')

    for o in nobel_winners:
        row = [str(o[col]) for col in cols]
        f.write(','.join(row) + '\n')

print('Output, using readlines to read csv file created from list of dictionaries:')
with open('data/nobelwinners.csv') as f:
    for line in f.readlines():
        print(line, end = "")

print('\n')

with open('data/nobel_winners_csv.csv', 'w', newline = '') as f:
    '''use csv.DictWriter to create csv from dictinary '''
    fn_keys = nobel_winners[0].keys()
    fieldnames = sorted(fn_keys)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for w in nobel_winners:
        writer.writerow(w)


print('Output, using csv reader to output data, instead of readlines (csv created with csv.DictWriter):')
with open('data/nobel_winners_csv.csv') as f:
    ''' use csv to output new csv file, instead of readlines '''
    reader = csv.reader(f)
    for row in reader:
        print(row)

print('\n')

with open('data/nobel_winners_csv.csv') as f:
    ''' use csv.DictReader() to read in csv file '''
    reader = csv.DictReader(f)
    nw_DictReader = list(reader)

for w in nw_DictReader:
    w['year'] = int(w['year'])

print('Output, read csv with csv.DictReader (creates ordered dictionary):\n', nw_DictReader)

with open('data/nobel_winners.json', 'w') as f:
    json.dump(nw_DictReader, f)
print('\n')

with open('data/nobel_winners.json') as f:
    nw_json = json.load(f)

print('Output converted to JSON:\n', nw_json)



