import csv
import os.path as path

'''
Check that the files listed in the csv are
present in the data dir and check for duplicates.
A duplicate may be a mistake or it may mean two views
of the same event.

The csv files come from the original webpages for the
Z and W challenges.

'''

base_dir = path.abspath('../')
csv_dir = path.join(base_dir, 'app')
data_dir = path.join(base_dir, 'app', 'static', 'data')

checks_log = open('checks_log.txt', 'w')

def check_missing(file_name):

    checks_log.write(
        f'Checking for missing files in {path.basename(file_name)}\n'
    )
    
    with open(file_name, 'r') as csv_data:
        csv_reader = csv.reader(csv_data)
        next(csv_reader, None)
        for fn, i in csv_reader:
            try:
                assert(
                    path.isfile(
                        path.join(data_dir, f'{fn}')
                    )
                )
            except AssertionError:
                checks_log.write(
                    f'{fn},{i} not found\n'
                )


def check_duplicates(file_name):
    
    checks_log.write(
        f'Checking for duplicate ids in {path.basename(file_name)}\n'
    )
    
    ids = {}
    duplicates = []

    with open(file_name, 'r') as csv_data:
        csv_reader = csv.reader(csv_data)
        next(csv_reader, None)

        for fn, i in csv_reader:

            if i in ids:
                ids[i].append(fn)
                duplicates.append(i)
            else:
                ids[i] = [fn]

        if len(duplicates):

            dfs = [(i, ids[i]) for i in duplicates]

            for d in dfs:
                checks_log.write(
                    f'{d[0]}: {d[1]}\n'
                )
                
    
check_missing(path.join(csv_dir, 'Z-challenge.csv'))
check_missing(path.join(csv_dir, 'W-challenge.csv'))
               
check_duplicates(path.join(csv_dir, 'Z-challenge.csv'))
check_duplicates(path.join(csv_dir, 'W-challenge.csv'))

print(
    'Output written to checks_log.txt'
)
