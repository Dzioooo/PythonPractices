import csv
import os

def main():
    decision = None
    os.system("clear")
    
    while decision is not "11":
        print ("1.Reverse Tuple\n2.Print Even Numbers\n3.Fibonacci Sequence"
               "\n4.Cube Numbers\n5.Default Parameters and Keyword Arguments\n"
               "6.Write to CSV\n7.Read From CSV\n8.Inverted Dictionary\n9.List" 
               " Comprehension\n10.Palindrome\n11.Exit")
        decision = input("Choose a number from 1-10: ")
        match decision:
            case "1":
                os.system("clear")
                reverse_tuple()
            case "2":
                os.system("clear")
                even_num(min=2,max=10)
            case "3":
                os.system("clear")
                fibonacci(5)
            case "4":
                os.system("clear")
                cube_numbers()
            case "5":
                os.system("clear")
                default_parameters_keyword_arguments("HX0001")
                default_parameters_keyword_arguments("HX0001", 
                                                     client="ETarget")
                default_parameters_keyword_arguments("HX0001", 
                                                     client="ETarget", 
                                                     courier="Yodel")
            case "6":
                os.system("clear")
                write_to_csv(name="Kiko", age="22")
                write_to_csv(name="Joelle", age="18")
                write_to_csv(name="Ray", age="23")
            case "7":
                os.system("clear")
                read_from_csv("trainee.csv")
            case "8":
                os.system("clear")
                dictionary()
            case "9":
                os.system("clear")
                list_comprehension()
            case "10":
                os.system("clear")
                is_palindrome("racecar")

def reverse_tuple():
    exit_key = None
    tuple_input = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tuple_output = tuple_input[::-1]
    print(tuple_output)

    while exit_key is None:    
        exit_key = input("Enter any key to continue. ")
    os.system("clear")

def even_num(max, min):
    exit_key = None
    result = []
    for i in range(min, max + 1):
        if i % 2 == 0:
            result.append(str(i))
    str_num = ", ".join(result)
    print(str_num)
    while exit_key is None:
        exit_key = input("Enter any key to continue")
    os.system("clear")

def fibonacci(num):
    first_num = 0
    second_num = 1
    result = []
    exit_key = None

    while first_num <= num:
            result.append(str(first_num)) #0 #1
            temp_num = first_num + second_num #0 + 1 = 1, 1 + 1 = 2
            first_num = second_num #1
            second_num = temp_num #1

    str_num = ", ".join(result)
    print(str_num)

    while exit_key is None:    
        exit_key = input("Enter any key to continue. ")
    os.system("clear")

def cube_numbers():
    exit_key = None
    num_list = [1, 2, 3, 4, 5]
    cubed_numb = list(map(lambda num: num**3, num_list))
    print(cubed_numb)

    while exit_key is None:    
        exit_key = input("Enter any key to continue. ")
    os.system("clear")

def default_parameters_keyword_arguments(code, client=None, courier=None):
    exit_key = None
    if courier is None:
        print(code, client)
    elif client is None:
        print(code, courier)
    else:
        print(f'{code}, {client}, {courier}')
    
    while exit_key is None:    
        exit_key = input("Enter any key to continue. ")
    os.system("clear")

def write_to_csv(name, age):
    exit_key = None
    with open('trainee.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        header = 'name', 'age'

        writer.writerow(header)
        writer.writerow((name, age))

    while exit_key is None:    
        exit_key = input("Enter any key to continue. ")
    os.system("clear")

def read_from_csv(file_name):
    exit_key = None
    data = []

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
        
        for row in data:
            print(row)

    while exit_key is None:    
        exit_key = input("Enter any key to continue. ")
    os.system("clear")

def invert(dictionary):
    # your logic here
    dictionary = {key: len(dictionary) - value + 1 for key, value in 
                  sorted(dictionary.items())}
    return dictionary

def dictionary():
    exit_key = None
    my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
    inverted_dict = invert(my_dict)
    print(inverted_dict) # should be { 'a': 4, 'b': 3, 'c': 2, 'd': 1 }


    my_other_dict = { 'a': 1, 'b': 2, 'c': 3 }
    inverted_other_dict = invert(my_other_dict)
    print(inverted_other_dict) # should be { 'a': 3, 'b': 2, 'c': 1 }

    while exit_key is None:    
        exit_key = input("Enter any key to continue. ")
    os.system("clear")

def list_comprehension():
    exit_key = None
    list1=['a', 'b']
    list2=['b', 'c', 'd']

    combined_list = [x + y for x in list1 for y in list2]
    print(combined_list)

    while exit_key is None:    
        exit_key = input("Enter any key to continue. ")
    os.system("clear")

def is_palindrome(str):
    exit_key = None
    str = str.replace(" ", "").lower()

    if (str == str[::-1]):
        print(True)
    else:
        print(False)

    while exit_key is None:    
        exit_key = input("Enter any key to continue. ")
    os.system("clear")

os.system("clear")
main()

