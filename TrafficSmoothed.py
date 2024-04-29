import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d


data = pd.read_csv("wr_timestamp.csv")
data['Timestamps'] = pd.to_datetime(data['Timestamps'])

# Define start and end timestamps (replace with your desired timestamps)
start_time = pd.Timestamp("2024-03-06 00:00:00")  # Adjust start time as needed
end_time = pd.Timestamp("2024-03-06 23:55:00")  # Adjust end time as needed
date = "2024-03-06"

# Filter data for the specified time range
data = data[(data['Timestamps'] >= start_time) & (data['Timestamps'] <= end_time)]

# Define features to plot (excluding timestamps and dominant protocol ports)
features = [
    "Bytes_Sent (TCP)", "Bytes_Sent (UDP)", "Bytes_Sent (Other)",
    "Bytes_Received (TCP)", "Bytes_Received (UDP)", "Bytes_Received (Other)",
    "Packets_Sent (TCP)", "Packets_Sent (UDP)", "Packets_Sent (Other)",
    "Packets_Received (TCP)", "Packets_Received (UDP)", "Packets_Received (Other)"
]

# Create a figure with a grid of subplots (adjust rows and columns as needed)
fig, axes = plt.subplots(3, 4, figsize=(15, 12))  # Adjust figure size

# Loop through each feature and plot on a separate subplot
row = 0
col = 0
for feature in features:

    # Filter data for the current feature within the time range
    filtered_data = data[['Timestamps', feature]]

    # Apply Gaussian smoothing (adjust sigma as needed)
    smoothed_data = gaussian_filter1d(filtered_data[feature], sigma=1)

    # Plot the smoothened data vs Timestamps on the current subplot
    axes[row, col].plot(filtered_data['Timestamps'], smoothed_data, label=feature)
    axes[row, col].set_xlabel('Time')
    axes[row, col].set_ylabel(feature)
    axes[row, col].set_title(f'{feature}')  # Shortened title for subplots
    axes[row, col].grid(True)
    axes[row, col].xaxis.set_visible(False)

    col += 1
    if col == 4:  # Move to the next row after 4 columns
        col = 0
        row += 1

# Tight layout to prevent overlapping elements
plt.tight_layout()

# Optional: Add a main title for the overall plot
plt.subplots_adjust(top=0.85)
fig.suptitle(f'Network Traffic Features (Smoothed) over Time (from {start_time} to {end_time}) with Time along X-axis', fontsize=12)

# Save the plot as a PNG file
plt.savefig(f"network_traffic_smoothed_{date}.png", bbox_inches='tight')

# Optional: Show the plot on screen
plt.show()