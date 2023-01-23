"""Je n'est pas réussi à faire les calculs pour le masque de classes A, je les ai laissé dans mon code, mais je n'ai pas réussi à aboutir.
La classe C et B fonctionne par le calculs avec les sous réseaux.
Si l'utilisateur veut faire les calcules par le nombre d'hotes, uniquement la classe C fonctionnera"""


def saisirIp():
    """Fonction qui demande à l'utilisateur de saisir l'adresse IP souhaité"""
    adrIp = str(input("Saisir une adresse réseau au format décimal pointé : "))
    return adrIp

def decoupIp(adrIp):
    """Fonction qui permet de passer l'adresse souhaité sous forme de liste

    Paramètre optionnel:
    adrIp : adresse choisi précédemment par l'utilisateur"""
    adrIp = adrIp.split(".")
    return adrIp

def saisirMasque():
    """Fonction qui demande à l'utilisateur de saisir un masque souhaité"""
    adrMas = str(input("Saisir un masque au format décimal pointé (255.255.0.0 ou 255.255.255.0): "))
    return adrMas

def decoupMasque(adrMas):
    """Fonction qui permet de passer le masque sous forme de liste

    Paramètre optionnel :
    adrMas : masque choisi précédemment"""
    adrMas = adrMas.split(".")
    return adrMas

def choixUti():
    """Fonction qui demande à l'utilisateur de calculer via le nombre de sous réseaux ou le nombre d'hotes"""
    choixUti = str(input("Saisir \"o\" pour calculer avec le nombre d'hote ou alors \"n\" pour calculer avec le nombre de sous réseaux"))
    return choixUti

def nbHotes():
    """Fonction qui demande à l'utilisateur de saisir le nombre d'hote"""
    nbHotes = int(input("Quels est le nombre d'hôtes souhaités ?"))
    return nbHotes

def sousRes():
    """Fonction qui permet de demander le nombre de sous réseaux à l'utilisateur"""
    sousReseau = int(input("Quel est le nombre de sous-réseau : "))
    return sousReseau

ad = saisirIp()
ad1 = decoupIp(ad)
ad2 = ad1
adm = saisirMasque()
adm1 = decoupMasque(adm)
repo = choixUti()

def classeMasque(adm1):
    """Permet de définir à qu'elle classe de masque appartient le masque choisi

    Paramètre optionnel:
    adm1 : le masque sous forme de liste"""
    if adm1[0] == "255" and adm1[1] == "255" and adm1[2] == "255" and adm1[3] == "0":
        classeMasque = "C"
    elif adm1[0] == "255" and adm1[1] == "255" and adm1[2] == "0" and adm1[3] == "0":
        classeMasque = "B"
    elif adm1[0] == "255" and adm1[1] == "0" and adm1[2] == "0" and adm1[3] == "0":
        classeMasque = "A"
    return classeMasque

