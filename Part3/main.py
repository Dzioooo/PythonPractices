import os
import functions
import dictionaries
from panthera import Panthera


def main():
    dictionaries.object_dictionary()

    action_dictionary = {
        1: breed_first_generation_menu,
        2: print_instances,
        3: functions.instances_to_csv,
        4: exit
    }
    action = True

    while action is True:
        os.system('clear')
        print('1. Breed First Generations\n2. Print Panthera Instances'
              '\n3. Panthera Instances to CSV\n4. Exit')
        action = int(input('Choose an option: '))

        if action in action_dictionary:
            action_dictionary[action]()
            action = True
        else:
            print('Invalid selection!')


def breed_first_generation_menu():
    """
    menu for panthera breeding.
    Functions:
        object_dictionary = retrieves all female and male panthera
                            objects
        print_pantheras = prints both male and female panthera objects
        check_input = checks input from the user
        breed_pantheras = checks if the two panthera objects have the
                          same gender and also checks if the first
                          three characters of panthera names are the
                          same and then creates a new dynamic class
    """
    print('Breed First Generations')
    action = True

    while action is True:
        os.system('clear')
        dictionary = dictionaries.object_dictionary()

        functions.print_pantheras("male")
        male_panthera = functions.check_input('male')
        if male_panthera == 5:
            os.system('clear')
            main()
        else:
            # access the male panthera key-value pairs
            male_panthera = dictionary['male_pantheras'][male_panthera]

        os.system('clear')

        print(f'Selected Male Panther: {male_panthera.name}')
        functions.print_pantheras("female")
        female_panthera = functions.check_input('female')
        if female_panthera == 5:
            breed_first_generation_menu()
        else:
            female_panthera = dictionary['female_pantheras'][
                female_panthera]

            os.system('clear')
            breed_pantheras(male_panthera, female_panthera)

        while True:
            decision = input('Do you want to breed another pair?: y/n: ')

            if decision.lower() == 'y':
                breed_first_generation_menu()
            elif decision.lower() == 'n':
                action = False
                main()
            else:
                print('You have entered an invalid character!')


def breed_pantheras(male_panthera, female_panthera):
    """
    This function generates the offspring randomized gender,
    offspring name, and offspring generation from both male_panthera
    and female_panthera objects. Also creates a dynamic class for the
    panthera offspring
    Functions called:
        create_panthera = returns the generated name and randomized
                          gender
    """
    generation = None

    if (male_panthera.gender == female_panthera.gender):
        print('Cannot cross breed with the same breed!')
    elif (male_panthera.name[:3] == female_panthera.name[:3]):
        generated_name, randomized_gender = functions.create_panthera(
            male_panthera, female_panthera)
        generation = 1
    else:
        generated_name, randomized_gender = functions.create_panthera(
            male_panthera, female_panthera)
        generation = 2

    class_attributes = {
        'name': generated_name,
        'generation': generation,
        'gender': randomized_gender
    }
    os.system('clear')
    bred_panthera_class = generated_name

    print(f'{male_panthera.name} + {female_panthera.name} = '
          f'{generated_name}')

    BredPanthera = type(bred_panthera_class, (Panthera,), class_attributes)
    bred_panthera = BredPanthera(generated_name, generation, randomized_gender)

    print(bred_panthera)
    print(bred_panthera.__class__.__name__)
    print(bred_panthera.__class__)
    print(type(bred_panthera))


def print_instances():
    """
    Prints all the instances of Panthera objects
    """
    os.system('clear')
    panthera_instances = Panthera.sorted_instances()
    for instance in panthera_instances:
        print(f'{instance.name} : {instance.generation}', end=", ")
    get_input = None
    while True:
        get_input = input('\nPress the "e" key to exit.')
        if get_input == 'e':
            main()
            break
        else:
            print('Invalid input!')


if __name__ == '__main__':
    main()
