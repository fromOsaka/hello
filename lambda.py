class_of_people = [
    {'name':'Harry', 'house':"Gryff"},
    {"name":"Cho","house":"Revenclaw"}
        ] 
def f(class_of_people):
    return class_of_people['house']


class_of_people.sort(key=f)

print(class_of_people)
