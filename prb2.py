def print_depth(data, dep):
    if isinstance(data, dict):
        for key, value in data.items():
            print(str(key) + " " + str(dep))
            if isinstance(value, dict):
                print_depth(value, dep+1)
            elif isinstance(value, Person):
                print_depth(value, dep+1)
    elif isinstance(data, Person):
        print("first_name " + str(dep))
        print("last_name " + str(dep))
        print("father " + str(dep))
        if isinstance(data.father, Person):
            print_depth(data.father, dep+1)

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person("User", "1", "none")
person_b = Person("User", "2", person_a)

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b,
        }
    },
}

# print(a)
print_depth(a, 1)
