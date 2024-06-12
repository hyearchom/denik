from glob import glob
import os

# Nastavení:

CESTA_ZDROJOVY_ADRESAR = './denik/'
CESTA_CILOVY_ADRESAR = './test/'

# Kód:

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

# Zpracování:

for zaznam in glob(CESTA_ZDROJOVY_ADRESAR + '*.md'):
    data = precist_zaznam(zaznam)

    jmeno_souboru = os.path.basename(zaznam)
    doplnit_zaznam(CESTA_CILOVY_ADRESAR, jmeno_souboru, data)