def compter_occurrences(tableau, element):
    return tableau.count(element)

def moyenne_et_minimum(tableau):
    if not tableau:
        return None, None  
    moyenne = sum(tableau) / len(tableau)
    minimum = min(tableau)
    return moyenne, minimum

def est_trie(tableau):
    return tableau == sorted(tableau)

def inverser_tableau(tableau):
    return tableau[::-1]



tableau = [1, 2, 3, 4, 2, 5]

print("Occurrences de 2:", compter_occurrences(tableau, 2))

moyenne, minimum = moyenne_et_minimum(tableau)
print("Moyenne:", moyenne)
print("Minimum:", minimum)

print("Le tableau est trié :", est_trie(tableau))



