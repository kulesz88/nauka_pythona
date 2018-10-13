baza = {"unibike": 4000.00,
        "romet": 1890.21,
        "skladak":699.99}
raty = [2, 6, 12]
while True:

    marka = raw_input("Podaj marke roweru: ")
    ilosc_rat = int(raw_input("Podaj liczbe rat: "))
    oprocentowanie = 14.0

    if marka in baza and ilosc_rat in raty:
        cena = baza[marka]
        print("Ilosc rat {1} i rata mieseczna za rower {0} to: ".format(marka, ilosc_rat))
        print(cena / ilosc_rat) * (oprocentowanie/12)
        break
    else:
        print("Nie znam roweru {0}".format(marka))
