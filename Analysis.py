"""
Exploring temperature trends for shiraz and global
"""
from pandas import read_csv
import matplotlib.pyplot as plt

def moving_average_calculator(data_frame, coloum_index, moving_count):
    """
    calculate moving average on a given data_frame and coloum_index by moving_count
    """
    averages = []
    for index in range(len(data_frame)):
        avg = sum(data_frame.iloc[index - moving_count: index, coloum_index])/moving_count
        averages.append(avg)
    return averages

DATA_FRAME = read_csv("shiraz_vs_global.csv")
MOVING_AVERAGE = 10

SHIRAZ_TEMP_AVG = moving_average_calculator(DATA_FRAME, 1, MOVING_AVERAGE)
GLOBAL_TEMP_AVG = moving_average_calculator(DATA_FRAME, 2, MOVING_AVERAGE)

plt.plot(DATA_FRAME['year'].iloc[MOVING_AVERAGE:], SHIRAZ_TEMP_AVG[MOVING_AVERAGE:], label='Shiraz')
plt.plot(DATA_FRAME['year'].iloc[MOVING_AVERAGE:], GLOBAL_TEMP_AVG[MOVING_AVERAGE:], label='Global')
plt.xlabel("Year")
plt.ylabel("Temperature (C°)")
plt.legend(loc=6)
plt.title("Temperature in Shiraz vs Global ({} year(s) moving average)".format(MOVING_AVERAGE))
plt.show()
