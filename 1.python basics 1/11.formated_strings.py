name="jhony"
age=55
print("\nhi " + name + ". you are " + str(age) + " years old")

print(f"\nhi {name}. you are {age} years old")#f determines that it is a formated string

print("\nhi {}. you are {} years old".format(name,age))#these is used in older version of python(python2)

print("\nhi {1}. you are {0} years old".format(name,age))
#you can values and set the order "it will always starts from zero"
