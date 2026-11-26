---
title: "Exercice 6 — Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation"
tags:
  - td
  - chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/index|⬅ Retour]] · <a href="/pdfs/td4_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 6. Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation *(facultatif)*

*Difficulté ●●●●○ · ⏱ 90 min · Type : Complément original, problème guidé de type concours*

**Exercice complémentaire original (niveau 2).** Trois masses ponctuelles identiques $m=0{,}10$ kg, notées $M_1,M_2,M_3$, glissent sans frottement sur une tige horizontale fixe entre deux parois rigides. Elles sont reliées entre elles et aux parois par quatre ressorts identiques de raideur $k=20\ \mathrm{N\cdot m^{-1}}$ et de longueur à vide $\ell_0$ : paroi -- $M_1$ -- $M_2$ -- $M_3$ -- paroi. À l'équilibre, tous les ressorts sont à leur longueur à vide. On note $x_i(t)$ l'écart de $M_i$ à sa position d'équilibre et $\omega_0=\sqrt{k/m}$.


> [!question]- 🪝 Accroche
> **Combien de modes, et à quoi ressemblent-ils ?**
>
> *Durée de l'introduction : 5 min*
>
> *Trois masses identiques sont reliées en chaîne entre deux murs. Combien de fréquences propres le système possède-t-il ? La masse du milieu peut-elle rester immobile dans un mode ?*
>
> **Idée clé : un système de $N$ masses a $N$ modes ; leur forme se déduit de la symétrie.** Les modes sont soit symétriques, soit antisymétriques par rapport au centre. Dans un mode antisymétrique, la masse centrale reste immobile (c'est un nœud).




> [!abstract]- 🧠 À savoir avant
> **Exercices 1, 2 et 4 du TD4**
>
> Équations couplées, matrice des raideurs $K$, déterminant, modes propres, découplage par symétrie.
>
> **Algèbre linéaire**
>
> Valeurs propres d'une matrice symétrique réelle (réelles, vecteurs propres orthogonaux) ; déterminant $3\times3$ ; changement de base.




> [!info]- 🎯 Ce que tu sauras faire
> **Écrire un système de trois oscillateurs couplés**
>
> Savoir lire les signes de la matrice $K$ à partir des allongements des ressorts, sans approximation : en une dimension et pour des ressorts alignés, les équations sont *exactes*.
>
> **Utiliser une symétrie pour réduire la taille du problème**
>
> Séparer modes symétriques et antisymétriques par rapport à l'échange $M_1\leftrightarrow M_3$ ; ramener le problème $3\times3$ à un problème $2\times2$ et un problème $1\times1$.
>
> **Résoudre à la mathématicienne et comparer**
>
> Obtenir par le déterminant les trois pulsations, par les vecteurs propres les trois formes de mode, puis décomposer une condition initiale.
>
> **Estimer l'effet d'une petite perturbation**
>
> Calculer au premier ordre le décalage de pulsation propre quand une masse est modifiée (formule de Rayleigh).




> [!note]- 🧮 Outils mathématiques
> **Déterminant d'une matrice $3\times3$ tridiagonale**
>
> $\det\begin{pmatrix}a&-1&0\\-1&a&-1\\0&-1&a\end{pmatrix}=a(a^2-1)-a=a(a^2-2)$ en posant $a=2-\lambda$.
>
> **Formule de Rayleigh (perturbation du premier ordre)**
>
> $\omega^2=\dfrac{u^{\mathsf T}Ku}{u^{\mathsf T}Mu}$ (quotient de Rayleigh) : stationnaire aux modes propres, donc l'erreur sur $\omega^2$ est du second ordre en l'erreur sur $u$.
>
> **Orthogonalité des modes**
>
> Pour $M=mI$ les vecteurs propres de $K$ sont orthogonaux au sens usuel : $c_p=\vec u_p\cdot X(0)$ avec $\vec u_p$ normalisé.



**q1.** **Question 1.** Établir les équations du mouvement des trois masses. Montrer qu'elles sont *exactes* (sans approximation des petits déplacements) et les mettre sous la forme $M\ddot X+KX=0$.


> [!tip]- 💡 Coup de pouce
> **Allongements**
>
> Écrivez l'allongement algébrique de chacun des quatre ressorts en fonction de $x_1,x_2,x_3$. Le premier est attaché à la paroi : son allongement vaut $x_1$.
>
> **Signe des forces**
>
> Un ressort allongé tire ses deux extrémités l'une vers l'autre. Pour chaque masse, écrivez la somme des deux forces.




> [!success]- ✅ Correction
> **Équations**
>
> $$m\ddot x_1=-kx_1+k(x_2-x_1),\quad m\ddot x_2=-k(x_2-x_1)+k(x_3-x_2),\quad m\ddot x_3=-k(x_3-x_2)-kx_3,$$
> soit $\ddot X+\omega_0^2\mathcal KX=0$ avec $\mathcal K=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}$.




