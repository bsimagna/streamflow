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

# AI helped me with opening and writing to a CSV file, as well as formatting the output for the summary table.
def summarize(dates, flows, sites):
    print(f"{'Gauge':<10}{'Max (cfs)':>12}{'Date of max':>22}{'Min (cfs)':>12}{'Avg (cfs)':>12}")

    outfile = open("streamflow_summary.csv", "w")
    outfile.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

    for i in range(len(sites)):
        max_flow = np.max(flows[:, i])
        min_flow = np.min(flows[:, i])
        avg_flow = np.mean(flows[:, i])

        max_index = np.argmax(flows[:, i])
        max_date = dates[max_index]

        print(
            f"{sites[i]:<10}"
            f"{max_flow:>12.1f}"
            f"{max_date:>22}"
            f"{min_flow:>12.1f}"
            f"{avg_flow:>12.1f}")

        outfile.write(
            f"{sites[i]},{max_flow:.1f},{max_date},{min_flow:.1f},{avg_flow:.1f}\n")

    outfile.close()

# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates (1).csv")

summarize(dates, flows, sites)

plot_streamflow(dates, flows, sites)

threshold = float(input("Enter a flowrate threshold (cfs): "))
print(f"\nHours above {threshold} cfs: ")

for i in range(len(sites)):
    readings_above = np.sum(flows[:, i] > threshold)
    hours_above = readings_above * 0.25
    print(f"{sites[i]}: {hours_above:.2f} hours")