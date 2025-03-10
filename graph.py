import pandas as pd
import matplotlib.pyplot as plt

# File paths
files = ["never-trust-log.csv", "always-trust-log.csv", "random-trust-log.csv"]
labels = ["Never-Trust", "Always-Trust", "Random-Trust"]
colors = ["blue", "red", "green"]

plt.figure(figsize=(10, 5))

# Read and plot each file
for file, label, color in zip(files, labels, colors):
    df = pd.read_csv(file, delimiter=";", skipinitialspace=True)  # Read CSV
    plt.plot(df["tick_nr"], df["completeness"], label=label, color=color)

# Graph Formatting
plt.xlabel("Tick Number")
plt.ylabel("Completeness")
plt.title("Completeness over Time")
plt.legend()
plt.grid(True)
# Save the plot as an image
plt.savefig("completeness_plot.png", dpi=300, bbox_inches='tight')
plt.show()