> [!example]- 📝 Solution détaillée
> **Allongements algébriques**
>
> Axe $x$ de la paroi gauche vers la paroi droite ; les masses sont repérées par leur écart $x_i$ à l'équilibre. Les quatre ressorts ont les allongements : $e_0=x_1$ (paroi--$M_1$), $e_1=x_2-x_1$, $e_2=x_3-x_2$, $e_3=-x_3$ (le dernier est comprimé quand $M_3$ avance vers la paroi droite). Ces expressions sont *exactes* : en une dimension, avec des ressorts alignés, la longueur d'un ressort est simplement la différence des abscisses de ses extrémités ; il n'y a pas de linéarisation.
>
> **Forces**
>
> Le ressort $i$ exerce sur son extrémité de gauche $+ke_i$ et sur celle de droite $-ke_i$. Par application directe :
> $M_1$ : ressort 0 à sa gauche (force $-kx_1$) et ressort 1 à sa droite (force $+k(x_2-x_1)$) ; $M_2$ : ressort 1 à sa gauche ($-k(x_2-x_1)$) et ressort 2 à sa droite ($+k(x_3-x_2)$) ; $M_3$ : ressort 2 à sa gauche ($-k(x_3-x_2)$), ressort 3 à sa droite ($-kx_3$).
>
> **Forme matricielle**
>
> $$m\ddot x_1=-2kx_1+kx_2,\qquad m\ddot x_2=kx_1-2kx_2+kx_3,\qquad m\ddot x_3=kx_2-2kx_3,$$
> $$M\ddot X+KX=0,\quad M=mI_3,\quad K=k\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}.$$
> La matrice $K$ est symétrique (réciprocité : l'action de $M_i$ sur $M_j$ vaut celle de $M_j$ sur $M_i$), tridiagonale (un ressort ne relie que des voisins) ; la diagonale vaut $2k$ (chaque masse est reliée à deux ressorts). *Contrôle* : décalage uniforme $X=(1,1,1)$ : $KX=k(1,0,1)\ne0$ puisque les extrémités sont attachées aux parois.



**q2.** **Question 2.** *Méthode du physicien.* En utilisant la symétrie du système par rapport à la masse centrale, découpler le problème : (a) montrer qu'il existe un mode antisymétrique $x_1=-x_3$, $x_2=0$ et calculer sa pulsation ; (b) pour les mouvements symétriques $x_1=x_3$, se ramener à un système à deux inconnues et en déduire les deux autres pulsations.


> [!tip]- 💡 Coup de pouce
> **Antisymétrique**
>
> Posez $x_1=-x_3=a\cos\omega t$ et $x_2=0$ dans les trois équations. Une seule équation est non triviale.
>
> **Symétrique**
>
> Posez $x_3=x_1$. La première et la troisième équations coïncident ; il reste deux équations en $x_1$ et $x_2$. Attention : le système $2\times2$ obtenu n'est pas symétrique (coefficients $-1$ et $-2$) car $x_2$ est couplé à deux voisins.




> [!success]- ✅ Correction
> **Résultats**
>
> Antisymétrique : $\omega^2=2\omega_0^2$. Symétrique : $\ddot x_1+2\omega_0^2x_1-\omega_0^2x_2=0$, $\ddot x_2+2\omega_0^2x_2-2\omega_0^2x_1=0$, de matrice $\omega_0^2\begin{pmatrix}2&-1\\-2&2\end{pmatrix}$ ; $\omega^2=(2\pm\sqrt2)\omega_0^2$.




> [!example]- 📝 Solution détaillée
> **Symétrie et sous-espaces**
>
> L'échange $M_1\leftrightarrow M_3$ (symétrie par rapport à $M_2$) laisse le système invariant : toute solution se décompose en une partie symétrique $(x_1=x_3)$ et une partie antisymétrique $(x_1=-x_3,\ x_2=0)$ ; ces deux parties évoluent indépendamment (c'est le découplage « à la physicienne » : on forme $x_1\pm x_3$).
>
> **Partie antisymétrique**
>
> $a=\dfrac{x_1-x_3}2$ : en retranchant la troisième équation de la première, $\ddot a=-2\omega_0^2a+\omega_0^2\dfrac{x_2-x_2}{2}=-2\omega_0^2a$ (les termes en $x_2$ se compensent). Donc $\omega_a^2=2\omega_0^2$ et la seconde équation est vérifiée avec $x_2=0$ (en effet $x_1+x_3=0$). Interprétation : $M_2$ est un nœud ; $M_1$ et $M_3$ vibrent chacune comme une masse attachée à deux ressorts dont l'extrémité centrale est fixe : $\omega^2=2k/m$.
>
> **Partie symétrique**
>
> Avec $s=x_1+x_3$ et $x_2$ : la somme des équations 1 et 3 donne $\ddot s+2\omega_0^2s-2\omega_0^2x_2=0$ ; l'équation 2 s'écrit $\ddot x_2+2\omega_0^2x_2-\omega_0^2s=0$. En prenant $x_1=x_3=s/2$ : $\ddot x_1+2\omega_0^2x_1-\omega_0^2x_2=0$ et $\ddot x_2+2\omega_0^2x_2-2\omega_0^2x_1=0$. Cherchons $x_i=A_i\cos\omega t$ :
> $$(2\omega_0^2-\omega^2)A_1-\omega_0^2A_2=0,\qquad-2\omega_0^2A_1+(2\omega_0^2-\omega^2)A_2=0.$$
> Déterminant : $(2\omega_0^2-\omega^2)^2-2\omega_0^4=0$, soit $2\omega_0^2-\omega^2=\pm\sqrt2\,\omega_0^2$ : $\omega^2=(2\mp\sqrt2)\omega_0^2$.
>
> **Formes des modes**
>
> Pour $\omega^2=(2-\sqrt2)\omega_0^2$ : $A_2/A_1=\sqrt2$ (mode $(1,\sqrt2,1)$, sans nœud) ; pour $\omega^2=(2+\sqrt2)\omega_0^2$ : $A_2/A_1=-\sqrt2$ (mode $(1,-\sqrt2,1)$, deux nœuds entre les masses). Le bloc symétrique $\begin{pmatrix}2&-1\\-2&2\end{pmatrix}$ n'est pas symétrique : c'est normal, car on a regroupé $x_1$ et $x_3$ et la variable $s$ n'est pas normalisée ; avec $\tilde x=\sqrt2x_1=s/\sqrt2$ il le devient $\begin{pmatrix}2&-\sqrt2\\-\sqrt2&2\end{pmatrix}$.



