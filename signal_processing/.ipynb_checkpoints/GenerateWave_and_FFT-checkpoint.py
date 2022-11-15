import numpy as np
from matplotlib import pyplot as plt
import scipy as sp

#create time signal

SAMPLE_RATE = 44100 #Hz
DURATION = 5 #seconds

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate *duration, endpoint=False)
    frequencies = x * freq
    #2pi because np.sin takes radians
    y = np.sin((2*np.pi)*frequencies)
    return x,y

#generate a 2 Hertz sine wave tha t lastd 5 seconds
x,y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
plt.plot(x,y)
plt.show()

#mix a signal / a tone
_, nice_tone = generate_sine_wave(200, SAMPLE_RATE, DURATION) #use underscore to discard the x-values returned by generate_sine_Wave()

_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3

mixed_tone = nice_tone + noise_tone

normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767) #this creates a 16bit signal, +-32767 is the range of 16bit
plt.plot(normalized_tone[:1000]) #only plot first 1000 samples
plt.show()

#create a WAV-File
from scipy.io.wavfile import write

#Remember SAMPLE_RATE = 44100 Hz is our playback rate
write("mysinewave.wav", SAMPLE_RATE, normalized_tone)

#perfrom FFT
from scipy.fft import fft, fftfreq, rfftfreq, rfft

#number of samples in normalized tone
N = SAMPLE_RATE * DURATION

yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

#plot results
plt.plot(xf, np.abs(yf))
plt.show()

#filtering the signal

#the maximum frequency is half the sample rate
points_per_freq = len(xf) / (SAMPLE_RATE / 2)

#our target frequency is 4000 Hz
target_idx = int(points_per_freq * 4000)

yf[target_idx - 1 : target_idx + 2] = 0

plt.plot(xf, np.abs(yf))
plt.show()

#inverse FFT to get the time_domain again

from scipy.fft import irfft

new_sig = irfft(yf)

plt.plot(new_sig[:1000])
plt.show()

norm_new_sig = np.int16(new_sig * (32767 / new_sig.max()))
write("clean.wav", SAMPLE_RATE, norm_new_sig)