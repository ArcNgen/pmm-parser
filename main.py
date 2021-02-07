import os
import json
from datetime import date
from dateutil.relativedelta import relativedelta
from progress.bar import Bar

import parser

directory = r'./TXT_DATA'   # TXT files are saved to the TXT_DATA directory
pmm_data = dict()

three_months = date.today() + relativedelta(months=-3)
year = three_months.year
month = three_months.month

print('Report date: ' + str(month) + ' ' + str(year))
report_date = input('Enter date here if above is not correct: ') or str(
    month) + ' ' + str(year)

print()
bar = Bar('Reading files: ', max=56)
i = 0

for filename in os.listdir(directory):
    if filename.endswith('.TXT') or filename.endswith('.txt'):
        # print(filename)
        table_parser = parser.Parser(directory, filename, month, year)
        table_parser.parse_txt_data()

    bar.next()

print()
bar.finish()
print("Finished processing")
