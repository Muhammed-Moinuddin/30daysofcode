cities = ["karachi","lahore","islamabad","peshawer"]
print(cities[1])
categories = ["hello",2,9.38,True]
print(categories[3])
categories.append("World")
print(categories)
cities = cities + ["multan","quetta","murree","gilgit-baltistan"]
print(cities)
names = []
print(names)
names.append("Moinuddin")
print(names)
'''If you want to just add something in list without looking towards its position use .append() 
method but if you want to add something specifically on a certain position then use insert method'''
cities.insert(0, "Quetta")
print(cities)
# To change the value we simply used indexing with list name
cities[2] = "lahore lahore hai"
print(cities)
smaller_list_of_cities = cities[3:7]
print(smaller_list_of_cities)
check_list = cities[4:]
print(check_list)
# delete something with indexing using del operator and delete something through value using remove operator
del cities[8]
cities.remove('murree')
print(cities)
tasks = ["email shahzaib","call ayan","meet with inshal","voicenote to dad"]
task_accomplished = ["message to mom"]
latest_task_accomplished = tasks.pop(1)
print(tasks)
print(task_accomplished)
print(latest_task_accomplished)
task_accomplished.append(tasks.pop(1))
# tasks.append(latest_task_accomplished)
# print(tasks)
print(task_accomplished)
task_accomplished.insert(1, tasks.pop(1))
print(task_accomplished)
# The code above strikes the second element off the tasks list and inserts it
# as the second element in the tasks_accomplished list.