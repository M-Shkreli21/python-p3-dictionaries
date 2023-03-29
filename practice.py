def pour_coffee(size):
    size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20
    }
    print(size_to_ounce_map.get(size, "Please enter a valid cup size"))

pour_coffee("Jumbo")

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

[item for item in my_dict.items()]
[key for key, value in my_dict.items()]
[value for key, value in my_dict.items()]