from panthera import Panthera
import random
import dictionaries
import csv


def check_input(gender):
    user_input = None

    while user_input is None or user_input != 5:
        try:
            user_input = int(input(f'Choose {gender.upper()} Panthera: '))
            if user_input in (1, 2, 3, 4, 5):
                return user_input
            else:
                raise ValueError('Invalid input! Please enter a valid input'
                                 '(1, 2, 3, 4, 5)')
        except ValueError as e:
            print(e)


def create_panthera(male_panthera, female_panthera):
    random_gender = [male_panthera.gender, female_panthera.gender]
    randomized_gender = random.choice(random_gender)

    if randomized_gender.lower() == male_panthera.gender.lower():
        generated_name = dictionaries.male_names(
            male_panthera.name, female_panthera.name)
        return generated_name, randomized_gender
    else:
        generated_name = dictionaries.female_names(
            male_panthera.name, female_panthera.name)
        return generated_name, randomized_gender


def instances_to_csv():
    csv_file_path = 'Part3/panthera_breeds.csv'
    panthera_instances = Panthera.sorted_instances()

    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        header = 'name', 'generation', 'gender'

        writer.writerow(header)
        for instance in panthera_instances:
            writer.writerow((instance.name, instance.generation,
                            instance.gender))


def print_pantheras(gender):
    dictionary = dictionaries.object_dictionary()

    if gender == "male":
        for key, value in dictionary['male_pantheras'].items():
            if isinstance(value, Panthera):
                print(f"{key}. {value.name}")
    else:
        for key, value in dictionary['female_pantheras'].items():
            if isinstance(value, Panthera):
                print(f"{key}. {value.name}")
    print('5. Exit')
