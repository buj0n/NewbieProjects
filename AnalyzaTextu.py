###############################################################################################################################
#####                                      Analýza textu                                                                  #####
###############################################################################################################################

# Import modulu pro počítání nejčastějších slov
# https://www.guru99.com/python-counter-collections-example.html
from collections import Counter

# Prázdná proměnná na počítaná vět
pocet_vet = 0
# Vstup od uživatele. Provedu zmenšení, aby všechna stejná slova měla stejné velikosti znaků.
text = input("Zadejte text a já vám spočítám počet slov, vět a tři nejčastěji používaná slova: ").lower()
# Cyklus počítá interpunčkní znaménko na konci věty. Pokud skončí věta znaky ".", "?" nebo "!" tak přidá po jednom bodu do proměnné "pocet_vet"
for veta in text:
    if veta in ".?!":
        pocet_vet += 1
# Rozdělení slov po každé mezeře do seznamu. Každé další slovo je z logiky stavby vět oddělené mezerou.
text_slova = text.split(" ")
# print(text_slova)
# Spočítání tří nejpoužívanějsích slov
pocet_napsanych_slov = Counter(text_slova)
# Získáme tři nejčastější prvky
nejcastejsi_slova = pocet_napsanych_slov.most_common(3)
# Vyprintování výsledku
print(f"Text obsahuje {pocet_vet} vět/y a {len(text_slova)} slov. Tři nejčastěji se opakující slova jsou: {list(nejcastejsi_slova)} ")


