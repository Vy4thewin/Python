
# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.

import random 

def ask_meal():
    #Have some pre selected menu choices for our randomizer to decide
    meal=1
    bk=["lets do eggs and bacon", "how about pancakes", "robot loves some rocks and metals","I recommend one grape", "Im tired of deciding breakfast! Nothing…starve"]
    ln=["how about a pizza?","let’s get some pho","sausage and peppers for today","we decided on some apple slices and Bacardi"]
    dn=["lets get some curry goat","calzone tonite?", "Im feeling steak and eggs, you joining??","the magic ball decided on frank and beans for dinner"]
    while (meal !=0):
        meal=input("Enter your meal below for a idea: Breakfast, Lunch, or Dinner. Enter exit when finished ")
        #After user inputs their meal choice of the day, it will go through the menu options
        #It will randomly select a food choice based on the meal selected and prompt user input until user quits program

        if (meal.lower()=="breakfast"):
            ans=random.choice(bk)
            print(ans)

        elif(meal.lower()=="lunch"):
            ans= random.choice(ln)
            print(ans)

        elif (meal.lower()=="dinner"):
            ans=random.choice(dn)
            print(ans)


        elif ( meal.lower()== "exit"):
            print("closing meal decider now, hope you enjoy your meal! ")
            meal=0

        else:
            print("wrong selection, try again ")

ask_meal()

# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. 
# You should take in the user’s input for the number of hours worked, and their rate of pay.

def payroll_sim():
    hours=input("Enter in the hours work for the pay period ")
    rate=input("Enter in the pay rate of the employee ")
    hours=int(hours)
    rate=float(rate)
    #check if user's work over time to seperate two calculations 
    if (hours>20):
        #If over 20 hours work, find regular hours pay and the overtime rate
        reg_pay=20*rate
        over_rate=rate*1.5

        #Find the hours worked overtime and mutliply by the overtime rate for the extra pay. Add two totals together for the takehome amount
        over_hours=hours-20
        over_pay=over_hours*over_rate
        paycheck=over_pay+reg_pay
        return paycheck
    else:
        paycheck=rate*hours
        return paycheck

jules_pay=payroll_sim()
print(f"Jules was paid ${jules_pay}")

# Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.

def times_ten(c):
    ten=c*10
    print(f"{c} was multiply to 10 and resulted in {ten}")

times_ten(5)

# Q4: Find the errors, debug the program, and then execute to show the output.

#first error, no colons in the methods
def main():
      #Format error, Captialized names and same statment in the second calories
      calories1 = input( "How many calories are in the first food? ")
      calories2 = input( "How many calories are in the second food? ")
      showCalories(calories1, calories2)

def showCalories(cal1,cal2): 
    #Need arguments in the method called for cal 1 and 2 
    #Cannot use format and addition, needs to be seperate function
    cal1=int(cal1)
    cal2=int(cal2)
    total_cal=cal1+cal2
    print(f"The total calories you ate today, {total_cal:.2f}")

#also need to call main in order for this to run
main()


# Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#          1/30 + 2/29 + 3/28 ............. + 30/1

def backwards():
    r=0
    for n in range(30):
        if(n==0):
            r=1/30
        else:
            fw=n+1/(30-n)
            r=fw+r
    print(f"This formula resulted in {r}")
    return r

#Results of that equation above
results=backwards()

# Q6: Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT

def compute_tri(b,h):
    area=(1/2)*(b*h)
    print(f"The area of the triangle is {area}")
    return area

t_tri=compute_tri(5,15)