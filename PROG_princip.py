#Salles Théophile, Mathieu Mendouga
#______________.
#PROJET_ChatBot.
#FONCTIONS

from math import log10
from math import sqrt 
import os

#Import pour l'affichage
from string import ascii_uppercase
import time as time

#VARIABLES

liste_pres = []
liste_MI = []
   

#____________________________________________________________________________________________________|
#--------------------------------------------|
#Fonction qui extrait à partir des noms des fichiers, le nom des présidents.

def extraction_nom():
    arr = os.listdir("speeches")

    liste_nomP = []
    
    for file in arr:
        decod = False
        stock = ""
        print(file)
        for x in range(len(file)-4):

            if decod == True and ord(str.lower(file[x])) >= 97 and ord(str.lower(file[x])) <= 122:
                stock += file[x]

            if file[x] == "_":
                decod = True
                
        if stock not in liste_nomP:
            liste_nomP.append(stock)

    return liste_nomP

#--------------------------------------------|
#Fonction qui associe un nom à un prénom, à l'aide d'un dictionnaire predéfinie.
prenomP = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Hollande": "François", "Macron": "Emmanuel", "Mitterrand": "François", "Sarkozy": "Nicolas"}

def association_nom_prenom(listeP):
    pren = []
    for x in listeP:
        pren.append(prenomP[x])
    
    return pren

#--------------------------------------------|
#Fonction qui reprend l'intégralité des fichiers txt du dossier "speeches" et les re-crées dans
#un second dossier nommé "cleaned", cette fois tout en minuscules

def recreation_min(fichier):
    
    for file in fichier:

        f = open(f"speeches\{file}", "r", encoding = "utf-8")
        g = open(f"cleaned\{file}", "w", encoding = "utf-8")
        for x in f:
    
            g.write(str(str.lower(x)))
    f.close()
    
    return os.listdir("cleaned")


#--------------------------------------------|
#Fonction reprenant un corpus de document, celle-ci modifie et créée au sein du fichier "cleaned",  un texte en minuscule et sans ponctuation.

Ponc = "!?.,;-()[]_'{}=+~&\/"

def file_encore(fichier, ouv):
    
    
    for file in fichier:
        
        fichier_init = open(f"speeches\{file}", "r", encoding = "utf-8")
        fichier_modi = open(f"cleaned\{file}", "w", encoding = "utf-8")
        encodeur = ""
        
        for lignes in fichier_init:
            
            verid_debut_ligne = True
            
            for lettres in lignes:
                
                if lettres == " " and verid_debut_ligne:
                    pass
                
                elif lettres not in Ponc:
                    
                    encodeur += str.lower(lettres)
                    verid_debut_ligne = False
                
                elif lettres in Ponc[6:]:
                    
                    encodeur += " "
                    verid_debut_ligne = False

                #print(encodeur)
                    
        fichier_modi.write(encodeur)
    
    fichier_init.close()
    fichier_modi.close()
    
    return os.listdir("cleaned")

#____________________________________________________________________________________________________|
#--------------------------------------------|
#PROGRAMME

ensemble_des_fichiers_init = os.listdir("speeches")
fichier_clea = file_encore(ensemble_des_fichiers_init, "speeches")

#--------------------------------------------|
#FONCTIONS IDF/TF


def TF_chaine(chaine:str):

    assert isinstance(chaine, str)
    chaine = chaine + " "
    dico = {}
    mot = ""
    for lettres in chaine: 
        
        if lettres == " ":
            
            if mot in dico:
                dico[mot] = dico[mot] + 1
                mot = ""
                
            else:
                dico[mot] = 1
                mot=""
            
        else:
            mot = mot + lettres
    return dico

#--------------------------------------------|

def TF_fichier(fichier, ouv):

    chaine = chaine + " "
    dico = {}
    mot = ""
    f = open(f"{ouv}\{fichier}", "r", encoding = "utf-8")
    
    for chaine in fichier:
        for lettres in chaine:
            
            if lettres == " ":
                
                if mot in dico:
                    
                    dico[mot] = dico[mot] + 1
                    mot = ""
                
                else:
                    dico[mot] = 1
                    mot=""
            
            else:
                mot = mot + lettres
    f.close()
    return dico

