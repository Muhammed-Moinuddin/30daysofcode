provinces_of_pakistan = ("Sindh","Punjab","Balochistan","KPK") ##tuple element are fixed.
second_province = provinces_of_pakistan[1]
print("The second province of Pakistan is " + second_province)
# second_province_pop = provinces_of_pakistan.pop(1)
# print(second_province_pop)
#It does not work because elements within tuple are fixed with their location as well
#you have to re-code the whole tuple, to change it
cleanest_cities = ["Islamabad","Lahore","Peshawer"]
city_to_check = "Peshawer"
if city_to_check == cleanest_cities[0]:
    print("One of the cleanest city is",cleanest_cities[0])
elif city_to_check == cleanest_cities[1]:
    print("One of the cleanest city is",cleanest_cities[1])
elif city_to_check == cleanest_cities[2]:
    print("One of the cleanest city is",cleanest_cities[2])        
for x in cleanest_cities:
    if x == city_to_check:
        print("One of the cleanest sity is",x)        
a = (1,3,5,7,9)
check_number = 5
for x in a:
    if x == check_number:
        print("We've found the number")
        break     
#nested loop
first_names = ("Moinuddin","Owais","Ahmed","Muhiuddin","Mudassir")
last_names = ("Ilyas","Mohsin","Imran","Abubakkar","Iqbal")
full_names = []
for x in first_names:
    for y in last_names:
        full_names.append(x + " " + y)
        print(x + " " + y)    
print(full_names)
amount = int(input("Please enter your income: "))
calculation = amount * 5/100
print("Your 5% tax is",calculation ,"And your remaining amount is:",amount-calculation)
calculation = str(calculation)
print("Your 5% tax is " + calculation)
print(type(calculation))