import csv

# Prep data
ntc_temp_csvs = []
for x in range(1, 18):
    ntc_temp_csvs.append('raw_data/digikey/ntc_temperature_{}.csv'.format(x))

ptc_temp_csvs = []
for x in range(1, 6):
    ptc_temp_csvs.append('raw_data/digikey/ptc_temperature_{}.csv'.format(x))

sbc_cvss = []
for x in range(1, 5):
    sbc_cvss.append('raw_data/digikey/sbc_{}.csv'.format(x))


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def calc_ntc_avgs():
    avgs, total_sampled = calc_avgs_from_csvs(ntc_temp_csvs, 23)
    avg_of_avgs = sum(avgs) / len(avgs)
    return avg_of_avgs


def calc_ptc_avgs():
    avgs, total_sampled = calc_avgs_from_csvs(ptc_temp_csvs, 17)
    avg_of_avgs = sum(avgs) / len(avgs)
    return avg_of_avgs


def calc_sbc_avgs():
    avgs, total_sampled = calc_avgs_from_csvs(sbc_cvss, 17)
    print(total_sampled)
    print(len(avgs))
    avg_of_avgs = sum(avgs) / len(avgs)
    return avg_of_avgs


def calc_temp_avgs():
    avg_of_avgs = [calc_ntc_avgs(), calc_ptc_avgs()]
    return sum(avg_of_avgs) / len(avg_of_avgs)


def calc_avgs_from_csvs(data_list, power_index):
    avgs = []
    total_sampled = 0
    for data_file in data_list:
        with open(data_file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')

            total = 0
            num_total = 0

            for row in spamreader:
                raw_power = row[power_index]
                # print(raw_power)
                if "mW" in raw_power and RepresentsInt(raw_power[:raw_power.index("mW")]):
                    # print(raw_power)
                    total += int(raw_power[:raw_power.index("mW")]) / 1000
                    num_total += 1
                elif "W" in raw_power and RepresentsInt(raw_power[:raw_power.index("W")]):
                    print(raw_power)
                    total += int(raw_power[:raw_power.index("W")])
                    num_total += 1

            if num_total != 0:
                avg = total / num_total
                total_sampled += num_total

                avgs.append(avg)

    return avgs, total_sampled


def main():
    # avgs = calc_temp_avgs()
    avgs = calc_sbc_avgs()
    print(avgs)


main()
