import random


cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]


incercari_ramase = 6
litere_incercate = []


print("Bine ai venit la jocul Spânzurătoarea!")
print("Cuvântul de ghicit este: " + " ".join(progres))
print(f"Încercări rămase: {incercari_ramase}")
print("-" * 20)


while incercari_ramase > 0 and "_" in progres:
    
    litera = input("Introdu o literă: ").lower()

    
    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o singură literă validă.")
        continue  

    if litera in litere_incercate:
        print(f"Ai mai încercat litera '{litera}' înainte. Alege o altă literă.")
        continue  

    
    litere_incercate.append(litera)

    
    if litera in cuvant_de_ghicit:
        print(f"Bravo! Litera '{litera}' se află în cuvânt.")
        
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
    else:
        incercari_ramase -= 1
        print(f"Oops! Litera '{litera}' nu se află în cuvânt. Mai ai {incercari_ramase} încercări rămase.")

    
    print("Progresul cuvântului este: " + " ".join(progres))
    print(f"Încercări rămase: {incercari_ramase}")
    print("-" * 20)


if "_" not in progres:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")
