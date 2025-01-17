import numpy as np
import matplotlib.pyplot as plt

# Load a sample EEG data point (replace with your data loading logic)
eeg_data = np.random.rand(19, 500)  # Example: Replace with actual 19x500 matrix

# Plot individual channels
for i in range(19):
    plt.figure()
    plt.plot(eeg_data[i, :])
    plt.title(f'Channel {i+1}')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.show()

# Superimposed plot
plt.figure(figsize=(10, 6))
for i in range(19):
    plt.plot(eeg_data[i, :], label=f'Channel {i+1}')
plt.title('Superimposed EEG Channels')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.legend(loc='upper right', ncol=2, fontsize=8)
plt.show()

# Compute metrics
metrics = {}
for i in range(19):
    channel_data = eeg_data[i, :]
    metrics[f'Channel {i+1}'] = {
        'Mean': np.mean(channel_data),
        'Zero Crossing Rate': ((channel_data[:-1] * channel_data[1:]) < 0).sum(),
        'Range': np.max(channel_data) - np.min(channel_data),
        'Energy': np.sum(channel_data ** 2),
        'RMS': np.sqrt(np.mean(channel_data ** 2)),
        'Variance': np.var(channel_data),
    }

# Display metrics in a table
import pandas as pd
metrics_df = pd.DataFrame(metrics).T
print(metrics_df)
