# Refer to the README.md file in this project for a description 
# of the challenge and requirements. When viewing the README.md, 
# replit will show an option to Open Preview, which will open a 
# more readable view.

# The Python module math is imported and available to use but not required.
# Please do not import any additional modules (such as NumPy).

import math

def bubble_tea_calculator(tea_base, add_ons, loyalty_discount):
    # Place your implementation for bubble_tea_calculator here, 
    # after removing this comment, and the pass statement.
  #  pass

  # creating tea base dictionary to access values for each tea base (key)
  tea_base_dictionary = {
    "milk" : 4.35,
    "oolong" : 4.60,
    "rose" : 5.85,
    "mango" : 5.47
  }

  # creating add ons dictionary
  add_ons_dictionary = {
    "boba" : 0.50,
    "lychee" : 0.75,
    "jelly" : 0.65,
    "taro" : 1.00,
    "chia" : 0.35
  }

  # creating a total variable to change later when making calculations
  total = 0

  # accessing tea base dict
  if tea_base.lower() in tea_base_dictionary:
    total += tea_base_dictionary[tea_base.lower()]
  # user needs to input an offered tea base
  else: 
    print ("Sorry that tea base is unavailable. We have milk, oolong, rose, and mango.")
    # there will be no loyalty discount needed in this scenario
    return False

  # accessing add ons dictionary using a for loop
  # Loop through both keys and values, by using the items() method
  for key,value in add_ons_dictionary.items():
    for item in add_ons:
      if item.lower() == key:
        total += value

  #applying loyalty discount if True
  if loyalty_discount:
    total -= 1.00
   #interviewer requested to change discount to 15% off order
#  if loyalty_discount:
#    total *= 0.85

  #output and making sure there are two decimals because $
  print("The cost is $" + str(format(total, '.2f')))
  return
# You may call bubble_tea_calculator with your own arguments here.
# For example, if the following line is uncommented, and the Run button
# is clicked, it will call bubble_tea_calculator with the listed
# parameters. The supplied example uses the same arguments as the
# test Challenge01.
    
# bubble_tea_calculator("Milk", ["Boba", "Jelly", "taro"], True)

#using existing bubble tea calculator, function with calculate the order based on the following dictionary
#def calculate_total(order): 
#  bubble_tea_calculator(order["tea"], order["add_ons"], order["loyalty_discount_card"])
#  return
# interviewer provided following dictionary to use with bubble tea calculator
#order = {
# "tea": "Oolong",
# "add_ons": ["chia"],
# "loyalty_discount_card": True
# }
 
#calculate_total(order)

# should still print the cost

# The challenges are provided as a set of tests that can be run 
# from the Tests panel at the left (the icon looks like a check 
# mark). Clicking the Run tests button will run the Challenge 
# inputs against your code, displaying either a success message, 
# or a message about what was expected and what was observed.
