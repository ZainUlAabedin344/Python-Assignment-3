# Question No 01
#  Calculate your age based on the current year and your birth year.
print("----------------------------------=<Age Calculator=>----------------------------------")
birthYear:int = int(input("Enter your Birth Year :"))
currentYear:int =int(input("Enter the Current Year to calculate your age :"))
print(("My age is ") +str (currentYear - birthYear) + (" year"))


# Question No 02
#  Write a program that calculates the area of a rectangle using length and width variables
print("----------------------------------=<Area Calculator  of Rectangle=>----------------------------------")
length:int = int(input("Enter the length of rectangle :"))
width:int = int(input("Enter the width of rectangle :"))
area:int = length * width
print("Total area of the Rectangle is :" , area) 

# Question No 03
#  Write a program that calculates the area of a circle
print ("----------------------------------<=Area Calculator of circle=>----------------------------------")
circleRadius:int =int(input("Enter the diameter of circle : "))/2
piValue:int =3.141
print("The area of circle is :" , piValue*circleRadius**2)

# Question No 04
#  Write a program that calculates the area of the cube.
print("----------------------------------<=Area calculator of cube=>----------------------------------")
length:int = int(input("Enter the length of one side of cube : "))**2
area:int = length * 6
print("The area of cube is : " , area)

# Question No 05
#  Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
print("----------------------------------<=Temperature Convertor=>----------------------------------")
print("----------------------------------<=Fahreenheit to Celsius=>----------------------------------")
fahrenheit:int = int(input("Enter the temperature in Fahrenheit : ")) -32
celsius:int =(fahrenheit *5)/9
print("After converting fahrenheit to celcius, Temperatue is : ", celsius)

print("----------------------------------<=Celcius to Fahrenheit=>----------------------------------")
celsius1:int = int(input("Enter temperature in Cellcius : "))*9/5
fahrenheit1:int = celsius1 + 32
print("After converting celcius to fahrenheit, Temperatur is : ", fahrenheit1)


# Question No 06
# Convert a given number of seconds into minutes and seconds using variables.
print("----------------------------------<=Time Calculation=>----------------------------------")
print("----------------------------------<=Minutes into Seconds=>----------------------------------")
timeCalculation:int =int(input("Enter time in Minutes to calculate it into second : "))
result:int = timeCalculation * 60
print("Your given Minutes in seconds :" , result)

print("----------------------------------<=Second into Minutes=>----------------------------------")
timeCalculate:int = int(input("Enter time in seconds  to calculate it  into minutes : "))
timeInMinutes:int = timeCalculate / 60
print("Your given Seconds in Minutes :",  timeInMinutes)

# Question No 07
#  - Write a program that calculates the percentage.
print("----------------------------------<=Percentage Calculation=>----------------------------------")
obtainedMarks:int = int(input("Enter Your Obtained Marks : "))
totalMarks:int =int(input("Enter total marks : "))
percentage:int = obtainedMarks / totalMarks * 100
print("Your Obtained marks in percentage is : ", percentage )

# Question No 08
# - Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables
print("----------------------------------<=BMI or Body Mass index Calculation=>----------------------------------")
height:int =float(input("Enter Your height in meter : "))
weight:int =int(input("Enter your body weight in kg : "))
bmi:int = weight /( height**2)
print("Your BMI is : ",bmi)

# Question No 09
# - Write a program that calculates the volume of a cylinder using the formula .
print("----------------------------------<=Calculate Volume of cylinder=>----------------------------------")
radius:int = int(input("Enter the radius  : "))
height1:int =int(input("Enter the height : "))
print("The volume of cylinder is : ", 3.14*(radius**2)*height)
