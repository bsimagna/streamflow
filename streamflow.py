import numpy as np
import matplotlib.pyplot as plt


def load_streamflow(filename):
    data = np.loadtxt(
        filename,
        delimiter=",",
        skiprows=1,
        dtype=str)

    dates = data[:, 0]
    flows = data[:, 1:6].astype(float)

    return dates, flows


def plot_streamflow(dates, flows, sites):
    colors = ["purple", "blue", "green", "gold", "orangered"]
    for i in range(len(sites)):
        plt.plot(flows[:, i],
                 color=colors[i],
                 label=sites[i])
    tick_positions = np.arange(0, len(dates), 384)
    plt.xticks(
        tick_positions,
        [dates[i][:10] for i in tick_positions],
        rotation=45)
    plt.ylim(0, 800)
    plt.yticks(range(0, 801, 100))
    plt.xlabel("Date")
    plt.ylabel("Flowrate (cfs)")
    plt.title("Provo River Streamflow Data (2021)")
    plt.legend(loc="upper right")
    plt.grid()
    plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates (1).csv"
)

plot_streamflow(dates, flows, sites)