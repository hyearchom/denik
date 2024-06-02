#!/usr/bin/env python3

import os
from datetime import datetime

#---Nastavení---

SLOUPEC_OD, SLOUPEC_DO, SLOUPEC_CINNOST = 0,1,2

# Umístění zdrojové tabulky
dnesni_den = datetime.today().strftime('%Y-%m-%d')

adresar_skript = os.path.dirname(os.path.abspath(__file__))
cesta_denik = os.path.join(adresar_skript + '/denik/', dnesni_den + '.md')


#---Aplikace---

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

    # Vypsání předešlých činností dne
    for radek in obsah:
        print(radek)

    # Vstup uživatele pro popis činnosti
    # Volitelně může upravit nabízené hodiny
    zadano_uzivatelem = input(f'{zacatek}\t{dalsi_hodina}\t***Zadej činnost***\n')
    if zadano_uzivatelem:
        if '\t' in zadano_uzivatelem:
            ulozit_zaznam(zadano_uzivatelem + '\n')
        else:
            ulozit_zaznam(f'{zacatek}\t{dalsi_hodina}\t{zadano_uzivatelem}\n')
    

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

    print("\nZáznam uložen.")


if __name__ == "__main__":
    spustit_aplikaci()
    input('Dokončeno, zadej cokoli') # Vyčkání stisku klávesy pro ukončení