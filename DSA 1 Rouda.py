import time  # import time module

# q1 - chocolate distribution algorithm
class Chocolate:
    """"Class to represent a Chocolate"""

    # the __init__ method initializes a Chocolate object with the specified weight, price, type, and ID
    def __init__(self, weight, price, type, ID):
        self.weight = weight
        self.price = price
        self.type = type
        self.ID = ID
        self.student = None  # assigned to none because it will store the student assigned to this chocolate


# function that distributes chocolate to students iteratively
def distribute_iteratively(chocolates_list, students_list):
    start_time = time.time()  # get the current date and time
    distribution = {}  # empty dictionary to store the distribution
    num_chocolates = len(chocolates_list)
    num_students = len(students_list)

    for i in range(num_chocolates):  # iterate over the chocolates using for loop
        chocolates_list[i].student = students_list[i]  # assign a chocolate to a student
        distribution[students_list[i]] = chocolates_list[i].type  # add chocolate type to distribution
    end_time = time.time()  # get the current date and time
    elapsed_time = end_time - start_time  # calculate the elapsed time
    return distribution, elapsed_time


# function that distributes chocolate to students recursively
def distribute_recursively(chocolates_list, students_list, index=0, distribution=None):
    if distribution == None:  # Checks if distribution is None (first call of the function).
        distribution = {}
    if index < len(students_list) and index < len(chocolates_list):  # checks if there are more students and chocolates
        chocolates_list[index].student = students_list[index]  # assigns a chocolate to a student
        distribution[students_list[index]] = chocolates_list[index].type  # adds chocolate type to the distribution
        distribute_recursively(chocolates_list, students_list, index + 1, distribution)  # calls function recursively for the next student and chocolate
    return distribution


students_list = ['Alice', 'Bob', 'John', 'Max', 'Sara']

# chocolate objects with specified attributes
chocolate_1 = Chocolate('5 gm', '2 AED', 'Almond chocolate', 2)
chocolate_2 = Chocolate('7 gm', '4 AED', 'Peanut butter chocolate', 5)
chocolate_3 = Chocolate('8 gm', '10 AED', 'White chocolate', 3)
chocolate_4 = Chocolate('6 gm', '5 AED', 'Dark chocolate', 1)
chocolate_5 = Chocolate('9 gm', '12 AED', 'Milk chocolate', 4)

chocolates_list = [chocolate_1, chocolate_2, chocolate_3, chocolate_4, chocolate_5]

iterative_distribution, iterative_elapsed_time = distribute_iteratively(chocolates_list,students_list)  # distributing chocolates to students iteratively
recursive_distribution = distribute_recursively(chocolates_list, students_list)  # distributing chocolates to students recursively

print("Iterative Distribution:", iterative_distribution)
print("Iterative Time:", iterative_elapsed_time)

# Measure the time taken by the recursive distribution
start_time = time.time()
recursive_distribution = distribute_recursively(chocolates_list, students_list)  # distributing chocolates to students recursively
end_time = time.time()
recursive_elapsed_time = end_time - start_time

# Measure the time taken by the recursive distribution
start_time = time.time()
recursive_distribution = distribute_recursively(chocolates_list, students_list)  # distributing chocolates to students recursively
end_time = time.time()
recursive_elapsed_time = end_time - start_time

print("Recursive Distribution:", recursive_distribution)
print("Recursive Time:", recursive_elapsed_time)

# q2 - sorting the chocolates
# sort chocolates by weight using insertion sort
def sort_weight(chocolates_list):  # define function, take chocolates list as input
    start_time = time.time()  # Get the current date and time
    for i in range(1, len(chocolates_list)):  # for loop iterates from second to last element
        current_chocolate = chocolates_list[i]  # gets current chocolate from chocolates_list
        position = i - 1  # initialize position to the index before the current index i

        # compare current_chocolate weight with the previous and move the heavier to the right
        # while loop that continues as long as the position is >= to 0 and the weight of the chocolate at position is greater than the current chocolate
        while position >= 0 and chocolates_list[position].weight > current_chocolate.weight:
            chocolates_list[position + 1] = chocolates_list[position]  # moves chocolate at position to the right
            position -= 1  # decrements position to move to the previous chocolate in the list
        # insert current chocolate into the correct position
        chocolates_list[position + 1] = current_chocolate

    # create a list of chocolate types sorted by weight
    sorted_chocolates_types = [chocolate.type for chocolate in chocolates_list]  # iterate over sorted list and get the 'type' attribute
    end_time = time.time()  # Get the current date and time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    return sorted_chocolates_types, elapsed_time  # Return the list of chocolates types sorted by weight and the execution time


