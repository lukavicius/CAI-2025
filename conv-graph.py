import pandas as pd
import matplotlib.pyplot as plt

# File path to the CSV file
file_path = 'beliefs/trustBeliefLogAlice.csv'  # Replace with your file path

# Read the data from the file
data = pd.read_csv(file_path, delimiter=';')

# Detect the restart points where ticks decrease
restart_indices = data.index[data['ticks'].diff() < 0].tolist()

# Make the ticks continuous
continuous_ticks = data['ticks'].copy()
offset = 0
for i in range(1, len(data)):
    if data['ticks'].iloc[i] < data['ticks'].iloc[i - 1]:  # Detect restart
        offset += data['ticks'].iloc[:i].max()  # Add the max ticks before restart
    continuous_ticks.iloc[i] += offset

# Plotting
plt.figure(figsize=(10, 6))

# Plot each column against continuous ticks
for column in data.columns[2:]:  # Skip 'ticks' and 'name' columns
    plt.plot(continuous_ticks, data[column], label=column, marker='o', linestyle='-', markersize=4)

restart_label_added = False  # To ensure the label is added only once
for restart_index in restart_indices:
    restart_tick = continuous_ticks.iloc[restart_index]
    if not restart_label_added:
        plt.axvline(x=restart_tick, color='red', linestyle='--', label='Restart Game')
        restart_label_added = True
    else:
        plt.axvline(x=restart_tick, color='red', linestyle='--')

# Add labels, title, and legend
plt.xlabel('Ticks')
plt.ylabel('Values')
plt.legend()

# Save the plot as an image file
output_file = 'plot.png'  # Replace with your desired output file name
plt.savefig(output_file, dpi=300, bbox_inches='tight')

# Show the plot (optional)
plt.show()

print(f"Plot saved as {output_file}")