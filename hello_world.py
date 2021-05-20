# python hello.py to run the code in the terminal 
""" print("Hello Python interpreter!") """

#############################################################

# Variables 
""" message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message) """

##############################################################

# Data Types
# 1. String
""" name = "ada lovElace"
print(name.title()) # prints Ada Lovelace --> Capitalizes first character of a word and non-capitalizes other characters of a word
print(name.upper()) # prints ADA LOVELACE
print(name.lower()) # prints ada lovelace """

""" first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name) # prints ada lovelace
print(f'Hello, {full_name.title()}!') # prints Hello, Ada Lovelace! """

""" print("Python") # prints Python
print("\tPython") # prints      Python --> \t adds a tab space, 
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# Languages:
#     Python
#     C
#     JavaScript --> \n to add a new line """

""" favorite_language = 'python '
print(favorite_language.rstrip()) # strips whitespace at right end, [rstrip(), lstrip() & strip()] """

# 2. Numbers [integers, float]
""" Python uses two multiplication symbols to represent exponents: 3**3 = 9 """

""" # Underscores in Numbers --> When you’re writing long numbers, you can group digits using underscores to make large numbers more readable: 
 universe_age = 14_000_000_000
print(universe_age) # prints 14000000000 """

""" # Multiple Assignment
x, y, z = 0, 0, 0 """

""" # Constants --> Python doesn’t have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed
MAX_CONNECTIONS = 5000 """

# The Zen of Python
# import this
# prints:
""" The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! """

#######################################################################

# 1. Lists -->  collection of items in a particular order. You can put anything you want into a list, and the items in your list don’t have to be related in any particular way. In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas
""" bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # prints ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # prints trek
print(bicycles[0].title()) # prints Trek
print(bicycles[-1]) # prints specialized --> By asking for the item at index -1, Python always returns the last item in the list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message) # prints My first bicycle was a Trek. """

# Changing, Adding, and Removing Elements
# motorcycles = ['honda', 'yamaha', 'suzuki']

# Modifying Elements in a List
""" print(motorcycles) # prints ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles) # prints ['ducati', 'yamaha', 'suzuki'] """

# Adding Elements to a List
""" motorcycles.append('ducati')
print(motorcycles) # prints ['honda', 'yamaha', 'suzuki', 'ducati'] """

# Inserting Elements into a List
""" motorcycles.insert(0, 'ducati')
print(motorcycles) # prints ['ducati', 'honda', 'yamaha', 'suzuki'] """

# Removing Elements from a List
""" del motorcycles[0] 
print(motorcycles) # prints ['yamaha', 'suzuki'] """

# Removing an Item Using the pop() Method
""" popped_motorcycle = motorcycles.pop() 
print(motorcycles) # prints ['honda', 'yamaha']
print(popped_motorcycle) # prints suzuki """

# Popping Items from any Position in a List
""" first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.") # prints The first motorcycle I owned was a Honda """

# Removing an Item by Value
""" motorcycles.remove('honda') # The remove() method deletes only the first occurrence of the value you specify
print(motorcycles) # prints ['yamaha', 'suzuki'] """
""" too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles) # prints ['yamaha', 'suzuki']
print(f"\nA {too_expensive.title()} is too expensive for me.") # prints A Honda is too expensive for me. """

# Organizing a List
# Sorting a List Permanently with the sort() Method
""" cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # prints ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars) # prints ['toyota', 'subaru', 'bmw', 'audi'] """

# Sorting a List Temporarily with the sorted() Function
""" print("Here is the original list:")
print(cars) # prints ['toyota', 'subaru', 'bmw', 'audi']
print("\nHere is the sorted list:")
print(sorted(cars)) # prints ['audi', 'bmw', 'subaru', 'toyota'],
# if we pass  reverse= True as a second argument, this will display in reverse order
print("\nHere is the original list again:")
print(cars) # prints ['toyota', 'subaru', 'bmw', 'audi'] """

# Printing a List in Reverse Order
""" cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars) # prints ['subaru', 'toyota', 'audi', 'bmw']
len(cars) # prints 4 """

# Looping Through an Entire List
""" magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick!")
print("Thank you, everyone. That was a great magic show!") """

# Using the range() Function
""" for value in range(1, 5):
 print(value) # prints 1 2 3 4

numbers = list(range(1, 6))
print(numbers) # prints [1, 2, 3, 4, 5]

even_numbers = list(range(2, 11, 2)) 
print(even_numbers) # prints [2, 4, 6, 8, 10]

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # 0
print(max(digits)) # 9
print(sum(digits)) # 45

squares = [value**2 for value in range(1, 11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] """

