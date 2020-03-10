
from Adafruit_IO import Client,Feed
import sys
import time
import os
import random
import numpy as np

ADAFRUIT_IO_KEY = 'aio_ZWbI31fl9XVSloQe6WIX5paCVbTs'

ADAFRUIT_IO_USERNAME = 'C_Project'

aio = Client (ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

micron_feed=aio.feeds('testing')

while True:
    kappa=random.randint(0,100)
    aio.send(micron_feed.key, int(kappa))
    print('Publishing {0} '.format(kappa))
    time.sleep(1)
    
    value=aio.receive(micron_feed.key).value
    print(value)
