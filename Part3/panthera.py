class Panthera():
    all_instance = []
    female_instance = []
    male_instance = []

    def __init__(self, name, generation, gender):
        self.name = name
        self.generation = generation
        self.gender = gender
        self.check_instances()
        # self.check_instance_gender()

    def check_instances(self):
        if not any(instance.name == self.name for
                   instance in Panthera.all_instance):
            Panthera.all_instance.append(self)

    def check_instance_gender(self):
        """
        disregard this function, this function is supposedly for the
        bonus item
        """
        if self.gender == "Male" and not any(instance.name == self.name for
                                             instance in
                                             Panthera.male_instance):
            Panthera.male_instance.append(self)
        elif self.gender == "Female" and not any(instance.name == self.name for
                                                 instance in
                                                 Panthera.female_instance):
            Panthera.female_instance.append(self)

    def __lt__(self, other):
        if isinstance(other, Panthera):
            return (self.generation, self.name) < (other.generation,
                                                   other.name)

    @classmethod
    def sorted_instances(cls):
        sorted_instances = sorted(cls.all_instance)
        return sorted_instances

    @classmethod
    def male_instances(cls):
        """
        disregard this function, this function is supposedly for the
        bonus item
        """
        return cls.male_instance

    @classmethod
    def female_instances(cls):
        """
        disregard this function, this function is supposedly for the
        bonus item
        """
        return cls.female_instance


class Tiger(Panthera):
    def __init__(self, name, gender, generation):
        super().__init__(name, gender, generation)

    def show_details(self):
        print(self.name, self.generation, self.gender)


class Lion(Panthera):
    def __init__(self, name, gender, generation):
        super().__init__(name, gender, generation)

    def show_details(self):
        print(self.name, self.generation, self.gender)


class Jaguar(Panthera):
    def __init__(self, name, gender, generation):
        super().__init__(name, gender, generation)

    def show_details(self):
        print(self.name, self.generation, self.gender)


class Leopard(Panthera):
    def __init__(self, name, gender, generation):
        super().__init__(name, gender, generation)

    def show_details(self):
        print(self.name, self.generation, self.gender)