#--------------------------------------------|
#Recherche le Tf pour chaque documents dans un corpus

def TF_ensemble(fichier, ouv):
    
    fall = []
    mot = ""
    
    for file in fichier:

        f = open(f"{ouv}\{file}", "r+", encoding = "utf-8")
        dico = {}
        
        for x in f:
            for lettres in x:
                if lettres == " " or lettres == "\n": #Vérifie les espaces et les sauts à la ligne [frontière entre les mots]:
                    
                    if mot in dico:
                        dico[mot] = dico[mot] + 1
                        mot = ""
                    
                    else:
                        dico[mot] = 1
                        mot=""
                else:
                    mot = mot + lettres
        fall.append(dico)
    return fall


#--------------------------------------------|
#Recherche l'IDF au sein d'un corpus

def IDF_ensemble(fichier, ouv):
    
    dico = {}
    mot = ""

    for file in fichier:
        
        list_verif = []
        
        f = open(f"{ouv}\{file}", "r", encoding = "utf-8")
        
        for x in f:
            
            for lettres in x:
    

                if lettres == " " or lettres == "\n": #Vérifie les espaces et les sauts à la ligne [frontière entre les mots]
                    
                    if mot in dico and mot not in list_verif:
                        
                        list_verif.append(mot)
                        dico[mot] = dico[mot] + 1
                        mot = ""
                    
                    elif mot not in dico:
                        list_verif.append(mot)
                        dico[mot] = 1
                        mot = ""
                        
                    else:
                        mot = ""

                else:
                    mot = mot + lettres
                  
    for y in dico:
        dico[y] = log10((len(fichier) / dico[y]) + 0)
    
    return dico

#--------------------------------------------|
#Fonction reprenant les fonctions TF et IDF, pour ainsi calculer le TF-IDF, au sein d'un corpus.

def TF_IDF_ensemble(fichier, ouv):
    lanceur_TF = TF_ensemble(fichier, ouv)
    lanceur_IDF = IDF_ensemble(fichier, ouv)
    
    fina_rendu = []
    
    for x in range(len(fichier)):
        prep_rendu = []
        
        for y in lanceur_IDF:
            
            if y in lanceur_TF[x]:
                prep_rendu.append(lanceur_IDF[y] * lanceur_TF[x][y])
                
            else:
                prep_rendu.append(lanceur_IDF[y] * 0)
            
        fina_rendu.append(prep_rendu)
    
    return fina_rendu


#____________________________________________________________________________________________________|
#--------------------------------------------|
#|_____________________________________________________________________________|
"""###--_____________________-...PARTIE_2...-_____________________--"""       #|                                                                       |
#L_____________________________________________________________________________|
#__1.
#Fonction permettant de dissocier les mots d'une phrase donnée, et les stockes dans une liste.

def listage_mot_quest(quest):
    assert isinstance(quest, str)
    if quest[-1] != " ":
        quest += " "
    fall = []
    mot = ""
    for lettres in quest:
        
        if lettres == " ":
                    
            fall.append(mot)
            mot = ""
                        
        else:
            mot = mot + lettres
    return fall

#--------------------------------------------|
#__2.
#Fonction identifiant et renvoyant la liste des mots se retrouvant dans la
#question mais aussi parmi les fichiers sous surveillance.

def recherche_ins(quest, fichier, ouv):
    fall = []
    recherc_mot = listage_mot_quest(quest)
    reperag_mot = TF_ensemble(fichier, ouv)
    
    for x in reperag_mot:
        if x in recherc_mot:
            fall.append(x)
    
    return fall

#--------------------------------------------|
#__3.
#Fonction effectuant le calcul du TF-IDF, mais reprenant cette fois le TF de la question/phrase donnée en paramètre
#De plus celui-ci détermine aussi le mot avec le plus haut score TF_IDF 

