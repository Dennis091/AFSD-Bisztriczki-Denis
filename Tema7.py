def bubble_sort(arr, visualize=False):
    
    # Outer loop pentru a parcurge lista de la sfârșit spre început
    for n in range(len(arr) - 1, 0, -1):
        swapped = False  # Folosim swapped pentru a verifica dacă s-au făcut schimburi
        
        # Inner loop pentru a compara elementele adiacente
        for i in range(n):
            if arr[i] > arr[i + 1]:  # Dacă elementul curent este mai mare decât următorul
                # Schimbăm elementele dacă sunt în ordine greșită
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True  # Marcam că am făcut un schimb
                
            if visualize:  # Dacă dorim să vizualizăm procesul
                print("Lista după schimbul dintre {} și {}:".format(arr[i], arr[i + 1]))
                print(arr)
        
        # Dacă nu au fost făcute schimbări, lista este deja sortată
        if not swapped:
            print("Lista este deja sortată!")
            break

def print_list(arr):
    
    print("Lista curentă:", arr)

# Exemplu de listă pentru sortare
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Lista nesortată este:")
print_list(arr)

# Apelăm funcția bubble_sort cu vizualizare activată
bubble_sort(arr, visualize=True)

print("\nLista sortată este:")
print_list(arr)