**q3.** **Question 3.** *Méthode du mathématicien.* Calculer les valeurs propres et vecteurs propres de $\mathcal K$ par le déterminant. Vérifier l'orthogonalité des vecteurs propres, donner la matrice de passage $P$ et la matrice diagonale $D=P^{\mathsf T}\mathcal KP$. Comparer avec la question 2.


> [!tip]- 💡 Coup de pouce
> **Déterminant**
>
> Posez $a=2-\lambda$ : $\det(\mathcal K-\lambda I)=a(a^2-2)$. Quelles sont les trois racines ?
>
> **Vecteurs propres**
>
> Pour chaque $\lambda$, résolvez $(\mathcal K-\lambda I)\vec u=0$ : la première ligne donne $u_2$ en fonction de $u_1$, la deuxième $u_3$.




> [!success]- ✅ Correction
> **Résultats**
>
> $\lambda\in\{2-\sqrt2,\ 2,\ 2+\sqrt2\}$ ; $\vec u_1=\tfrac12(1,\sqrt2,1)$, $\vec u_2=\tfrac1{\sqrt2}(1,0,-1)$, $\vec u_3=\tfrac12(1,-\sqrt2,1)$ ; $\omega_p^2=\lambda_p\omega_0^2=4\omega_0^2\sin^2\dfrac{p\pi}8$.




