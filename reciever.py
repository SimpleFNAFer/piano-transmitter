import struct

import pyaudio
import numpy as np
import scipy


def calculate_note(input_data):
    fmt = "%dH" % (len(input_data) / 2)
    data_array = struct.unpack(fmt, input_data)
    data_array = np.array(data_array).astype(dtype='h')

    fourier = scipy.fftpack.fft(data_array)
    amplitude = np.abs(fourier)

    sample_freq = scipy.fftpack.fftfreq(fourier.size, d=1/RATE)

    amp_freq = np.array([amplitude, sample_freq])
    amp_position = amp_freq[0, :].argmax()

    peak_freq = amp_freq[1, amp_position]
    detect_note_by_freq(peak_freq)


def detect_note_by_freq(freq):
    if 430 <= freq < 450:
        print('A')
    elif 484 < freq < 504:
        print('B')
    elif 513 < freq < 533:
        print('C')
    elif 577 < freq < 597:
        print('D')
    elif 649 < freq < 669:
        print('E')
    elif 689 < freq < 709:
        print('F')
    elif 774 < freq < 794:
        print('G')
    elif freq > 120:
        print(f'Cannot detect note for {freq} Hz')


CHUNK_SIZE = 65536
CHANNELS = 1
FORMAT = pyaudio.paInt16
RATE = 48000

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK_SIZE)
try:
    while True:
        data = stream.read(CHUNK_SIZE)
        if len(data) > 0:
            calculate_note(data)
except KeyboardInterrupt:
    pass
finally:
    stream.close()
