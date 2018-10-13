
pozycje = [
    {'produkt':'wyklady', 'cena': 1.10, 'vat_procent': 50},
    {'produkt':'sprzatanie', 'cena': 51.24, 'vat_procent': 8},
    {'produkt':'somochod', 'cena': 199.99, 'vat_procent': 13},
    {'produkt':'masaz', 'cena': 482, 'vat_procent': 2}
]

wybory = ['wyklady', 'samochod']

total_netto = 0
total_brutto = 0

for poz in pozycje:
    if poz['produkt'] in wybory:
            total_netto = total_netto + poz['cena']
            print(total_netto)
            print(total_brutto)
