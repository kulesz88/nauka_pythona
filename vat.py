def calculate_vat(netto, rate):
    return float(netto * rate) / 100

def prepare_report(pozycje, wybory):
    total_netto = 0
    total_brutto = 0

    for poz in pozycje:
        if poz['produkt'] in wybory:
            total_netto = total_netto + poz['cena']
            total_brutto = total_brutto + poz['cena'] + calculate_vat(poz['cena'], poz['vat_procent'])
            return total_netto, total_brutto

def export_to_file(netto, brutto):
    print("netto,{0}".format(netto))
    print("brutto,{0}".format(brutto))

def retrieve_data(client_id, user_id):
    pozycje = [
        {'produkt':'wyklady', 'cena': 121.10, 'vat_procent': 50},
        {'produkt':'sprzatanie', 'cena': 51.24, 'vat_procent': 8},
        {'produkt':'somochod', 'cena': 199.99, 'vat_procent': 13},
        {'produkt':'masaz', 'cena': 482, 'vat_procent': 2}
        ]
        return pozycje

def main()

wybory = ['wyklady', 'samochod']

netto,brutto = prepare_report(pozycje, wybory)

export_to_file(netto, brutto)

if __name_ == "__main__":
    main()
