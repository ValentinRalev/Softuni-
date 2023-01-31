def age_assignment(*args, **kwargs):
    my_dict = {}
    for name in args:
        my_dict[name] = kwargs[name[0]]
    return my_dict



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))