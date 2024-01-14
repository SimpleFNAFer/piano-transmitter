import threading
from pynput import keyboard
import numpy as np
import simpleaudio as sa

event = threading.Event()


def stop():
    raise KeyboardInterrupt


def beep(frequency, s):
    fs = 48000

    t = np.linspace(0, s, round(s * fs), False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2 ** 15 - 1) / np.max(np.abs(note))

    audio = audio.astype(np.int16)

    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()


A = 440
B = 494
C = 523
D = 587
E = 659
F = 699
G = 784

dur = 0.5


def on_press_a():
    beep(A, dur)


def on_press_b():
    beep(B, dur)


def on_press_c():
    beep(C, dur)


def on_press_d():
    beep(D, dur)


def on_press_e():
    beep(E, dur)


def on_press_f():
    beep(F, dur)


def on_press_g():
    beep(G, dur)


h = keyboard.GlobalHotKeys({
    'a': on_press_a,
    'b': on_press_b,
    'c': on_press_c,
    'd': on_press_d,
    'e': on_press_e,
    'f': on_press_f,
    'g': on_press_g,

    '<ctrl>+q': stop,
})

try:
    h.start()
    h.join()
except KeyboardInterrupt:
    h.stop()
