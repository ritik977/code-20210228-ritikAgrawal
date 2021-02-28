import math

def bmi_cal(mass,height):
    bmi=round(mass/(height*height)*10000,2)
    #print("Printing BMI",bmi)
    if bmi <= 18.4:
        return {"BMI":bmi,"BMI_Category":"Under_weight","Health_risk":"malnutrition"}
    elif bmi >=18.5 and bmi < 24.9:
        return {"BMI":bmi,"BMI_Category":"Normal_weight","Health_risk":"low_risk"}
    elif bmi >=25 and bmi < 29.9:
        return {"BMI":bmi,"BMI_Category":"over_weight","Health_risk":"enhanced_risk"}
    elif bmi >=30 and bmi < 34.9:
        return {"BMI":bmi,"BMI_Category":"Moderately_obese","Health_risk":"Medium"}
    elif bmi >=35 and bmi <39.9:
        return {"BMI":bmi,"BMI_Category":"Severely_obese","Health_risk":"High"}
    else:
        return {"BMI":bmi,"BMI_Category":"Very_Severely_obese","Health_risk":"Very_High_risk"} 

