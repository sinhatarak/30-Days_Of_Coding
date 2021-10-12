'''
First day (start date: 11-Oct-2021)

https://www.teclado.com/30-days-of-python/python-30-day-1-exercise-solutions

#1) Print your age to the console.
# print("36")
# 2) Calculate and print the number of days, weeks, and months in 27 years.
print(27 * 365, "Days in 27 Years")
print(27 * 52, "Weeks in 27 Years")
print(27 * 12, "Months in 27 Years")
'''
#3) Calculate and print the area of a circle with a radius of 5 units.

# print(3.141 ** 5)

# Questions 

# Reverse a string not using any pre-built method.

# 1) solution
# a = 'Python'

deck_cards = [0,100,21,322,4,8,10]
query = 21
pos = 0

while True:
  if query in deck_cards and query == deck_cards[pos]:
     print("found it", pos)
     break
  pos+=1














