###############################################################################################################################
#####                                      RPG souboj                                                                     #####
###############################################################################################################################

# Tohle mě hodně bavilo, prosím více takových úkolů :)

# Naimportován modul pro abstraktní třídy
from abc import ABC, abstractmethod
# Naimportován modul pro čas, pro hezké vypisování řádků boje
import time
# Definování třídy Zbran
class Zbran():
    # název zbraně, síla útoku, durabilita zbraně, váha zbraně, magické vylepšení a dosah zbraně
    def __init__(self, nazev, utok, durabilita, vaha, magie, dosah):
        self.nazev = nazev
        self.utok = utok
        self.durabilita = durabilita
        self.vaha = vaha
        self.magie = magie
        self.dosah = dosah

    @abstractmethod
    def zautoc(self):
        ...
    # Hráč si může nechat u kováře / mistra lučistníka opravit zbraň
    def oprav(self):
        self.durabilita += 8
        return f"Zbraň {self.nazev} byla opravena! Durability zvýšena na {self.durabilita}."

# Definování nové zbraně, která bude vycházet ze svého rodiče Zbran
class Mec(Zbran):
    def __init__(self, nazev, utok, durabilita, vaha, magie):
        super().__init__(nazev, utok, durabilita, vaha, magie, dosah=1)
        
    # Způsob boje s mečem
    def zautoc(self):
        # Hráč zaútočí a sníží se durabilita
        if self.durabilita > 0:
            self.durabilita -= 1
            # do celkového poškození se počítá útok + magické vlastnosti zbraně
            celkove_poskozeni = self.utok + self.magie
            return f"Zaútočil jsi mečem {self.nazev} a způsobil jsi {celkove_poskozeni} bodů poškození! Zbývá ti {self.durabilita} durability."
        else:
            return f"Hele, ten tvůj meč nevypadá moc dobře. Utíkej za kovářem a nech si ho opravit"

# Definování nové zbraně, která bude vycházet ze svého rodiče Zbran
class Luk(Zbran):
    def __init__(self, nazev, utok, durabilita, vaha, magie, pocet_sipu):
        super().__init__(nazev, utok, durabilita, vaha, magie, dosah=10)
        self.pocet_sipu = pocet_sipu
    
    def zautoc(self):
        # Hráč zaútočí a sníží se durabilita a počítá se počet vystřelených šípů
        if self.pocet_sipu > 0 and self.durabilita > 0:
            self.pocet_sipu -= 1
            self.durabilita -= 1
            celkove_poskozeni = self.utok + self.magie
            return f"Vystřelil jsi z luku {self.nazev} a způsobil jsi {celkove_poskozeni} bodů poškození! Zbývá ti {self.durabilita} durability a zbývá ti {self.pocet_sipu} šípů."
        elif self.durabilita == 0:
            return f"Ten tvůj luk by zasloužil nějakou péči, navštiv nejbližšího lučištníka"
        else:
            return f"Vypadá to, že ti došli šípy. Nemůžeš zaútočit!"

def boj_s_mecem():
    muj_mec = Mec("Orcrist", 10, 5, 10, 0)
    print("********************************************************************************************")
    print("Procházíš se lesem a všimneš si, že ti září meč. Rozhlednéš se a narazíš na osamělého skřeta.")
    print("********************************************************************************************")
    time.sleep(3)
    print("Tasíš svůj Orcrist a ženeš se do boje!")
    print("********************************************************************************************")
    time.sleep(3)
    for utok in range(3):
        print(muj_mec.zautoc())
        time.sleep(3)
    print("********************************************************************************************")
    print("Je dobojováno, skřet padá k zemi.")
    print("********************************************************************************************")
    time.sleep(3)
    print("Navštívil si kováře a ten ti opravil zbraň.")
    print("********************************************************************************************")
    print(muj_mec.oprav())
    time.sleep(3)
    print("********************************************************************************************")
    print("Tentokrát narážíš na menší skupinku skřetů. Vytahuješ luk.")
    print("********************************************************************************************")

def boj_s_lukem():
    muj_luk = Luk("Legolasův luk", 15, 10, 2, 5, 8)
    time.sleep(3)
    for utok in range(muj_luk.durabilita-1):
        time.sleep(3)
        print(muj_luk.zautoc())
    time.sleep(3)
    print("*********************************************************************************************************************************")
    print("Skřeti využívají situace a vrhají se na tebe vší silou. Naštěstí se ti podařilo utéct a schoval ses jim. Tentokrát si měl štěstí!")
    print("*********************************************************************************************************************************")


# Vyprintování takového krátkého příběhu bojovníka ze Středozemě :)
boj_s_mecem()
boj_s_lukem()




        




