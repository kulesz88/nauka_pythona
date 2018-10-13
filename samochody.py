baza = {"volvo": 1.9,
        "kia": 7.0,
        "dodge":14.2}

while True:

    marka = raw_input("Podaj marke: ")
    podaj_km = 3000
    cena_za_litr = 5.32

    if marka in baza:
        spalanie = baza[marka]
        print("Koszt za {0} samochodem {1} to:".format(podaj_km, marka))
        print((podaj_km / 100.0) * spalanie * cena_za_litr)
        break
    else:
        print("NIe znam {0}".format(marka))
