if __name__ == '__main__':
    my_dictionary = {"name": "John",
                     "age": 25}

    my_dictionary = dict (name="John",
                          age=25)

    my_dictionary["age"] = 26
    print(my_dictionary['age'])

    students = [
        {"name": "John", "grades": (90, 85, 88)},
        {"name": "Jane", "grades": [90, 85, 88]}
    ]
    print(students[0]['grades'][1])

