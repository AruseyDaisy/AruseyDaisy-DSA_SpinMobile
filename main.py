# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_items(n):
    # Use a breakpoint in the code line below to debug your script.
    for i in range(1,n):
        for j in range(n):
            print(i,j)  # Press F9 to toggle the breakpoint.
def multiply(a,b=2):
    return a*b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''num_1 = 11
    num_2 = num_1

    print("Before num2 value is updated:")
    print("num1 = ", num_1)
    print("num2 = ",num_2)

    print("\nnum1 points to:", id(num_1))
    print("num2 points to:", id(num_2))

    num_2 = 22

    print("After num2 value is updated:")
    print("num1 = ", num_1)
    print("num2 = ", num_2)

    print("\nnum1 points to:", id(num_1))
    print("num2 points to:", id(num_2))
    '''

    dict1 = {'value': 11}
    dict2 = dict1

    print("Before dict1 value is updated:")
    print("dict1 = ", dict1)
    print("dict2 = ",dict2)

    print("dict1 points to:", id(dict1))
    print("dict2 points to:", id(dict2))

    dict2['value'] = 22
    print("\nAfter dict2 value is updated:")
    print("dict1 = ", dict1)
    print("dict2 = ",dict2)
    print("dict1 points to:", id(dict1))
    print("dict2 points to:", id(dict2))







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
