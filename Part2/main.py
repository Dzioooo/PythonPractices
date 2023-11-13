import os
import math
import json
import csv


def main():
    decision = None
    os.system("clear")

    actions = {
        "1": mathematical_operations,
        "2": area_of_a_circle,
        "3": area_of_a_shape,
        "4": show_gender,
        "5": json_to_csv,
        "6": mathematical_operations,
        "7": exit
    }

    while decision is None or decision != 7:
        print("1.Mathematical Operations\n2.Area of a Circle\n3.Shape's Area\n"
              "4.Male - Female\n5.JSON to CSV and Keyword Arguments\n"
              "6.Bonus Question\n7.Exit")

        decision = input("Choose a number from 1-7: ")

        if decision in actions:
            os.system("clear")
            actions[decision]()
        else:
            print("Invalid input! Please enter a valid option (1-7).")
    

def mathematical_operations():
    decision = None
    check_input = False

    while check_input is False:
        try:
            print("a - Addition\nb - Subtraction\nc - Multiplication\n"
                  "d - Division\ne - Exit")
            decision = input("Please select an operation ").lower()

            if decision not in ("a", "b", "c", "d", "e"):
                check_input = False
                raise ValueError("Invalid input! Please enter a valid"
                                 "option (a, b, c, d, e)")

            if decision == "e":
                main()

            print("Enter num1: ", end="")
            num1 = num_input()
            print("Enter num2: ", end="")
            num2 = num_input()

            result = perform_operations(operation=decision, num1=num1,
                                        num2=num2)
            os.system("clear")
            print(f"{num1} + {num2} = {result}")
        except Exception as e:
            check_input = False
            os.system("clear")
            print(e)


def perform_operations(operation, num1, num2):
    if operation == "a":
        return num1 + num2
    elif operation == "b":
        return num1 - num2
    elif operation == "c":
        return num1 * num2
    elif operation == "d":
        return num1 / num2


def num_input():
    check_input = False

    while check_input is False:
        try:
            num = int(input())
            check_input = True
        except ValueError as e:
            print("Input must be a number!")
            print(e)
            check_input = False

    return num


def area_of_a_circle():
    '''
    instantiates the Circle class with a new object and calls
    the compute_area method of the Circle class which computes the
    area of the circle
    '''
    circle = Circle(8)
    print(f"Area is: {circle.compute_area()}")


def area_of_a_shape():
    shape = Shape()
    square = Square(7)

    print("Area: ", shape.compute_area())
    print("Area: ", square.compute_area())


def show_gender():
    '''
    FUnction that intializes male and female objects from the Male and
    Female subclasses and calls their respective methods.
    '''
    male = Male()
    female = Female()

    male.get_gender()
    female.get_gender()


def json_to_csv():
    ''' converts input.json file to .csv file'''
    file_name = "Part2/input.json"
    csv_file_path = "Part2/csv_file.csv"
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)

    json_data = data['tracking_events']
    csv_file = open(csv_file_path, 'w')

    csv_writer = csv.writer(csv_file)

    get_all_keys = []    # collects all keys from the json file

    ''' collects all the keys from input.json '''
    for json_element in json_data:
        for key in json_element.keys():
            if key not in get_all_keys:
                get_all_keys.append(key)

    csv_writer.writerow(get_all_keys)

    ''' writes all the rows from input.json '''
    for json_element in json_data:
        csv_writer.writerow([json_element.get(key, "") for key in
                            get_all_keys])

    csv_file.close()


class Circle():
    '''
    Constructor/s:
        radius - initializes a new Circle object with the given radius
    Method/s:
        compute_area - computes and returns the area of a circle
    '''
    def __init__(self, r):
        self.radius = r

    def compute_area(self):
        '''
        Computes and returns the area of a circle with a type of float
        '''
        return math.pow(self.radius, 2) * math.pi


class Shape():
    '''
    Constructor/s:
        none
    Method/s:
        compute_area - returns a default of zero
    '''
    def __init__(self):
        pass

    def compute_area(self):
        '''
        returns a default value of zero
        '''
        return 0


class Square(Shape):
    '''
    A subclass of Shape Class
    Constructor/s:
        length - initializes a new Square object with the given length
    Method/s:
        compute_area - computes and returns the area of a square
    '''
    def __init__(self, length):
        super().__init__()
        self.length = length

    def compute_area(self):
        return math.pow(self.length, 2)


class Person():
    '''
    Parent class of both Male and Female subclasses
    '''
    def __init__(self):
        pass

    def get_gender(self):
        pass


class Male(Person):
    '''
    Subclass of Person Class, prints "Male" if its method is called
    by the object.
    '''
    def __init__(self):
        super().__init__()

    def get_gender(self):
        print("Male")


class Female(Person):
    '''
    Subclass of Person Class, prints "Male" if its method is called
    by the object.
    '''
    def __init__(self):
        super().__init__()

    def get_gender(self):
        print("Female")


main()