# Slicing a List
""" players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[1:3]) # ['martina', 'michael']
print(players[:3]) # ['charles', 'martina', 'michael']
print(players[2:]) # ['michael', 'florence', 'eli']
print(players[-3:]) # ['michael', 'florence', 'eli'] """

# Looping Through a Slice --> You can use a slice in a for loop if you want to loop through a subset of the elements in a list
""" players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())
# Charles
# Martina
# Michael """

# Copying a List
""" my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods) # ['pizza', 'falafel', 'carrot cake']
print("\nMy friend's favorite foods are:")
print(friend_foods) # ['pizza', 'falafel', 'carrot cake'] """

# 2. Tuples --> Python refers to values that cannot change as immutable, and an immutable list is called a tuple
""" dimensions = (200, 50)
print(dimensions[0]) # 200
print(dimensions[1]) # 50 """
# Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma

# Looping Through All Values in a Tuple
""" dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)
 
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension) """

 #################################################################

 # If statements
""" cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# other operators: ==, !=, >, <, >=, <=, age_0 >= 21 and age_1 >= 21, age_0 >= 21 or age_1 >= 21 """

# Checking Whether a Value Is in a List
""" requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # True """

# Checking Whether a Value Is Not in a List
""" banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(f"{user.title()}, you can post a response if you wish.") # works """

# The if-elif-else Chain
""" age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.") """

# Python does not require an else block at the end of an if-elif chain. Sometimes an else block is useful; sometimes it is clearer to use an additional elif statement that catches the specific condition of interest

# Checking That a List Is Not Empty
""" requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?") """

########################################################################

# Dictionaries --> allow you to connect pieces of related information
""" alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points']) """

# Adding New Key-Value Pairs
""" alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) """

# Modifying Values in a Dictionary
""" alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.") """

# Removing Key-Value Pairs
""" alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0) """

# Using get() to Access Values
""" alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value) """
# If the key 'points' exists in the dictionary, you’ll get the corresponding value. If it doesn’t, you get the default value. In this case, points doesn’t exist, and we get a clean message instead of an error. If you leave out the second argument in the call to get() and the key doesn’t exist, Python will return the value None. The special value None means “no value exists.” This is not an error: it’s a special value meant to indicate the absence of a value

# Looping Through a Dictionary
# Looping Through All Key-Value Pairs
""" user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
 print(f"\nKey: {key}")
 print(f"Value: {value}") """

 # Looping Through All the Keys in a Dictionary
""" favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in favorite_languages.keys():
 print(name.title())
for name in favorite_languages:
 print(name.title()) # both of them prints the same
# Jen
# Sarah 
# Edward
# Phil  """

""" favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
 if name in friends:
     language = favorite_languages[name].title()
     print(f"\t{name.title()}, I see you love {language}!")
     # Sarah, I see you love C!
     # Phil, I see you love Python! """

""" favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
if 'erin' not in favorite_languages.keys():
 print("Erin, please take our poll!") """

# Looping Through a Dictionary’s Keys in a Particular Order
""" favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
 print(f"{name.title()}, thank you for taking the poll.") """

# Looping Through All Values in a Dictionary
""" favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title()) """

""" favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): # A set is a collection in which each item must be unique, avoids repeating of same value twice
 print(language.title()) """

# Nesting

# A List of Dictionaries
""" alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien) """

# A List in a Dictionary
""" pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }
print(f"You ordered a {pizza['crust']}-crust pizza "
 "with the following toppings:")
for topping in pizza['toppings']:
 print("\t" + topping) """

# A Dictionary in a Dictionary
""" users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}") """

#########################################################################

# User inputs and while loops

""" message = input("Tell me something, and I will repeat it back to you: ")
print(f"You said: {message}") """

""" name = input("Please enter your name: ")
print(f"\nHello, {name}!") """

""" prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!") """

# Using int() to Accept Numerical Input
""" height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
 print("\nYou're tall enough to ride!")
else:
 print("\nYou'll be able to ride when you're a little older.") """

# The Modulo Operator
""" number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print(f"\nThe number {number} is even.")
else:
 print(f"\nThe number {number} is odd.") """

# Introducing while Loops
""" current_number = 1
while current_number <= 5:
 print(current_number)
 current_number += 1 """