def TF_IDF_quest(quest, fichier, ouv):
    assert isinstance(quest, str)
    lanceur_TF_quest = TF_chaine(quest)
    lanceur_TF = TF_ensemble(fichier, ouv)
    lanceur_IDF = IDF_ensemble(fichier, ouv)
    
    score_max = -1
    score_max_ind = ""
    
    fina_rendu = []
    
    for x in range(len(fichier)):
        prep_rendu = []
        
        for y in lanceur_IDF:
            
            if y in lanceur_TF_quest:
                prep_rendu.append(lanceur_IDF[y] * lanceur_TF_quest[y])
                
                if lanceur_IDF[y] * lanceur_TF_quest[y] > score_max:
                    score_max = lanceur_IDF[y] * lanceur_TF_quest[y]
                    score_max_ind = y
                
            else:
                prep_rendu.append(lanceur_IDF[y] * 0)
            
        fina_rendu.append(prep_rendu)
    
    return fina_rendu, score_max, score_max_ind
    
#--------------------------------------------|
#__4_+_5.
#Fonction
#Renvoie le ou les fichier(s), où la valeur de la similarité est la plus elevée 


def simila_ensemble_quest(quest, fichier, ouv):
    assert isinstance(quest, str)
    lanceur_IDF = IDF_ensemble(fichier, ouv)
    lanceur_TF_IDF = TF_IDF_ensemble(fichier, ouv)
    lanceur_TF_IDF_quest = TF_IDF_quest(quest, fichier, ouv)
    
    retour_ind = []
    val_simil_max = 0
    
    for x in range(len(fichier)):
        
        val_calc_prodscal = 0
        val_calc_sommCEnsem = 0
        val_calc_sommCQuest = 0
        
        for y in range(len(lanceur_TF_IDF[x])):
            
            val_calc_prodscal += lanceur_TF_IDF[x][y] * lanceur_TF_IDF_quest[0][x][y]
            val_calc_sommCEnsem += lanceur_TF_IDF[x][y] ** 2
            val_calc_sommCQuest += lanceur_TF_IDF_quest[0][x][y] ** 2
        
        val_simil = val_calc_prodscal / ((sqrt(val_calc_sommCEnsem)) * (sqrt(val_calc_sommCQuest)))
        
        if val_simil > val_simil_max:
            val_simil_max = val_simil
            retour_ind = []
            retour_ind.append(fichier[x])
        
        elif val_simil == val_simil_max:
            retour_ind.append(fichier[x])
    
    return val_simil_max, retour_ind

"""simila_ensemble_quest("présidents présidents je suis les vivant mais là mesdames", file_encore(ensemble_des_fichiers_init, "speeches"), "cleaned") """
#--------------------------------------------|
#__6_+_7.           

question_debut = {"Comment": "Après analyse, ", "Pourquoi": "Car, ", "Peux-tu": "Oui, bien sûr!"}

def gener_ensemble_quest(quest, fichier, ouv):
    
    assert isinstance(quest, str)
    
    result_simil = simila_ensemble_quest(quest, fichier, ouv)[1][0]
    mot_imp = TF_IDF_quest(quest, fichier, ouv)[2]
    
    fall = []
    phrase = ""
    f = open(f"speeches\{result_simil}", "r", encoding = "utf-8")
    
    for x in f:
        for lettres in x:
    
                if lettres == ".":
                    
                    fall.append(phrase)
                    phrase = ""
                    

                elif lettres != "\n":
                    phrase = str.lower(phrase) + lettres
                    
    f.close()
    
    for y in range(len(fall)):
        if mot_imp in fall[y]:
            
            for w in question_debut:
                
                if w in quest:
                    return question_debut[w] + fall[y] + "."
            return "On donne, " + fall[y] + "."
        
    return None
    
"""gener_ensemble_quest("présidents présidents je suis les vivant mais là mesdames", file_encore(ensemble_des_fichiers_init, "speeches"), "cleaned") """ 

