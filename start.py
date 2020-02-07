import csv


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


with open('raw_data/digikey/ntc_temperature_1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')

    total = 0
    num_total = 0

    for row in spamreader:
        # digi key part number
        # print(row[2])

        # # price
        # print(row[8])

        # # power max
        # print(row[23])

        raw_power = row[23]
        if "mW" in raw_power and RepresentsInt(raw_power[:raw_power.index("mW")]):
            total += int(raw_power[:raw_power.index("mW")])
            num_total += 1

    print(total)
    print(num_total)
    avg = total / num_total
    print(avg)
