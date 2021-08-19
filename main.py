import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(names)

#print(names[0])
#print(type(names))

#print(random.choice(names))
#print(names1)

name_count = len(names)

name_count = 0

# count is a variable which was never defined in the for loop
for count in names:
  name_count = name_count + 1
#print(name_count)

#pick_name = random.choice(names)
#print(pick_name)

pick_name = random.randint(0, name_count-1)
#print(type(pick_name))
names1 = names[pick_name]
#print(names1)
#print(type(names1))
#pick_name = str(pick_name)
print (f"{names1} is going to buy meal today!")

