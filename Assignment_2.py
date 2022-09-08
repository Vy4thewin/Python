#Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
#print(numbers[1:-5]) Bugged statement
#ans: It prints out a empty array
print(numbers) #prints out entire list of numbers

#Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

def Total_sales():
  total_sales=[]
  #In the for loop: append user's total spend in the list and return the sum of the list items
  for x in range(1,8):
    sales = input(f'Enter the sale for day {x}: ')
    total_sales.append(float(sales))
      
  return sum(total_sales)

sales_week=Total_sales()
print(str(sales_week))

# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order
# ● Print your list in its original order.
# ● Use the sort() function to arrange your list in order and reprint your list.
# ● Use the sort(reverse=True) and reprint your list.
vacay=['Zoo', 'Colorado', 'Italy', 'Canada', 'Museum']  
print(vacay)
vacay.sort()
print(vacay)
vacay.sort(reverse=True)
print(vacay)

# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time. course[x]=y


courses={}
courses['DATA101']={"RoomNumber":100,"Instructor":"nicholas","MeetingTime":"8:00pm"}
courses['DATA302']={"RoomNumber":201,"Instructor":"Mia","MeetingTime":"6:00pm"}
courses['DATA606']={"RoomNumber":151,"Instructor":"Jason","MeetingTime":"6:30pm"}
courseTest=input('Enter in the course number ')

print('Room Number:', courses[courseTest]['RoomNumber'])
print('Instructor:', courses[courseTest]['Instructor'])
print('Meeting Time:', courses[courseTest]['MeetingTime'])



# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.


def eBook(address_book):
  ans=input("Enter option : Add new entry, change entry, delete entry ")
  # for adding contacts, enter "add", delete entry: "delete", change entry: "change"

  if(ans=="add"):
    name=input("Enter name ")
    email=input("Enter email ")
    address_book[name]=email
    return address_book
  elif(ans=="change"):
    ch=input("Enter the name of the email to change ")
    ch_em=input("Enter in the new email")
    address_book[ch]=ch_em
    return address_book
  elif(ans=="delete"):
    de=input("Enter in the contact name to delete ")
    address_book.pop(de)
    return address_book
  else:
    print("wrong entry")
  

ad_book={}
#adding a contact
my_add=eBook(ad_book)
print(my_add)

#changing a contact
my_change=eBook(my_add)
print(my_change)

my_delete=eBook(my_change)
print(my_delete)