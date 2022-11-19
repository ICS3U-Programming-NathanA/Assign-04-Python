#!/usr/bin/env python3

# Created By: Nathan A
# Date: Nov. 15, 2022
# This program asks the user for 2 numbers, it then calculates the lowest common multiple


def main():

    # set the counter to 1
    counter = 1
    # Makes a list that will contain the numbers
    list_product = []
    list_product_2 = []
    list_lowest_num = []

    # Gets the first integer
    user_num_one_str = input("Enter a integer: ")

    # Gets the second integer
    user_num_two_str = input("Enter another integer: ")

    # Try catch to catch any inputted strings or decimals
    try:
        user_num_one_int = int(user_num_one_str)
        user_num_two_int = int(user_num_two_str)
    except:
        print("You must enter a valid integer.")
    else:
        # If statement to see if user_num_one_int is greater than user_num_two_int
        if user_num_one_int > user_num_two_int:
            # sets the greatest_num to user_num_one_int
            greatest_num = user_num_one_int
        else:
            # sets the greatest_num to user_num_two_int
            greatest_num = user_num_two_int
        # Adds 1 to the greatest_num
        greatest_num = greatest_num + 1
        # If statement to see if the integer the user entered is positive
        if user_num_one_int > 0 and user_num_two_int > 0:
            # for loop to calculate the product of all of the numbers times the counter until the counter reaches the greatest_num
            for counter in range(greatest_num):
                product_2 = user_num_two_int * counter
                # Adds each product to the list_product_2
                list_product_2.append(product_2)
                # If statement to see if any of the numbers in the two lists have the same numbers
                if product_2 in list_product:
                    # puts all the same numbers in a new list called list_lowest_num
                    list_lowest_num.append(product_2)
                    # selects the lowest out of the list_lowest_num
                    lcm = min(list_lowest_num)
                # while loop to repeat every time the counter is less than the greatest_num
                while counter < greatest_num:
                    product = user_num_one_int * counter
                    # puts all the products into list_product
                    list_product.append(product)
                    # Adds 1 to the counter
                    counter = counter + 1
            # displays the final result
            print("The lowest common multiple is of {} and {} is {}".format(user_num_two_int, user_num_one_int, lcm))
        else:
            print("Enter a positive integer")


if __name__ == "__main__":
    main()
