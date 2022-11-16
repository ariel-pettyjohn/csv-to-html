import csv
from html import escape

def parse_csv_as_dictionary(path):
    with open(path, newline='') as f:
        csv_reader = csv.reader(f)

        try:
            headers = next(csv_reader)
        except: 
            print('CSV file cannot be empty')
        
        rows = list(csv_reader)
        try:
            if rows[0]:
                for row in rows:
                    yield {key: value for key, value in zip(headers, row)}
        except:
            print('CSV file must contain at least one row excluding headers')

def parse_csv_as_html_string(path):
    dictionary_list = list(parse_csv_as_dictionary(path))
    headers = []
   
    for dictionary in dictionary_list:
        for key in dictionary.keys():
            if key not in headers:
                headers.append(key)

    return ''.join([
        '<table>', 
            *[
                '<tr>', 
                    *[f'<th>{escape(header)}</th>' for header in headers], 
                '</tr>'
            ], 
            *[markup for row in [[
                '<tr>', 
                    *[f'<td>{escape(dictionary.get(header, ""))}</td>' for header in headers], 
                '</tr>'
            ] for dictionary in dictionary_list] for markup in row], 
        '</table>'
    ])