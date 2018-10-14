def main():
    d = [
        {'nazwa':'banany', 'id': 1, 'waga': 10, 'ilosc': 4, 'cena': 8.10, 'toxic': True},
        {'nazwa':'mleko', 'id': 2, 'waga': 5, 'ilosc': 20, 'cena': 2.20, 'toxic': True},
        {'nazwa':'karma', 'id': 82, 'waga': 25, 'ilosc': 41, 'cena': 42},
        {'nazwa':'ser', 'id': 4, 'waga': 1, 'ilosc': 32, 'cena': 28},
        {'nazwa':'pomidory', 'id': 8, 'waga': 2, 'ilosc': 12, 'cena': 5.21, 'toxic': True},
        {'nazwa':'cukierki', 'id': 24, 'waga': 1, 'ilosc': 17, 'cena': 14.21},
        {'nazwa':'czekoloda', 'id': 54, 'waga': 0.5, 'ilosc': 19, 'cena': 21.10,'toxic': False},
        {'nazwa':'zabawki', 'id': 81, 'waga': 1.2, 'ilosc': 21, 'cena': 100},
        ]
    total_toxic = 0
    total_nottoxic = 0

    for towar in d:
        if 'toxic' in towar:
            if towar["toxic"] == True:
                total_toxic = total_toxic + 1
                print(towar)

    for towar in d:
        if 'toxic' in towar:
            if towar["toxic"] == False:
                total_nottoxic = total_nottoxic + 1
                print(towar)
        else:
            total_nottoxic = total_nottoxic + 1
            print(towar)

    print(total_toxic)
    print(total_nottoxic)

if __name__ == "__main__":
    main()