def premierAppa():
    """Permet de définir l'adresse IP du premier appareil en fonction du nombre de sous réseau"""
    for cpt in range(nbSousReseau):
        if classeMasque1 == "C":
            ad1[3] = cpt * (nbAppareilSousRes1 + 2) +1
            ipPremierApp = ad1
        elif classeMasque1 == "B":
            nbSousReseau2 = nbSousResPos(sousReseau)
            ad1[3] = 1
            div = 256 // nbSousReseau2
            ad1[2] = cpt * div
            ipPremierApp = ad1

        elif classeMasque1 == "A":
            ad1[3] = 1
            ad1[2] = 0
            ad1[1] = cpt * (255 // nbSousReseau)
            ipPremierApp = ad1
    return ipPremierApp


def dernAppa():
    """Permet de définir l'ip du dernier appareil de chaque sous réseau"""
    ab = nbAppareilSousRes1
    if classeMasque1 == "C":
        for cpt in range(nbSousReseau):
            if cpt == 0:
                cpt = cpt + 1
                ad2[3] = round(cpt * ab, 0)
                ipDernierApp = ad2
                ab = nbAppareilSousRes1
                ab = ab + 2
            else:
                ab = nbAppareilSousRes1
                ad2[3] = ad1[3]-1 + ab + 3
                ipDernierApp = ad2

    elif classeMasque1 == "B":
        for cpt in range(nbSousReseau):
            if cpt == 0:
                nbSousReseau2 = nbSousResPos(sousReseau)
                ad2[2] = 256 // nbSousReseau2 - 1
                ad2[3] = 254
                ipDernierApp = ad2
            else:
                cpt += 1
                nbSousReseau2 = nbSousResPos(sousReseau)
                ad2[2] = cpt * (256 // nbSousReseau2) -1
                ad2[3] = 254
                ipDernierApp = ad2

    elif classeMasque1 == "A":
        for cpt in range(nbSousReseau):
            cpt = cpt + 1
            ad2[1] = round(cpt * ab, 0)
            ipDernierApp = ad2
            ab = nbAppareilSousRes1
            ab = ab + 2
            ad2[1] = ad2[1] - 2
    return ipDernierApp

def nbSousResPos(sousReseau):
    """Permet de re-définir le nombre de sous réseaux en fonction du nombre sélectionné. Par exemple si l'utilisateur demande 5 sous réseaux, il faudra en faire 8

    Paramètre optionnel:
    sousReseau : le nombre de sous réseau demandé par l'utilisateur"""
    if sousReseau == 1:
        sousReseau = 1
    else :
        n = 1
        while sousReseau > 2**n:
            n += 1
        sousReseau = 2**n
    return sousReseau

def nbAppareilSousRes(nbSousReseau):
    """Permet de définir le nombre d'appareil possible par sous réseau"""
    if classeMasque1 == "C":
        nbAppareil = 254
        nbAppareilSousRes = nbAppareil // nbSousReseau -1
    elif classeMasque1 == "B":
        nbAppareil = 65534
        nbAppareilSousRes = nbAppareil // nbSousReseau -1
    elif classeMasque1 == "A":
        nbAppareil = 16777214
        nbAppareilSousRes = nbAppareil // nbSousReseau -1
    return nbAppareilSousRes

"""Si l'utilisateur choisi de calculer avec le nombre d'hotes"""

if repo == "o":
    nbHotes = nbHotes()
    ipDefault = ad1
    classeMasque1 = classeMasque(adm1)


    def nbSousResPos(nbHotes):
        """Permet de re-définir le nombre de sous réseaux en fonction du nombre sélectionné.

        Paramètre optionnel:
        nbHotes : le nombre d'appareil par sous réseau demandé par l'utilisateur"""
        if classeMasque1 == "C":
            if nbHotes <= 4:
                sousReseau = 64
            elif nbHotes <= 6:
                sousReseau = 32
            elif nbHotes <= 14:
                sousReseau = 16
            elif nbHotes <= 30:
                sousReseau = 8
            elif nbHotes <= 62:
                sousReseau = 4
            elif nbHotes <= 126:
                sousReseau = 2
            else:
                sousReseau = 1
            return sousReseau

        elif classeMasque == "B":
            if nbHotes <= 6:
                sousReseau = 8192
            elif nbHotes <= 14:
                sousReseau = 4096
            elif nbHotes <= 30:
                sousReseau = 2048
            elif nbHotes <= 62:
                sousReseau = 1024
            elif nbHotes <= 126:
                sousReseau = 512
            elif nbHotes <= 254:
                sousReseau = 256
            elif nbHotes <= 510:
                sousReseau = 128
            elif nbHotes <= 1022:
                sousReseau = 64
            elif nbHotes <= 2046:
                sousReseau = 32
            elif nbHotes <= 4094:
                sousReseau = 16
            elif nbHotes <= 8190:
                sousReseau = 8
            elif nbHotes <= 16382:
                sousReseau = 4
            elif nbHotes <= 32766:
                sousReseau = 2
            else:
                sousReseau = 1
            return sousReseau

    nbSousReseau = nbSousResPos(nbHotes)
    nbAppareilSousRes1 = nbAppareilSousRes(nbSousReseau)



    """Si l'utilisateur choisi de calculer avec le nombre de sous réseaux"""


elif repo == "n":
    sousReseau = sousRes()
    ipDefault = ad1
    classeMasque1 = classeMasque(adm1)
    nbSousReseau = nbSousResPos(sousReseau)
    nbAppareilSousRes1 = nbAppareilSousRes(nbSousReseau)



while nbSousReseau > 0:
    print("Le",nbSousReseau,"sous réseau")
    print("Vous avez saisie un masque de classe :", classeMasque1)
    print("Le nombre d'appareils par sous réseau est :", nbAppareilSousRes1)
    print("Le premier appareil est :", premierAppa())
    print("Le dernier appareil est :", dernAppa())
    print()
    nbSousReseau = nbSousReseau - 1