from scipy import signal
def butter_low(mixed_tone,fs,fc):
    w = fc / ( fs/ 2) 
    b, a = signal.butter(5, w, 'low')
    output = signal.filtfilt(b, a, mixed_tone)
    return output