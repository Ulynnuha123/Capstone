

from firebase import firebase
import time
import pandas as pd
import numpy as np
import json
 
firebase = firebase.FirebaseApplication("https://capstone-2496f.firebaseio.com/", None)

result=firebase.get('/DATA TEST/',None)
df = pd.DataFrame(result)
# result2 = df[~df.stat1.str.contains("NaN")]

z = pd.DataFrame.transpose(df)
variable = list(df.columns)


x = []
final = []

def convert(s): 
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new


for i in range (0, len(z)):
    y = z.iloc[i,:]
    x.append(variable[i]+",")
    nest = y.dropna()
    for j in range (0, len(nest)):
        val = nest[j]+","
        n = val.replace("[","").replace("]","").replace(" ","")
        x.append(n)
    
h=np.asarray(x)
bw=int(len(h)/len(variable))

for k in range(0,len(z)):
    b = convert(h[(bw*k):(bw*(k+1))])
    
    final.append(b)


lost = np.asarray(final)
cetak = pd.DataFrame(lost)

# directory to save csv

cetak.to_csv (r'C:\Users\BLACK\Desktop\contoh.csv')
