def print_depth(data, dep):
    for key, value in data.items():
        print(str(key) + " " + str(dep))
        if isinstance(value, dict):
            print_depth(value, dep+1)

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}

print_depth(a, 1)
