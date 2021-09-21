import addition
import subtraction
import multiplication
import division

print("1 : Addition")
print("2 : Subtraction")
print("3 : Multiplication")
print("4 : Division")
user_calculation_choice = int(input("Please select an option for the calculation : "))
user_num_one = int(input("Please enter your first number : "))
user_num_two = int(input("Please enter your second number : "))
if (user_calculation_choice == 1):
    result = addition.add_calculation(user_num_one, user_num_two)
elif(user_calculation_choice == 2):
    result = subtraction.subtract_calculation(user_num_one, user_num_two)
elif(user_calculation_choice == 3):
    result = multiplication.multiply_calculation(user_num_one, user_num_two)
elif(user_calculation_choice == 4):
    result = division.divide_calculation(user_num_one, user_num_two)
print("Your result is : " +str(result))



