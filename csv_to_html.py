import csv
from html import escape

def record(headers, row):
     _record = {key: value for key, value in zip(headers, row)} 
     return _record

def parse_csv_as_records(path):
    with open(path, newline='') as f:
        csv_reader = csv.reader(f)

        try:
            headers = next(csv_reader)
        except:
            print('CSV file cannot be empty')

        csv_rows = list(csv_reader)
        try:
            if csv_rows[0]:
                return [record(headers, csv_row) for csv_row in csv_rows]
        except:
            print('CSV file must contain at least one row excluding headers')


def flatten(list):
    flattened_list = [element for sublist in list for element in sublist]
    return flattened_list


def body_cell(record, header):
    _body_cell = f'<td>{escape(record.get(header, ""))}</td>'
    return _body_cell


def body_cells(record, csv_headers):
    _body_cells = [body_cell(record, header) for header in csv_headers]
    return _body_cells


def row(cells):
    _row = ['<tr>', *cells, '</tr>']
    return _row


def parse_csv_as_html_string(path):
    records = parse_csv_as_records(path)    
    
    record_headers = [record.keys() for record in records]
    csv_headers = list(dict.fromkeys(flatten(record_headers)))
    
    header_row = row([f'<th>{escape(header)}</th>' for header in csv_headers])
    body_rows = [row(body_cells(record, csv_headers)) for record in records] 
    
    table = [
        '<table>',
            '<thead>', *header_row,         '</thead>',
            '<tbody>', *flatten(body_rows), '</tbody>',
        '</table>'
    ]

    html_string = ''.join(table)
    return html_string