# Letting the User Choose When to Quit
""" prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
 message = input(prompt)
 print(message) """

# Using a Flag
""" prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
 
    if message == 'quit':
        active = False
    else:
        print(message) """

# Using break to Exit a Loop
""" prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
 city = input(prompt)
 
 if city == 'quit':
    break
 else:
    print(f"I'd love to go to {city.title()}!") """

# Using continue in a Loop
""" current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number) """

# Using a while Loop with Lists and Dictionaries
""" A for loop is effective for looping through a list, but you shouldn’t modify 
a list inside a for loop because Python will have trouble keeping track of the 
items in the list. To modify a list as you work through it, use a while loop. 
Using while loops with lists and dictionaries allows you to collect, store, and 
organize lots of input to examine and report on later. """

# Moving Items from One List to Another
""" unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
 print(confirmed_user.title()) """

# Removing All Instances of Specific Values from a List
""" pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
 pets.remove('cat')
 
print(pets) """

# Filling a Dictionary with User Input
""" responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
 print(f"{name} would like to climb {response}.") """

##################################################################################

# Functions
""" def greet_user():
 print("Hello!")
 
greet_user() """

# Passing Information to a Function
""" def greet_user(username):
 print(f"Hello, {username.title()}!")
 
greet_user('ashwin') """

# Passing Arguments --> Order Matters in Positional Arguments
# Positional Arguments
""" def describe_pet(animal_type, pet_name):
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') """

# Multiple Function Calls
""" def describe_pet(animal_type, pet_name):
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie') """

# Keyword Arguments --> A keyword argument is a name-value pair that you pass to a function, Order doesn't Matter in Keyword Arguments, When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition.
""" def describe_pet(animal_type, pet_name):
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster') """

# Default Values --> When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.
""" def describe_pet(pet_name, animal_type='dog'):
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie') """

# Equivalent Function Calls
""" def describe_pet(pet_name, animal_type='dog'):
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry') """

# Return Values
# Returning a Simple Value
""" def get_formatted_name(first_name, last_name):
 full_name = f"{first_name} {last_name}"
 return full_name.title()
musician = get_formatted_name('ashwin', 'magalu')
print(musician) """

# Making an Argument Optional
""" def get_formatted_name(first_name, last_name, middle_name=''):
 if middle_name:
    full_name = f"{first_name} {middle_name} {last_name}"
 else:
    full_name = f"{first_name} {last_name}"
 return full_name.title()
 
musician1 = get_formatted_name('ashwin', 'maglu', 'gowda')
musician2 = get_formatted_name('ashwin', 'magalu')
print(musician1)
print(musician2) """

# Returning a Dictionary
""" def build_person(first_name, last_name):
 person = {'first': first_name, 'last': last_name}
 return person
musician = build_person('ashwin', 'magalu')
print(musician) """

""" def build_person(first_name, last_name, age=None):
 person = {'first': first_name, 'last': last_name}
 if age:
    person['age'] = age
 return person
musician = build_person('ashwin', 'magalu', age=27)
print(musician) """

# Using a Function with a while Loop
""" def get_formatted_name(first_name, last_name):
 full_name = f"{first_name} {last_name}"
 return full_name.title()

while True:
 print("\nPlease tell me your name:")
 print("(enter 'q' at any time to quit)")
 
 f_name = input("First name: ")
 if f_name == 'q':
 break
 
 l_name = input("Last name: ")
 if l_name == 'q':
 break
 
 formatted_name = get_formatted_name(f_name, l_name)
 print(f"\nHello, {formatted_name}!") """

# Passing a List
""" def greet_users(names):
 for name in names:
    msg = f"Hello, {name.title()}!"
    print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames) """

# Modifying a List in a Function
""" unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
 current_design = unprinted_designs.pop()
 print(f"Printing model: {current_design}")
 completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
 print(completed_model) """

""" def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models) """

# Preventing a Function from Modifying a List
""" def print_models(unprinted_designs, completed_models): 
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)# The slice notation [:] makes a copy of the list to send to the function.
show_completed_models(completed_models) """

# Passing an Arbitrary Number of Arguments
""" def make_pizza(*toppings): # The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple
 print("\nMaking a pizza with the following toppings:")
 for topping in toppings:
    print(f"- {topping}")
 
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese') """

# Mixing Positional and Arbitrary Arguments --> If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter
""" def make_pizza(size, *toppings): 
 print(f"\nMaking a {size}-inch pizza with the following toppings:") 
 for topping in toppings: 
    print(f"- {topping}") 
 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') """

