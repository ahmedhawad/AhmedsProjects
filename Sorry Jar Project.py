import random

"""
My professor has students put a fake dollar in a jar everytime they apologize for asking a question.


This is a program to show how much he could make if we invested the money he could have actualy collected.
"""


quantity_of_apologies = random.randrange(1,10)
quantity_of_classes = random.randrange(1,10)
quanitity_of_sessions_per_class = random.randrange(20,200)

P = (quantity_of_apologies) * (quantity_of_classes) * (quanitity_of_sessions_per_class)    # random number of sorrys at a timeprincipal, intial value
r = .02       #Interest rate, put in .01 form
n = 12       #number of times compounded per year (if t is in years)
t = 10       #number of times per year 

def SorryJar(P,r,n,t):
   calculation =  P*(1+(r/n))**(n*t)
   return calculation

#SorryJar = P*(1+(r/n))**(n*t)

finalNumber = round(SorryJar(P,r,n,t),2)
print ( "You will make:" + " $" + str(finalNumber))


