import os 
import re
import pandas as pd
import pygsheets
from glob import glob

#  VALUE 20001V1
# Extract file name from file path
valueMultiFile = pd.DataFrame(glob('/home/datbike/Documents/FullStack/Python/Records/AnotherValue/20001v1/*'))
valueMultiFile.columns = ['location']

istOneLocation = valueMultiFile['location'].iloc[:]
# print(istOneLocation)
# extract link file out link folder
getValueArray = []
def getValue(GetValue):
        for line in GetValue:
                data = line.split("/", 7)[7]
                replaceValue = data.replace("(","_").replace(")"," ")
                splitFile = replaceValue.split('_',2)[2]
            
                splitMultiCharacter = re.split(pattern=r"[-\_\.]", string=splitFile)
                getValueArray.append(splitMultiCharacter)
                
                # print(type(splitMultiCharacter), splitMultiCharacter)
               
getValue(istOneLocation)
getStringV2 = getValueArray
convertValue = pd.DataFrame(getValueArray,columns=['STT','SDT','Timing','ID','TypeFile'])

# print(convertValue)
# convertValue['SDT'] = convertValue["SDT"].str.replace('+'," ")
convertValue.loc[~convertValue['SDT'].str.startswith('+84'), 'SDT'] = '+84' + convertValue[~convertValue['SDT'].str.startswith('+84')]['SDT']

# print(convertValue)
        # print(getValueTuple)
                

# 
        # print(data, splitMultiCharacter)
        
# splitDirect.split()
# Use re.split() to split on several different characters
# splitMultiCgarecters = re.split(pattern= r"[_\-\(\)\.]", string = splitDirect)
# print(splitMultiCgarecters)