> [!example]- 📝 Solution détaillée
> **Valeurs propres**
>
> $\det(\mathcal K-\lambda I)=\begin{vmatrix}a&-1&0\\-1&a&-1\\0&-1&a\end{vmatrix}=a(a^2-1)-(-1)\cdot(-a)\cdot1=a(a^2-1)-a=a(a^2-2)$ avec $a=2-\lambda$. Racines : $a=0$ ($\lambda=2$) ou $a=\pm\sqrt2$ ($\lambda=2\mp\sqrt2$). Les trois racines sont réelles et distinctes (matrice symétrique réelle), positives (matrice définie positive : les ressorts attachés aux parois suppriment la translation d'ensemble). Les pulsations sont $\omega_p=\omega_0\sqrt{\lambda_p}$ : $\omega_1=0{,}765\,\omega_0$, $\omega_2=1{,}414\,\omega_0$, $\omega_3=1{,}848\,\omega_0$.
>
> **Vecteurs propres**
>
> Ligne 1 : $a u_1-u_2=0$, donc $u_2=au_1$ ; ligne 3 : $u_2=au_3$ donc $u_1=u_3$ (si $a\ne0$) ; $\lambda=2-\sqrt2$ ($a=\sqrt2$) : $(1,\sqrt2,1)$ ; $\lambda=2+\sqrt2$ ($a=-\sqrt2$) : $(1,-\sqrt2,1)$ ; $\lambda=2$ ($a=0$) : $u_2=0$ et $-u_1-u_3=0$ : $(1,0,-1)$.
>
> **Orthogonalité et matrice de passage**
>
> $\vec u_1\cdot\vec u_3\propto1-2+1=0$, $\vec u_1\cdot\vec u_2\propto1-1=0$, $\vec u_2\cdot\vec u_3\propto1-1=0$ : orthogonaux (théorème spectral). Normalisés : $P=\begin{pmatrix}\tfrac12&\tfrac1{\sqrt2}&\tfrac12\\\tfrac{\sqrt2}2&0&-\tfrac{\sqrt2}2\\\tfrac12&-\tfrac1{\sqrt2}&\tfrac12\end{pmatrix}$ (colonnes $\vec u_1,\vec u_2,\vec u_3$), $P^{\mathsf T}P=I$ et $D=P^{\mathsf T}\mathcal KP=\mathrm{diag}(2-\sqrt2,\,2,\,2+\sqrt2)$. Les coordonnées normales $q=P^{\mathsf T}X$ obéissent à $\ddot q_p+\omega_p^2q_p=0$ : trois oscillateurs indépendants.
>
> **Formule générale**
>
> $\omega_p^2=4\omega_0^2\sin^2\dfrac{p\pi}{8}$ pour $p=1,2,3$ : $4\sin^2\frac\pi8=2-\sqrt2$, $4\sin^2\frac\pi4=2$, $4\sin^2\frac{3\pi}8=2+\sqrt2$. C'est le cas $N=3$ de $\omega_p=2\omega_0\sin\dfrac{p\pi}{2(N+1)}$.
>
> **Comparaison des deux méthodes**
>
> La symétrie donne le même résultat plus vite (un problème $1\times1$ et un $2\times2$) : à utiliser dès qu'une symétrie est visible. La diagonalisation ne dépend pas de la symétrie et marche en général (exercice 2) ; ici elle n'apporte que la *justification* (orthogonalité, complétude) : les trois modes constituent une base, donc toute condition initiale se décompose.



**q4.** **Question 4.** *Décomposition modale.* À $t=0$, on écarte $M_1$ de $a$ vers la droite, les autres masses étant à l'équilibre, et on lâche toutes les masses sans vitesse. Calculer $x_1(t),x_2(t),x_3(t)$. Pour $k=20\ \mathrm{N\cdot m^{-1}}$ et $m=0{,}10$ kg, calculer les fréquences propres $f_p$.


> [!tip]- 💡 Coup de pouce
> **Coefficients**
>
> Avec la base orthonormée $\vec u_p$ : $c_p=\vec u_p\cdot X(0)$ ; vitesses nulles donc $x(t)=\sum_pc_p\vec u_p\cos\omega_pt$.




> [!success]- ✅ Correction
> **Résultat**
>
> $c_1=\dfrac a2,\ c_2=\dfrac a{\sqrt2},\ c_3=\dfrac a2$ ; $x_1=\dfrac a4\cos\omega_1t+\dfrac a2\cos\omega_2t+\dfrac a4\cos\omega_3t$ ; $x_2=\dfrac{\sqrt2a}4(\cos\omega_1t-\cos\omega_3t)$ ; $x_3=\dfrac a4\cos\omega_1t-\dfrac a2\cos\omega_2t+\dfrac a4\cos\omega_3t$. $f_1=1{,}72$ Hz, $f_2=3{,}18$ Hz, $f_3=4{,}16$ Hz.




> [!example]- 📝 Solution détaillée
> **Coefficients modaux**
>
> $X(0)=(a,0,0)^{\mathsf T}$ : $c_1=\vec u_1\cdot X(0)=\dfrac a2$, $c_2=\dfrac a{\sqrt2}$, $c_3=\dfrac a2$. Vitesses nulles : tous les déphasages sont nuls et
> $$X(t)=\frac a2\cdot\frac12\begin{pmatrix}1\\\sqrt2\\1\end{pmatrix}\cos\omega_1t+\frac a{\sqrt2}\cdot\frac1{\sqrt2}\begin{pmatrix}1\\0\\-1\end{pmatrix}\cos\omega_2t+\frac a2\cdot\frac12\begin{pmatrix}1\\-\sqrt2\\1\end{pmatrix}\cos\omega_3t.$$
> Contrôles : $x_1(0)=\dfrac a4+\dfrac a2+\dfrac a4=a$ ; $x_2(0)=\dfrac{\sqrt2a}4(1-1)=0$ ; $x_3(0)=\dfrac a4-\dfrac a2+\dfrac a4=0$ ; $\dot X(0)=0$.
>
> **Fréquences**
>
> $\omega_0=\sqrt{k/m}=\sqrt{200}=14{,}14\ \mathrm{rad\cdot s^{-1}}$ ; $\omega_1=10{,}82$, $\omega_2=20{,}0$, $\omega_3=26{,}13\ \mathrm{rad\cdot s^{-1}}$ ; $f_1=1{,}72$ Hz, $f_2=3{,}18$ Hz, $f_3=4{,}16$ Hz. Le mouvement n'est pas périodique en général : les rapports $\omega_p/\omega_q$ ne sont pas rationnels ($\omega_3/\omega_1=\sqrt{(2+\sqrt2)/(2-\sqrt2)}=1+\sqrt2$, irrationnel).
>
> **Interprétation**
>
> Le mouvement est une superposition de trois sinusoïdes de pulsations différentes : l'énergie se redistribue entre les masses (comme les battements à deux oscillateurs), sans jamais quitter les trois modes. L'énergie de chaque mode est constante : $E_p=\tfrac12m\,\omega_p^2c_p^2$ : $E_1=\tfrac12m\omega_1^2\dfrac{a^2}4$, $E_2=\tfrac12m\omega_2^2\dfrac{a^2}2$, $E_3=\tfrac12m\omega_3^2\dfrac{a^2}4$. La part de l'énergie dans chaque mode se lit sur $\omega_p^2c_p^2$.



**q5.** **Question 5.** *Perturbation.* On remplace $M_3$ par une masse $m(1+\varepsilon)$ avec $\varepsilon\ll1$. Montrer, par le quotient de Rayleigh, que la pulsation du mode $p$ est décalée de $\delta(\omega_p^2)=-\varepsilon\,\omega_p^2\,u_{p,3}^2$ où $u_{p,3}$ est la troisième composante du mode normalisé. Application numérique pour $\varepsilon=0{,}02$ ; quel mode est le plus affecté ? Pourquoi $(1,0,-1)$ l'est-il quand même ?


> [!tip]- 💡 Coup de pouce
> **Quotient de Rayleigh**
>
> $\omega^2=\dfrac{X^{\mathsf T}KX}{X^{\mathsf T}MX}$ est stationnaire aux modes propres ; au premier ordre on peut donc l'évaluer avec l'ancien vecteur propre et la nouvelle masse.




> [!success]- ✅ Correction
> **Résultat**
>
> $\omega_p'^2\simeq\omega_p^2\big(1-\varepsilon u_{p,3}^2\big)$ avec $u_{1,3}^2=u_{3,3}^2=\tfrac14$ et $u_{2,3}^2=\tfrac12$ : $\dfrac{\delta\omega_1^2}{\omega_1^2}=\dfrac{\delta\omega_3^2}{\omega_3^2}=-\dfrac\varepsilon4$, $\dfrac{\delta\omega_2^2}{\omega_2^2}=-\dfrac\varepsilon2$. Le mode $(1,0,-1)$ est le plus affecté (en proportion).




> [!example]- 📝 Solution détaillée
> **Quotient de Rayleigh**
>
> Pour $M'=m\,\mathrm{diag}(1,1,1+\varepsilon)$ : $\omega^2=\dfrac{X^{\mathsf T}KX}{X^{\mathsf T}M'X}$. En $X=\vec u_p$ (non perturbé, $\vec u_p^{\mathsf T}\vec u_p=1$) : $\omega'^2\simeq\dfrac{m\omega_p^2}{m(1+\varepsilon u_{p,3}^2)}\simeq\omega_p^2(1-\varepsilon u_{p,3}^2)$. L'erreur est du second ordre ($O(\varepsilon^2)$) parce que le quotient est stationnaire : une erreur d'ordre $\varepsilon$ sur le vecteur donne une erreur d'ordre $\varepsilon^2$ sur la valeur.
>
> **Application numérique**
>
> $\varepsilon=0{,}02$ : $\delta\omega_1^2/\omega_1^2=-0{,}5\,\%$ ; $\delta\omega_2^2/\omega_2^2=-1\,\%$ ; $\delta\omega_3^2/\omega_3^2=-0{,}5\,\%$ ; soit sur les pulsations $-0{,}25\,\%$, $-0{,}5\,\%$, $-0{,}25\,\%$. (Vérifié numériquement par diagonalisation du problème généralisé.)
>
> **Interprétation**
>
> Le décalage est proportionnel à la *fraction de l'énergie cinétique portée par $M_3$* dans le mode : $\tfrac12m\dot x_3^2/E_c=u_{p,3}^2$. Le mode $(1,0,-1)$ en porte la moitié (toute l'énergie est sur les deux masses extrêmes) ; les deux autres un quart seulement ($x_2$ est grand dans ces modes). Un mode ne « sent » une perturbation que là où il bouge.
>
> **Pourquoi les modes ne sont-ils plus de simple symétrie ?**
>
> La perturbation brise la symétrie $M_1\leftrightarrow M_3$ : les trois modes restent bien trois directions propres mais $(1,0,-1)$ n'est plus un mode exact (la masse centrale se met à bouger faiblement). La correction au vecteur propre est d'ordre $\varepsilon$ et fait intervenir un couplage entre modes proportionnel à $u_{p,3}u_{q,3}/(\omega_q^2-\omega_p^2)$.



