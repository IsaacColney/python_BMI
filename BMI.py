#BMI Calculator
w = input("Enter your weigth (kg)")
h = input("Enter your Height (m)")

def bmi():
    a = float(w)/(float(h)*float(h))
    return a
    
print ("Your BMI is :", bmi())