# sorting chocolates_list based on their weights
sorted_chocolates_weight, weight_elapsed_time = sort_weight(chocolates_list)
print("List of the types of chocolates sorted by weight:", sorted_chocolates_weight)
print("Weight Execution Time:", weight_elapsed_time)

# sort chocolates by price using insertion sort
def sort_price(chocolates_list):  # define function, take chocolates list as input
    start_time = time.time()  # Get the current date and time
    for i in range(1, len(chocolates_list)):  # for loop iterates from second to last element
        current_chocolate = chocolates_list[i]  # gets current chocolate from chocolates_list
        position = i - 1  # initialize position to the index before the current index i

        # compare current_chocolate price with the previous and move the expensive to the right
        # while loop that continues as long as the position is >= to 0 and the price of the chocolate at position is greater than the current chocolate
        while position >= 0 and float(chocolates_list[position].price[:-4]) > float(current_chocolate.price[:-4]):  # compares prices after converting to float and removing 'AED' since it's string
            chocolates_list[position + 1] = chocolates_list[position]  # moves chocolate at position to the right
            position -= 1  # decrements position to move to the previous chocolate in the list
        # insert current chocolate into the correct position
        chocolates_list[position + 1] = current_chocolate

    sorted_chocolates_types = [chocolate.type for chocolate in chocolates_list]  # creates list that has types of chocolates sorted by price and iterates over sorted list and get the 'type' attribute
    end_time = time.time()  # Get the current date and time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    return sorted_chocolates_types, elapsed_time  # Return the list of chocolates types sorted by price and the execution time


# sorting chocolates_list based on their prices
sorted_chocolates_price, price_elapsed_time = sort_price(chocolates_list)
print("List of the types of chocolates sorted by price:", sorted_chocolates_price)
print("Price Execution Time:", price_elapsed_time)

# q3 - searching for a specific chocolate
# define function that takes list of the objects and price as inputs
def find_student_price(chocolates_list, price):
    start_time = time.time()  # Get the current date and time
    for chocolate in chocolates_list:  # for loop iterates over each chocolate in chocolates_list
        if chocolate.price == price:  # checks if price of current chocolate is equal to the specified price
            end_time = time.time()  # Get the current date and time
            elapsed_time = end_time - start_time  # Calculate the elapsed time
            return chocolate.student, elapsed_time  # Return the student who is holding the chocolate with the specified price and the execution time


# define function that takes list of the objects and weight as inputs
def find_student_weight(chocolates_list, weight):
    start_time = time.time()  # Get the current date and time
    for chocolate in chocolates_list:  # for loop iterates over each chocolate in chocolates_list
        if chocolate.weight == weight:  # checks if weight of current chocolate is equal to the specified weight
            end_time = time.time()  # Get the current date and time
            elapsed_time = end_time - start_time  # Calculate the elapsed time
            return chocolate.student, elapsed_time  # Return the student who is holding the chocolate with the specified weight and the execution time


price_search = '10 AED'  # sets the price to search for to '10 AED'
weight_search = '6 gm'  # sets the weight to search for to '6 gm'

student_by_price, price_time = find_student_price(chocolates_list, price_search)  # calls the find_student_price function with the chocolates_list and price_search as arguments, and assigns the result to the variable student_by_price
student_by_weight, weight_time = find_student_weight(chocolates_list, weight_search)  # calls the find_student_weight function with the chocolates_list and weight_search as arguments, and assigns the result to the variable student_by_weight
print("The student that is holding a chocolate with the price", price_search, "is", student_by_price)  # prints the student holding a chocolate with the specified price
print("The student that is holding a chocolate with the weight", weight_search, "is", student_by_weight)  # prints the student holding a chocolate with the specified weight
print("Price Execution Time:", price_time)
print("Weight Execution Time:", weight_time)
