def main():
    koszyk = [
        {"nazwa": "blok", "cena": 2.00},
        {"nazwa": "kredki", "cena": 5.30},
        {"nazwa": "plastelina", "cena": 4.99},
        {"nazwa": "zeszyt", "cena": 1.79},
        {"nazwa": "czasopismo", "cena": 8.50},
        ]

    total_cena = 0.00

    for k in koszyk:
        total_cena = total_cena + k['cena']

    print("Total cena {0}zl".format(total_cena))

    file = open ("koszyk.csv", "w")
    file.write(str("Total cena;{0}".format(total_cena)))
    file.close()



if __name__ == "__main__":
    main()
