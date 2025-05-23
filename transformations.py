import numpy as np
import pywt

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

def normalization(mixed_tone,numpy_multiplier):
    normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * numpy_multiplier)
    return normalized_tone

def wavelet_transform(signal, numpy_multi):
    scales = np.arange(1, numpy_multi)
    coefficients, frequencies = pywt.cwt(signal, scales, 'cmor1.5-1.0')
    return coefficients, frequencies