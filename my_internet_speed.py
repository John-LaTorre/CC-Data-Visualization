import csv
from datetime import datetime
from matplotlib import pyplot as plt
from statistics import mean, median, mode, stdev


filename = 'SpeedTestExport_20200126.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, dates2, home_speed, other_speed, new_speed, old_speed = [], [], [], [], [], []
    new_internet = datetime.strptime('1/4/2020 11:57', "%m/%d/%Y %H:%M")
    for row in reader:
        if row[2] != '':
            if row[2] == 'SSID: Holly Hill':
                try:
                    current_date = datetime.strptime(row[0], "%m/%d/%Y %H:%M")
                    up_speed = float(int(row[5])/ 1000)
                except ValueError:
                    print(current_date, 'missing data')
                else:
                    dates.append(current_date)
                    home_speed.append(up_speed)
                    if current_date >= new_internet:
                        new_speed.append(up_speed)
                    else:
                        old_speed.append(up_speed)
            else:
                try:
                    current_date = datetime.strptime(row[0], "%m/%d/%Y %H:%M")
                    up_speed = float(int(row[5])/ 1000)
                    if up_speed > 80:
                        up_speed = 0
                except ValueError:
                    print(current_date, 'missing data')
                else:
                    dates2.append(current_date)
                    other_speed.append(up_speed)


plt.bar(dates, home_speed, align='center', alpha=0.5, color= 'b', label= 'Home WiFi')
plt.bar(dates2, other_speed, align='center', alpha=0.5, color= 'r', label = 'Other')

plt.legend()

plt.ylabel('Speed in Mbps')
plt.title('Internet speed over time')

median_home = median(home_speed)
average_home = mean(home_speed)
variance = stdev(home_speed)

new_median_home = median(new_speed)
new_average_home = mean(new_speed)
new_variance = stdev(new_speed)

old_median_home = median(old_speed)
old_average_home = mean(old_speed)
old_variance = stdev(old_speed)

results = open('speed_stats.txt', 'w') 
  
print("WiFi Home Median = " + str(median_home), file = results)
print("\nWiFi Home Average(Mean) = " + str(average_home), file = results)
print("\nWiFi Home Variance = " + str(variance), file = results)

print("\nNew WiFi Home Median = " + str(new_median_home), file = results)
print("\nNew WiFi Home Average(Mean) = " + str(new_average_home), file = results)
print("\nNew WiFi Home Variance = " + str(new_variance), file = results)

print("\nOld WiFi Home Median = " + str(old_median_home), file = results)
print("\nOld WiFi Home Average(Mean) = " + str(old_average_home), file = results)
print("\nOld WiFi Home Variance = " + str(old_variance), file = results)

results.close() 

plt.show()