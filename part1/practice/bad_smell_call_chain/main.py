# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self, get_person_room, get_city_population):
        self.get_person_room = get_person_room
        self.get_citi_population = get_city_population

    def get_room(self):
        return self.get_person_room

    def get_population(self):
        return self.get_citi_population

# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.
