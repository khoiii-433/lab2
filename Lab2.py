
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    
    number_strings = user_input.split(",")

    numbers = []
    for num in number_strings:
        numbers.append(float(num.strip()))

    return numbers

def calc_average_temperature(temperature_list):
    total = 0

    for temp in temperature_list:
        total += temp

    average = total / len(temperature_list)
    return average

def calc_min_max_temperature(temperature_list):
    min_temp = min(temperature_list)
    max_temp = max(temperature_list)

    return [min_temp, max_temp]

def sort_temperature(temperature_list):
    sorted_list = sorted(temperature_list)
    return sorted_list

def calc_median_temperature(temperature_list):
    
display_main_menu()

temperatures = get_user_input()

average = calc_average_temperature(temperatures)
min_max = calc_min_max_temperature(temperatures)
sorted_temps = sort_temperature(temperatures)

print("Average:", average)
print("Min and Max:", min_max)
print("Sorted list:", sorted_temps)
