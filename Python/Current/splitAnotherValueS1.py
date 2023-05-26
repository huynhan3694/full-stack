
import os 
import re
import pandas as pd
import pygsheets
from glob import glob
from splitAnotherValueS2 import getStringV2
# VALUE 20001
# Extract file name from file path
valueMultiFile = pd.DataFrame(glob('/home/datbike/Documents/FullStack/Python/Records/AnotherValue/20001/*'))
valueMultiFile.columns = ['location']

istOneLocation = valueMultiFile['location'].iloc[:]
# print(istOneLocation)
# extract link file out link folder
getValueArray = []
# print(getValueArray)
def getValue(GetValue):
        for line in GetValue:
                data = line.split("/", 7)[7]
                replaceValue = data.replace("(","_").replace(")"," ")
                splitFile = replaceValue.split('_',1)[1]
                splitMultiCharacter = re.split(pattern=r"[-\_\.]", string=splitFile)
                getValueArray.append(splitMultiCharacter)
              
                # print(type(splitMultiCharacter), splitMultiCharacter)
               
getValue(istOneLocation)
addValueV1_V2 = getValueArray + getStringV2
convertValue = pd.DataFrame(addValueV1_V2,columns=['SDT','ID_Agent','Timing','Other','TypeFile'])
changeColumns = ['ID_Agent','SDT','Timing','Other','TypeFile']
convertValue = convertValue[changeColumns]
convertValue.loc[~convertValue['SDT'].str.startswith('+84'), 'SDT'] = '+84' + convertValue[~convertValue['SDT'].str.startswith('+84')]['SDT']
convertValueS1 = convertValue.reindex(columns=changeColumns)
# print(convertValue)
# convertValue['SDT'] = convertValue["SDT"].str.replace('+'," ")
exportConvertValue = convertValue

print(exportConvertValue)
        # print(getValueTuple)
                

# 
        # print(data, splitMultiCharacter)
        
# splitDirect.split()
# Use re.split() to split on several different characters
# splitMultiCgarecters = re.split(pattern= r"[_\-\(\)\.]", string = splitDirect)
# print(splitMultiCgarecters)