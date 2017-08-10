'''number =  4

Bool = True

number = number + 1

print (Bool)

print (number)

division = 4/5

number = number * division
print (number)

exponent = 2**3

number = number * division + exponent

print (number)

modulo = 20% 3
print (modulo) '''


'''
cost = 25

tax = 0.13

tip = 0.15

totalcost = cost * (1 + tax) * (1+ tip)

print (totalcost)

# cost = 25 tax = 13% tip = 15%; total cost?

'''



'''for  i in range (1,cost): 
        print (i)'''



'''
name = "Justin"
name1 = "Lu Han" 

print (name)
print("my name is " + name[3] + name[4])# print on of  the letter of the string

print(len(name))# print the number of the string including letters and space

print(name1.lower()) # dot notation can only be used on strings 
print(name.upper()) # type everything in the upper version


quantity = 15
fruit = " Apples"
print("there are " + str(quantity) + fruit) # how to combine string with number

'''


'''
askname = input(" what is your name ")
print ("Hello " + askname)

favourate = input ("what is your favourate team")
print ("Hello " + askname + ", fan of " + favourate)
''' 
# == is euqal to; != not euqal to; < less than





# and statement: one false all false
# or statement:

'''
siwi=4

air = 8



if 8>9 : print(air)
    
elif 4>1 : print ("u r tiraer")
else : print(siwi)    
    
'''

'''
fruit = "apple"

app = fruit [0:2]
print(app)
'''

'''
askword = input("Please enter a word please")


length  = len (askword)

first = askword [0]


new = askword [1:length] + first + "ay"

if length < 1: print("the word need to have more than 1 character")
elif askword == " " : print ("the word cannot be 1 space")
else: print (new) 
'''



'''
def square(x):
    return(x**3)




def div(y):
    if y%3 == 0 :
        return (square(y) + 5)  
    else: return False

print(div(6))
'''



'''

def cost(nights):
     return (nights * 150)




def plane(place):
     
     
     if place == "shanghai":
          return 183
     elif place == "Dubai":
          return 220
     elif place == "Toronto":
          return 222
     elif place == "NewYork":
          return 475
     else: print("please give a correct destination")
     

def rent(days):
     cost = 40 * days

     if days >= 7:
          cost = cost - 50
          return(cost)
     
     elif days >= 3:
          cost = cost -20
          return(cost)

     else:
           return cost

     
     

def total():
     
     
     days = int(input("How long are you staying"))
     city = input("which city are you going to ?")

     
     return plane(city)+ cost(days) + rent(days)
'''


     






'''
numbers.pop(1)
'''

"""

animals = ["cat", "tiger", "dragon", "tiger"]
print (animals.index("tiger"))
animals.append("cow")
animals.insert(1, "cow") 


print(animals)

animals.sort()

print(animals)




numbers = [3,2,4,1,4,6,5,27,123]
numbers.sort()
print (numbers)


letters = ["a","b","c","d","e"]
bc = letters[1:3]
print(bc)

"""


'''

square =[1,2,3,4,5]
blank = []

for num in square:
     blank.append(num**2)


print(blank)




d = { "key1":1, "key2":2, "key3": 3}
print(d)

print (d["key2"])

d["key3"] = 6

del d["key3"]

print(d)

d["apple"] = 4

print(d)


for key in d:
     print(d[key])

'''

food = {"Banana":4, "Apple":2, "Orange":1.5, "Pear":3}


stock = {"Banana":6, "Apple":2, "Orange":32, "Pear":15}


cac = 0
total = 0

     
for price in food:
     
     cac = food [price] * stock[price]
     
     total = total + cac



     
print (total)

'''
for thing in food:
    print (thing)
    print ("price: " + str (food[thing]))
    print ("stock: " + str (stock[thing]))




'''




























