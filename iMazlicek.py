###############################################################################################################################
#####                                      iMazlicek                                                                      #####
###############################################################################################################################

# Původně jsem měl kód napsaný s pevnými hodnotami a bez vstupu uživatele. 
# Přišlo mi to ale škoda a udělal jsem z toho něco jako Tamagochi a hodně mě to bavilo :)
# Doufám, že jsem se moc neodchýlil od zadání, kdyžtak kód předělám

# Pro hezké vypisování když mazlíček začne usínat :)
import time 

# Definice třídy "Mazlicek" dle zadání
class Mazlicek():
    def __init__(self, jmeno, majitele, druh):
        # iMazlíček se bude nějak jmenovat
        self.jmeno = jmeno
        # Majitelů může být více
        self.majitele = majitele
        # Druh iMmzlíčka
        self.druh = druh
        # Hlad iMazlíčka v procentech
        self.hlad = 100
        # Vyvenčen nastaveno na nepravdu
        self.vyvencen = False
    
    def vyvenceni(self):
        # Pokud bude iMazlíček vyvenčen, tak se hodnota nastavít na "pravdu"
        self.vyvencen = True
    
    def krmeni(self, mnozstvi):
        # Hlad nesmí klesnout pod nulu. iMazlíček nemůže mít záporný hlad.
        # Proto jsem si poradil tak, že jsem si dal počítat hodnotu max z proměnných 0 a zadaného množství krmení
        # Pokud uživatel zadá jednotky krmení a hodnota bude vyšší jak 100, tak se vždy načte proměnná 0 
        self.hlad = max(0, self.hlad - mnozstvi)
    
    def spanek(self):
        # Pokud se iMazlíček vyspí, tak má automaticky hlad na 100% a není vyvenčen
        self.hlad = 100
        self.vyvencen = False

        # Vyprintování údajů pro uživatele aplikace
    def __str__(self):
        return f"**********\nJméno iMazlíčka: {self.jmeno}\n**********\nMajitelé: {', '.join(self.majitele)}\n**********\nDruh zvířete: {self.druh}\n**********\nHlad: {self.hlad}%\n**********\nVyvenčen: {self.vyvencen}\n**********"
    
majitele = ["Tomáš", "Hana", "Dominik"]
muj_mazlicek = Mazlicek("Chester", majitele, "Pes")

while True:
    # Vyprintování základních statistik uživateli
    print(muj_mazlicek)
    # Pokud má iMazlíček procento hladu od 35 do 100, tak na uživatele bude pořád skákat varování, že má iMazlíček hlad
    if muj_mazlicek.hlad == 100 or muj_mazlicek.hlad >= 35:
        # Uživatel zadá na stupnici 1-100 jakým množstívm jídla chce svého iMazlíčka nakrmit
        mnozstvi = int(input("Mazlíček je hladový, nakrmte ho. Kolik jídla mu chcete dát? Zadejte číslo v rozmezí 1 - 100: "))
        muj_mazlicek.krmeni(mnozstvi)
        print(muj_mazlicek)
        # Pokud se nenaplní podmínka hladu, tak se apikace snaží zjistit, zda je iMazlíček vyvenčen
    elif muj_mazlicek.vyvencen == False:
        prochazka = input("Váš mazlíček potřebuje vyvenčit. Chcete s ním jít na procházku? A / N: ").lower()
        if prochazka == "a":
            # Pokud uživatel vybere, že chce jít vyvenčit svého iMazlíčka, tak se zavolá pripravená funkce
            muj_mazlicek.vyvenceni()
            print("**********\nHurááá na procházku!")
        print(muj_mazlicek)
    # Pokud se nenaplní podmínky výše, tak začne být iMazlíček unavený a usne. Tím se mu resetujou všechny statistiky na původní hodnoty
    # a hra může začít znovu
    else:
        print("Váš mazlíček vypadá pěkně unavený a začíná usínat.")
        time.sleep(3)
        print("Začíná si hledat místečko a pomalu zavírá oči.")
        time.sleep(3)
        print("ZzZZzzZZZzZZzZZzZ")
        muj_mazlicek.spanek()
    
    time.sleep(1)
    
    # Pokud uživatele aplikace iMazlíček omrzí, tak může hru ukončit
    konec_hry = input("Přejete si dále hrát s mazlíčkem? A / N: ").lower()
    if konec_hry == "a":
        continue
    elif konec_hry == "n":
        break
    else:
        print("Neplatný výběr!")

# Vyprintování textu při ukončení aplikace iMazlíček
print("****************************************************************************************************")
print("Děkujeme za využití aplikace iMazlíček. Nezapomeňte si pravidelně všímat potřeb vašeho iMazlíčka :) ")
print("****************************************************************************************************")


    
