#librairie qui permet d'établire des connexions à distance
import socket
#on établie une connexion, en paramètre AF_INET signifie que c'est une adresse ip v4 sinon mettre AF_INET6 pour une ip v6
#ensuite indiquer le type de protocol que l'on souhaite utilisé et dans notre SOCK_STREAM fait référence au protocol TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#va permettre d'arrêter le scan après 3s d'attente
#sock.settimeout(20)
#on demande la saisie de l'ip pour faire le scan en fonction de l'ip
#si on veut le faire en local on met l'ip 127.0.0.1
ip = input("saisir l'ip pour réaliser le scan : ")

choice = int(input("Sélectionner la version du scan que vous voulez utiliser : \n \t 1 : vous scannez un seul port de votre choix \n \t 2 : vous scanner les ports selon une range de votre choix \n \t 3 : vous scanner plusieurs port de votre choix \n \t 4 : vous scanner les ports selon une range minimum et maximum de votre choix \n votre choix : "))
try :
    #vous scannez un seul port de votre choix
    if choice == 1 : 
        port = int(input("choissisez un seul port : "))
        #on test la connexion donc si la connexion echoue on affiche un message etc
        #si la fonction connect_ex renvoie 0 alors port ouvert sinon 1 donc port fermé
        if sock.connect_ex((ip, port)) :
            print("Port " + str(port) + " fermé")
        else : 
            print("Port " + str(port) + " ouvert")

    #vous scanner les ports selon une range de votre choix
    elif choice == 2 : 
        #on demande à l'utilisateur une range max pour faire une recherche jusqu'à la range (ex : 1024)
        portrange = int(input("range du port : "))
        #for i in range(la range que l'utilisateur à saisie (ex : 1024))
        #la boucle va tester tous les ports jusqu'au port 1024
        for port in range(portrange+1) :
            #on test la connexion donc si la connexion echoue on affiche un message etc
            if sock.connect_ex((ip, port)) :
                print("Port " + str(port) + " fermé")
            else : 
                print("Port " + str(port) + " ouvert")
            #puisqu'on veut faire un port après l'autre on augmente le port initial de 1 pour faire le port suivant 

    #vous scanner plusieurs port de votre choix
    elif choice == 3 : 
        #on demande les ports à l'utulisateur avec comme séparateur un /
        portlist = input("Port à scanner (mettre un slash '/' entre chaque port) : ")
        #on split la chaine ce qui va nous rendre une liste
        portsplit = portlist.split("/")
        #for i in le nombre de port qu'il y a dans la liste
        #la boucle va tester tous les ports qui se trouve dans la liste
        for port in portsplit :
            #on test la connexion donc si la connexion echoue on affiche un message etc
            if sock.connect_ex((ip, int(port))) :
                print("Port " + str(port) + " fermé")
            else : 
                print("Port " + str(port) + " ouvert")

    #vous scanner les ports selon une range minimum et maximum de votre choix
    elif choice == 4 :
        #on demande à l'utilisateur une range min pour faire une recherche à partir d'un minimum (ex : 22)
        portrangemin = int(input("range min du port : "))
        #on demande à l'utilisateur une range max pour faire une recherche jusqu'à la range (ex : 82)
        portrangemax = int(input("range max du port : "))
        #saisie min car on veut que ça commence à partir de ce port là
        #for i in range(la range min que l'utilisateur à saisie, la range max que l'utilisateur à saisie (ex : 22 jusqu'à 82))
        #la boucle va tester tous les ports jusqu'au port en partant du port min (soit 22 dans l'ex) jusqu'au port max (soit 82 dans l'ex)
        for port in range(portrangemin, portrangemax+1) :
            #on test la connexion donc si la connexion echoue on affiche un message etc
            if sock.connect_ex((ip, port)) :
                print("Port " + str(port) + " fermé")
            else : 
                print("Port " + str(port) + " ouvert")
            #puisqu'on veut faire un port après l'autre on augmente le port initial de 1 pour faire le port suivant 
except Exception as error :
    #on ferme les sockets sinon ça va ouvrir pleins de socket
    print("erreur")
finally :
    sock.close()