#____________________________________________________________________________________________________|
#--------------------------------------------|
#STOCK
Aut = 1
Direc = 0
Direc1 = 1

if Aut:
    while Direc == 0:
        Direc = input("Programmme en attente, rentrer une touche pour lancer (0 exclus):  ")

fichier_selec = ensemble_des_fichiers_init #Fichiers désignés par l'utilisateur, par défaut l'ensemble des fichiers
fichier_selec_clean = file_encore(fichier_selec, "speeches")

r = True #Sert de passage à certaines boucles while
resultat = [] #Liste contenant les résultats des différentes requêtes

option_affichage = [["||| Texte(s) en traitement", f"STATUT: {ensemble_des_fichiers_init}", ""],
                    ["||| Information(s) relevée(s): ", f"{resultat}", ""],
                    ]

#--------------------------------------------|

def affichage_console(dec, cod, enr):
    
    print("".rjust(3), end=" ")  # rjust() justifie à droite le contenu de la chaîne
    
    for i in range(47):
        print("_", end=" ")
    print() # On passe à la ligne
    print("_________________________________________________________________________________________________")
    print()
    
    for y in range(dec):
        
        print(ascii_uppercase[y].rjust(3),end=" ") 
        
        for x in range(cod):

            print(enr[y][x], end = "   ")
        print("|||".rjust(1),end=" ")
        print()
        print("_________________________________________________________")
        print()
        
    return " "

#____________________________________________________________________________________________________|
#--------------------------------------------|
#---------------------------------------\
#PROGRAMME PRINCIPAL

#---------------------------------------\
#SECTION0_

while Direc != 0 :
    time.sleep(1) 
    print("Bienvenue au sein de se programme (encore temporaire)") 
    time.sleep(3)
    
    print("Voici les fichiers prêt à être traités (fichiers texte dans 'speeches')")
    print()
    arr = os.listdir("speeches")
    for file in arr:
        print("- " + file)
        time.sleep(0.5)
    
    time.sleep(4)

#---------------------------------------\
#SECTION1_

    print(affichage_console(1, 3, option_affichage))
    
    fichier_selec = file_encore(fichier_selec, "speeches")

#---------------------------------------\
#SECTION2_
    
    while Direc1 == 1:
        print()
        print(affichage_console(2, 3, option_affichage))
        time.sleep(5)
        print()
        print("Voici les différentes fonctions de recherche à votre disposition")
        time.sleep(2)
        codeur_appel = ""
        
        while codeur_appel not in ["a", "b", "c", "d", "A"]:
            print()
            print("||_ a_.     -Rechercher les mots les moins importants parmi les fichiers (mot(s) dont le TD-IDF = 0)")
            print("||_ b_.     -Rechercher les mots les plus importants parmi les fichiers (mot(s) dont le TD-IDF est élévé") 
            print("||_ c_.     -Rechercher des mots étant le plus répétés par un des présidents de votre choix") 
            print("||_ d_.     -Indiquer le ou les noms des présidents ayant mentionnés un terme de votre choix (dont celui qui l'a le plus répété, mis en valeur")
            print()
            print("Fonction CHATBOT")
            print("||_ A_.     -Poser une question")
            print()
            print("________________")
        
            codeur_appel = str(input("Veuillez à l'aide des codes ci-dessus, sélectionner une opération (EX: 'a'):  "))

#---------------------------------------\
            
        if codeur_appel == "a":
            print()
            print("Recherche des mots les moins importants (mots dont le TD-IDF = 0)")
            
            res = []
            for v in TF_IDF_ensemble(fichier_selec, "cleaned"):
                if TF_IDF_ensemble(fichier_selec, "cleaned")[v] == 0:
                    res.append(v)
                    
            resultat.append(res)
            print(res)
            time.sleep(3)

