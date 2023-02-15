import winsound
import time
import random

chimes = ["chime1.wav", "chime2.wav", "chime3.wav", "chime4.wav"]

while True:
    e = time.localtime()
    if e.tm_min == 59 and e.tm_sec == 59:
        winsound.PlaySound(chimes[random.randint(0, 3)], winsound.SND_FILENAME | winsound.SND_ASYNC)
    time.sleep(1)
 
