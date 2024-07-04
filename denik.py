#!/usr/bin/env python3

from glob import glob
import os
from datetime import datetime
import argparse

#---Nastavení---

# Přepínače aplikace
parser = argparse.ArgumentParser(
                    prog='Deník',
                    description='Zápis denních aktivit')
parser.add_argument(
                '-p', '--prenest',
                help='Přenést záznamy do zvolené složky',
                action="store_true")

# Konstanty
SLOUPEC_OD, SLOUPEC_DO, SLOUPEC_CINNOST = 0,1,2
CESTA_ZDROJOVY_ADRESAR = './denik/'
CESTA_CILOVY_ADRESAR = './test/'

# Umístění zdrojové tabulky
dnesni_den = datetime.today().strftime('%Y-%m-%d')
cesta_denik = os.path.join(CESTA_ZDROJOVY_ADRESAR, dnesni_den + '.md')


#---Definování---

# Přenesení záznamů:

def prepinac_preneseni():
    argumenty = parser.parse_args()
    return argumenty.prenest


def prenest_zaznamy():
    for zaznam in glob(CESTA_ZDROJOVY_ADRESAR + '*.md'):
        data = precist_zaznam(zaznam)

        jmeno_souboru = os.path.basename(zaznam)
        doplnit_zaznam(CESTA_CILOVY_ADRESAR, jmeno_souboru, data)


def precist_zaznam(jmeno_souboru):
    with open(jmeno_souboru, 'r') as soubor:
        obsah = soubor.read()
    os.remove(jmeno_souboru)
    return obsah


def doplnit_zaznam(umisteni, jmeno_souboru, doplneni):
    nadpis = '\n\nPrůběh dne:\n'
    with open(umisteni + jmeno_souboru, 'a+') as soubor:
        soubor.write(nadpis + doplneni)
    print(f'{jmeno_souboru} doplněn')


# Vytváření záznamů:

def spustit_aplikaci():
    
    obsah, radky = ziskani_dat_deniku()
    
    # Vyhledání konce posledního záznamu
    if radky:
        zacatek = radky[-1][SLOUPEC_DO]
    else:
        zacatek = '06'
    
    # Určení současné hodiny jako konce
    hodina = datetime.now().strftime('%H')
    dalsi_hodina = int(hodina) +1
    konec = str(dalsi_hodina)
    # Korekce vypuštění nuly u jednociferného čísla
    if len(konec) == 1:
        konec = '0' + konec

    # Vypsání předešlých činností dne
    for radek in obsah:
        print(radek)

    # Vstup uživatele pro popis činnosti
    # Volitelně může upravit nabízené hodiny
    zadano_uzivatelem = input(f'{zacatek}\t{konec}\t***Zadej činnost***\n')
    if zadano_uzivatelem:
        if '\t' in zadano_uzivatelem:
            ulozit_zaznam(zadano_uzivatelem + '\n')
        else:
            ulozit_zaznam(f'{zacatek}\t{konec}\t{zadano_uzivatelem}\n')

    # Vrátit status, jestli uživatel poskytl data    
    return bool(zadano_uzivatelem)

def ziskani_dat_deniku():
    # Přečtení dat z tabulky deníku
    # Pokud soubore neexistuje, tímto se vytvoří
    obsah = []
    with open(cesta_denik, "a+") as soubor:
        soubor.seek(0)
        cteni = soubor.read().splitlines()
        for radek in cteni:
            obsah.append(radek.split('\t'))

    #obsah.pop(0)  # Odstranění nepotřebné hlavičky z dat
    return [cteni, obsah]


def ulozit_zaznam(vystup):
    # Uložit nove hodnoty urovni jednotlivých slov do CSV souboru
    with open(cesta_denik, "a", newline="") as soubor:
        soubor.write(vystup)

    print("\nZáznam uložen.\n")


#---Zpracování---

if __name__ == "__main__":
    if prepinac_preneseni():
        prenest_zaznamy()
    else:
        # zacyklení pro více záznamů
        ocekavat_data = True
        while ocekavat_data:
            ocekavat_data = spustit_aplikaci()
    input('Dokončeno, zadej cokoli') # Vyčkání stisku klávesy pro ukončení