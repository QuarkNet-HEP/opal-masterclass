import csv
import os

base_dir = os.path.abspath('../')
data_dir = os.path.join(base_dir, 'app', 'static', 'data')

with open('./examples.csv', 'r') as csv_data:

    csv_reader = csv.reader(csv_data)
    next(csv_reader, None)

    for et, fn in csv_reader:

        try:
            assert(
                os.path.isfile(
                    os.path.join(data_dir, f'{fn}')
                )
            )
        except AssertionError:
            print(
                f'{fn} not found'
            )
