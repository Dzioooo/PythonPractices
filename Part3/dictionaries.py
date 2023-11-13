from panthera import Lion, Tiger, Leopard, Jaguar


def male_names(male_panthera, female_panthera):
    return {
        ('Tiger', 'Tigress'): 'Tiger',
        ('Tiger', 'Lioness'): 'Tigon',
        ('Tiger', 'Jaguaress'): 'Tiguar',
        ('Tiger', 'Leopardess'): 'Tigard',
        ('Lion', 'Tigress'): 'Liger',
        ('Lion', 'Lioness'): 'Lion',
        ('Lion', 'Jaguaress'): 'Liguar',
        ('Lion', 'Leopardess'): 'Lipard',
        ('Jaguar', 'Tigress'): 'Jagger',
        ('Jaguar', 'Lioness'): 'Jaglion',
        ('Jaguar', 'Jaguaress'): 'Jaguar',
        ('Jaguar', 'Leopardess'): 'Jagupard',
        ('Leopard', 'Tigress'): 'Leoger',
        ('Leopard', 'Lioness'): 'Leopon',
        ('Leopard', 'Jaguaress'): 'Leguar',
        ('Leopard', 'Leopardess'): 'Leopard'
    }.get((male_panthera, female_panthera))


def female_names(male_panthera, female_panthera):
    return {
        ('Tiger', 'Tigress'): 'Tigress',
        ('Tiger', 'Lioness'): 'Tigoness',
        ('Tiger', 'Jaguaress'): 'Tiguaress',
        ('Tiger', 'Leopardess'): 'Tigardess',
        ('Lion', 'Tigress'): 'Ligress',
        ('Lion', 'Lioness'): 'Lioness',
        ('Lion', 'Jaguaress'): 'Liguaress',
        ('Lion', 'Leopardess'): 'Lipardess',
        ('Jaguar', 'Tigress'): 'Jaggress',
        ('Jaguar', 'Lioness'): 'Jaglioness',
        ('Jaguar', 'Jaguaress'): 'Jaguaress',
        ('Jaguar', 'Leopardess'): 'Jagupardess',
        ('Leopard', 'Tigress'): 'Leogress',
        ('Leopard', 'Lioness'): 'Leoponess',
        ('Leopard', 'Jaguaress'): 'Leguaress',
        ('Leopard', 'Leopardess'): 'Leopardess'
    }.get((male_panthera, female_panthera))


def object_dictionary():
    ''' initialization of Female Panthera Class Objects since
    male pantheras are already a subclass of Panthera class in
    Panthera.py
    '''

    lioness = Lion('Lioness', 1, 'Female')
    tigress = Tiger('Tigress', 1, 'Female')
    jaguaress = Jaguar('Jaguaress', 1, 'Female')
    leopardess = Leopard('Leopardess', 1, 'Female')

    ''' Initialization of Male Panthera Subclass Objects
        (subclass of Panthera class in panthera.py)
    '''
    lion = Lion('Lion', 1, 'Male')
    tiger = Tiger('Tiger', 1, 'Male')
    jaguar = Jaguar('Jaguar', 1, 'Male')
    leopard = Leopard('Leopard', 1, 'Male')

    ''' Dictionary for Female and Male Pantheras '''
    female_pantheras = {
        1: lioness,
        2: tigress,
        3: jaguaress,
        4: leopardess,
    }

    male_pantheras = {
        1: lion,
        2: tiger,
        3: jaguar,
        4: leopard,
    }

    return {'female_pantheras': female_pantheras,
            'male_pantheras': male_pantheras}
