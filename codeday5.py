top_five_students = ['moin','ayan','shahzaib','ayeza','fatima']
user = input("Enter your name: ")
user = user.lower()
for finding_name in top_five_students:
    if finding_name == user:
        print(f'Congratulation! {finding_name.title()} You are one of them')
        break        
else:
    print("Sorry your name is not there")        
# Add a break statement in the if block when the string is found, and move the 
# else to be the else of the for loop. If this case if the string is found the 
# loop will break and the else will never be reached, and if the loop doesn't 
# brake the else will be reached and 'String not found' will be printed.    

if any([user in x for x in top_five_students]):
    print("String Found")
else:
     print("Not found")

lists = [12,"moin",3.09]
print(lists[0])     

phone_customer = {"first name":"Moinuddin","last name":"Ilyas","address":"karachi","phone":"12345678"}
print(phone_customer["address"])
countries = {"Pakistan":1, "USA":2, "Bangladesh":3 ,"Nepal":4}
print("Ranking of Bangladesh is",countries["Bangladesh"])