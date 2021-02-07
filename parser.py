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
        txt_data_file = open('TXT_DATA/' + self.file_name, 'r')

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

            group_number = self.get_group_number(table_number, source_key, product_code)


            print(table_number + ' - ' + group_number + ' ' + year + ' ' + month + ' ' + from1 + ' ' + product_code + ' ' + seller + ' ' + seller_type + ' ' + padd + ' ' + state + ' ' + data_type + ' ' + source_key + ' ' + suppression_code + ' ' + gen_code + ' ' + value)

        txt_data_file.close()
    
    def get_group_number(self, table_number, source_key, product_code):
        group_number = table_number

        if table_number == 39 or table_number == 40 or table_number == 45:
            product_code_dictionary = {
                '39': {
                    '163' : '39a',
                    '164' : '39a',

                    '165' : '39b',
                    '100' : '39b'
                },
                '40': {
                    '152' : '40a',
                    '150' : '40b',
                    '100' : '40c'
                },
                '45': {
                    '159' : '45a',
                    '153' : '45a',
                    '163' : '45a',
                    '160' : '45a',
                    '154' : '45a',
                    '164' : '45a',

                    '161' : '45b',
                    '155' : '45b',
                    '165' : '45b',
                    '152' : '45b',
                    '150' : '45b',
                    '100' : '45b'
                }
            }
            if table_number in product_code_dictionary and product_code in product_code_dictionary[table_number]:
                group_number = product_code_dictionary[table_number][product_code]
        
        else:

            group_number_dictionary = {
                'A1' : {
                    'R12000000003' : 'A1a',
                    'R13000000003' : 'A1a',
                    'R00000000003' : 'A1a',
                    'R01000000003' : 'A1a',
                    'R02000000003' : 'A1a',
                    'R00100000003' : 'A1a',
                    'R03000000003' : 'A1a',
                    'R04000000003' : 'A1a',
                    'R00200000003' : 'A1a',
                    'R05000000003' : 'A1b',
                    'R06000000003' : 'A1b',
                    'R00300000003' : 'A1b',
                    'R07000000003' : 'A1b',
                    'R08000000003' : 'A1b',
                    'R00400000003' : 'A1b',
                    'R09000000003' : 'A1b',
                    'R10000000003' : 'A1b',
                    'R00500000003' : 'A1b'
                },
                '6' : {
                    'A16331400002' : '6a',
                    'A16331000002' : '6a',
                    'A16332100002' : '6a',
                    'A16332200002' : '6a',
                    'A16332300002' : '6a',
                    'A16332000002' : '6a',
                    'A16431400002' : '6a',
                    'A16431000002' : '6a',
                    'A16432100002' : '6a',
                    'A16432200002' : '6a',
                    'A16432300002' : '6a',
                    'A16432000002' : '6a',
                    'A16531400002' : '6b',
                    'A16531000002' : '6b',
                    'A16532100002' : '6b',
                    'A16532200002' : '6b',
                    'A16532300002' : '6b',
                    'A16532000002' : '6b',
                    'A10031400002' : '6b',
                    'A10031000002' : '6b',
                    'A10032100002' : '6b',
                    'A10032200002' : '6b',
                    'A10032300002' : '6b',
                    'A10032000002' : '6b'
                },
                '7' : {
                    'A16331400007' : '7a',
                    'A16331000007' : '7a',
                    'A16332100007' : '7a',
                    'A16332200007' : '7a',
                    'A16332300007' : '7a',
                    'A16332000007' : '7a',
                    'A16431400007' : '7a',
                    'A16431000007' : '7a',
                    'A16432100007' : '7a',
                    'A16432200007' : '7a',
                    'A16432300007' : '7a',
                    'A16432000007' : '7a',
                    'A16531400007' : '7b',
                    'A16531000007' : '7b',
                    'A16532100007' : '7b',
                    'A16532200007' : '7b',
                    'A16532300007' : '7b',
                    'A16532000007' : '7b',
                    'A10031400007' : '7b',
                    'A10031000007' : '7b',
                    'A10032100007' : '7b',
                    'A10032200007' : '7b',
                    'A10032300007' : '7b',
                    'A10032000007' : '7b'
                },
                '8' : {
                    'A15931400002' : '8a',
                    'A15931000002' : '8a',
                    'A15932100002' : '8a',
                    'A15932200002' : '8a',
                    'A15932300002' : '8a',
                    'A15932000002' : '8a',
                    'A16031400002' : '8a',
                    'A16031000002' : '8a',
                    'A16032100002' : '8a',
                    'A16032200002' : '8a',
                    'A16032300002' : '8a',
                    'A16032000002' : '8a',
                    'A16131400002' : '8b',
                    'A16131000002' : '8b',
                    'A16132100002' : '8b',
                    'A16132200002' : '8b',
                    'A16132300002' : '8b',
                    'A16132000002' : '8b',
                    'A15231400002' : '8b',
                    'A15231000002' : '8b',
                    'A15232100002' : '8b',
                    'A15232200002' : '8b',
                    'A15232300002' : '8b',
                    'A15232000002' : '8b'
                },
                '9' : {
                    'A15931400007' : '9a',
                    'A15931000007' : '9a',
                    'A15932100007' : '9a',
                    'A15932200007' : '9a',
                    'A15932300007' : '9a',
                    'A15932000007' : '9a',
                    'A16031400007' : '9a',
                    'A16031000007' : '9a',
                    'A16032100007' : '9a',
                    'A16032200007' : '9a',
                    'A16032300007' : '9a',
                    'A16032000007' : '9a',
                    'A16131400007' : '9b',
                    'A16131000007' : '9b',
                    'A16132100007' : '9b',
                    'A16132200007' : '9b',
                    'A16132300007' : '9b',
                    'A16132000007' : '9b',
                    'A15231400007' : '9b',
                    'A15231000007' : '9b',
                    'A15232100007' : '9b',
                    'A15232200007' : '9b',
                    'A15232300007' : '9b',
                    'A15232000007' : '9b'
                },
                '10' : {
                    'A15331400002' : '10a',
                    'A15331000002' : '10a',
                    'A15332100002' : '10a',
                    'A15332200002' : '10a',
                    'A15332300002' : '10a',
                    'A15332000002' : '10a',
                    'A15431400002' : '10a',
                    'A15431000002' : '10a',
                    'A15432100002' : '10a',
                    'A15432200002' : '10a',
                    'A15432300002' : '10a',
                    'A15432000002' : '10a',

                    'A15531400002' : '10b',
                    'A15531000002' : '10b',
                    'A15532100002' : '10b',
                    'A15532200002' : '10b',
                    'A15532300002' : '10b',
                    'A15532000002' : '10b',
                    'A15031400002' : '10b',
                    'A15031000002' : '10b',
                    'A15032100002' : '10b',
                    'A15032200002' : '10b',
                    'A15032300002' : '10b',
                    'A15032000002' : '10b'
                },
                '11' : {
                    'A15331400007' : '11a',
                    'A15331000007' : '11a',
                    'A15332100007' : '11a',
                    'A15332200007' : '11a',
                    'A15332300007' : '11a',
                    'A15332000007' : '11a',
                    'A15431400007' : '11a',
                    'A15431000007' : '11a',
                    'A15432100007' : '11a',
                    'A15432200007' : '11a',
                    'A15432300007' : '11a',
                    'A15432000007' : '11a',

                    'A15531400007' : '11b',
                    'A15531000007' : '11b',
                    'A15532100007' : '11b',
                    'A15532200007' : '11b',
                    'A15532300007' : '11b',
                    'A15532000007' : '11b',
                    'A15031400007' : '11b',
                    'A15031000007' : '11b',
                    'A15032100007' : '11b',
                    'A15032200007' : '11b',
                    'A15032300007' : '11b',
                    'A15032000007' : '11b'
                },
                '18' : {
                    'F00000000003' : '18a',
                    'F00996000003' : '18a',
                    'F00100000003' : '18a',
                    'F00123600003' : '18a',
                    'F00124200003' : '18a',
                    'F00135400003' : '18a',
                    'F00200000003' : '18a',
                    'F00201700003' : '18a',
                    'F00201800003' : '18a',
                    'F00202000003' : '18a',
                    'F00202100003' : '18a',
                    'F00202600003' : '18a',
                    'F00203100003' : '18a',

                    'F00203800003' : '18b',
                    'F00203900003' : '18b',
                    'F00204000003' : '18b',
                    'F00204600003' : '18b',
                    'F00300000003' : '18b',
                    'F00300100003' : '18b',
                    'F00300500003' : '18b',
                    'F00302200003' : '18b',
                    'F00302800003' : '18b',
                    'F00303500003' : '18b',
                    'F00304800003' : '18b',
                    'F00307500003' : '18b',

                    'F00400000003' : '18c',
                    'F00400800003' : '18c',
                    'F00403000003' : '18c',
                    'F00404900003' : '18c',
                    'F00405600003' : '18c',
                    'F00500000003' : '18c',
                    'F00507100003' : '18c',
                    'F00506100003' : '18c',
                    'F00500600003' : '18c',
                    'F00507400003' : '18c'
                },
                '27' : {
                    'I11025000008' : '27a',
                    'I17628000008' : '27a',
                    'I19244000008' : '27a',
                    'I19263000008' : '27a',
                    'I19241000008' : '27a',

                    'I25050000008' : '27b',
                    'I25499000008' : '27b',
                    'I36100000008' : '27b',
                    'I40281000008' : '27b',
                    'I42150000008' : '27b',

                    'I42144000008' : '27c',
                    'I47499000008' : '27c',
                    'I47699000008' : '27c',
                    'I47799000008' : '27c',
                    'I61339000008' : '27c'
                }, 
            }
            if table_number in group_number_dictionary and source_key in group_number_dictionary[table_number]:
                group_number = group_number_dictionary[table_number][source_key]

        return group_number
    
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
