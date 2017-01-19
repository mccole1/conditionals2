# Function to determine whose name is longer in pair.
name1 = raw_input("What is the first person's name? ")
name2 = raw_input("What is the second person's name? ")

if int(len(name1)) > int(len(name2)):
    print "The first person's name is longer!"
elif int(len(name1)) < int(len(name2)):
    print "The second person's name is longer!"
else:
    print "Both names are the same length."

#Function to output a message depending on what day of the week it is
day_of_week = raw_input("What day of the week is it? ")

if day_of_week == "Monday":
    print "Monday sucks!"
elif day_of_week == "Tuesday":
    print "Sigh, it's only Tuesday"
elif day_of_week == "Wednesday":
    print "Humpday!"
elif day_of_week == "Thursday":
    print "#tbt"
elif day_of_week == "Friday":
    print "TGIF!"
else:
    print "Time to party!"

#Function to tell if you can vote and go to a bar based on your age
age = raw_input("How old are you? ")

if int(age) >= 21:
    print "I can go to a bar!"
elif int(age) >= 18 and int(age) < 21:
    print "I can vote but I cannot go to a bar."
else:
    print "Aww, I cannot vote or go to a bar. (But I don't have to do jury duty.)"

#Function to tell if a number (or 2 numbers) are even and/or odd
number1 = raw_input("What's your first number? ")
number2 = raw_input("What's your second number? ")

if int(number1) % 2 == 0 and int(number2) % 2 == 0:
    print "Both numbers are even."
elif int(number1) % 2 == 0 and int(number2) % 2 == 1:
    print "The first number is even and the second number is odd."
elif int(number1) % 2 == 1 and int(number2) % 2 == 0:
    print "The first number is odd and the second number is even."
else:
    print "Both numbers are odd."

#Function to tell if your favorite color is primary or secondary
color = raw_input("What is your favorite color? ")

if color.lower() == "blue" or color.lower() == "yellow" or color.lower() == "red":
    print "My favorite color is a primary color!"
else:
    print "My favorite color is a secondary color."
