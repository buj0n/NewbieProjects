###############################################################################################################################
#####                                      Matematický kvíz                                                                #####
###############################################################################################################################


############################### 1. část #################################
# Program si u mě už klasicky ( :) ) rozdělím na několik částí
# První část bude zásobník otázek
# Jelikož budu chtít otázky losovat náhodně, tak potřebuji modul random
# Náhodu budu také potřebovat při generování čísel do jednoduchých výpočtů

# Import modulu pro náhodu
import random                               
def generovani_otazky():
    """
    Generování náhodných matematických otázek
    """
    # Generování čísel v rozmezí 1 - 10
    cislo1 = random.randint(1, 10)   
    # Generování čísel v rozmezí 1 - 10       
    cislo2 = random.randint(1, 10)          
    # Seznam matematických znamének, které chci použít do kvízu a jejich náhodné zvolení
    matematicka_operace = random.choice(["+", "-", "*"])    
    # Podmínky, co nastane, když se zvolí matematické znaménko
    if matematicka_operace == "+":
        vysledek = cislo1 + cislo2
    elif matematicka_operace == "-":
        vysledek = cislo1 - cislo2
    else:
        vysledek = cislo1 * cislo2
    # Vygenerování otázky do kvízu
    otazka = f"Kolik je {cislo1} {matematicka_operace} {cislo2}?"
    # Funkce vrátí dvě proměnné vygenerovanou otázku "otazka" a správný výsledek "vysledek"
    return otazka, vysledek
############################### 2. část #################################
# Druhá část bude samotná hra, která bude počítat skóre a vyhodnocovat výsledek
def hrani_kvizu():
    """
    Hlavní hra kvízu
    """
    # Pozdravení uživatele
    print("Vítejte v matematickém kvízu!")
    # Počítání bodů uživatele
    body = 0                 
    # Proměnná na základě které se generuje počet otázek       
    pocet_otazek = 5
    # Cyklus, který vygeneruje definovaný počet otázek
    for i in range(pocet_otazek):
        # Cyklus si "zavolá" do funkce "generovani_otazky" o otázku a správný výsledek
        otazka, vysledek = generovani_otazky()
        # Uživateli se vyprintuje číslo otázky a samotná otázka
        print(f"Otázka {i + 1}: {otazka}") # 0+1, 1+1....kvůli číslování Pythonu od 0
        # Uživatel zadá svou odpověď
        odpoved_hrace = float(input("Zadejte svou odpověď: "))
        # Podmínka, která ověří že uživatelova odpověď se rovná správnému výsledku
        if odpoved_hrace == vysledek:
            # Pokud se vstup a výsledek rovnají, tak uživatel obdrží bod
            body += 1
    # Vyprintování výsledků
    print(f"\nVaše body: {body} / {pocet_otazek}")
    if body == pocet_otazek:
        print("Dokonalé, máte to bez chyby!")
    else:
        print("Nic se neděje, příště to bude lepší")

# Zavolání hlavního programu kódu
if __name__ == "__main__":
    hrani_kvizu()
