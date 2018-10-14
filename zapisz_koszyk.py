def zapisz_koszyk():
    koszyk = [
        {"nazwa": "blok", "cena": 2.00},
        {"nazwa": "kredki", "cena": 5.30},
        {"nazwa": "plastelina", "cena": 4.99},
        {"nazwa": "zeszyt", "cena": 1.79},
        {"nazwa": "czasopismo", "cena": 8.50},
        ]

    file = open ("zapisz_koszyk.csv", "w")
    for poz in koszyk:
        linia = "{0},{1}\n".format(poz["nazwa"], poz["cena"])
        file.write(linia)
    file.close()

if __name__ == "__main__":
    zapisz_koszyk()
