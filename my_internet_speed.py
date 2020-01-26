import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'SpeedTestExport_20200126.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, speed = [], []
    for row in reader:
        if row[2] == 'SSID: Holly Hill':
            try:
                current_date = datetime.strptime(row[0], "%m/%d/%Y %H:%M")
                up_speed = float(int(row[5])/ 1000)
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                speed.append(up_speed)


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.bar(dates, speed, align='center', alpha= 0.5, color='b')

plt.ylabel('Speed in Mbps')
plt.title('Internet speed over time')

plt.show()