import pandas as pd

# Prep data
temp_data = 'raw_data/ti/temperature.csv'


def calc_temp_avgs():
    min_voltage_mean = calc_avgs_from_csv(
        temp_data, "Supply voltage  (Min) (V)")
    max_voltage_mean = calc_avgs_from_csv(
        temp_data, "Supply voltage (Max) (V)")
    max_current_mean = calc_avgs_from_csv(
        temp_data, "Supply current(Max) (uA)")

    print(min_voltage_mean)
    print(max_voltage_mean)
    print(max_current_mean)


def calc_avgs_from_csv(data_file, col_name):
    data = pd.read_csv(data_file)
    raw_col = pd.to_numeric(
        data[col_name],
        errors='coerce'
    )
    return raw_col.mean()


def main():
    calc_temp_avgs()


main()
