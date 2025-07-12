import csv
from matplotlib import pyplot as plt

from datetime import datetime

filename = 'death_valley_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[4])
            low = int(row[5])

        except ValueError:
            print(f"Missing data for {row[2]}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
    # print(highs)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates,highs, c='red')
    plt.plot(dates, lows, c='blue')
    plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)
    plt.title("Daily High Temperatures, July 2021", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