**q6.** **Question 6.** *Équation différentielle d'ordre $n$.* Écrire le système sous la forme d'ordre $1$ $\dot Y=\mathcal AY$ avec $Y=(X,\dot X)^{\mathsf T}$. Quelle est la taille de $\mathcal A$ ? Quelles sont ses valeurs propres en fonction des $\omega_p$ ? Comparer avec l'équation scalaire d'ordre $6$ satisfaite par $x_1(t)$.


> [!tip]- 💡 Coup de pouce
> **Matrice par blocs**
>
> $\dot X=\dot X$ et $\ddot X=-M^{-1}KX$ : écrivez $\mathcal A$ par blocs $3\times3$.
>
> **Valeurs propres**
>
> Pour $Y=(\vec u,\lambda\vec u)\,e^{\lambda t}$, montrez que $\lambda^2\vec u=-M^{-1}K\vec u$.




> [!success]- ✅ Correction
> **Résultat**
>
> $\mathcal A=\begin{pmatrix}0&I_3\\-M^{-1}K&0\end{pmatrix}$ ($6\times6$) ; valeurs propres $\lambda=\pm i\omega_p$ ($p=1,2,3$), c'est-à-dire $\lambda^2=-\omega_p^2$. L'équation scalaire d'ordre $6$ sur $x_1$ est $\prod_{p}(\mathrm D^2+\omega_p^2)\,x_1=0$ ($\mathrm D=\mathrm d/\mathrm dt$).




