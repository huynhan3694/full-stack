import os 
import re
import pandas as pd
import pygsheets
from glob import glob

#  VALUE 20002
# Extract file name from file path
valueMultiFile = pd.DataFrame(glob('/home/datbike/Documents/FullStack/Python/Records/AnotherValue/20002/*'))
valueMultiFile.columns = ['location']

istOneLocation = valueMultiFile['location'].iloc[:]
# print(istOneLocation)
# extract link file out link folder
getValueArray = []
def getValue(GetValue):
        for line in GetValue:
                data = line.split("/", 7)[7]
                replaceValue = data.replace("(","_").replace(")"," ")
                splitFile = replaceValue.split('_',1)[1]
            
                splitMultiCharacter = re.split(pattern=r"[-\_\.]", string=splitFile)
                getValueArray.append(splitMultiCharacter)
                
                # print(type(splitMultiCharacter), splitMultiCharacter)
               
getValue(istOneLocation)
getStringV2 = getValueArray
convertValue = pd.DataFrame(getValueArray,columns=['ID_Agent','SDT','Timing','Other','TypeFile'])

# print(convertValue)
# convertValue['SDT'] = convertValue["SDT"].str.replace('+'," ")
convertValue.loc[~convertValue['SDT'].str.startswith('+84'), 'SDT'] = '+84' + convertValue[~convertValue['SDT'].str.startswith('+84')]['SDT']

print(convertValue)
        # print(getValueTuple)
                

# 
        # print(data, splitMultiCharacter)
        
# splitDirect.split()
# Use re.split() to split on several different characters
# splitMultiCgarecters = re.split(pattern= r"[_\-\(\)\.]", string = splitDirect)
# print(splitMultiCgarecters)