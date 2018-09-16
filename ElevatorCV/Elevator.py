from Person import Person


class Elevator:

    def __init__(self, floors):
        self._current_floor = 1
        self.ele_list = []
        self.create_list(floors)

    #creates 2d list of floors. column 0 describes the total time spent on the floor, column 1 describes the num of people
    #currently on that floor in the elevator
    def create_list(self, floors):
        for i in range(0, floors):
            self.ele_list.append([0,0])
        #print(self.ele_list)

    #Changes floor that the elevator is in. keeps track of all the people in the elevator and multiplies that value by
    #5 to find the number of time units. time is stored in the index associated with the destination. make sure that the
    #index pointing to floor is accurate. index 0 points to floor 1, etc.
    #make sure to move the number of people from one floor to the next when changing floors.
    #Precondition: arg cannot be larger than the number of floors or a negative number
    def floor_change_up(self):
        self.ele_list[self._current_floor][1] = self.ele_list[self._current_floor-1][1] #index num is weird but sets to correct value
        self.ele_list[self._current_floor-1][1] = 0
        self.ele_list[self._current_floor][0] += self.ele_list[self._current_floor][1] * 5
        self._current_floor += 1

    def floor_change_down(self):
        self.ele_list[self._current_floor - 2][1] = self.ele_list[self._current_floor-1][1]
        self.ele_list[self._current_floor - 1][1] = 0
        self.ele_list[self._current_floor - 2][0] += self.ele_list[self._current_floor-2][1] * 5
        self._current_floor -= 1

    def add_people_to_floor(self, num_people, floor):
        self.ele_list[floor-1][1] = num_people

    def remove_people_from_ele(self, num_people):
        self.ele_list[self._current_floor-1][1] -= num_people
        self.ele_list[self._current_floor-1][0] += 10

    def get_total_time(self):
        time = 0
        for i in range(0, len(self.ele_list)):
            time += self.ele_list[i][0]
        return time

    def get_ele_list(self):
        return self.ele_list

    # def set_floor_people(self):
    def get_current_floor(self):
        return self._current_floor
