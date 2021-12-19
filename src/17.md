### Observations

```
..........................................
..........................................
................#....#....................
..........#..............#................
..........................................
...S........................#.............
..........................................
..........................................
..............................#...........
..........................................
.......................TTTTTTTTTTT........
.......................TTTTTTTTTTT........
.......................TTTTTTTT#TT........
.......................TTTTTTTTTTT........
.......................TTTTTTTTTTT........
.......................TTTTTTTTTTT........
..........................................
..........................................
..........................................
```

O.01 À cause du drag, il peut exister des vx tels que x n'atteindra jamais
xmin. Par exemple, vx = 1, vx devient tout de suite zéro, x ne dépassera jamais
1.

O.02 Il existe des vitesses pour lesquelles la sonde rate la cible, mais en
augmentant encore la vitesse, la sonde touche à nouveau la cible.

### Hypothèses

H.01 La cible est toujours à droite, le vx max recherché est toujours positif.

H.02 La cible est toujours en dessous, Le vy max recherché est toujours positif.

H.03 Pour y, ça semble un peu plus compliqué à cause de l'inversion de signe, à voir.

H.04 Il semble que grâce à la gravité, il y aura toujours un y tel que y < ymin.

H.05 Il est possible de traiter d'abord vy, puis vx (ou l'inverse). Pour un vy
donné, tous les y seront identiques quel que soit vx et réciproquement.

### Propositions

Comme la gravité fait que y va dépasser ymin (H.04), commencer par trouver vy ?

Commencer par un vx dont on est certain qu'il est trop grand, puis décrémenter
jusqu'à ce que x soit dans l'interval souhaité.

Problème : pour certaines valeurs il est possible que x loupe l'interval et se
retrouve dans une boucle infinie (O.01) => arrêter la recherche dès que vx
atteint zéro.

### Questions

Suite à O.02, comment savoir qu'il n'existe pas de vitesse supérieur où la
sonde touche à nouveau la cible ?


(23,-10), (25,-9), (27,-5), (29,-6), (22,-6), (21,-7), (9,0), (27,-7), (24,-5),
(25,-7), (26,-6), (25,-5), (6,8), (11,-2), (20,-5), (29,-10), (6,3), (28,-7),
(8,0), (30,-6), (29,-8), (20,-10), (6,7), (6,4), (6,1), (14,-4), (21,-6),
(26,-10), (7,-1), (7,7), (8,-1), (21,-9), (6,2), (20,-7), (30,-10), (14,-3),
(20,-8), (13,-2), (7,3), (28,-8), (29,-9), (15,-3), (22,-5), (26,-8), (25,-8),
(25,-6), (15,-4), (9,-2), (15,-2), (12,-2), (28,-9), (12,-3), (24,-6), (23,-7),
(25,-10), (7,8), (11,-3), (26,-7), (7,1), (23,-9), (6,0), (22,-10), (27,-6),
(8,1), (22,-8), (13,-4), (7,6), (28,-6), (11,-4), (12,-4), (26,-9), (7,4),
(24,-10), (23,-8), (30,-8), (7,0), (9,-1), (10,-1), (26,-5), (22,-9), (6,5),
(7,5), (23,-6), (28,-10), (10,-2), (11,-1), (20,-9), (14,-2), (29,-7), (13,-3),
(23,-5), (24,-8), (27,-9), (30,-7), (28,-5), (21,-10), (7,9), (6,6), (21,-5),
(27,-10), (7,2), (30,-9), (21,-8), (22,-7), (24,-9), (20,-6), (6,9), (29,-5),
(8,-2), (27,-8), (30,-5), (24,-7)
