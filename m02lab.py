# Garrett Collier
# SDEV 220
# M02 Lab: Asks user to input student's name and gpa to determine if student has made either Dean's List or Honor Roll

last_name = str(input("Please enter the student's last name: "))

# Determines if program will run based on input from user
while last_name != "ZZZ":

    # Asks user for student's first name
    first_name = str(input("Please enter the student's first name: "))

    # Asks user for student's GPA
    gpa = float(input("Please enter the student's GPA: "))

    # If it is then student has made Dean's List
    if gpa >= 3.5:
        print("Congrats!", first_name, last_name, "has made the Dean's List!")

    # Determines if gpa is 3.25 or more (Honor Roll)
    else:
        if gpa >= 3.25:
            print("Congrats!", first_name, last_name, "has made the Honor Roll!") 
    last_name = str(input("\nEnter Student Last Name: "))
    # Repeats program until 'ZZZ' entered