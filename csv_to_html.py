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
    records = list(parse_csv_as_dictionary(path))
    record_headers = [record.keys() for record in records]
    csv_headers = list(dict.fromkeys([header for record in record_headers for header in record]))
    
    html_list = [
        '<table>', 
            *[
                '<tr>', 
                    *[f'<th>{escape(header)}</th>' for header in csv_headers], 
                '</tr>'
            ], 
            *[markup for row in [[
                '<tr>', 
                    *[f'<td>{escape(record.get(header, ""))}</td>' for header in csv_headers], 
                '</tr>'
            ] for record in records] for markup in row], 
        '</table>'
    ]
    
    html_string = ''.join(html_list)
    return html_string