# Using Arbitrary Keyword Arguments --> Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information will be passed to the function
""" def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')
print(user_profile)
# You’ll often see the parameter name **kwargs used to collect non-specific keyword arguments. """

# Storing Your Functions in Modules
""" One advantage of functions is the way they separate blocks of code from your main program. By using descriptive names for your functions, your main program will be much easier to follow. You can go a step further by storing your functions in a separate file called a module and then importing
that module into your main program. An import statement tells Python to make the code in a module available in the currently running program file. Storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic. It also allows you to reuse functions in many different programs. When you store your functions in separate files, you can share those files with other programmers without having to share your entire program. Knowing how to import functions also allows you to use libraries of functions that other programmers have written. """

# Importing an Entire Module
""" To start importing functions, we first need to create a module. A module is a file ending in .py that contains the code you want to import into your program """
""" import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') """

# Importing Specific Functions
""" from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') """

# Using as to Give a Function an Alias
""" from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese') """

# Using as to Give a Module an Alias
""" import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') """

# Importing All Functions in a Module
""" from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') """

""" If you specify a default value for a parameter, no spaces should be used on either side of the equal sign. The same convention should be used for keyword arguments in function calls """

####################################################################################################

# Files and Exceptions
# Reading from a File
""" with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip()) # 3.14..............
# open('pi_digits.txt') returns an object representing pi_digits.txt. Python assigns this object to file_object. You could open and close the file by calling open() and close() """

# Reading Line by Line
""" filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line) """

# Making a List of Lines from a File
""" filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip()) """

# Working with a File’s Contents
""" filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    print(pi_string)
    print(len(pi_string)) """


# Writing to a File

# Writing to an Empty File
""" filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
# The call to open() in this example has two arguments u. The first argument is still the name of the file we want to open. The second argument, 'w', tells Python that we want to open the file in write mode. You can open a file 192 Chapter 10 in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+'). If you omit the mode argument, Python opens the file in read-only mode by default. """

# Writing Multiple Lines
""" filename = 'programming.txt'
with open(filename, 'w') as file_object:
 file_object.write("I love programming.\n")
 file_object.write("I love creating new games.\n") """

# Appending to a File --> If you want to add content to a file instead of writing over existing content, you can open the file in append mode
""" filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n") """


# Exceptions
""" Python uses special objects called exceptions to manage errors that arise during a program’s execution. Whenever an error occurs that makes Python unsure what to do next, it creates an exception object. If you write code that handles the exception, the program will continue running. If you don’t handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised.
Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised. When you use try-except blocks, your programs will continue running even if things start to go wrong. Instead of tracebacks, which can be confusing for users to read, users will see friendly error messages that you write. """

# Using try-except Blocks
""" try:
 print(5/0)
except ZeroDivisionError:
 print("You can't divide by zero!") """

# Using Exceptions to Prevent Crashes
""" print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer) """

# Handling the FileNotFoundError Exception
""" filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.") """

# Analyzing Text
""" title = "Alice in Wonderland"
print(title.split()) # ['Alice', 'in', 'Wonderland'] """

""" filename = 'programming.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
 print(f"Sorry, the file {filename} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.") # The file programming.txt has about 26 words. """

# Working with Multiple Files
""" def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read() 
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filenames = ['programming.txt',  'ashwin.txt', 'text_files/pi_digits.txt']
for filename in filenames:
    count_words(filename) """

# Storing Data

# Using json.dump() and json.load()
# import json

""" numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
# we use the json.dump() function to store the list numbers in the file numbers.json """

""" filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers) """

# Saving and Reading User-Generated Data
# import json

""" username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!") """

""" filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!") """

""" filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!") """

# Refactoring
""" import json

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

greet_user() """

############################################################################################

# Testing Your Code
""" When you write a function or a class, you can also write tests for that code. Testing proves that your code works as it’s supposed to in response to all the input types it’s designed 
to receive. When you write tests, you can be confident that your code will work correctly as more people begin to use your programs. You’ll also be able to test new code as you add it to make sure your changes don’t break your program’s existing behavior. """

""" from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
 
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.") """

# Unit Tests and Test Cases
# A Passing Test
""" import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
if __name__ == '__main__':
    unittest.main() """

# A Failing Test
import unittest
from name_function import get_formatted_name2

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name2('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
if __name__ == '__main__':
    unittest.main()
