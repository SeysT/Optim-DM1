Autheur : Thibaut Seys

Date : 01/02/2018

Lien github : https://github.com/SeysT/Optim-DM1

# Optimisation - Devoir-Maison 1 : Mots Croisés

## Organisation et utilisation du code source

La modélisation et la résolution du problème se situent dans le fichier `crossword_solver.py`. Ce fichier attend deux arguments obligatoires et un optionnel. Le premier est le chemin vers le fichier contenant la grille de mots croisés, le deuxième le chemin vers le fichier contenant le vocabulaire et le troisième, optionnel, permet de maintenir ou non l'arc de consistence. Si un troisième argument est présent, peu importe sa valeur, alors l'arc sera maintenu et s'il n'est pas présent alors l'arc ne le sera pas. Voici quelques examples d'utilisation :

```sh
python crossword_solver.py Data/crossword1.txt Data/words1.txt
python crossword_solver.py Data/crossword1.txt Data/words1.txt maintain_arc
python crossword_solver.py Data/crossword2.txt Data/words2.txt
python crossword_solver.py Data/crossword2.txt Data/words2.txt maintain_arc
```

## Choix de modélisation du problème

Pour modéliser le problème sous forme de programmation par contraintes, nous allons avoir besoin de définir les variables du modèle et leur domaine de définitions ainsi que les contraintes les reliant. 

### Modélisation des variables

En ce qui concerne les variables du problème, nous avons choisi de les séparer en deux types différents :
1. Les variables de types 'cases' : elles représentent la valeur que peut prendre une case libre de la grille. Leur domaine correspond donc à l'ensemble des lettres et symboles que l'on peut trouver dans le vocabulaire. Pour nommer ces variables nous allons utiliser un tuple dont le premier élément sera la string 'c' et dont le second élément sera un tuple contenant les coordonnées de la case libre représentée : `('c', (x, y))`.
2. Les variables de types 'segments' : elles représentent le mot que peut contenir un segment libre au sein de la grille. Leur domaine de définition correspond donc à l'ensemble des mots du vocabulaire ayant la longueur du segment. Pour nommer ces variables nous allons utiliser un tuple dont le premier élément sera la string 's', et le second un autre tuple contenant la liste des coordonnées des cases du segment, elles aussi sous forme de tuple : `('s', ((x, y), ...))`.

### Modélisation des contraintes

Pour compléter la modélisation de notre problème, nous allons établir les contraintes exclusivement entre les deux différents types de variables de notre problème. Pour chaque variable de type 'case', nous allons regarder les variables de type 'segment' qui contiennent cette case et on note sa position dans le segment. Pour chacune d'entre elles on regarde chaque mot de son domaine de définition et on ajoute une contrainte liant la lettre du mot à la position correspondante à la position de la case dans le mot et le mot en lui même. Par exemple, on a une case c à la 2e position d'un segment s de longueur 3. Les mots de l'ensemble de définition de s sont 'tea' et 'eat'. On ajoute donc les deux contraintes ('e', 'tea') et ('a', 'eat') à notre modèle.

## Influence de l'arc de consistence

Pour mesurer l'influence de l'arc de consistence sur la perfomance de notre modèle, nous allons le résoudre de deux manières : avec et sans maintien de l'arc de consistence. Pour cela nous allons faire tourner notre programme python sur les fichiers `Data/crossword2.txt` et `Data/words2.txt` et mesurer le temps de résolution (appel à la méthode solve() de l'objet constraint_programming). Sans maintien l'arc nous obtenons :

```sh
$ python crossword_solver.py Data/crossword2.txt Data/words2.txt
Loading data from file...
Creating solveur and variables...
Adding constraints...
Solving...
Solved in 0.0988471508026123 seconds
# # # # # # # # # # # # # # #
# # # N e w s w e e k l y # #
# f # o # r # i # f # u # # #
# o b v i a t e # f u n n y #
# r # a # p # l # e # a # a #
# f a k e # e d u c a t o r #
# e # # # N # s # t # i # d #
# i t c h e s # D o r c a s #
# t # l # w # A # r # # # t #
# u n e a s i l y # N a z i #
# r # a # w # i # L # v # c #
# e e r i e # s k y h o o k #
# # # e # e # o # l # w # s #
# # b r o k e n n e s s # # #
# # # # # # # # # # # # # # #
```

Et avec maintien de l'arc :

```sh
$ python crossword_solver.py Data/crossword2.txt Data/words2.txt maintain_arc
Loading data from file...
Creating solveur and variables...
Adding constraints...
Solving...
Solved in 4.570987701416016 seconds
# # # # # # # # # # # # # # #
# # # C h i c a g o a n s # #
# p # u # b # n # p # i # # #
# r e b u i l t # a b b e y #
# i # a # d # i # q # b # a #
# o w n s # S c h u y l e r #
# r # # # p # s # e # e # d #
# i d e a l s # b l a s t s #
# t # m # a # b # y # # # t #
# i m p l i c i t # F i j i #
# e # t # n # g # i # v # c #
# s w i n e # g i m m i c k #
# # # l # s # e # p # e # s #
# # h y s t e r e s i s # # #
# # # # # # # # # # # # # # #
```

En répétant ces commandes plusieurs fois, nous avons toujours un écart de l'ordre de 10^2 entre les deux méthodes. Nous pouvons donc conclure expérimentalement ici que le maintien de l'arc de consistence dégrade les performances dans le cas de notre problème.

## Liste des fichiers utilisés

- **crossword_solver.py** : implémentation de la modélisation et la résolution du problème
- **constraint_programming.py** : solver de programmation par contrainte fourni par l'énoncé
- **utils.py** : fonctions permettant la résolution du problème
- **Data/crossword1.txt** : première grille de mots croisés fournie par l'énoncé
- **Data/crossword2.txt** : seconde grille de mots croisés fournie par l'énoncé
- **Data/words1.txt** : premier jeu de vocabulaire fourni par l'énoncé
- **Data/words2.txt** : second jeu de vocabulaire fourni par l'énoncé
