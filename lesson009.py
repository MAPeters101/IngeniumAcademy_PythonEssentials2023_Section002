if __name__ == '__main__':
    my_set = {1, 2, 3, 4, 5, 5, 5}
    print(my_set)

    # Adding elements
    my_set.add(6)
    print(my_set)
    my_set.update([7, 8])
    print(my_set)

    my_set.remove(8) # raises error if element is not present
    my_set.discard(10) # Does not raise error if element is not present
    print(my_set)