> [!example]- 📝 Solution détaillée
> **Passage à l'ordre 1**
>
> $Y=\begin{pmatrix}X\\V\end{pmatrix}$ avec $V=\dot X$ : $\dot X=V$ et $\dot V=-M^{-1}KX$ ; $\mathcal A=\begin{pmatrix}0&I\\-M^{-1}K&0\end{pmatrix}$ est une matrice $6\times6$ (le double de la dimension de $X$).
>
> **Spectre**
>
> $\mathcal AY=\lambda Y$ avec $Y=(\vec u,\vec w)$ : $\vec w=\lambda\vec u$ et $-M^{-1}K\vec u=\lambda\vec w=\lambda^2\vec u$. Donc $\vec u$ est vecteur propre de $M^{-1}K$ pour la valeur propre $-\lambda^2=\omega_p^2$ : $\lambda=\pm i\omega_p$. Les six valeurs propres de $\mathcal A$ sont purement imaginaires, comme il se doit pour un système conservatif sans frottement. Les valeurs propres de $\mathcal A$ ne sont *pas* les $\omega_p^2$ du problème mécanique : ce sont leurs racines carrées (imaginaires).
>
> **Solution et exponentielle de matrice**
>
> $Y(t)=e^{\mathcal At}Y(0)$ ; en base propre $e^{\mathcal At}$ se réduit à $e^{\pm i\omega_pt}$ ; en regroupant les paires conjuguées on retrouve $\cos\omega_pt$ et $\sin\omega_pt/\omega_p$ : $x(t)=\sum_p\big[c_p\cos\omega_pt+\dfrac{\vec u_p\cdot\dot X(0)}{\omega_p}\sin\omega_pt\big]\vec u_p$ avec $c_p=\vec u_p\cdot X(0)$.
>
> **Équation scalaire d'ordre 6**
>
> Le polynôme caractéristique de $\mathcal A$ est $\prod_p(\lambda^2+\omega_p^2)=\lambda^6+\dots$ : toute coordonnée $x_i(t)$ vérifie l'équation scalaire d'ordre $6$
> $$(\mathrm D^2+\omega_1^2)(\mathrm D^2+\omega_2^2)(\mathrm D^2+\omega_3^2)\,x_i=0,$$
> et la solution générale dépend de $6$ constantes (les trois $c_p$ et les trois coefficients de $\sin\omega_pt$, c'est-à-dire $X(0)$ et $\dot X(0)$). Un système d'ordre $2$ en dimension $3$ équivaut à une équation d'ordre $6$ en dimension $1$ ou à un système d'ordre $1$ en dimension $6$ : le nombre de constantes d'intégration est le même.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Chimie**
>
> Les vibrations d'une molécule triatomique linéaire (CO$_2$) : mode de flexion, d'élongation symétrique et antisymétrique ; même analyse par symétrie.
>
> **Génie civil**
>
> Un bâtiment à trois étages de rigidités et masses identiques est modélisé par la même matrice : les trois modes correspondent à des formes avec $0$, $1$, $2$ nœuds.




> [!question]- 🔭 Aller plus loin — Licence : Chaîne de $N$ masses
> Montrer que pour $N$ masses entre deux parois les modes sont $A_n=\sin\dfrac{np\pi}{N+1}$ et $\omega_p=2\omega_0\sin\dfrac{p\pi}{2(N+1)}$, $p=1,\dots,N$. Vérifier pour $N=3$.




> [!question]- 🔭 Aller plus loin — Master : Version transversale
> Si les masses vibrent transversalement (ressorts tendus initialement), le résultat est le même avec $\omega_0^2=T/(m\,a)$ (tension $T$, pas $a$) mais seulement à petits angles ; l'équation exacte est non linéaire (voir exercice 8).




> [!question]- 🔭 Aller plus loin — Master : Forme matricielle d'ordre 1
> Écrire $Y=(X,\dot X)$, $\dot Y=\mathcal AY$ avec $\mathcal A=\begin{pmatrix}0&I\\-M^{-1}K&0\end{pmatrix}$ ; montrer que $\mathrm{spec}(\mathcal A)=\{\pm i\omega_p\}$ (six valeurs propres) et que $e^{\mathcal At}$ contient $\cos\omega_pt$ et $\sin\omega_pt/\omega_p$.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex2-couplage-de-deux-oscillateurs-harmoniques-dissymetriques|Exercice 2 — Couplage de deux oscillateurs harmoniques dissymétriques]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex3-oscillations-libres-et-forcees-d-un-couplage-pendule-chariot|Exercice 3 — Oscillations libres et forcées d'un couplage pendule-chariot]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex4-frequence-propre-d-une-molecule-diatomique|Exercice 4 — Fréquence propre d'une molécule diatomique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex5-complement-niveau-1-cpge-pendules-couples-par-un-ressort-attache-a-mi-hauteur|Exercice 5 — Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex7-complement-niveau-2-ambitieux-oscillateurs-desaccordes-anticroisement-et-transfert-d-energie|Exercice 7 — Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex8-complement-niveau-3-ens-modes-non-lineaires-de-deux-pendules-couples-stabilite-et-instabilite-parametrique|Exercice 8 — Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex9-complement-niveau-3-ens-anneau-de-n-oscillateurs-modes-de-fourier-et-propagation-du-signal|Exercice 9 — Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex1-pendules-couples-et-battements|Exercice 1 — Pendules couplés et battements]]


