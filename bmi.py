def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height**2)
    print("BMI = " + str(round(bmi, 2)))

    if bmi < 18.5:
        print("you are underweight")
        return(-1)
    elif bmi >= 18.5 and bmi <= 25.0:
        print("you are classified as normal weight")
        return(0)
    else:
        print("you are over weight")
        return(1)

calculate_bmi(weight=92, height=1.83)