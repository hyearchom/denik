# Aplikace deník

#### Účel:
- aplikace slouží pro sledování denních aktivit
- můžete tak jednoduše zaznamenávat a zpětně hodnotit svoje úsilí během dne
- poskytne vám to nejen možnost ke zdokonalování, ale zároveň si vytváříte historii, kterou můžete kdykoli v budoucnu zpětně vyhledat

#### Spuštení:
- `denik.py` je python skript
- skript vyžaduje adresář s názvem `denik` ve stejném adresáři 
- pro spuštění je potřeba otevřít soubor přes Příkazovou řádku/Terminál
	*(ve Windows stačí soubor přejmenovat na `denik.pyw` a spustit dvojklikem )*

#### Návod:
- každé otevření vytvoří jeden záznam s názvem činnosti, které zadáte
- čas činnosti je zvolen jako interval mezi poslední činností a časem následující celé hodiny
- pokud si přejete zadat jiný interval, stačí před názvem činnosti zadat hodiny a **oddělit vše tabulátory**
- záznam se uloží ve formátu `md` pod aktuálním datem do adresáře `/denik`
- před uložením záznamu vám aplikace vypíše všechny dnešní zaznamenané aktivity


## Přenesení dat

#### Spuštení:
- `denik_prenasec.py` je python skript
- skript vyžaduje přespat cílové umístění v souboru pod názvem CESTA_CILOVY_ADRESAR
- pro spuštění je potřeba otevřít soubor přes Příkazovou řádku/Terminál
	*(ve Windows stačí soubor přejmenovat na `denik.pyw` a spustit dvojklikem )*

#### Návod:    
- Doplnění o samostatný skript, který slouží:
  - k přemístění dat
  - přidání k předchozím záznamům (pokud už záznam v adresáři existuje)
  - ke smazání přenesených záznámů v adresáři `/denik`


##### Pomůcky:
[(Návod na instalaci Pythonu)](https://naucse.python.cz/lessons/beginners/install/)
[(Návod na obsluhu příkazové řádky)](https://naucse.python.cz/lessons/beginners/cmdline/) 
