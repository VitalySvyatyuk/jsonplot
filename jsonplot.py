import json
import os
from datetime import datetime

# Read a bunch of json files
json_directory = 'json_examples'
# received_dates = []
correlation_dates = []
ii_review_dates = []
serial_numbers = []

for json_file in os.listdir(json_directory):
    if json_file.endswith('.json'):
        json_file_path = os.path.join(os.getcwd(), json_directory, json_file)
        with open(json_file_path) as json_file_content:
            data = json.load(json_file_content)
            received_date = datetime.strptime(data[0]['ii']['received']['date'], '%m/%d/%Y').date()
            correlation_date = datetime.strptime(data[0]['ii']['correlation']['date'], '%m/%d/%Y').date() - received_date
            ii_review_date = datetime.strptime(data[0]['ii']['ii_review']['date'], '%m/%d/%Y').date() - received_date
            # received_dates.append(received_date)
            correlation_dates.append(correlation_date.days)
            ii_review_dates.append(ii_review_date.days)
            serial_numbers.append(data[0]['sn'])


# Plot the data

import matplotlib.pyplot as plt
# plt.bar(received_dates, serial_numbers, label='Received date')
plt.bar(serial_numbers, ii_review_dates, label='II review date')
plt.bar(serial_numbers, correlation_dates, label='Correlation date')
plt.ylabel('days')
plt.xlabel('serial numbers')
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()
