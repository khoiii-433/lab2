def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Under Weight"
        return -1
    elif 18.5 <= bmi <= 25.0:
        return "Normal Weight"
        return 0
    else:
        return "Over Weight"
        return 1
    

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = calculate_bmi(height, weight)


category = classify_bmi(bmi)

print(f"Your BMI is: {bmi}")
print(f"Weight Classification: {category}")