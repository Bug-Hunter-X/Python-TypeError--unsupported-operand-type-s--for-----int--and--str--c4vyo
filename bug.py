def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") # this will print 0 which is correct

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}") # this will print 30.0 which is correct

my_list = [10, 20, 30, 40, 50, 'a']
average = calculate_average(my_list) 
print(f"The average is: {average}") # this will throw TypeError: unsupported operand type(s) for +: 'int' and 'str'