import os

class Parser:
    '''This class parses TXT data files for the PMM.'''

    def __init__(self, directory, file_name, month, year):
        self.directory = directory
        self.file_name = file_name
        self.month = month
        self.year = year
        self.table = dict()
        self.table_header = list()
        self.table_body = list()
        self.table_footer = list()
        self.map_data = list()
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.is_footnote = False

    def parse_txt_data(self):
        #with open(os.path.join(self.directory, self.file_name)) as txt_file:
            txt_number = self.file_name[-7:-4]
            txt_number = txt_number.strip('B')

            table_number = self.get_table_number(txt_number)
            if table_number:
                # print(' ' + table_number + ' ' + txt_number)
                self.parse_text_string()
            
    def parse_text_string(self):
        f = open('TXT_DATA/' + self.file_name, "r")
        print(self.file_name)
        print(f.read())
    
    def get_table_number(self, txt_number):
        table_number = None

        table_dictionary = {
            '00' : '0',
            '01' : '1',
            '53' : 'A1',
            '01E' : '1E',
            '02' : '2',
            '03' : '3',
            '04' : '4',
            '05' : '5',
            '06' : '6',
            '07' : '7',
            '08' : '8',
            '09' : '9',
            '12' : '10',
            '13' : '11',
            '19' : '16',
            '20' : '17',
            '21' : '18',
            '22' : '19',
            '23' : '20',
            '24' : '21',
            '25' : '22',
            '26' : '23',
            '27' : '24',
            '28' : '25',
            '29' : '26',
            '30' : '27',
            '35' : '31',
            '36' : '32',
            '37' : '33',
            '43' : '39',
            '44' : '40',
            '45' : '41',
            '46' : '42',
            '51' : '43',
            '47' : '44',
            '48' : '45',
            '49' : '46',
            '50' : '47',
        }

        if txt_number in table_dictionary:
            table_number = table_dictionary[txt_number]
        
        return table_number
