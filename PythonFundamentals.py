##27.08.2022

##Basic Input Output

print ("Hello World")

##Data types and variables

text_to_print = "Hello World"
print (text_to_print)


##integer  data type

number1 = 23
number2 = 78
print(number1+number2)


##String Data Type

s = "100"
# print(s)
s = 12
print(s)

#Here, the value of variable s has been changed. The print(s) function prints the second one. 


#Input Function
num1 = input("Please type an integer and press enter: ")
num2 = input("Please type an integer and press enter: ")
print(num1+num2)

####Answer is 23. Because all of the inputs taken are in STRING. This is a default case. If we want to give int, just add 



###List
list = [1,2,3,4,5]
print(list)
print(list[3]) ##To find the value at 4th place



saarc = ["Bangladesh","India","Sri Lanka","Nepal"]
print(saarc)
print(len(saarc)) #To find the length of the list
#'int' before the input!

num1 = int (input())
num2 = int (input())
print(num1+num2)









##10/09/2022


##Exercise with list(SAARC Countries)
saarc = ['Bangladesh','India','Sri Lanka']
country = input("Enter the name of the country: ")
if country in saarc:
    print(country, " is a member of saarc!")
else:
    print(country," is not a member of saarc!")
