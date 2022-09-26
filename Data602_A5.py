
class BankAccount:
  def  __init__(self,bankname,firstname,lastname,balance=0):
    #create a bank account object with user info
      self.bankname=bankname
      self.firstname=firstname
      self.lastname=lastname
      self.balance=balance
    
  def deposit(self,depsoit):
    #add money into the person's balance
      self.balance+=depsoit
  def withdrawl(self,withdrawl):
    #if the withdrawl amount is more than the account balance, refuse withdral. Otherwise, reduce balance
      if(self.balance-withdrawl<0):
        print("Withdrawl cannot exceed balance in account")
      else:
        self.balance=self.balance-withdrawl
        
  def __str__(self):
      #return our standard string when the person checks their bank account
      return f'At {self.bankname} bank. Hello {self.firstname} {self.lastname}, Your account balance is ${self.balance}'

pp1=BankAccount("TD","Spongebob","SquarePants",1000)
print(pp1.__str__())
pp1.deposit(30)
print(pp1.__str__())
pp1.withdrawl(1000)
print(pp1.__str__())

from math import sqrt 


class Box:
  def  __init__(self,length,width):
    #create a box object w/ length and width 
      self.length=length
      self.width=width
  def render(self):
    #add the width of one asterisk or 1" to our box and prints our for the length of the object
    str_w=""
    for n in range(self.width):
      str_w+="*"
    for o in range(self.length):
        print(str_w)

  def invert(self):
    t_w=self.width
    t_l=self.length
    self.width=t_l
    self.length=t_w

  def get_area(self):
    area=self.width*self.length
    return area
  def get_perimeter(self):
    perimeter=2*(self.width+self.length)
    return perimeter

  def double(self):
  #we will take the double request as it doubles in size (i.e= A=12 -> 12*2= 24) increase length by 2 
    self.length=self.length *2
  def __eq__(self,other):
    # returns true if the two boxes' lengths and widths are identical.
    return self.length==other.length and self.width==other.width 
    
  def print_dim(self):
    print(f"The box's length is {self.length} cm and it's width is {self.width} cm ")
  def get_dim(self):
    return (self.length,self.width)
  def combine(self, other):
    #we will assume that we are increasing the metrics with the other box values
    self.length+=other.length
    self.width+=other.width
  def get_hypot(self):
    c=sqrt(self.length**2+self.width**2)
    return c
    
box1=Box(5,10)
box2=Box(3,4)
box3=Box(5,10)
box1.print_dim()
box2.print_dim()
box3.print_dim()
print(box1==box2)
print(box1==box3)
# ● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
# screen accordingly

# Combine box3 into box1 

box1.combine(box3)
box1.print_dim()

print(box2.get_area())
box2.double()
print(box2.get_area())

#Combine box2 into box1 (i.e. box1.combine())

box1.combine(box2)
box1.print_dim()
box1.invert()
box1.print_dim()
print(box3.get_hypot())