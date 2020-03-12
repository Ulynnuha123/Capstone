
from Adafruit_IO import Client,Feed
import sys
import time
import os
import random
import numpy as np

#ADAFRUIT_IO_KEY = '403d235a5abb43bc8f72041a8e524d52' 'punya babud'
#ADAFRUIT_IO_KEY = 'aio_ZWbI31fl9XVSloQe6WIX5paCVbTs'
ADAFRUIT_IO_KEY = 'aio_oylm32E2eiFKjVHcfgAwoRubSdLH'

ADAFRUIT_IO_USERNAME = 'C_Project'
#ADAFRUIT_IO_USERNAME = 'Bagasbudhi'

aio = Client (ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

data1_feed=aio.feeds('sensor-1')
data2_feed=aio.feeds('sensor-2')
data3_feed=aio.feeds('sensor-3')

while True:

    kappa1=random.randint(0,70)
    kappa2=random.randint(0,15)
    kappa3=random.randint(0,20)

    hades1=random.randint(0,1)

    data1=[kappa1,hades1]
    data2=[kappa2,hades1]
    data3=[kappa3,hades1]

    aio.send(data1_feed.key,str(data1))
    aio.send(data2_feed.key,str(data2))
    aio.send(data3_feed.key,str(data3))

    # lost=aio.receive(data1_feed.key).value
    # res = lost.strip('][').split(', ') 
    # for i in range(0, len(res)): 
    #     res[i] = int(res[i])
    #y=value.split(",")
    #casted_y = [float(y[i]) for i in range(len(y))]

    #print("data = {0}".format(res[0]))
    print("data1 = {0}\ndata2 = {1}\ndata3 = {2} \n".format(data1,data2,data3))


    time.sleep(1)
