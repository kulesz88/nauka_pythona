d = [
    {'nazwa':'banany', 'id': 1, 'waga': 10, 'ilosc': 4, 'cena': 8.10},
    {'nazwa':'mleko', 'id': 2, 'waga': 5, 'ilosc': 20, 'cena': 2.20},
    {'nazwa':'karma', 'id': 82, 'waga': 25, 'ilosc': 41, 'cena': 42},
    {'nazwa':'ser', 'id': 4, 'waga': 1, 'ilosc': 32, 'cena': 28},
    {'nazwa':'pomidory', 'id': 8, 'waga': 2, 'ilosc': 12, 'cena': 5.21},
    {'nazwa':'cukierki', 'id': 24, 'waga': 1, 'ilosc': 17, 'cena': 14.21},
    {'nazwa':'czekoloda', 'id': 54, 'waga': 0.5, 'ilosc': 19, 'cena': 21.10},
    {'nazwa':'zabawki', 'id': 81, 'waga': 1.2, 'ilosc': 21, 'cena': 100},
]
#import pprint

#pprint.pprint(magazyn)
def prepare_report(magazyn):
    total_waga = 0
    total_ilosc = 0
    total_cena = 0

    for towar in magazyn:
        total_waga = total_waga + (towar['waga'] * towar['ilosc'])
        total_ilosc = total_ilosc + towar['ilosc']
        total_cena = total_cena + (towar['cena'] * towar['ilosc'])

    return total_waga, total_ilosc, total_cena

def print_report(total_waga, total_ilosc, total_cena):
    print("Waga {0}".format(total_waga))
    print("Ilosc {0}".format(total_ilosc))
    print("Cena {0}".format(total_cena))

    return total_waga, total_ilosc, total_cena

def write_file(total_waga, total_ilosc, total_cena):
    file = open("magazyn.txt", "w")
    file.write(str("Waga {0}".format(total_waga)) + '\n')
    file.write(str("Ilosc {0}".format(total_ilosc)) + '\n')
    file.write(str("Cena {0}".format(total_cena)) + '\n')
    file.close()

def main():
    t_waga, t_ilosc, t_cena = prepare_report(d)
    print_report(t_waga, t_ilosc, t_cena)
    write_file(t_waga, t_ilosc, t_cena)

if __name__ == "__main__":
    main()
