meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = {'papanasi': 7, 'ceafa': 10, 'guias': 5}
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7
istoric_comenzi = []

comenzi_count = {'papanasi': 0, 'ceafa': 0, 'guias': 0}

def proceseaza_comenzi():
    while studenti and comenzi and tavi:
        student = studenti.pop(0)
        comanda = comenzi.pop(0)
        
        if comanda in preturi:
            tavi.pop()  
            istoric_comenzi.append(comanda)
            comenzi_count[comanda] += 1
            print(f"{student} a comandat {comanda}.")

proceseaza_comenzi()

def afiseaza_inventar():
    print("S-au comandat:", end=" ")
    print(", ".join(f"{count} {produs}" for produs, count in comenzi_count.items() if count > 0) + ".")
    print(f"Mai sunt {len(tavi)} tavi.")
  
    for produs in preturi.keys():
        stoc = meniu.count(produs)
        print(f"Mai este {produs}: {stoc > 0}.")

afiseaza_inventar()

def calculeaza_finante():
    total_incasa = sum(preturi[produs] * count for produs, count in comenzi_count.items())
    print(f"Cantina a încasat: {total_incasa} lei.")
    
    produse_sub_7 = {produs: pret for produs, pret in preturi.items() if pret <= 7}
    print(f"Produse care costă cel mult 7 lei: {list(produse_sub_7.items())}.")

calculeaza_finante()
