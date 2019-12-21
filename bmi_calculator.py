#BMI Calculator
#Author Isaac
def bmi():
    a = float(w)/(float(h)*float(h))
    return a
    
again = "y"

while again.lower() == "y":
    w = input("Enter your weigth (kg)")
    h = input("Enter your Height (m)")


    
    print ("Your BMI is :", bmi())

    again = input("Do you want to Calculate again?y/n:")
    if again == "n":
        print('Have a Great Day');
        break
