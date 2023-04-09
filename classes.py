class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(2,8)
#print(p.x)
#print(p.y)

class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

guys = ["Harry", "Mary", "Ron",'Andrian']
flight = Flight(2)
for person in guys:
    secces = flight.add_passenger(person)
    if secces:
        print(f'We added {person} to Flight')
    else:
        print(f"Sorry, mr/ms {person}, not today")
