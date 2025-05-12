def ouvre_fichier()
    file = open("nat2022.csv", "r", encoding='utf-8')
    ligne = file.readline()
    liste = []
    ligne = file.readline()

    while ligne != "":
        valeurs = ligne.split(";")
        dico = {"sexe":int(valeurs[0]),
                "preusuel":valeurs[1],
                "annais":valeurs[2],
                "nombre":int(valeurs[3])}
        liste.append(dico)
        ligne = file.readline()
    file.close()
    return liste
