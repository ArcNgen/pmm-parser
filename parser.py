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
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.is_footnote = False

    def parse_txt_data(self):
            txt_number = self.file_name[-7:-4]
            txt_number = txt_number.strip('B')

            table_number = self.get_table_number(txt_number)
            if table_number:
                self.parse_text_string(table_number)
            
    def parse_text_string(self, table_number):
        txt_data_file = open('TXT_DATA/' + self.file_name, "r")

        for line in txt_data_file:
            
            year = line[0:4]
            month = line[4:6]
            
            from1 = line[6:7]
            product_code = line[7:10]
            seller = line[10:11]
            seller_type = line[11:13]
            padd = line[13:15]
            state = line[15:17]
            data_type = line[17:18]

            source_key = line[6:18]
            suppression_code = line[18:19]
            gen_code = line[19:20]
            value = line[20:30]
            value = value.lstrip('0')
            value = self.get_suppression_value(suppression_code, value)


            print(table_number + ' - ' + year + ' ' + month + ' ' + from1 + ' ' + product_code + ' ' + seller + ' ' + seller_type + ' ' + padd + ' ' + state + ' ' + data_type + ' ' + source_key + ' ' + suppression_code + ' ' + gen_code + ' ' + value)

        txt_data_file.close()
    
    def get_suppression_value(self, suppression_code, value):
        display_value = value

        suppression_dictionary = {
            '1' : 'W',
            '2' : 'NA',
            '3' : 'W',
            '6' : 'NA',
            '7' : 'R' + value,
            '8' : '-'
        }

        if suppression_code in suppression_dictionary:
            display_value = suppression_dictionary[suppression_code]

        return display_value

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
