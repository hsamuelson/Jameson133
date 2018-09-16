from Person import Person
from Elevator import Elevator


e = Elevator(6)
p = Person(1, 4)
p1 = Person(3, 5)

e.add_people_to_floor(4, 1)
e.floor_change_up()
e.floor_change_up()
e.remove_people_from_ele(2)
e.floor_change_down()
e.floor_change_down()
print(e.get_ele_list())
print(e.get_total_time())


