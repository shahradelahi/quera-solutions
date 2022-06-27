weight, height = int(input()), float(input())


def bmi(w, h):
    return w / (h ** 2)


def fixed_decimal_places(n):
    return "{:.2f}".format(n)


print(fixed_decimal_places(bmi(weight, height)))

if bmi(weight, height) < 18.5:
    print("Underweight")
elif bmi(weight, height) < 25:
    print("Normal")
elif bmi(weight, height) < 30:
    print("Overweight")
else:
    print("Obese")
