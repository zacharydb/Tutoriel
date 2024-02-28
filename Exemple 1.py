

ventes = {'janvier': 1500, 'février': 2200, 'mars': 1800, 'avril': 2500, 'mai': 2000}

# Tri par valeur
# Pour trier ce dictionnaire par valeur (c'est-à-dire par montant de ventes),
# nous pouvons utiliser la fonction sorted() avec le paramètre key
# pour spécifier que nous voulons trier par valeur :

ventes_triées = dict(sorted(ventes.items(), key=lambda item: item[1]))
print(ventes_triées)  # Cela produira :

# {'janvier': 1500, 'mars': 1800, 'mai': 2000, 'février': 2200, 'avril': 2500}

# Tri par clé
# Pour trier le dictionnaire par clé (c'est-à-dire par mois),
# nous n'avons même pas besoin de spécifier le paramètre key,
# car c'est le comportement par défaut de la fonction sorted() :

if __name__ == "__main__":
    ventes_triées = dict(sorted(ventes.items()))
    print(ventes_triées)

    clés = ventes.keys()
    valeurs = ventes.values()

    print("Clés :", clés)
    print("Valeurs :", valeurs)


