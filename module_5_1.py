class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        for i in range(int(new_floor)):
            if 0 < int(new_floor) and int(new_floor) <= int(self.number_of_floors):
                print(i+1)
            else:
                print("Такого этажа не существует.")
                break

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)

