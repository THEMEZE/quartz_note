---
title: "Exercice 2 — Son, Doppler et cône de Mach : de la vitesse du son au bang supersonique"
tags:
  - tp
  - ondes-mecaniques-sonores-electromagnetiques-et-lumineuses
---

[[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/index|⬅ Retour]]

### Exercice 2. Son, Doppler et cône de Mach : de la vitesse du son au bang supersonique

Un avion qui passe au-dessus de nous fait entendre un son qui descend d'un ton au moment où il nous dépasse : c'est l'effet Doppler. Quand l'avion va plus vite que le son, il traîne derrière lui un cône d'ondes de choc, le **cône de Mach**, entendu au sol comme un « bang ». Ce TP reprend ces trois idées (vitesse du son, Doppler, Mach) avec un simple smartphone.

**q1.** (a) Calculer $c$ à partir des données de l'écho (le son fait un aller-retour). (b) Estimer l'incertitude en supposant $\Delta d=0{,}2\ \text{m}$ et $\Delta t=0{,}005\ \text{s}$. (c) Comparer avec la formule $c=331{,}3\sqrt{1+\theta/273{,}15}$. (d) Quelle est la variation de $c$ pour une température de $-56{,}5\ ^\circ\text{C}$ ?

**q2.** Mach et altitude. Un avion de ligne vole à la vitesse vraie $v=236\ \text{m}\cdot\text{s}^{-1}$ ($850\ \text{km/h}$). Calculer son nombre de Mach (a) au niveau de la mer à $15\ ^\circ\text{C}$ et (b) à $11\ \text{km}$ où $\theta=-56{,}5\ ^\circ\text{C}$. Un chasseur croise à $M=1{,}5$ : calculer l'angle du cône de Mach. Concorde volait à $M=2{,}02$ à $18\ \text{km}$ d'altitude : à quelle distance derrière l'avion se situe le point du sol où l'on entend le bang au moment où l'avion est à la verticale de ce point ? (voir la construction de la question 4).

> [!tip]- 💡 Coup de pouce
> **Formule**
>
> $\sin\mu=\dfrac{1}{M}$. Le point du sol touché à l'instant $t$ par le cône est à la distance horizontale $\dfrac{h}{\tan\mu}$ derrière l'avion.


**q3.** Doppler. (a) Établir $f_a=\dfrac{f_0}{1-v/c}$ pour une source qui se rapproche d'un récepteur immobile, et $f_r=\dfrac{f_0}{1+v/c}$ pour un éloignement. (b) Montrer que $v=c\,\dfrac{f_a-f_r}{f_a+f_r}$ (indépendante de $f_0$). (c) Calculer $v$ avec les données ($c=343\ \text{m/s}$). (d) Déduire l'incertitude sur $v$ si $\Delta f=3\ \text{Hz}$.

> [!tip]- 💡 Coup de pouce
> **Longueur d'onde reçue**
>
> Pendant une période $T_0$, la source parcourt $vT_0$. La longueur d'onde reçue est $\lambda_a=(c-v)T_0$, et $f_a=\dfrac{c}{\lambda_a}$.


**q4.** Construction de Mach. Une source se déplace sur un axe à la vitesse $v=Mc$ et émet une impulsion à chaque instant $t_n=n\tau$. (a) Décrire les fronts à l'instant $t=5\tau$ pour $M=0{,}5$, $M=1$ et $M=2$ : la source est-elle devant ou derrière ses propres fronts ? (b) Montrer que pour $M>1$ l'enveloppe des fronts est un cône de demi-angle $\mu$ tel que $\sin\mu=\dfrac{c\,t}{v\,t}=\dfrac{1}{M}$. (c) Mesurer $\mu$ sur la construction pour $M=2$ et $M=3$ et comparer à $30^\circ$ et $19{,}5^\circ$.

**q5.** (*) Hélice. Une hélice de diamètre $D=1{,}9\ \text{m}$ tourne à $2500\ \text{tr/min}$ ; l'avion vole à $60\ \text{m}\cdot\text{s}^{-1}$ au niveau de la mer ($c=340\ \text{m/s}$). Calculer la vitesse en bout de pale et le nombre de Mach correspondant. Pourquoi la pointe des pales est-elle la partie la plus bruyante ? À quel régime le bout de pale atteindrait-il $M=1$ ?
