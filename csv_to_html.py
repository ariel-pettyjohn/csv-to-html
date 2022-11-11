import csv
from html import escape

def parse_csv_as_dictionary(path):
    with open(path, newline='') as f:
        csv_reader = csv.reader(f)
        headings   = next(csv_reader)
        rows       = list(csv_reader)
        for row in rows:
            dictionary = {key: value for key, value in zip(headings, row)}
            yield dictionary

def parse_csv_as_html_string(path):
    dictionary_list = list(parse_csv_as_dictionary(path))
    headings = []

    for dictionary in dictionary_list:
        for key in dictionary.keys():
            if key not in headings:
                headings.append(key)
    
    html_strings = []
    
    html_strings.append('<table>')
    
    html_strings.append('<tr>')
    for heading in headings:
        html_strings.append('<th>{}</th>'.format(escape(heading)))
    html_strings.append('</tr>')
    
    for dictionary in dictionary_list:
        html_strings.append('<tr>')
        for heading in headings:
            value = dictionary.get(heading, '')
            html_strings.append('<td>{}</td>'.format(escape(value)))
        html_strings.append('</tr>')
    
    html_strings.append('</table>')
    
    html_string = ''.join(html_strings)
    return html_string