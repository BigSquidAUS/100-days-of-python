height = float(input("Height (m): "))
weight = int(input("Weight (kg): "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)