from cmath import e
import codecs
import json
from pyexpat.errors import codes
import re 
import matplotlib.pyplot as plt
from time import sleep
#from Wav2Vec2LargeV3 import Wav2Vec2LargeV3 
from numpy import asmatrix 
import os

#wav = Wav2Vec2LargeV3()
with open('tel_files/result.json', 'r', errors='ignore') as myfile:   
    df = json.load(myfile)


for i in df['messages']:
    try:
        if i['media_type'] == 'voice_message':
            print(i['file'])
            path = os.getcwd() + '/' + i['file']
            print(path)
            #i['text'] = wav.useModel(path)
            
    except:
        continue

with open('tel_files/result_new.json', 'a+') as myfile:
    json.dump(df, myfile, sort_keys=True, indent=4)