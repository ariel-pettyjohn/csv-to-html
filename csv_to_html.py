import csv

def read_csv(path):
    with open(path, newline='') as f:
        csv_reader = csv.reader(f)
        headings   = next(csv_reader)
        rows       = list(csv_reader)
        for row in rows:
            dictionary = {key: value for key, value in zip(headings, row)}
            yield dictionary