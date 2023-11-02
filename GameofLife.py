###############################################################################################################################
#####                                      3. Lekce - DÚ - Hra života                                                     #####
###############################################################################################################################

# Rozdělím si kód na několik částí, ať vím, kde začít
# 1. Vydefinování 2D mřížky
#     - výška a šířka
#     - generování náhodných pozic v mřížce 6x6 v rozmězí 0 až 1
#           - 0 = mrtvá buňka
#           - 1 = živá buňka
# 2. Vygenerování 1. generace
#     - musím vytvořit cyklus, který v rozsahu výšky a šířky změní 0 a 1 na symboly
#     - symbol života (1,⬜) a symbol smrti (0, ⬛)
# 3. Vygenerování dalších nových generací
#     - nová generace musí počítat sousedy v okolí
#     - na základě počtu sousedů budu vyhodnocovat podmínky, které jsou definovány pro "Hru života"

############################### 1. část #################################
# Naimportování modulů 
import random       # mi zajistí generování náhody
import time         # https://www.programiz.com/python-programming/time/sleep vygenerování nové generace za nějaký čas, ať se to hezky vykresluje :)
# Velikost herního pole
vyska = 6
sirka = 6
# Jednotkou času je ve Hře života generace. Jedna generace představuje jedno provedení přechodové funkce.
generace = 10
# Vytvoření náhodného hracího pole | Číslo 0 = mrtvá buňka | Číslo 1 = živá buňka
herni_pole = [[random.randint(0, 1) for i in range(sirka)] for i in range(vyska)]
print(herni_pole)
############################### 2. část #################################
# Cyklus pro vyprintování nadpisu generací podle hodnoty v proměnné generace
for generace in range(generace):
    print(f"Generace {generace + 1}:")
    
    # Vykreslení první generace
    for i in range(vyska):                # Cyklus pro generování výšky herního pole
        for j in range(sirka):            # Cyklus pro generování šířky herního pole
            if herni_pole[i][j] == 1:     # Sáhnutí podle indexů z cyklu do seznamů v proměnné "herni_pole" a zaměnění čísel za ikony
                print("⬜", end=" ")     # Živá buňka dostane emotikon ⬜ a oddělí se mezerou
            else:
                print("⬛", end=" ")     # Mrtvá buňka dostane emotikon ⬛ a oddělí se mezerou
        print()                       
############################### 3. část ##################################
# Tahle poslední část po mě byla hodně kritická. Hodně jsem se trápil, googlil a jel jsem trial and error metodu.

   # Výpočet každé další nové generace
    nove_herni_pole = [[0] * vyska for i in range(sirka)] # Nagenerování nového pole o stejných rozměrech jako v předešlé generaci
    # print(nove_herni_pole)
    for i in range(vyska):
        for j in range(sirka):
            sousede = 0                         # Počítání sousedů pro aktuálně zkoumanou buňku
            for x in range(-1, 2):              # Tohle se přiznám bez mučení, že jsem musel googlit - porovnávání sousední buňky v matici. Když jsem to pak viděl, tak to bylo logické :D
                for y in range(-1, 2):          # Tohle se přiznám bez mučení, že jsem musel googlit - porovnávání sousední buňky v matici  Když jsem to pak viděl, tak to bylo logické :D
                    if x == 0 and y == 0:       # Pokračování cyklu, buňka na souřadnicích 0,0  by kontrolovala sama sebe :)
                        continue
                    # 0 <= i + x < sirka and 0 <= j + y < vyska - Kontrola, zda je buňka v herním poli
                    # herni_pole[i + x][j + y] == 1: - Kontrola zda buňka na pozicích [i + x, j + y] je živá, pokud ano, tak se napočítá, že zkoumaná buňka má živého souseda
                    if 0 <= i + x < sirka and 0 <= j + y < vyska and herni_pole[i + x][j + y] == 1: 
                        sousede += 1
            if herni_pole[i][j] == 1:
                # Každá živá buňka s méně než dvěma živými sousedy zemře
                # Každá živá buňka s více než třemi živými sousedy zemře
                if sousede < 2 or sousede > 3:
                    nove_herni_pole[i][j] = 0
                else:
                # Každá živá buňka se dvěma nebo třemi živými sousedy zůstává žít
                    nove_herni_pole[i][j] = 1
            else:
                # Každá mrtvá buňka s právě třemi živými sousedy oživne
                if sousede == 3:
                    nove_herni_pole[i][j] = 1
    
    # Aktualizace hracího pole pro další generaci
    herni_pole = nove_herni_pole
    time.sleep(2)  # Zpoždění mezi generacemi

print("Konec simulace života.")