#---------------------------------------\
            
        elif codeur_appel == "b":
            print()
            print("Recherche du où des mots les plus importants (mots dont le TD-IDF //\)")
            res = ""
            maxi = 0
            for v in TF_IDF_ensemble(fichier_selec, "cleaned"):
                if TF_IDF_ensemble(fichier_selec, "cleaned")[v] > maxi:
                    maxi = TF_IDF_ensemble(fichier_selec, "cleaned")[v]
                    res = v
                
                if TF_IDF_ensemble(fichier_selec, "cleaned")[v] == maxi:
                    res += v
            
            resultat.append(res)
            print(res)
            time.sleep(3)
    
#---------------------------------------\
            
        elif codeur_appel == "c":
            TF(fichier_selec, "cleaned")
            print()
            nompresident_discours = {} #Créer un dictionnaire associant chaque nom de président à son/ses discours
            for nom_president in prenomP:
                L = []
                for nom_fichier in ensemble_des_fichiers_init:
                    if nom_president in nom_fichier:
                        L.append(nom_fichier)
                nompresident_discours[nom_president] = L
            president = str(input("Choisir un président : "))
            while president not in prenomP:
                print("Ce président ne peut pas être choisi.")
                president = str(input("Choisir un président : "))
            nombre_mot = int(input("Choisir un nombre de mot : "))
            print("Recherche des", nombre_mot, "mots les plus répétés par le président", prenomP[president],president, "...")
            TF = TF_ensemble(nompresident_discours[president], "./cleaned")
            occ_max = 0
            for mots in TF:
                if TF[mots] > occ_max:
                    occ_max = TF[mots]
            Liste = []
            compteur = 0
            for mots in TF:
                if TF[mots] >= occ_max:
                    if compteur < nombre_mot:
                        Liste.append(mots)
                        compteur += 1
                else:
                    occ_max -= 1
            print("Les mots les plus répétés par le président", prenomP[president], president, "sont :")
            print(Liste)

            time.sleep(10)

#---------------------------------------\
            
        elif codeur_appel == "d":
            print()
            print("Indiquer le ou les noms des présidents ayant mentionnés un terme de votre choix (dont celui qui l'a le plus répété, mis en valeur")
            ter_decod = ""
            res_temp = []
            val_max = [-1, ""]
            while ter_decod == "":
                ter_decod = str(input("Veuillez rentrer un terme/mot :  "))
            
            time.sleep(2)
            lanceur_TF = TF_ensemble(fichier_selec_clean, "speeches")
            for x in range(len(fichier_selec_clean)):
                if ter_decod in lanceur_TF[x]:
                    res_temp.append(fichier_selec_clean[x])
                    if lanceur_TF[x][ter_decod] > val_max[0]:
                        val_max[0] = lanceur_TF[x][ter_decod]
                        val_max[1] = fichier_selec_clean[x]
            print(res_temp)
            print(val_max)
            if len(res_temp) == 1:
                print(f"Le seul président ayant mentionné '{ter_decod}' dans un de ses discours est {res_temp[0]}, l'ayant répété {val_max[0]} fois.")
            elif len(res_temp) > 1:
                print(f"les présidents ayant mentionné '{ter_decod}' dans un de ses discours sont:")
                for y in range(len(res_temp)):
                    print(f"- {res_temp[y]}")
                print(f"{val_max[1]} l'ayant répété le plus de fois, avec {val_max[0]}.")
            else:
                print(f"Aucun président n'a prononcé '{ter_decod}' dans un de ses discours")
            time.sleep(9)

#---------------------------------------\
        
        elif codeur_appel == "A":
            print()
            print("Poser une question, au sein du mode Chatbot")
            quest_decod = ""
            while quest_decod == "":
                quest_decod = str(input("Veuillez rentrer une question a poser :  "))
            
            time.sleep(1)
            
            print(gener_ensemble_quest(quest_decod, fichier_selec_clean, "speeches"))
            resultat.append(gener_ensemble_quest(quest_decod, fichier_selec_clean, "speeches"))
            
            time.sleep(5)


#---------------------------------------\  
