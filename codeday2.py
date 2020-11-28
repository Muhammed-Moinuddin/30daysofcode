
first_name = "Muhammad Moinuddin"
last_name = "Rehmani"
full_name = "Muhammad Moinuddin Rehmani"
if full_name == "Muhammad Moinuddin" + " " + "Rehmani":
    print(full_name)
if full_name == first_name + last_name:
    print(full_name)
if full_name == first_name + " " + "Ilyas":
    print("Yep,you are right")
else:
    print("No,you are wrong")        
cost_of_donut = 0
donut_condition = "fresh"
donut_flavour = "choclate"
donut_price = "high"
#understanding if ,else and elif
if donut_condition == "fresh":
    cost_of_donut += 20
elif donut_flavour == "choclate":
    cost_of_donut += 30
else:
    print("Nothing is selected")
print(cost_of_donut)
if donut_condition == "fresh":
    cost_of_donut += 20
if donut_flavour == "choclate":
    cost_of_donut += 15
if donut_price == "low":
    cost_of_donut -= 20
print("You've selected the right item and your bill is:",cost_of_donut)
weight = float(input("Please enter your weight in pounds: "))
height = float(input("Please enter your height in cm: "))
education = str(input("Please enter your education: "))
age = int(input("Please enter your age: "))
if weight > 300 and height > 163 and education == "Graduation" and (age < 23 or age > 18):
    print("try to recruit")
        
