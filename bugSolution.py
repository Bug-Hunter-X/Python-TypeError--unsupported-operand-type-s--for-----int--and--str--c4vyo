def calculate_average(numbers):
    if not numbers:
        return 0
    for number in numbers:
        if not isinstance(number,(int,float)):
            raise TypeError("List must contain only numbers")
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [10, 20, 30, 40, 50, 'a']
try:
    average = calculate_average(my_list) 
    print(f"The average is: {average}")
except TypeError as e:
    print(f"Error: {e}")