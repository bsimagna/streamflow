import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('June-2021-Provo-River-Streamflow-Rates (1).csv',
                  delimiter=',',
                  skiprows=1,
                  dtype = str)

x = data[:, 0]

y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)

plt.plot(y_1, color = 'purple',
         label = '10163000')
plt.plot(y_2, color = 'blue',
         label = '10155200')
plt.plot(y_3, color = 'green',
         label = '10155500')
plt.plot(y_4, color = 'gold',
         label = '10154200')
plt.plot(y_5, color = 'orangered',
         label = '10155000')

tick_positions = np.arange(0, len(x), 384)
plt.xticks(tick_positions,
           [x[i][:10] for i in tick_positions],
           rotation = 45)
plt.ylim(0, 800)
plt.yticks(range(0, 801, 100))

plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')
plt.title('Provo River Streamflow Data (2021)')
plt.legend(loc = 'upper right')
plt.grid()

plt.show()