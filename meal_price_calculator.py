"""
        Madison Rollins
        Meal Price Caclculator

        Ask the user for the following:
            The price of a child's meal (floating point)
            The price of an adult's meal (floating point)
            The number of children (integer)
            The number of adults (integer)
        Then, complete the following steps:
            Determine the meal's subtotal (before adding sales tax) by multiplying
            the number of children by the price of their meal and multiplying the number 
            of adults by the price of their meal and adding those two values together.
        Display the subtotal.
"""
# title
print('Meal Price Calculator')
print()
print()
print('-----------')
#input info
print('Please Submit the Following:')
print()
child_meal = input('Price of childs meal:')
print()
adult_meal = input('Price of adult meal:')
print()
child_num = input('Number of children:')
print()
adult_num = input('Number of Adults:')
#math :)
child_price = (float(child_meal) * int(child_num))
adult_price = (float(adult_meal) * int(adult_num))
#subtotal
subtotal = (float(child_price) + float(adult_price))
print()
print('-----------')
#sub- print
print(f'The Subtotal is {subtotal}')
