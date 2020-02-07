import csv
from functools import reduce

ntc_temp_csvs = [
    'raw_data/digikey/ntc_temperature_1.csv',
    'raw_data/digikey/ntc_temperature_2.csv',
]


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def calc_ntc_avgs():
    avgs = calc_avgs_from_csvs(ntc_temp_csvs, 23)
    avg_of_avgs = sum(avgs) / len(avgs)
    return avg_of_avgs


def calc_temp_avgs():
    avgs = calc_ntc_avgs()
    return avgs


def calc_avgs_from_csvs(data_list, power_index):
    avgs = []
    for data_file in data_list:
        with open(data_file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')

            total = 0
            num_total = 0

            for row in spamreader:
                raw_power = row[power_index]
                if "mW" in raw_power and RepresentsInt(raw_power[:raw_power.index("mW")]):
                    total += int(raw_power[:raw_power.index("mW")])
                    num_total += 1

            avg = total / num_total

            avgs.append(avg)
    return avgs


def main():
    avgs = calc_temp_avgs()
    print(avgs)


main()
