import os
import shutil
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Affiche la liste
def print_list(files_names):
    print(files_names)


# Extrait les noms de fichier de la liste et ajoute les noms des présidents dans une nouvelle liste
def extraction(nom_fichier: list):
    L = []
    for i in nom_fichier:
        if i[-5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            L.append((i[11:-5]))
        else:
            L.append((i[11:-4]))
    return L


# Permet de supprimer les doublons d'une liste
def sans_doublon(liste: list):
    L = []
    for i in liste:
        if i not in L:
            L.append(i)
    return L


# Associe à chaque noms de président un prénom et l'ajoute dans une liste
def prenom_nom(liste: list):
    prenom = {"Macron": "Emmanuel", "Mitterrand": "François", "Sarkozy": "Nicolas", "Giscard dEstaing": "Valéry",
              "Chirac": "Jacques", "Hollande": "François"}
    L = []
    for i in liste:
        L.append(prenom[i] + ' ' + i)
    return L


# Créer un fichier avec les textes en minuscule et sans -,; etc
def cleaned(directory, extension):
    files_names = []
    os.mkdir("cleaned")
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    for fichier in files_names:
        f = open(directory + "/" + fichier, "r")
        contenu = f.readlines()
        for ligne in contenu:
            ligne = minuscule(ligne)
            ligne = suite_mot(ligne)
            f2 = open("./cleaned" + "/" + minuscule(fichier), "a")
            f2.write(ligne)
        f2.close()
    f.close()


def minuscule(texte:str):
    minuscule = ""
    for car in texte:
        if ord(car) >= ord('A') and ord(car) <= ord('Z'):
            car = chr(ord(car) + 32)
        minuscule = minuscule + car
    return minuscule

# Supprime tous les ',?! etc des textes d'un fichier
def suite_mot(texte:str):
    characters = "!?.,;()[]_'-"
    for x in range(len(characters)):
        if characters[x] in characters[:-3]:
            texte = texte.replace(characters[x], "")
        else:
            texte = texte.replace(characters[x], " ")
            texte = texte.replace('\n', " ")
    return texte


# Affiche le contenu d'un fichier donné dans un répertoire donné
def lecture(directory, file):
    lecture = ""
    for filename in os.listdir(directory):
        if file in filename:
            f = open(directory + "/" + file, 'r')
            contenu = f.readlines()
            for line in contenu:
                lecture = lecture + line
    return lecture


# Retourne une liste contenant tous les mots d'un texte
def liste_mot(texte:str):
    L = []
    mot = ""
    for lettre in texte:
        if lettre != " ":
            mot = mot + lettre
        else:
            L.append(mot)
            mot = ""
    return L






#Calcul le TF d'une chaine de caractère
def TF(texte: str):
    TF = {}
    texte_mots = liste_mot(texte)
    for elt in texte_mots:
        if elt in TF:
            TF[elt] = TF[elt] + 1
        else:
            TF[elt] = 1
    return TF


directory = "./speeches"
files_names = list_of_files(directory, "txt")
print_list(files_names)
cleaned(directory, "txt") # Appel de la fonction minuscule pour créer et remplir le fichier cleaned


# retourne l'indice IDF des documents textes d'un répertoire
def IDF(directory):
    dico = {}
    Liste_files = list_of_files(directory, "txt") #Créer une liste du nom de chaque fichier du dossier
    Liste_mot = []
    nbre_fichier = len(Liste_files)
    for elt in Liste_files:
        Liste_mot = Liste_mot + liste_mot(lecture(directory, elt)) #puis la fonction lecture pour lire le contenu du fichier et enfin la fonction liste de mot pour créer une liste des mots du fichier.
    Liste_mot = sans_doublon(Liste_mot)
    for mot in Liste_mot:
        nbre_fichier_mot = 0
        for i in Liste_files:
            L = []
            L = liste_mot(lecture(directory, i))
            if mot in L:
                nbre_fichier_mot += 1
            if nbre_fichier_mot == 0:
                dico[mot] = "pas de mot"
            else:
                IDF = math.log((nbre_fichier / nbre_fichier_mot) + 1)
                dico[mot] = IDF
    return dico


# Effectue le dictionnaire TF de chaque document
files_cleaned = list_of_files("./cleaned", "txt")
dictionnaire_files = {}
for files in files_cleaned:
    print("Le nombre TF du fichier", files, "est :")
    print(TF(lecture("./cleaned", files)))
    print("")
    dictionnaire_files[files] = TF(lecture("./cleaned", files))
    print(dictionnaire_files)

def produit_scalaire(matrice1:list, matrice2:list):
    scalaire = []
    for i in range(len(matrice1)):
        for j in range(len(matrice1[i])):
            scalaire.append(matrice1[i][j] * matrice2[i][j])
    return scalaire


def norme_vecteur(matrice: list):
    norme = 0
    for i in range(len(matrice)):
        norme += matrice[i] * matrice[i]
    return sqrt(norme)

def similarite(vecteur1:list, vecteur2:list):
    similarite = produit_scalaire(vecteur1, vecteur2) / (norme_vecteur(vecteur1) * norme_vecteur(vecteur2))
    return similarite

#_______________________________________________________________________________________________________________________________________________________|

def TF(chaine:str):

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

def IDF():
    arr = os.listdir("speeches")
    txtfiles = []
    
    for file in arr:
        print(file)
        f = open(f"speeches\{file}", "r+", encoding = "utf-8")
        
        for x in f:
            print(TF(str(f.readline())))
            txtfiles.append(file)
        #print(TF(str(f.readline())))
        #txtfiles.append(file)
    print(txtfiles)
    return 0

#____________________________________________________________________________________________________|
#--------------------------------------------|

def extraction():
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
prenomP = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Hollande": "François", "Macron": "Emmanuel", "Mitterrand": "François", "Sarkozy": "Nicolas"}

def associa(listeP):
    pren = []
    for x in listeP:
        pren.append(prenomP[x])
    
    return pren

#--------------------------------------------|

def conversMin():
    arr = os.listdir("speeches")
    
    for file in arr:

        f = open(f"speeches\{file}", "r+", encoding = "utf-8")
        g = open(f"cleaned\{file}", "w", encoding = "utf-8")
        for x in f:
    
            g.write(str(str.lower(x)))
    f.close()
    g.close()
    return None

#--------------------------------------------|
listPonc = ["'", "-", "_", ",", "?", "!", ".", ";", ":", "/", "(", ")"]

def triPonc():
    
    brr = os.listdir("cleaned")
    
    for file in brr:

        f_init = open(f"cleaned\{file}", "r", encoding = "utf-8")     
        lecture = f_init.readlines()
        f_init.close()
        
        for x in lecture:
            fall = ""
            for y in x:
                
                if y in listPonc:
                    fall += " "
                else:
                    fall += y
            print(fall)
            f_trs = open(f"cleaned\{file}", "w", encoding = "utf-8")
            f_trs.write(fall)
            f_trs.close() 


    return None



#FONCTIONS

from math import log
import os
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
prenomP = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Hollande": "François", "Macron": "Emmanuel", "Mitterrand": "François", "Sarkozy": "Nicolas"}

def association_nom_prenom(listeP):
    pren = []
    for x in listeP:
        pren.append(prenomP[x])
    
    return pren

#--------------------------------------------|
#Fonction quireprend l'intégralité des fichiers txt du dossier "speeches" et les re-crées dans
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

characters = "!?.,;()[]_'-"

def triPonc(fichier):
    
    files_names = []
    
    for file in fichier:
        f_init = open(f"cleaned\{file}", "r", encoding = "utf-8")
        lecture = f_init.readlines()
        
    for x in lecture:
        
        for y in range(len(characters)):
            
            if characters[y] in characters[:-3]:
                x = x.replace(characters[y], "")
                
            else:
                x = x.replace(characters[y], " ")
                x = x.replace('\n', " ")
            print(x)
            
            f2 = open(f"cleaned\{file}", "a", encoding = "utf-8")
            f2.write(x)
        f2.close()
    f_init.close()
        
    return os.listdir("cleaned")

#-------------------------------------------------------------------------------------------------------------|
#PROGRAMME
#--------------------------------------------|
#PROGRAMME

ensemble_des_fichiers_init = os.listdir("speeches")
#fichier_mini = recreation_min(ensemble_des_fichiers_init)
#fichier_clea = triPonc(fichier_mini)

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

def TF_ensemble(fichier, ouv):
    
    dico = {}
    mot = ""
    
    for file in fichier:

        f = open(f"{ouv}\{file}", "r+", encoding = "utf-8")
        
        for x in f:
            for lettres in x:
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


def IDF_ensemble(fichier, ouv):
    
    dico = {}
    mot = ""

    for file in fichier:
        
        list_verif = []
        
        f = open(f"{ouv}\{file}", "r", encoding = "utf-8")
        
        for x in f:
        
            
            for lettres in x:
    
                
                if lettres == " ":
                    
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
        dico[y] = log((len(fichier) / dico[y]) + 1)
     
    return dico

#--------------------------------------------|

def TF_IDF_ensemble(fichier, ouv):
    dico_TF = TF_ensemble(fichier, ouv)
    dico_IDF = IDF_ensemble(fichier, ouv)
    
    
    for x in dico_TF:
        dico_IDF[x] = dico_TF[x] * dico_IDF[x]
    
    return dico_IDF

#____________________________________________________________________________________________________|
#--------------------------------------------|
#STOCK
Direc = 1
Direc1 = 1

fichier_selec = ensemble_des_fichiers_init #Fichiers désignés par l'utilisateur, par défaut l'ensemble des fichiers

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

#---------------------------------------\
#PROGRAMME PRINCIPAL

input("Programmme en attente, rentrer une touche pour lancer:  ")

#---------------------------------------\
#SECTION0_

while Direc == 1 :
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
    
    fichier_selec = triPonc(recreation_min(fichier_selec))

#---------------------------------------\
#SECTION2_
    
    while Direc1 == 1:
        print()
        print(affichage_console(2, 3, option_affichage))
        time.sleep(2)
        print()
        print("Voici les différentes fonctions de recherche à votre disposition")
        time.sleep(1)
        codeur_appel = ""
        
        while codeur_appel not in ["a", "b", "c", "d", "e", "f"]:
            print()
            print("||_ a_.     -Rechercher les mots les moins importants parmi les fichiers (mot(s) dont le TD-IDF = 0)")
            print("||_ b_.     -Rechercher les mots les plus importants parmi les fichiers (mot(s) dont le TD-IDF est élévé") 
            print("||_ c_.     -Rechercher des mots étant le plus répétés par un des présidents de votre choix") 
            print("||_ d_.     -Indiquer le ou les noms des présidents ayant mentionnés un terme de votre choix (dont celui qui l'a le plus répété, mis en valeur")
            print("||_ e_.     -Indiquer le premier président a avoir mentionné un terme de votre choix")
            print("||_ f_.     -Rechercher les mots dont tous les présidents ont évoqués, en excluant les mots non-importants")
            print()
        
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
    # ---------------------------------------\

        elif codeur_appel == "c":
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
