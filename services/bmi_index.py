import json
import sys
sys.path.append('../')
from services.index_cal import *

with open('data/raw.json','r') as myfile:
    bmi_json_data=myfile.read()

data=json.loads(bmi_json_data)
#print(data)

def bmi_table():
    for entries in data:
        height =entries["HeightCm"]
        mass= entries["WeightKg"]
        #print ("the mass is ",mass," and height is",height)
        entries.update(bmi_cal(mass,height))
    return data

def cal_overweight_people():
    count = 0
    data=bmi_table()
    print(data)
    for rows in data:
        if rows['BMI'] >=25 and rows['BMI'] <=30:
            count+=1
    print("The Count of total no. of overweight people are ",count)
    return count
    

if __name__ == "__main__":
    cal_overweight_people()
 