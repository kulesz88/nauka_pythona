baza = {"unibike": 4000.00,
        "romet": 1890.21,
        "skladak":699.99}
def print_dict(d):
    for key in baza:
        print("{0}:{1}".format(key, d[key]))

if __name__ == "__main__":
    baza = {"unibike": 4000.00,
            "romet": 1890.21,
            "skladak":699.99}

print_dict(baza)
