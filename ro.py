#utuliser la commande cette commande pour installler les library naicessaire
#pip install networkx matplotlib
#on a utulise ces library que pour afficher le reseau 



print('')
print('///////  ///////  ///    ///')
print('//   //  //         //   //  ')
print('///////  ///////      ///')
print('// //    //            //')
print('//  ///  ///////       //')
print('')
print('Projet RO réalisé par : -RAMDANI Ramdane -AMEUR Samy_Lyes -LARIBI Nacer -Sahouli Sabrina -Kadri Imane -Ketir Melissa -Rouas Massilva')
print('')


# Fonction pour afficher le tableau
def afficher_tableau(tableau):
    for ligne in tableau:
        ligne_formattee = " | ".join(map(str, ligne))
        print(f"| {ligne_formattee} |")
        print("-" * (len(ligne_formattee) + 4))

#dijkstra algorithm 
def dijkstra(tableau, sommets, sommet_depart, sommet_arrivee):
    # Initialisation 
    s = []  # Ensemble de sommets
    pi = {sommet: float('inf') for sommet in sommets}  # cout de chaque sommet et fkighasen ga3 + l'infinit
    pred = {sommet: None for sommet in sommets}  # Dictionnaire des predecesseurs de chaque sommet
    x = [sommet_depart]  # Liste des sommets a traiter

    pi[sommet_depart] = 0  # Initialisation du potentiel du sommet de depart en ecrasnt l'infinit deja donnee

    # Algorithme de Dijkstra
    while len(s) < len(sommets) and pi[x[-1]] < float('inf'): #j'ai pas utulise k en rigueuer j ai tester la taille de s par raport au nb de sommets
        for row in range(len(tableau)):
            # Parcours des arcs sortants du sommet en cours
            if x[-1] == tableau[row][0] and tableau[row][1] not in s: # le x[-1] c est pour acceder au dernier ellemet ajoutee a x dans la ligne 53
                u = tableau[row][1]  # Sommet destination de l'arc
                poids = tableau[row][2]  # Poids de l'arc

                # Mise a jour du poids si un chemin plus court est trouve
                if pi[x[-1]] + poids < pi[u]:
                    pi[u] = pi[x[-1]] + poids
                    pred[u] = x[-1]

        s.append(x[-1])  # Ajout du sommet en cours a l'ensemble des sommets traites
        min_pi = float('inf')
        for sommet in sommets:
            # Selection du prochain sommet a traiter (celui avec le plus petit cout)
            if sommet not in s and pi[sommet] < min_pi:
                min_pi = pi[sommet]
                x.append(sommet)

    # Reconstruction du chemin optimal et calcul de sa longueur
    chemin_optimal = [] # Liste pour stocker les sommets du chemin optimal
    longueur_chemin = -1 # Variable pour accumuler la longueur totale du chemin optimal
    current = sommet_arrivee  # Initialisation du sommet actuel avec le sommet d'arrivee
    while current is not None:
        chemin_optimal.insert(0, current)  # Ajout du sommet actuel au debut de la liste du chemin optimal
        # Vérification si le sommet actuel a un predecesseur
        if pred[current] is not None:
            for row in tableau:
                # Ajout du poids de l'arc au calcul de la longueur du chemin
                if row[0] == pred[current] and row[1] == current:
                    longueur_chemin += row[2]
        # Mise a jour du sommet actuel avec son predecesseur
        current = pred[current]

    return chemin_optimal, longueur_chemin



import networkx as nx
import matplotlib.pyplot as plt

#fonction qui affiche le reseau
def draw_graph(graph_table, chemin_optimal):
    G = nx.DiGraph()  

    for row in graph_table:
        G.add_edge(row[0], row[1], weight=row[2])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", arrowsize=15)
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='blue', font_size=10, label_pos=0.5)

    edge_list = [(chemin_optimal[i], chemin_optimal[i+1]) for i in range(len(chemin_optimal)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='red', width=2, arrowsize=15)

    plt.show()





# Saisie des sommets
sommets = []
nombre_de_sommets = int(input("Le nombre de sommets : "))
for i in range(nombre_de_sommets):
    sommet = input(f'Le sommet n {i+1} : ')
    sommets.append(sommet)
sommet_depart = input('entrer le sommet de depart : ')
sommet_arrivee = input('entrez le sommet d arrivee : ')

# Saisie des arcs
graph_table = []
saisie = True
while saisie:
    sommet_source = input('Sommet source (tapez "rey" pour terminer) : ')
    if sommet_source == 'rey':
        saisie = False
    else:
        sommet_dest = input('Destination : ')
        poids_arc=-1
        while poids_arc<0 :
            poids_arc = int(input(f'Poids de l arc {sommet_source}->{sommet_dest}"une entree positive svp (>=0)": '))
        graph_table.append([sommet_source, sommet_dest, poids_arc])

# Affichage du tableau

print("\nTableau des arcs :")
afficher_tableau(graph_table)
chemin_optimal, longueur_chemin = dijkstra(graph_table, sommets, sommet_depart, sommet_arrivee)

if not chemin_optimal:
    print("Il n'y a pas de chemin entre les sommets spécifiés.")
elif longueur_chemin ==-1:
    print("Votre graphe n'est pas connexe.")
else:
    print(f"Chemin optimal de {sommet_depart} à {sommet_arrivee} : {' -> '.join(chemin_optimal)}")
    print(f"Longueur du chemin optimal : {longueur_chemin+1}")
    draw_graph(graph_table, chemin_optimal)



