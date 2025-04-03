import matplotlib.pyplot as plt
import numpy as np

def plot_time_series(df, electrodes):
    plt.figure(figsize=(12, 6))
    offset = 0
    
    for i, col in enumerate(electrodes):
        if col in df.columns:
            x = df[col].values.astype('float32')
            m = np.nanmean(x)
            if np.isnan(x).mean() < 1:
                x = np.nan_to_num(x, nan=m)
            else:
                x[:] = 0
            
            if i != 0:
                offset += x.max()
            plt.plot(df.index, x - offset, label=col)
            offset -= x.min()
    
    plt.xlabel('Time')
    plt.ylabel('Signal Value')
    plt.title('EEG Time Series Plot')
    plt.legend()
    plt.grid()
    plt.show()