from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    image=image.binarisation(S)
    image=image.localisation()
    x=0
    indice=0
    for k in range (len(liste_modeles)):
        liste_modeles[k]=liste_modeles[k].binarisation(S)
        liste_modeles[k]=liste_modeles[k].localisation()
        liste_modeles[k]=liste_modeles[k].resize(image.H,image.W)
        y=image.similitude(liste_modeles[k])
        if y>x:
            x=y
            indice=k
    return(indice)
