import unittest
import csv_to_html

class TestCSVToHTML(unittest.TestCase):
    def test_read_csv(self):
        dictionary_list1 = list(csv_to_html.read_csv('test.csv'))
        
        self.assertEqual(dictionary_list1[0], {
            '1' : '1',
            '2' : 'Eldon Base for stackable storage shelf, platinum',
            '3' : 'Muhammed MacIntyre',
            '4' : '3',
            '5' : '-213.25',
            '6' : '38.94',
            '7' : '35',
            '8' : 'Nunavut',
            '9' : 'Storage & Organization',
            '10': '0.8'
        })